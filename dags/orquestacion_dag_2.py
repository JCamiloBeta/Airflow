from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='orquestacion_dag_2',
    description='A DAG for orchestrating tasks version 2',
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 1),
    schedule_interval='@monthly',
) as dag:
    t1 = EmptyOperator(
        task_id='task_1'
    )

    t2 = EmptyOperator(
        task_id='task_2'
    )

    t3 = EmptyOperator(
        task_id='task_3'
    )

    t4 = EmptyOperator(
        task_id='task_4'
    )

    t1 >> t2 >> [t3, t4]  # t3 and t4 run in parallel after t1 and t2