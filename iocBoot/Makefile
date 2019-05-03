TOP = ..
include $(TOP)/configure/CONFIG
DIRS += $(shell find . -mindepth 2 -type f -name 'Makefile' | xargs dirname)
include $(CONFIG)/RULES_DIRS
