#!../../bin/linux-x86_64-debug/bug

< envPaths

epicsEnvSet("PYEPICS_LIBCA", "$(EPICS_BASE)/lib/$(ARCH)/libca.so")
epicsEnvSet("PREFIX", "bug:")

dbLoadDatabase("${TOP}/dbd/bug.dbd",0,0)
bug_registerRecordDeviceDriver(pdbbase)

py "import bug"
py "bug.build()"

dbLoadRecords("$(TOP)/db/bug.db", "P=$(PREFIX)")

var atExitDebug 1

iocInit()

