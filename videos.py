import cv2
import os
from functions import create_folder

#Creación de la carpeta nueva salida para guardar los frames que se generan de todos los videos
create_folder('salida')

#Definición del directorio de salida donde se generan los frames
os.chdir('../ComputerVision/salida')

#Definición de la ruta de entrada de los videos
path_e = '../videos'

files_names = os.listdir(path_e)

#Contador de frames
currentframe = 0

for file_name in files_names:

  #Lectura del contenido del video
  path_video = os.path.join(path_e, file_name)

  cam = cv2.VideoCapture(path_video)

  while cam.isOpened():

    #Lectura de frames
    ret, frame = cam.read()

    #Mientras haya frames que extraer del video tratado generamos los archivos .jpg
    if ret:
      name = 'frame' + str(currentframe) + '.jpg'
      print('Creating ...' + name)

    #Escritura del frame extraído
      cv2.imwrite(name, frame)

    #Aumentar contador de frames
      currentframe += 1

    #Si no hay más frames que extraer del video tratado, nos salimos del bucle while
    else:
      break

  cam.release()

cv2.destroyAllWindows()