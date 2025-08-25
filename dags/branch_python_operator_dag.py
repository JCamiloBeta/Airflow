from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow import DAG
from datetime import datetime
from datetime import date

default_args = {
    "start_date": datetime(2023, 1, 1),
    "end_date": datetime(2023, 2, 10)
}

def _choose(**kwargs):
    if kwargs["logical_date"].date() < date(2023, 1, 15):
        return "finish_14"
    return "start_15"

with DAG(dag_id="branch_python_operator_dag",
         description="A DAG demonstrating BranchPythonOperator",
         schedule_interval="@daily",
         default_args=default_args) as dag:
    
    branching = BranchPythonOperator(
        task_id="branch",
        python_callable=_choose)
    

    finish_14 = BashOperator(
        task_id="finish_14",
        bash_command='echo "Finishing {{ ds}}"')

    start_15 = BashOperator(
        task_id="start_15",
        bash_command='echo "Starting {{ ds}}"')
    
    branching >> [finish_14, start_15]