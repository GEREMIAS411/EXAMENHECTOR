from PIL import Image
url = input("ingrese la url de la imagen:")
abrir = Image.open(url)
rotacion = int(input("ingrese el angulo de rotacion:"))
imagenrotada = abrir.rotate(rotacion,expand=True).show()

abrir.save("img/copia/imagencopiamessi.webp")




