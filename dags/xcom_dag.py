from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {"depend_on_past": True}

def myfunction(**kwargs):
    ti = kwargs['ti']
    xcom_value = int(ti.xcom_pull(task_ids='tarea1'))-14
    print(f"Pulled XCom value in PythonOperator: {xcom_value}")
    return xcom_value

with DAG(dag_id="xcom_dag",
         description="A DAG demonstrating XComs",
         start_date=datetime(2023, 1, 1),
         schedule_interval="@once",
         max_active_runs=1,
         default_args=default_args) as dag:
    
    t1 = BashOperator(
        task_id="tarea1",
        bash_command="sleep 5 && echo $((3*8))"
    )

    t2 = BashOperator(
        task_id="tarea2",
        bash_command="sleep 3 && echo 'Pulled XCom value: {{ ti.xcom_pull(task_ids='tarea1') }}'"
    )

    t3 = PythonOperator(
        task_id="tarea3",
        python_callable=myfunction)

    t1 >> t2 >> t3