# Python & Encriptación 🔒⚡

> **Presentación oficial y laboratorio interactivo de ciberseguridad y criptografía moderna con Python.**  
> Diseñada para exposiciones en proyector (100vh, fondo OLED Black, animaciones fluidas y sin barras invasivas).

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

5. **05. DEMO en Vivo (Laboratorio Web Crypto API)**:
   - Cifrado simétrico autenticado **AES-256-GCM** con derivación de claves PBKDF2 y medidor de entropía en tiempo real.
   - Función hash **SHA-256** con demostración del efecto avalancha en vivo (conteo de mutación de bits/caracteres).
   - **Cifrado César** didáctico con selector de desplazamiento rotacional.
   - Generador y exportador dinámico de código Python listo para ejecutar.

6. **06. Conclusiones & Quiz**:
   - Síntesis de buenas prácticas: importancia de la gestión de claves, uso de librerías auditadas y rol en la banca digital y privacidad moderna.
   - Quiz interactivo de evaluación rápida para la audiencia con retroalimentación instantánea.

---

## 🚀 Cómo Ejecutar el Proyecto

No requiere instalación de servidores ni dependencias externas; funciona directamente en cualquier navegador moderno:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/stevenortiz-dev/python-encriptacion.git
   ```
2. Abre el archivo `index.html` en tu navegador favorito (Chrome, Edge, Firefox, Brave).
3. (Opcional) Presiona <kbd>F11</kbd> o el botón **Pantalla Completa** para proyectar en modo cine/auditorio.

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

- **HTML5 semántico** con optimización de layout `100vh`.
- **Tailwind CSS** para un diseño moderno, tipografías y efectos de cristal (*Glassmorphism*).
- **JavaScript Moderno (ES6+)** con la **Web Cryptography API** nativa del navegador.
- **HTML5 Canvas** interactivo para la constelación criptográfica de fondo reactiva al cursor.
- **Google Fonts**: *Plus Jakarta Sans*, *Space Grotesk* y *JetBrains Mono*.
- **Font Awesome 6.5.1** para iconografía de ciberseguridad.

---

## 👤 Autor

- **Steven Ortiz** — [@stevenortiz-dev](https://github.com/stevenortiz-dev)
