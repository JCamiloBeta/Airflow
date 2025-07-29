# Proyecto Airflow

Este proyecto utiliza [Apache Airflow](https://airflow.apache.org/) para la orquestación y automatización de flujos de trabajo.

## Requisitos

- Python 3.7+
- Apache Airflow 2.4.2
- Docker (recomendado)
- Docker Compose

## Instalación

Actualmente, el proyecto cuenta con la siguiente estructura y archivos principales:

- Carpeta `dags/` para los DAGs personalizados.
- Carpeta `plugins/` para agregar funcionalidades adicionales a Airflow.
- Archivo `docker-compose.yml` para levantar el entorno completo de Airflow usando Docker.
- Carpeta `.devcontainer/` con la configuración para el entorno de desarrollo en contenedores.
- Archivo `requirements.txt` para dependencias adicionales de Python.
- Archivo `README.md` con la documentación básica para la instalación y uso del proyecto.

Se recomienda utilizar Docker y Docker Compose para facilitar la gestión de dependencias y la portabilidad del entorno. El proyecto incluye un entorno de desarrollo preconfigurado mediante un *devcontainer* para facilitar la configuración y el desarrollo consistente en diferentes sistemas.

Para trabajar desde el *devcontainer*, simplemente abre el proyecto en [Visual Studio Code](https://code.visualstudio.com/) y selecciona "Reopen in Container" cuando se te solicite. Esto configurará automáticamente el entorno de desarrollo con todas las dependencias necesarias, permitiéndote desarrollar y ejecutar Airflow sin configuraciones adicionales en tu sistema local.

A medida que avances, recuerda actualizar este archivo con nuevas configuraciones, dependencias o instrucciones relevantes.

## Estructura del Proyecto

```
.
├── dags/
│   └── operator_dag.py
├── plugins/
├── .devcontainer/
│   └── devcontainer.json
├── docker-compose.yml
├── requirements.txt
├── README.md
```

## Uso

1. Levantar el entorno de Airflow con Docker Compose:

    ```bash
    docker-compose up -d
    ```

2. Inicializar la base de datos de Airflow (solo la primera vez):

    ```bash
    docker-compose run --rm airflow-webserver airflow db init
    ```

3. Acceder a la interfaz web en: [http://localhost:8080](http://localhost:8080)

4. Para detener el entorno:

    ```bash
    docker-compose down
    ```

## Personalización

- Agrega tus DAGs en la carpeta `dags/`.
- Configura conexiones y variables desde la interfaz web.
- Agrega dependencias adicionales en `requirements.txt`.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

## Recursos útiles

- [Documentación oficial de Airflow](https://airflow.apache.org/docs/)
- [Guía de instalación de Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)
- [Comunidad de Apache Airflow](https://airflow.apache.org/community/)

## Preguntas frecuentes

### ¿Cómo instalo dependencias adicionales?

Agrega los paquetes requeridos en un archivo `requirements.txt` y ejecuta:

```bash
docker-compose build
docker-compose up -d
```

### ¿Cómo abro la interfaz web desde el contenedor?

Puedes abrir la interfaz web en tu navegador ejecutando:

```bash
$BROWSER http://localhost:8080
```

### ¿Dónde reporto problemas o solicito mejoras?

Abre un *issue* en el repositorio o contacta a los mantenedores del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *pull request* o sugiere cambios mediante *issues*.

---
¿Tienes dudas o sugerencias? ¡No dudes en contribuir o contactar al equipo!