from imgurpython import ImgurClient
 
import os
import urllib.request
import timeit
from concurrent.futures import ThreadPoolExecutor  
from multiprocessing import Pool
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
links = []
 
def descarga_url_img(link):
   print(link)
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "C:/Users/gabri/Desktop/Nueva carpeta/{}.{}"
  
   #Guardar en local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def multiplesHilos():
      with ThreadPoolExecutor(max_workers=len(links)) as executor:
         executor.map(descarga_url_img,links)
   
def multiplesProcesos():
   with Pool(len(links)) as p:
        p.map(descarga_url_img,links)

def estructural():
   for i in range(len(links)):
      descarga_url_img(links[i])


def getlinks():
   id_album = "bUaCfoz"
   imagenes = cliente.get_album_images(id_album)
   for imagen in imagenes:
       links.append(imagen.link)
   
 
if __name__ == "__main__":
   getlinks()
   print(f"Tiempo Multiples Hilos {timeit.Timer(multiplesHilos).timeit(number=1)}")
   print(f"Tiempo Multiples procesos {timeit.Timer(multiplesProcesos).timeit(number=1)}")
   print("Tiempo estructural {}".format(timeit.Timer(estructural).timeit(number=1)))