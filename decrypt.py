from PIL import Image
import io


def is_valid_image(byte_data):
    try:
        Image.open(io.BytesIO(byte_data)).verify()
        return True
    except:
        return False

try:

    path = input('Ingrese la ruta de la imagen: ')
    # Asegura que se ingrese un entero
    while True:
        try:
            key = int(input('Ingrese la clave para el descifrado de la imagen: '))
            break
        except ValueError:
            print("La clave debe ser un número entero. Intente de nuevo.")
    #Lee el archivo
    with open(path, 'rb') as file:
        image = file.read()
    #Valida si el archivo esta cifrado
    if not is_valid_image(image):
        print('La imagen parece estar cifrada')
    else:
        print('La imagen parece no estar cifrada. No se realizará ninguna acción.')
        raise SystemExit
    #Crea el mismo arreglo de bytes
    image = bytearray(image)
    # Executa la operacion XOR en cada uno de los bytes, usando la clave
    for index, values in enumerate(image):
        image[index] = values ^ key
    #valida si puede abrir la imagen, para ver si esta desencriptada, y si, si escribe en el archivo para desencriptarla
    if is_valid_image(image):
        with open(path, 'wb') as file:
            file.write(image)
        print('Descifrado completado...')
    else:
        print('El descifrado falló por que la clave no coincide o la imagen no estaba cifrada.')
#Manejo de errores
except FileNotFoundError:
    print('Error: El archivo no fue encontrado. Verifique la ruta.')
except IOError:
    print('Error de Entrada/Salida al manejar el archivo.')
except Exception as e:
    print('Error capturado: ', str(e))
