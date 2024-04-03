# Usa una imagen de Python como base
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido de la carpeta de tu proyecto Django al directorio de trabajo
COPY . .

# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Ejecuta el comando para arrancar tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
