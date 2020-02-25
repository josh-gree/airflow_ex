from airflow import DAG
from other_codebase import build_dags

for ind, dag in enumerate(build_dags()):
    globals()[f"dag_{ind}"] = dag

