TOP=../..

include $(TOP)/configure/CONFIG
PYDEVSUP ?= /etc/epics
include $(PYDEVSUP)/configure/CONFIG_PY

PY += bug.py

include $(TOP)/configure/RULES
include $(PYDEVSUP)/configure/RULES_PY
