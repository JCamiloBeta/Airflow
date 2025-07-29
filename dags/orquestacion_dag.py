from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='orquestacion_dag',
    description='A DAG for orchestrating tasks',
    start_date=datetime(2023, 10, 1),
    end_date=datetime(2023, 11, 1),
    schedule_interval='@daily',
    default_args={'depends_on_past': True},
    max_active_runs=1
) as dag:
    t1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 2 && echo "This is task 1"'
    )

    t2 = BashOperator(
        task_id='task_2',
        bash_command='sleep 2 && echo "This is task 2"'
    )

    t3 = BashOperator(
        task_id='task_3',
        bash_command='sleep 2 && echo "This is task 3"'
    )

    t4 = BashOperator(
        task_id='task_4',
        bash_command='sleep 2 && echo "This is task 4"'
    )

    t1 >> t2 >> [t3, t4]  # t3 and t4 run in parallel after t1 and t2