#!/usr/bin/env python

"""
***TODO
         * create timer sounds
         * show interrupt count
         * stopTimer

notes:
* where signal is received:
self.connect(self, QtCore.SIGNAL('updateUI(int)'), self.setTime)

* where signal is emmitted:
self.main.emit(QtCore.SIGNAL('updateUI(int)'), int(counter))

"""
import os, sys
try:
    from PyQt4 import QtGui, QtCore
except Exception, e:
    print "PyQt4 module import error: " +str(e)

from pmdrtool_ui import Ui_MainWindow as pmdGUI


## Because maemo,python and qt4 are cunts this needs to be imported on the sub-class
## if you want to run the program in maemo-devices (works on desktops though..)
# try:
#     import pynotify
# except Exception, e:
#     print "Pynotify module import error: " +str(e)
#     log_mode = "std"

##timer QtCore.QBasicTimer()
log_mode = None


class MainWindow(QtGui.QMainWindow, pmdGUI):

    def __init__(self):
        ##QtGui.QMainWindow.__init__(self)
        super(MainWindow, self).__init__()

        ## make splash screen:
        # self.s_pic = QtGui.QPixmap('ff.png')
        # self.splash = QtGui.QSplashScreen(self.s_pic)
        # self.splash.show()
        # self.splash.showMessage("Foobar")
        # self.splash.finish(self)

        pmdGUI.setupUi(self, self)
        self.initUI()
        self.createCustomActions()
        self.createSysTray()
        self.sys_tray.show()

        print "MainWindow::__init__"

    def initUI(self):
        #self.resize(450,350)
        self.setWindowTitle('Pomodoro Tool')
        self.statusBar().showMessage('Ready, steady, Pomodoro time..')

        self.connect(self.actionQuit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.setStatusTip('Exit APP')

        self.toolBar.addAction(self.actionQuit)

        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open configs')
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.setStatusTip('Save configs')

        self.BREAKbutton.setStatusTip('Break Pomodoro')
        self.BREAKbutton.setShortcut('Ctrl+B')

        self.STARTbutton.setStatusTip('Start Pomodoro')
        self.STARTbutton.setShortcut('Ctrl+A')

        self.EXTERNALINTbutton.setStatusTip('Break Pomodoro for external interruption')
        self.EXTERNALINTbutton.setShortcut('Ctrl+E')
        
        self.INTERNALINTbutton.setStatusTip('Break Pomodoro for internal interruption')
        self.INTERNALINTbutton.setShortcut('Ctrl+I')

        self.setWindowIcon(QtGui.QIcon('pmd.png'))



    def createCustomActions(self):
        self.actionMinimize = QtGui.QAction('Minimize', self, triggered=self.hide)
        self.actionMinimize.setObjectName('actionMinimize')
        self.actionMinimize.setStatusTip('Minimize')

        self.actionMaximize = QtGui.QAction('Maximize', self, triggered=self.showMaximized)
        self.actionMaximize.setStatusTip('Maximize')

        self.actionRestore = QtGui.QAction('Restore', self, triggered=self.showNormal)

    def setTime(self, time):
        self.TIMERlabel.setText(str(time))


    def createSysTray(self):
        self.sys_tray = QtGui.QSystemTrayIcon(QtGui.QIcon('pmd.png'), self)
        self.sys_menu = QtGui.QMenu(self)

        self.sys_menu.addAction(self.actionMinimize)
        self.sys_menu.addAction(self.actionMaximize)
        self.sys_menu.addAction(self.actionRestore)
        self.sys_menu.addSeparator()
        self.sys_menu.addAction(self.actionQuit)
        self.sys_tray.setContextMenu(self.sys_menu)

    ## minimize to sys-tray
    def changeEvent(self, e):
        if (e.type() == QtCore.QEvent.WindowStateChange and self.isMinimized()):
            self.hide()
            e.accept()
            return
        else:
            super(MainWindow, self).changeEvent(e)


######################################################################
#                                                                    #
######################################################################


class Timer(QtCore.QBasicTimer):
    lock = QtCore.QReadWriteLock()
    currentTimer = 0
    timePmd = 0
    timeBreak = 0

    def __init__(self):

        super(Timer, self).__init__()
        self.stopped = False
        print "Timer::__init__()"
    def startTimer(self, ctrl):
        self.start(1000, ctrl)
    def stopTimer(self, ctrl=None):
        self.stopped = True
        self.stop()
    def secsToMin(self, time):
        mins = time / 60
        secs = time % 60
        if (mins < 10):
            mins = str("0")+str(mins)
        if (secs < 10):
            secs = str("0")+str(secs)
        comb = str(mins)+str(":")+str(secs)        
        return comb

######################################################################
#                                                                    #
######################################################################

#urgencies:
## n.set_urgency(pynotify.URGENCY_LOW)
## n.set_urgency(pynotify.URGENCY_NORMAL)
## n.set_urgency(pynotify.URGENCY_CRITICAL)
#timeout
## n.set_timeout(10000) # 10s
###
## def emit_notification()
## def handle_closed(n)


class Notify(object):
    def __init__(self, app_name):
        print "Notify __init__"
        global log_mode 
        ## because maemo sucks balls:
        try:
            import pynotify
        except Exception, e:
            print "Pynotify module import error: " +str(e)
            log_mode = "std"
        try:
            pynotify.init(app_name)
        except Exception, e:
            print "Cannot init the pynotify for the app"
            sys.exit(-1)

        log_mode = "screen"
        self.pynotify = pynotify

        #super(Notify, self).__init__(app_name)
        #self.m = pynotify.Notification.__init__(self, app_name)
        #self.setTimeout(1000) # 1s

    def setUrgency(self, mode):
        if mode == "low":
            self.set_urgency(self.URGENCY_LOW)
        elif mode == "normal":
            self.set_urgency(self.URGENCY_NORMAL)
        elif mode == "critical":
            self.set_urgency(self.URGENCY_CRITICAL)
        else:
            self.setNotification("setUrgency", "Cannot set Urgency to "+str(mode))

    def setTimeout(self, timeout):
        self.set_timeout(timeout)

    def setNotification(self, title, msg, timeout=None):
        if log_mode == "std":
            print str(title) +":: "+ str(msg)
        elif log_mode == "screen":
            m = self.pynotify.Notification(title, msg)
            if not m.show():
                print "************** Cannot show notification ******************"
            if timeout != None:
                m.set_timeout(timeout)
            else:
                m.set_timeout(1000)


######################################################################
#                                                                    #
######################################################################

class Controller(QtCore.QObject):
    intInterrupt = 0
    extInterrupt = 0
    pomodoro = 25 * 60
    breaks = 5 * 60

    def __init__(self):
        self.notification = Notify("Pmdr App")
        print "Controller::__init__"
        super(Controller, self).__init__()

        #app = QtGui.QApplication(sys.argv)

        self.main = MainWindow()

        ## create timer
        self.timer = Timer()
        self.timer.timePmd = self.pomodoro
        self.timer.timeBreak = self.breaks

        self.mode = ["Break", "None"]
        
        ## connect signals & slots
        self.main.connect(self.main.STARTbutton, QtCore.SIGNAL('pressed()'), self.handleTimers)
        self.main.connect(self.main.BREAKbutton, QtCore.SIGNAL('pressed()'), self.handleTimers)
        self.main.connect(self.main.EXTERNALINTbutton, QtCore.SIGNAL('pressed()'), self.handleTimers)
        self.main.connect(self.main.INTERNALINTbutton, QtCore.SIGNAL('pressed()'), self.handleTimers)



        ## show main ui
        ##self.main.show()
        #sys.exit(app.exec_())

    ## ui signal slot
    def handleTimers(self):
        ##print "Controller::handleTimers()"
        ##print self.main.sender().text()

        if self.mode[0] == None:
            if self.mode[1] == "pmdr":
                self.timer.currentTimer = self.breaks
                self.timer.startTimer(self)
                self.mode[0] = "break"
                return
            elif self.mode[1] == "break":
                self.timer.currentTimer = self.pomodoro
                self.timer.startTimer(self)
                self.mode[0] = "pmdr"
                return

        ## control timers when signal comes from ui
        if self.main.sender().text() == "Start":
            self.timer.currentTimer = self.pomodoro
            self.mode[0] = "pmdr"
            self.main.STARTbutton.setText("Stop")

        elif self.main.sender().text() == "Stop":
            self.main.STARTbutton.setText("Start")
            self.mode[0] = "stop"
            self.timer.stopTimer()


        elif self.main.sender().text() == "Break":
            self.timer.currentTimer = self.breaks
            self.mode[0] = "break"

        elif self.main.sender().text() == "Interrupt(int.)":
            self.timer.currentTimer = self.breaks
            self.intInterrupt += 1
            self.mode[0] = "break"
            ## print self.intInterrupt

        elif self.main.sender().text() == "Interrupt(ext.)":
            self.timer.currentTimer = self.breaks
            self.extInterrupt += 1
            self.mode[0] = "break"
            ## print self.extInterrupt

        self.timer.startTimer(self)


    ## we get timer events here. Do ui update
    def timerEvent(self, timer):
        ## print "Contoller::timerEvent()"

        ## start new timer when the oldone goes to zero
        if self.timer.currentTimer <= 0:
            self.notification.setNotification("i am title", "END POMODOROOOORORORO")
            #self.timer.stop()
            self.mode[1] = self.mode[0]
            self.mode[0] = None
            self.handleTimers()

        if self.mode[0] != "stop":
            self.timer.currentTimer -= 1
            counter = self.timer.secsToMin(self.timer.currentTimer)
            ## update ui
            self.main.setTime(counter)


        

######################################################################
#                                                                    #
######################################################################

def main():
    print sys.argv
    a = QtGui.QApplication(sys.argv)
    ctrl = Controller()
    ctrl.main.show()
    sys.exit(a.exec_())

    # if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        #QtGui.QMessageBox.critical(None, "Systray", "I couldn't detect sys tray on this system")
        # sys.exit(1)

if __name__ == "__main__":
  main()

