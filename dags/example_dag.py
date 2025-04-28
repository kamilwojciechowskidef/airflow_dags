from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_airflow():
    print("Hello from Airflow!")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["example"],
) as dag:
    
    task_hello = PythonOperator(
        task_id="say_hello",
        python_callable=hello_airflow,
    )
