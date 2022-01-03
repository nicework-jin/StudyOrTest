### 싱글 머신에서 병렬 Task 실행하기
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
