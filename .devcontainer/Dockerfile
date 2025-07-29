# Dockerfile para entorno de desarrollo VS Code basado en la imagen de Airflow usada en producción
FROM apache/airflow:2.4.2

# Establece el directorio de trabajo
WORKDIR /opt/airflow

# Copia tus archivos (opcional, si VS Code ya los monta como volumen)
# COPY ./dags ./dags

# Instala herramientas útiles para desarrollo si las necesitas
# RUN pip install --no-cache-dir <tus-dependencias> \
#     && apt-get update && apt-get install -y vim

# Evita errores de permisos si estás trabajando como root
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
