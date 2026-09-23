bootstrap:
	python3 -m pytest tests -q

test:
	python3 -m pytest tests -q

.PHONY: bootstrap test
