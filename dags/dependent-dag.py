from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time


def dependent_fuction():
    """
    Waits 30 seconds before printing a statement to test dependency management,
    """
    time.sleep(60)
    print('Dependent DAG has completed.')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('dependent-dag',
         start_date=datetime(2021, 1, 1),
         max_active_runs=1,
         schedule_interval=None,
         catchup=False
         ) as dag:

    dependent_task = PythonOperator(
        task_id='depdenent_dag_task',
        python_callable=dependent_fuction,
        provide_context=True
    )
