from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.python import PythonOperator

def my_custom_function():
    raise Exception("This is a custom function that raises an exception.")

default_args = {}

with DAG(
    dag_id='trigger_rules_dag',
    description='A DAG to demonstrate trigger rules',
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 1),
    default_args=default_args,
    schedule_interval='@monthly',
) as dag:
    t1 = BashOperator(
        task_id='task_1',
        retries=2,
        retry_delay=5,
        depends_on_past=False,  # This task depends on the success of the previous run
        bash_command='sleep 5 && echo "Task 1 completed"',
        trigger_rule=TriggerRule.ALL_SUCCESS  # This task must succeed for the next tasks to run
    )

    t2 = BashOperator(
        task_id='task_2',
        bash_command='sleep 5 && echo "Task 2 completed"',
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,  # This task must succeed for the next tasks to run
        depends_on_past=True  # This task depends on the success of the previous run
    )

    t3 = BashOperator(
        task_id='task_3',
        bash_command='sleep 5 && echo "Task 3 completed"',
        trigger_rule=TriggerRule.ALWAYS,  # This task runs regardless of the success or failure of t1 and t2
        retries=2,
        retry_delay=5,
        depends_on_past=True 
    )

    t4 = PythonOperator(
        task_id='task_4',
        python_callable=my_custom_function,
        trigger_rule=TriggerRule.ALL_SUCCESS,  # This task runs if any of the previous tasks fail
        retries=2,
        retry_delay=5,
        depends_on_past=True
    )

    t5 = BashOperator(
        task_id='task_5',
        bash_command='sleep 5 && echo "Task 5 completed"',
        retries=2,
        retry_delay=5,
        depends_on_past=True
    )

    t1 >> t2 >> t3 >> t4 >> t5  # Sequential execution of tasks