from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("Hello, Airflow!")


with DAG(dag_id="python_operator_dag",
         description="DAG con Python Operator",
         start_date=datetime(2025,7,28),
         schedule_interval="@once") as dag:
    # Aquí puedes definir las tareas del DAG
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)
    
print("DAG 'python_operator' has been created with a PythonOperator task.")