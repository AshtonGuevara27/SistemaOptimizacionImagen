from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

CARPETA_SUBIDAS = os.path.join('static', 'uploads')
ANCHO_MAXIMO = 800  # ancho maximo que tendra la imagen optimizada


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # 1. Recibir los datos del formulario
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    imagen = request.files.get('imagen')

    # 2. Guardar la imagen original tal como llego
    nombre_archivo = imagen.filename
    ruta_original = os.path.join(CARPETA_SUBIDAS, nombre_archivo)
    imagen.save(ruta_original)

    # 3. Abrir la imagen con Pillow para procesarla
    img = Image.open(ruta_original)

    # 4. Si es muy ancha, la achicamos manteniendo su proporcion
    ancho, alto = img.size
    if ancho > ANCHO_MAXIMO:
        nueva_proporcion = ANCHO_MAXIMO / ancho
        nuevo_alto = int(alto * nueva_proporcion)
        img = img.resize((ANCHO_MAXIMO, nuevo_alto))

    # 5. Guardar la version optimizada (mas liviana)
    nombre_optimizada = 'optimizada_' + nombre_archivo
    ruta_optimizada = os.path.join(CARPETA_SUBIDAS, nombre_optimizada)
    img.save(ruta_optimizada, optimize=True, quality=60)

    # 6. Mostrar el resultado
    return render_template(
        'resultado.html',
        nombre=nombre,
        correo=correo,
        imagen_original=nombre_archivo,
        imagen_optimizada=nombre_optimizada
    )


if __name__ == '__main__':
    app.run(debug=True)