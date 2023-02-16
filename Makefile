all:
	pip install -r requirements.txt
	python app/main.py

test:
	pytest tests/

clean:
	rm -rf __pycache__