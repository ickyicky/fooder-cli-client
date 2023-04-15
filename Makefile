build: fooder_cli setup.py setup.cfg
	python3 setup.py sdist bdist_wheel

push:
	twine upload dist/*

clean:
	rm dist/*
