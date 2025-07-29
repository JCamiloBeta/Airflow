from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def print_hello():
    print("Hello World, Airflow!")


with DAG(dag_id="dependencias_entre_tareas",
         description="DAG para demostrar dependencias entre tareas",
         start_date=datetime(2025,7,28),
         schedule_interval="@once") as dag:
    
    # Aquí puedes definir las tareas del DAG
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)
    
    t2 = BashOperator(
        task_id="run_bash_command",
        bash_command="echo 'Hello, Airflow!'")
    
    t3 = PythonOperator(task_id="final_task",
                        python_callable=lambda: print("Final task executed!"))
    
    t4 = BashOperator(
        task_id="final_bash_task",
        bash_command="echo 'Final Bash Task executed!'")
    
    # Definir las dependencias entre las tareas
    # t1 >> t2 >> [t3, t4]
    t1.set_downstream(t2)
    t2.set_downstream([t3,t4])