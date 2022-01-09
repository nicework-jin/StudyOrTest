## 싱글 머신에서 병렬 Task 실행하기
지금까지 실습에서 sequentialexecutor을 사용했다.
dag이 task1 >> [task2, task3] >> task4라고 가정하자.

task2와 task3가 종료된 후에 task가 실행 되는데, sequentialexecutor을 사용하면 task2과 task3이 동시에 실행되지 않는다.
병렬로 태스크를 실행하기 위해서는 localExecutor를 사용해야 한다.

그러기 위해서는 두 가지를 변경해야 한다.
1. sqlite를 postgres 데이터베이스로!
2. sequentialExecutor를 localExecutor로!
3. 테스트

### sqlite를 postgres 데이터베이스로!
1. postgres를 다운 받는다.
2. postgres에서 id/password를 변경한다.
3. sql_alchemy_conn을 변경한다. 
   1. psycopg2 라이브러리 다운 받는다. python에서 postgres 사용할 수 있게 한다.
   2. 아래 형식으로 기입한다. 
      1. postgresql+psycopg2://postresID:postgresPassword@localhost/DB명
### sequentialExecutor를 localExecutor로!
1. executor를 LocalExecutor로 변경한다.

### 테스트
1. bashOperator로 task1 >> [task2, task3] >> task4 구조 만든 다음 실행한다.
2. Gantt 차트를 보면 명확하게 알 수 있다.

## airflow.cfg 속성 탐구
1. parallelism: 태스크인스턴스(프로세스)의 최대 개수
   - LocalExecutor의 parallelism이 0인 경우 무한대의 프로세스를 사용한다.
   - LocalExecutor의 parallelism이 1인 경우 SquentialExecutor와 같다
   - LocalExecutor의 parallelism이 2 이상인 경우 여러 개의 프로세스를 동시에 실행한다.
2. dag_concurrency: 하나의 DAG에서 사용할 수 있는 concurrency 수
   - 하나의 프로세스(태스크)가 동시에 작업하는 최대 수
3. max_active_runs_per_dag: 동일한 DAG을 실행할 수 있는 최대 개수
   - catchup=True이고, 실행되지 않은 dag이 존재할 경우 동일한 DAG이 실행될 수 있다.

##### [example 1]
<bold>DAG A: task1 >> [task2, task3] >> task4<br></bold>
아래와 같은 설정에서 DAG A의 task2, task3는 동시에 실행될까?
parallelism = 1 <br>
dag_concurrency = 16<br>
<br>
답: NO, dag_concurrency는 2개 이상이지만, parallelism이 1개 이므로 1개씩 순차대로 실행된다.

##### [example 2]
<bold>DAG A: task1 >> [task2, task3] >> task4<br></bold>
<bold>DAG B: task1 >> [task2, task3] >> task4<br></bold>

아래와 같은 설정에서 DAG A와 B의 task2, task3는 모두 동시에 실행될까?<br>
parallelism = 2 <br>
dag_concurrency = 4<br>
max_active_runs_per_dag = 1<br>
답: YES, parallelism과 dag_concurrency의 수가 적절하다.
또한, DAG A, B는 각각 한 번씩만 실행되면 된다. 따라서 max_active_runs_per_dag에 영향받지 않는다. 하지만 어떠한 이유로 DAG A를 동시에 두 번 실행해야 한다면 실행 불가능하다. 현재 max_active_runs_per_dag은 1이기 때문이다. 이 경우 2 이상이 되어야 한다. 
<br>

