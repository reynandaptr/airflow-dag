from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from random import randint
from datetime import datetime

def _task():
    print(randint(1, 10))

dag = DAG (
    dag_id="test",
    schedule_interval="0 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

task_start = DummyOperator(
    dag=dag,
    task_id='Start',
)

taskA = PythonOperator(
    dag=dag,
    task_id="task_A",
    python_callable=_task,
)
taskB = PythonOperator(
    dag=dag,
    task_id="task_B",
    python_callable=_task,
)
taskC = PythonOperator(
    dag=dag,
    task_id="task_C",
    python_callable=_task,
)

task_start >> taskA >> taskB >> taskC
