from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

meet_date = datetime.today() + timedelta(hours=9)
while meet_date.weekday() != 1:
    meet_date += timedelta(days=1)
meet_date = meet_date.strftime('%y%m%d')

default_args = {
    'start_date': datetime(2021, 12, 23, 16, 57, 50) + timedelta(minutes=1)
}

with DAG('test', schedule_interval='*/1 * * * *',
    default_args=default_args,
    catchup=False) as dag:


    echo_meet_date = BashOperator(
        task_id = 'echo_meet_date',
        bash_command=f'echo {meet_date}'
    )   

    echo_meet_date
