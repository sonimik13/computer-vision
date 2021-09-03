import cv2
import os
import shutil
from pathlib import Path

def create_folder(folder_name):
    """
    Función que crea carpetas
    Input:
        folder_name: string
    """

    if Path(folder_name).exists():
        print('Carpeta ' + folder_name + ' ya existe')

    else:
        os.mkdir(folder_name)


def change_label_horizontal(path_label_input, file_name, path_label_output):
    """
    Función que crea el archivo label (.txt) de la imagen volteada horizontalmente
    Inputs:
        path_label_input: path de donde leemos los archivos .txt
        file_name: nombre del archivo .txt leído
        path_label_output: path donde escribimos los archivos .txt
    """
    path_e = os.path.join(path_label_input, file_name)
    path_s = os.path.join(path_label_output, 'h' + file_name)

    datos = []
    datos1 = []

    f = open(path_e, "r")

    for linea in f:
        datos.append(linea.split())
        lista = linea.split()
        lista[1] = str(1 - float(lista[1]))
        datos1.append(lista)

    with open(path_s, "w") as s:
        for item in datos1:
            s.write(' '.join(item) + '\n')

    s.close()
    f.close()


def change_label_vertical(path_label_input, file_name, path_label_output):
    """
    Función que crea el archivo label (.txt) de la imagen volteada verticalmente
    Inputs:
        path_label_input: path de donde leemos los archivos .txt
        file_name: nombre del archivo .txt leído
        path_label_output: path donde escribimos los archivos .txt
    """

    path_e = os.path.join(path_label_input, file_name)
    path_s = os.path.join(path_label_output, 'v' + file_name)

    datos = []
    datos1 = []

    f = open(path_e, "r")

    for linea in f:
        datos.append(linea.split())
        lista = linea.split()
        lista[2] = str(1 - float(lista[2]))
        datos1.append(lista)

    with open(path_s, "w") as s:
        for item in datos1:
            s.write(' '.join(item) + '\n')

    s.close()
    f.close()


def change_image_horizontal_vertical(path_image_input, file_name, path_image_output, indicator):
    """
    Función que crea las imágenes volteadas (.jpg) horizontalmente o verticalmente
    Inputs:
        path_label_input: path de donde leemos los archivos .jpg
        file_name: nombre del archivo .jpg leído
        path_label_output: path donde escribimos los archivos .jpg
        indicator: 'h' --- genera imagen volteada horizontalmente
                   'v' --- genera imagen volteada verticalmente
                   distinto 'h' ó 'v' --- genera mensaje indicando que el parámetro indicator no es válido
    """

    path_e = os.path.join(path_image_input, file_name)
    image = cv2.imread(path_e)

    if indicator == 'h':
        rot_horiz = cv2.flip(image, 1)
        savepath = os.path.join(path_image_output, 'h' + file_name)
        cv2.imwrite(savepath, rot_horiz)

    elif indicator == 'v':
        rot_vert = cv2.flip(image, 0)
        savepath = os.path.join(path_image_output, 'v' + file_name)
        cv2.imwrite(savepath, rot_vert)

    else:
        print('Parámetro indicator no es válido ' + indicator + ", tiene que ser 'h' o 'v'")


def create_train_val(path_input, indicator):
    """
    Función que guarda las imágenes (.jpg) y los labels (.txt) en las carpetas train y val
    Input:
        path_image_input: path de donde leemos los archivos .jpg
        indicator: 'i' --- guarda las imágenes (.jpg) en las carpetas train y val
                   'l' --- guarda los labels (.txt) en las carpetas train y val
                   distinto 'i' ó 'l' --- genera mensaje indicando que el parámetro indicator no es válido
    """

    files = os.listdir(path_input)

    #División de datos en train y idation (80% de datos para train)
    number_files = int(len(files) * 0.8)

    if indicator == 'i':

        path_image_s1 = 'train_data/images/train'
        path_image_s2 = 'train_data/images/val'

        count = 0

        for file_name in files:
            if count <= number_files:

                path_image_e = os.path.join(path_input, file_name)
                path_image_s = os.path.join(path_image_s1, file_name)
                shutil.copy(path_image_e, path_image_s)

                count += 1

            else:
                path_image_e = os.path.join(path_input, file_name)
                path_image_s = os.path.join(path_image_s2, file_name)
                shutil.copy(path_image_e, path_image_s)

                count += 1

    elif indicator == 'l':

        path_label_s1 = 'train_data/labels/train'
        path_label_s2 = 'train_data/labels/val'

        count = 0

        for file_name in files:
            if count <= number_files:

                path_label_e = os.path.join(path_input, file_name)
                path_label_s = os.path.join(path_label_s1, file_name)
                shutil.copy(path_label_e, path_label_s)

                count += 1

            else:
                path_label_e = os.path.join(path_input, file_name)
                path_label_s = os.path.join(path_label_s2, file_name)
                shutil.copy(path_label_e, path_label_s)

                count += 1

    else:
        print('Parámetro indicator no es válido ' + indicator + ", tiene que ser 'i' ó 'l'")