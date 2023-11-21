# Cifrado y Descifrado de Imágenes

Este proyecto contiene dos scripts en Python: uno para cifrar imágenes y otro para descifrarlas. Los scripts realizan operaciones de cifrado/descifrado utilizando el método de cifrado XOR.

## Requisitos

Para utilizar estos scripts, necesitarás:
- Python 3.x instalado en tu sistema.
- La biblioteca Pillow instalada en tu entorno Python.

Puedes instalar Pillow utilizando pip:
pip install Pillow

## Uso

### Cifrado de Imágenes

Para cifrar una imagen, ejecuta el script de cifrado y sigue las instrucciones en pantalla. Se te pedirá que ingreses la ruta de la imagen y una clave de cifrado (un número entero).

El script verificará si el archivo proporcionado es una imagen válida y luego procederá a cifrarla utilizando la clave proporcionada.

### Descifrado de Imágenes

Para descifrar una imagen, ejecuta el script de descifrado y sigue las instrucciones en pantalla. Se te pedirá que ingreses la ruta de la imagen y la clave de descifrado (debe ser la misma clave utilizada para cifrar).

El script verificará si el archivo proporcionado es una imagen válida y luego intentará descifrarla utilizando la clave proporcionada. Si la imagen se descifra correctamente, se sobrescribirá el archivo original con la imagen descifrada.


Este codigo en otro codigo traido de la siguiente pagina, y se modifico para que pudiera tener un mejor manejo de errores, y no se ingerese datos no correspondientes:
https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/

Referencia:
GeeksforGeeks. (2022, June 8). Encrypt and Decrypt Image using Python. https://www.geeksforgeeks.org/encrypt-and-decrypt-image-using-python/
