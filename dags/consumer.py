from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime, date

my_file = Dataset("/tmp/file.txt")
START_DATE = datetime(2023, 1, 1)

with DAG(
    dag_id="consumer",
    schedule=[my_file],
    start_date=START_DATE,
    catchup=False
):

    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())

    read_dataset()