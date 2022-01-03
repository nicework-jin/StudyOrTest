from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2022, 1, 3, 8, 5, 48),
    'catchup': False
}

with DAG('localExecutorTest', default_args=default_args) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command='sleep 3'
    )   
    
    task2 = BashOperator(
        task_id = 'task2',
        bash_command='sleep 3'
    )   

    task3 = BashOperator(
        task_id = 'task3',
        bash_command='sleep 3'
    )   

    task4 = BashOperator(
        task_id = 'task4',
        bash_command='sleep 3'
    )   

    task1 >> [task2, task3] >> task4


