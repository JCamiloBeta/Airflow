from airflow import DAG
from datetime import datetime
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="file_sensor_dag",
    description="A DAG that uses FileSensor to monitor a file",
    schedule_interval="@daily",
    start_date=datetime(2023, 10, 1),
    end_date=datetime(2023, 10, 31),
    max_active_runs=1
) as dag:
    
    t1 = BashOperator(
        task_id="create_file_task",
        bash_command="sleep 5 && touch /tmp/file.txt"
    )

    t2 = FileSensor(
        task_id="file_sensor_task",
        filepath="/tmp/file.txt"
    )

    t3 = BashOperator(
        task_id="print_file_task",
        bash_command="echo 'File is present!'",
    )

    t1 >> t2 >> t3