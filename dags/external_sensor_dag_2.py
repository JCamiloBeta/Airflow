from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(
    dag_id='external_task_sensor_dag_2',
    description='A DAG to demonstrate external task sensors version 2',
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 12, 1),
    schedule_interval='@daily',
) as dag:
    
    t1 = ExternalTaskSensor(
        task_id='wait_for_external_task',
        external_dag_id='external_task_sensor_dag',
        external_task_id='task_1',
        poke_interval=10,  # Check every 10 seconds
    )

    t2 = BashOperator(
        task_id='task_2',
        bash_command='sleep 10 && echo "Dag 2 finished successfully"',
        depends_on_past=True  # This task does not depend on the success of the previous run
    )

    t1 >> t2  # t2 will run after t1 completes successfully