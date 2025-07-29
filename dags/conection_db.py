from airflow.providers.postgres.operators.postgres import PostgresOperator

populate_pet_table = PostgresOperator(
    task_id="populate_pet_table",
    postgres_conn_id="postgres_default",
    sql="sql/pet_schema.sql",
)