from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='external_task_sensor_dag',
    description='A DAG to demonstrate external task sensors',
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 12, 1),
    schedule_interval='@daily',
) as dag:
    
    # Define the tasks here
    t1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 10 && echo "Dag 1 finished successfully"',
        depends_on_past=True  # This task does not depend on the success of the previous run
    )




