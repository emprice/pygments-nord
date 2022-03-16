DISTDIR ?= dist

.PHONY: default

WHEEL := $(DISTDIR)/pygments_nord-1.0-py3-none-any.whl

default: $(WHEEL)

$(WHEEL): pynord/__init__.py pynordlight/__init__.py \
		  pynorddark/__init__.py setup.cfg pyproject.toml Makefile
	python -m build -o $(DISTDIR)
	pip install --force-reinstall $@

# vim: set ft=make:
