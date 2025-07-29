from airflow import DAG
from datetime import datetime
from hello_operator import HelloOperator

with DAG(
    dag_id='custom_operator_dag',
    description='A DAG to demonstrate custom operators',
    start_date=datetime(2023, 10, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    t1 = HelloOperator(
        task_id='hello_world_task',
        name='Airflow User'
    )
