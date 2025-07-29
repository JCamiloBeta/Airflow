from airflow import DAG
from airflow.operators.empty import EmptyOperator
# import pendulum
# from airflow.decorators import dag
from datetime import datetime

# ## Primera manera de crear un DAG en Airflow

# my_dag  = DAG(
#     dag_id='my_first_dag',
#     start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
#     schedule_interval='@daily',
#     catchup=False
#     )

# op = EmptyOperator(
#     task_id='start',
#     dag=my_dag
# )

# # Segunda manera de crear un DAG en Airflow

# with DAG(
#     dag_id='my_second_dag',
#     start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
#     schedule_interval='@daily',
#     catchup=False
# ) as my_second_dag:

#     op2 = EmptyOperator(
#         task_id='start',
#         dag=my_second_dag
#     )

# # Tercera manera de crear un DAG en Airflow

# @dag(start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
#      schedule_interval='@daily', catchup=False)

# def my_third_dag():   
#     op3 = EmptyOperator(
#         task_id='start',

#     )

# dag = my_third_dag()

with DAG(dag_id="primer_dag", 
         description="Nuestro primer DAG",
         start_date=datetime(2025,7,28),
         schedule_interval="@once") as dag:
    # Aquí puedes definir las tareas del DAG
    t1 = EmptyOperator(task_id="dummy")