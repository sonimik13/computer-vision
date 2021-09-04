## Computer vision

Las imágenes para realizar este análisis se han obtenido de los siguientes videos de Youtube: [Momentos más deportivos](https://www.youtube.com/watch?v=MLoGKahcQG0), [Mejores escenas de persecución](https://www.youtube.com/watch?v=KDbYC8a-Wtw), [Momentos más bonitos del Pitufo Vanidoso](https://www.youtube.com/watch?v=yURcfQUaAGM), [Criaturas más aterradoras](https://www.youtube.com/watch?v=jCONWIE2TYw).

Además también se ha usado el buscador de internet [Google](https://www.google.com/) como técnica añadida para obtener más imágenes.

Todo el código está escrito en Python utilizando `notebooks` de PyCharm y Google colab para ejecutar en la nube con GPU el entrenamiento de las imágenes y la detección del objeto.

A continuación se explica el código generado:

* functions.py --- Descripción de las funciones usadas en los scripts videos.py e images.py

* videos.py --- Generación de los frames (.jpg) a partir de la carpeta videos

* images.py --- Generación de los labels (.txt) y las imágenes rotadas horizontalmente y verticalmente (.jpg) a partir de la carpeta entrada

* object_detection.ipynb --- Detección del objeto en un video mediante YOLOv5 a partir del fichero train_data.zip y el archivo custom_data.yaml 

Y el resultado:

* pitufo.mp4 --- Video de entrada usado para la detección del objeto

* salida.mp4 --- Video que muestra la detección del objeto junto con el nombre de su label y la probabilidad



**Palabras clave** (Python, OpenCV, YOLO, object detection, computer vision, IA)
