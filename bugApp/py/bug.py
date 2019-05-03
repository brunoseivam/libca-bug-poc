# pyDevSup imports
import devsup.ptable as PT
from devsup.hooks import addHook

from epics import PV, ca

from threading import Thread, Event

# Workaround CTRL+C not working
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

ca.AUTO_CLEANUP = False

class bugSupport(PT.TableBase):
    trigger = PT.Parameter()
    a = PT.Parameter()
    b = PT.Parameter()
    s = PT.Parameter(iointr=True)

    def launch_monitors(self):
        def cb(self, pvname, *args, **kwargs):
            print('Got data for %s' % pvname)

        pvs = ['SOME', 'TEST', 'PVS']
        self.monitors = {
            pvname: PV(pvname, callback=cb)
            for pvname in pvs
        }

    @trigger.onproc
    def do_trigger(self):
        self.s.value = self.a.value + self.b.value
        self.s.notify()

def build():
    stopEvent = Event()

    sup = bugSupport(name='bug')

    print('pyDevSup thread libca ctx =', ca.current_context())

    # In order to get a fresh context, lets do pyepics
    # stuff in a different thread
    def launcher(stopEvent):
        ca.create_context()

        print('launcher thread libca ctx =', ca.current_context())

        sup.launch_monitors()

        # Keep thread alive until it is time to go
        stopEvent.wait()

        print('(AtIocExit) launcher thread libca ctx =', ca.current_context())

    t = Thread(target=launcher, args=(stopEvent,))

    def stopLauncher():
        stopEvent.set()
        t.join()

    addHook('AtIocExit', stopLauncher)

    # iocInit somehow messes up contexts, so start the thread
    # after iocInit
    addHook('AfterIocRunning', t.start)

    return sup

