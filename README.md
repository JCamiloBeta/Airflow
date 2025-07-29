# Proyecto Airflow

Este proyecto utiliza [Apache Airflow](https://airflow.apache.org/) para la orquestación y automatización de flujos de trabajo.

## Requisitos

- Python 3.7+
- Apache Airflow 2.x
- Docker (opcional)

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar Airflow
pip install apache-airflow
```

## Estructura del Proyecto

```
.
├── dags/
│   └── ejemplo_dag.py
├── plugins/
├── README.md
```

## Uso

1. Iniciar el scheduler y webserver de Airflow:

    ```bash
    airflow db init
    airflow scheduler
    airflow webserver
    ```

2. Acceder a la interfaz web en: [http://localhost:8080](http://localhost:8080)

## Personalización

- Agrega tus DAGs en la carpeta `dags/`.
- Configura conexiones y variables desde la interfaz web.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.