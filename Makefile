test:
	python3 -m unittest
coverage_test:
	coverage run -m unittest
.PHONY: test
