import airflow

from airflow import DAG
from airflow.operators import BashOperator
from airflow.operators import DummyOperator


def build_dags():

    args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(2),
    }

    with DAG(dag_id="dag1", default_args=args, schedule_interval="0 0 * * *") as dag1:

        run_this_last = DummyOperator(task_id="run_this_last")

        run_this_first = BashOperator(task_id="run_this_first", bash_command="echo 1")

        run_this_first >> run_this_last

    with DAG(dag_id="dag2", default_args=args, schedule_interval="0 0 * * *") as dag2:

        run_this_last = DummyOperator(task_id="run_this_last")

        run_this_first = BashOperator(task_id="run_this_first", bash_command="echo 1")

        run_this_first >> run_this_last

    return [dag1, dag2]
