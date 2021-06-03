from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime, timedelta


def downstream_fuction():
    """
    Downstream function with print statement.
    """
    print('Upstream DAG has completed. Starting other tasks.')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('external-task-sensor-dag',
         start_date=datetime(2021, 1, 1),
         max_active_runs=3,
         schedule_interval='*/1 * * * *',
         catchup=False
         ) as dag:

    child_task1 = ExternalTaskSensor(
        task_id="child_task1",
        external_dag_id='example_dag',
        external_task_id='bash_print_date2',
        allowed_states=['success'],
        failed_states=['failed', 'skipped']
    )

    child_task2 = PythonOperator(
        task_id='child_task2',
        python_callable=downstream_fuction,
        provide_context=True
    )

    child_task1 >> child_task2