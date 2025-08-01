from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='orquestacion_dag',
    description='A DAG for orchestrating tasks',
    start_date=datetime(2023, 7, 1),
    end_date=datetime(2023, 11, 1),
    schedule_interval='0 7 * * 1',
    default_args={'depends_on_past': True},
    max_active_runs=1
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