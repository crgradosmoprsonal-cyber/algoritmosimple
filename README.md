## Cómo ejecutar

1. Clonar el repositorio y abrirlo en VSCode o cualquier editor de Python.
2. Asegurarse de tener Python instalado (versión 3.6+).
3. Ejecutar el archivo `bruteforce.py` con: python bruteforce.py
4. Observar en consola la contraseña encontrada, número de intentos y tiempo total.
5. Ejemplos de salida:

Ejemplo 1 "hola":
<img width="365" height="70" alt="image" src="https://github.com/user-attachments/assets/b314028f-9b85-46a1-84ef-8933312cbcb2" />

Ejemplo 2 "abc":
<img width="381" height="67" alt="image" src="https://github.com/user-attachments/assets/86b32b7f-26fc-433f-af9e-f2f04266b467" />

Ejemplo 3 "123":
<img width="394" height="72" alt="image" src="https://github.com/user-attachments/assets/bfe37325-0674-45a4-b92c-48f8df4394b4" />

Nota: el número de intentos y tiempo dependerá del alfabeto y la contraseña.

## Reflexión

- Para contraseñas largas (8+) o con un alfabeto grande, el tiempo crece exponencialmente porque el número de combinaciones posibles aumenta mucho, haciendo la fuerza bruta inviable.
- Para contraseñas cortas y alfabeto pequeño, el algoritmo encuentra la contraseña casi al instante.
- Esto demuestra por qué es importante usar contraseñas largas y con símbolos: aumenta la seguridad contra ataques de fuerza bruta



