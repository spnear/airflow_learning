from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime, date

my_file = Dataset("/tmp/file.txt")
START_DATE = datetime(2023, 1, 1)

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=START_DATE,
    catchup=False
):
    @task
    def update_dataset(outlets=[my_file]):
        with open(my_file.uri, "a+") as f:
            f.write("producer update")

    update_dataset()