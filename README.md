# Python & Encriptación 🔒⚡

> **Presentación oficial y laboratorio interactivo de ciberseguridad y criptografía moderna con Python.**  
> Diseñada para exposiciones en proyector (100vh, fondo OLED Black, animaciones fluidas, sin barras invasivas y con la demo oficial `DEMO1.PY`).

---

## 🌐 Enlaces del Proyecto

- **Presentación Web en Vivo (GitHub Pages)**: [stevenortiz-dev.github.io/python-encriptacion](https://stevenortiz-dev.github.io/python-encriptacion/)
- **Repositorio en GitHub**: [github.com/stevenortiz-dev/python-encriptacion](https://github.com/stevenortiz-dev/python-encriptacion)

---

## 📋 Contenido de la Exposición

La plataforma está estructurada en los 6 ejes temáticos fundamentales:

1. **01. Conceptos**:
   - Los 4 pilares: *Texto Plano*, *Algoritmo (Cifrador)*, *Clave Criptográfica* y *Texto Cifrado*.
   - Las 3 familias: *Cifrado Simétrico* (AES), *Cifrado Asimétrico* (RSA) y *Funciones Hash Criptográficas* (SHA-256).

2. **02. Funcionamiento**:
   - Explicación secuencial paso a paso del mecanismo de cifrado en Python.
   - Demostración interactiva en vivo con la librería `cryptography` y el algoritmo `Fernet` (cifrado y descifrado de la clave WiFi).

3. **03. Características**:
   - **Confidencialidad**: Protección estricta contra accesos no autorizados.
   - **Algoritmos de cifrado**: AES, RSA y estándares industriales.
   - **Claves de seguridad**: Generación con entropía criptográfica segura (`os.urandom`).
   - **Protección de datos**: Seguridad en tránsito y en reposo (contraseñas, archivos y mensajes).
   - **Cifrado y descifrado**: Transformación bidireccional controlada por llaves.
   - **Integridad**: Detección de alteraciones no autorizadas mediante HMAC y firmas.
   - **Librerías de Python**: Ecosistema (`cryptography`, `pycryptodome`, `hashlib`).

4. **04. Aplicaciones**:
   - Hasheo de contraseñas con `bcrypt` y `argon2` en backends.
   - Comunicaciones seguras con TLS/HTTPS en APIs (FastAPI / Flask).
   - Almacenamiento seguro en buckets y bases de datos con cifrado de sobre (envelope encryption).
   - Autenticación con tokens JWT firmados digitalmente.
   - Mensajería cifrada de extremo a extremo (E2EE).
   - Control de versiones y firmas de commits en Git.

5. **05. DEMO Oficial: Argon2id + AES-GCM (`DEMO1.PY`)**:
   - **Derivación Robusta (Argon2id)**: Ganador de la Password Hashing Competition. Utiliza 64 MB de memoria y 4 lanes para neutralizar ataques paralelos con granjas de GPUs o ASICs.
   - **Cifrado Autenticado (AES-GCM)**: Cifra con clave de 256 bits y genera un tag MAC de autenticación.
   - **Detección de Manipulación en Vivo (`InvalidTag`)**: Si se altera un solo bit o se usa una contraseña incorrecta, el sistema aborta de inmediato.
   - **Empaquetado URL-Safe**: Empaqueta `sal (16B) + nonce (12B) + cifrado` en un único token Base64 URL-safe.
   - **Simulador de Terminal Web**: Reproduce la experiencia interactiva de la consola de comandos de Python directamente en el navegador.
   - **Módulos Complementarios**: Efecto Avalancha (SHA-256) y Cifrado César didáctico.

6. **06. Conclusiones & Quiz**:
   - Síntesis de buenas prácticas: importancia de la gestión de claves, uso de librerías auditadas y rol en la banca digital y privacidad moderna.
   - Quiz interactivo de evaluación rápida para la audiencia con retroalimentación instantánea.

---

## 🚀 Cómo Ejecutar la Demo Oficial (`DEMO1.PY`) en Python

Para ejecutar el script interactivo directamente en tu consola local:

```bash
# 1. Instalar la librería cryptography
pip install cryptography

# 2. Ejecutar la demo
python DEMO1.PY
```

### Menú Interactivo del Script:
```text
=== Demo Argon2id + AES-GCM ===
1. Cifrar un mensaje
2. Descifrar un mensaje de esta sesión
3. Borrar mensajes cifrados
4. Salir
Elige 1, 2, 3 o 4:
```

---

## 💻 Cómo Abrir la Presentación Web

No requiere servidores ni configuraciones complejas:

1. **Opción Online**: Ábrela directamente desde [GitHub Pages](https://stevenortiz-dev.github.io/python-encriptacion/).
2. **Opción Local**:
   ```bash
   git clone https://github.com/stevenortiz-dev/python-encriptacion.git
   ```
   Abre `index.html` en cualquier navegador web.
3. Presiona <kbd>F11</kbd> para activar el modo pantalla completa para proyector.

---

## ⌨️ Controles para la Exposición

| Tecla / Acción | Descripción |
| :--- | :--- |
| <kbd>↓</kbd> / <kbd>Espacio</kbd> / <kbd>AvPág</kbd> | Avanzar a la siguiente sección |
| <kbd>↑</kbd> / <kbd>RePág</kbd> | Retroceder a la sección anterior |
| <kbd>F</kbd> o <kbd>F11</kbd> | Alternar Pantalla Completa |
| <kbd>Scroll</kbd> | Desplazamiento suave con snapping adaptativo |

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12** con la librería `cryptography` (módulos `AESGCM`, `Argon2id`, `InvalidTag`).
- **HTML5 & Tailwind CSS** optimizado para proyector con fondo OLED Black y sin barras invasivas.
- **Web Cryptography API** nativa para ejecución segura y reactiva en el cliente web.
- **HTML5 Canvas** interactivo para constelación de partículas criptográficas.

---

## 👤 Autor

- **Steven Ortiz** — [@stevenortiz-dev](https://github.com/stevenortiz-dev)
