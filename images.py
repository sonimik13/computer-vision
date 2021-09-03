import cv2
import os
import shutil
import functions

#Creación de las carpetas nuevas labels e images
functions.create_folder('labels')
functions.create_folder('images')

#Definición de las rutas de entrada y salida
path_e = 'entrada'
path_label_sal = 'labels'
path_image_sal = 'images'

files_names = os.listdir(path_e)

for file_name in files_names:

#Tratamiento para los archivos labels (.txt)
    if file_name.endswith('.txt'):

        #Se crea una copia del archivo .txt en la carpeta labels
        path_label_e = os.path.join(path_e, file_name)
        path_label_s = os.path.join(path_label_sal, file_name)
        shutil.copy(path_label_e, path_label_s)

        #Se crea el archivo .txt de la imagen volteada horizontalmente en la carpeta labels
        functions.change_label_horizontal(path_e, file_name, path_label_sal)

        #Se crea el archivo .txt de la imagen volteada verticalmente en la carpeta labels
        functions.change_label_vertical(path_e, file_name, path_label_sal)

#Tratamiento para los archivos frames (.jpg)
    elif file_name.endswith('.jpg'):

        #Se guarda el archivo .jpg leído en la carpeta images
        image_path = os.path.join(path_e, file_name)
        image = cv2.imread(image_path)
        savepath = os.path.join(path_image_sal, file_name)
        cv2.imwrite(savepath, image)

        #Se crea el archivo .jpg de la imagen volteada horizontalmente en la carpeta images
        functions.change_image_horizontal_vertical(path_e, file_name, path_image_sal, indicator='h')

        #Se crea el archivo .jpg de la imagen volteada verticalmente en la carpeta images
        functions.change_image_horizontal_vertical(path_e, file_name, path_image_sal, indicator='v')

#Tratamiento para los archivos que no tienen extensión (.txt) ni (.jpg)
    else:
        print('El fichero ' + file_name + ' no tiene extensión .jpg ó .txt')



