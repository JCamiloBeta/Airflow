from airflow.models.baseoperator import BaseOperator

class HelloOperator(BaseOperator):
    def __init__(self, name:str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        print(f"Hello, {self.name}!")
        context['ti'].xcom_push(key='greeting', value=f"Hello, {self.name}!")