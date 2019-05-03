TOP=../..

include $(TOP)/configure/CONFIG
PYDEVSUP ?= /etc/epics
include $(PYDEVSUP)/configure/CONFIG_PY

PROD_IOC = bug
DBD += bug.dbd

bug_DBD += base.dbd
bug_DBD += pyDevSup.dbd

bug_LIBS += pyDevSup$(PY_LD_VER)

bug_SRCS += bug_registerRecordDeviceDriver.cpp
bug_SRCS_DEFAULT += bugMain.cpp

bug_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
include $(PYDEVSUP)/configure/RULES_PY
