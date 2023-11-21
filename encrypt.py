from PIL import Image
import io
#Verifica si el arcchivo es una imagen que pueda abrir
def is_image_file(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()
        return True
    except:
        return False

try:
    path = input('Ingrese la ruta de la imagen: ')
    #verifica si es una imagen
    if not is_image_file(path):
        print('El archivo proporcionado no es una imagen válida.')
        raise SystemExit
    #Ingresa la clave que solo permite enteros
    key = int(input('Ingrese la clave para el cifrado de la imagen: '))
    #Abre la imagen
    with open(path, 'rb') as file:
        image = file.read()
    #Transforma la imagen a un arreglo de bytes
    image = bytearray(image)
    #Executa la operacion XOR en cada uno de los bytes, usando la clave
    for index, values in enumerate(image):
        image[index] = values ^ key
    #Y reescribe el archivo con la nueva imagen ya encriptada
    with open(path, 'wb') as file:
        file.write(image)

    print('Cifrado completado...')
#Manejo de errores
except ValueError:
    print("La clave debe ser un número entero. Intente de nuevo.")
except FileNotFoundError:
    print('Error: El archivo no fue encontrado. Verifique la ruta.')
except IOError:
    print('Error de Entrada/Salida al manejar el archivo.')
except Exception as e:
    print('Error capturado: ', str(e))
