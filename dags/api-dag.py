from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta


# Define body of POST request for the API call to trigger another DAG
{
  "dag_run_id": "string",
  "execution_date": "2019-08-24T14:15:22Z",
  "state": "success",
  "conf": {}
}

def print_task_type(**kwargs):
    """
    Dummy function to call before and after depdendent DAG.
    """
    print(f"The {kwargs['task_type']} task has completed.")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('api-dag',
         start_date=datetime(2021, 1, 1),
         max_active_runs=1,
         schedule_interval='@daily',
         catchup=False
         ) as dag:

    start_task = PythonOperator(
        task_id='starting_task',
        python_callable=print_task_type,
        op_kwargs={'task_type': 'starting'}
    )

    api_trigger_dependent_dag = SimpleHttpOperator(
        task_id="api_trigger_dependent_dag",
        http_conn_id='airflow-api',
        endpoint='/api/v1/dags/dependent-dag/dagRuns',
        method='GET',
        headers={'Content-Type': 'application/json'}
    )

    end_task = PythonOperator(
        task_id='end_task',
        python_callable=print_task_type,
        op_kwargs={'task_type': 'ending'}
    )

    start_task >> api_trigger_dependent_dag >> end_task