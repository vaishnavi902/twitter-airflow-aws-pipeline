from datetime import datetime, timedelta
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/home/ubuntu/airflow/dags")
from twitter_etl import run_twitter_etl

default_args = {
    "owner": "vaishnavi",
    "depends_on_past": False,
    "start_date": datetime(2026, 10, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "twitter_dag",
    default_args=default_args,
    description="A simple Twitter ETL pipeline using Airflow",
    schedule=timedelta(days=1),
)

run_etl_task = PythonOperator(
    task_id="complete_twitter_etl",
    python_callable=run_twitter_etl,
    dag=dag,
)