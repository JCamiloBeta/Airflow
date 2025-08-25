
from datetime import datetime
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="file_sensor_dag_with_reschedule",
    description="A DAG that uses FileSensor with reschedule mode",
    schedule_interval="@daily",
    start_date=datetime(2023, 10, 1),
    end_date=datetime(2023, 10, 31),
    max_active_runs=1
) as dag:
    
    t1 = BashOperator(
        task_id="create_file_task_1",
        bash_command="sleep 5 && touch /tmp/file2.txt"
    )

    t2 = FileSensor(
        task_id="file_sensor_task_1",
        mode="reschedule",
        poke_interval=10,
        filepath="/tmp/file2.txt"
    )

    t3 = BashOperator(
        task_id="print_file_task_1",
        bash_command="echo 'File 2 is present!'",
    )

    t1 >> t2 >> t3