from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime

templated_command = """
{% for file in params.filenames %}
    echo " {{ ds }} "
    echo " {{ file }} "
{% endfor %}
"""
with DAG(dag_id="templating_dag",
         description="A DAG demonstrating templating",
         start_date=datetime(2023, 1, 1),
         end_date=datetime(2023, 1, 10),
         schedule_interval="@daily",
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="tarea1",
                      bash_command=templated_command,
                      params={"filenames": ["file1.txt", "file2.txt", "file3.txt"]},
                      depends_on_past=True)