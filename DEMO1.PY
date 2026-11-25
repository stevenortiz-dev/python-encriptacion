import base64
import os
from getpass import getpass

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id


def derivar_clave(contrasena: bytes, sal: bytes) -> bytes:
    kdf = Argon2id(
        salt=sal,
        length=32,
        iterations=3,
        lanes=4,
        memory_cost=64 * 1024,
    )
    return kdf.derive(contrasena)

def cifrar(mensaje: str, contrasena: bytes) -> str:
    sal = os.urandom(16)
    nonce = os.urandom(12)
    clave = derivar_clave(contrasena, sal)

    texto_bytes = mensaje.encode()
    cifrado = AESGCM(clave).encrypt(nonce, texto_bytes, None)
    paquete = sal + nonce + cifrado
    return base64.urlsafe_b64encode(paquete).decode("ascii")


def descifrar(token: str, contrasena: bytes) -> str:
    paquete = base64.urlsafe_b64decode(token.encode("ascii"))
    sal = paquete[:16]
    nonce = paquete[16:28]
    cifrado = paquete[28:]

    clave = derivar_clave(contrasena, sal)
    texto_bytes = AESGCM(clave).decrypt(nonce, cifrado, None)
    return texto_bytes.decode()

def main():
    tokens = {}
    siguiente_id = 1

    while True:
        print("\n=== Demo Argon2id + AES-GCM ===")
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje de esta sesión")
        print("3. Borrar mensajes cifrados")
        print("4. Salir")
        opcion = input("Elige 1, 2, 3 o 4: ").strip()


        if opcion == "1":
            contrasena = getpass("Contraseña: ").encode()
            if not contrasena:
                print("La contraseña no puede estar vacía.")
                continue

            mensaje = input("Mensaje para cifrar: ")
            token = cifrar(mensaje, contrasena)
            tokens[siguiente_id] = token

            print(f"\nToken de cifrado #{siguiente_id}:")
            print(token)
            siguiente_id += 1

        elif opcion == "2":
            if not tokens:
                print("Primero cifra un mensaje con la opción 1.")
                continue

            print("Tokens disponibles:", ", ".join(map(str, tokens.keys())))
            try:
                token_id = int(input("Número del token para descifrar: "))
                token = tokens[token_id]
            except (ValueError, KeyError):
                print("Ese token no está en el historial.")
                continue

            contrasena = getpass("Contraseña usada para cifrarlo: ").encode()
            try:
                mensaje = descifrar(token, contrasena)
            except InvalidTag:
                print("Contraseña incorrecta o token alterado.")
            else:
                print("\nToken recuperado")
                print(f"Token de cifrado #{token_id}:")
                print(token)
                print("Mensaje descifrado:", mensaje)

        elif opcion == "3":
            if input("¿Borrar historial? (s/n): ").strip().lower() == "s":
                tokens.clear()
                print("Historial borrado.")

        elif opcion == "4":
            print("Demo terminada.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()