from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bash_operator",
         description="DAG to demonstrate BashOperator",
         start_date=datetime(2025, 7, 28)) as dag:
    # Aquí puedes definir las tareas del DAG
    t1 = BashOperator(
        task_id="run_bash_command",
        bash_command="echo 'Hello, Airflow!'"
    )