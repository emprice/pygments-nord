DISTDIR ?= dist

.PHONY: default install

WHEEL := $(DISTDIR)/pygments_nord-1.0-py3-none-any.whl

default: $(WHEEL) install

$(WHEEL): pynord/__init__.py pynordlight/__init__.py \
		  pynorddark/__init__.py setup.cfg pyproject.toml Makefile
	python -m build -o $(DISTDIR)

install:
	pip install --force-reinstall $(WHEEL)

# vim: set ft=make:
