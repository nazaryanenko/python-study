task1:
	python3 ./task_1/main.py
task2:
	python3 -m venv ./task_2/env2
	source ./task_2/env2/bin/activate && pip install --upgrade pip && pip install -r ./task_2/requirements.txt && ./task_2/main.py
task3:
	python3 -m venv ./task_3/env3
	source ./task_3/env3/bin/activate && pip install --upgrade pip && ./task_3/main.py
task4:
	python3 -m venv ./task_4/env4
	source ./task_4/env4/bin/activate && pip install --upgrade pip && pip install -r ./task_4/requirements.txt && ./task_4/main.py