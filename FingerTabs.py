# Updated so a PyQT4 Designer TabWidget can be promoted to a FingerTabWidget

from PyQt4 import QtGui, QtCore
 
class FingerTabBarWidget(QtGui.QTabBar):
    def __init__(self, parent=None, *args, **kwargs):
        self.tabSize = QtCore.QSize(kwargs.pop('width',250), kwargs.pop('height',300))
        QtGui.QTabBar.__init__(self, parent, *args, **kwargs)
        self.status = [False] *9
        self.status[0] = True
        self.prev = 0
        self._paintDef()

    def _paintDef(self):
        self.pen_default = QtGui.QPen(QtGui.QColor(0,0,0),4)
        
        self.pen_contact = QtGui.QPen(QtGui.QColor(91, 155, 213),4)
        self.pen_email = QtGui.QPen(QtGui.QColor(237, 125, 49),4)
        self.pen_text = QtGui.QPen(QtGui.QColor(165, 165, 165),4)

        self.pen_wifi = QtGui.QPen(QtGui.QColor(255, 192, 0),4)
        self.pen_url = QtGui.QPen(QtGui.QColor(68, 114, 196),4)
        self.pen_sms = QtGui.QPen(QtGui.QColor(112, 173, 71),4)

        self.pen_phone = QtGui.QPen(QtGui.QColor(255, 153, 51),4)
        self.pen_geo = QtGui.QPen(QtGui.QColor(160, 98, 208),4)
        self.pen_event = QtGui.QPen(QtGui.QColor(244, 62, 223),4)

    def paintEvent(self, event):
        
        for index in range(self.count()):
            
            name = self.tabText(index)
            
            #print(name," : ",index)
            if name == "Contact" and self.status[index]:
                self.paint(index,self.pen_contact)
            elif name == "Wifi" and self.status[index]:
                self.paint(index,self.pen_wifi)
            elif name == "Url" and self.status[index]:
                self.paint(index,self.pen_url)
            elif name == "Email"and self.status[index]:
                self.paint(index,self.pen_email)
            elif name == "Text"and self.status[index]:
                self.paint(index,self.pen_text)
            elif name == "Phone"and self.status[index]:
                self.paint(index,self.pen_phone)
            elif name == "SMS" and self.status[index]:
                self.paint(index,self.pen_sms)
            elif name == "Geo" and self.status[index]:
                self.paint(index,self.pen_geo)
            elif name == "Event" and self.status[index]:
                self.paint(index,self.pen_event)
            else:
                self.paint(index,self.pen_default)
    def paint(self,index,pen):
        painter = QtGui.QStylePainter(self)
        option = QtGui.QStyleOptionTab()

        painter.setPen(pen)
        
        self.initStyleOption(option, index)
        tabRect = self.tabRect(index)
        tabRect.moveLeft(10)
        painter.drawControl(QtGui.QStyle.CE_TabBarTabShape, option)
        painter.drawText(tabRect, QtCore.Qt.AlignVCenter |\
                            QtCore.Qt.TextDontClip, \

                            self.tabText(index));
        painter.end()
            
    def change(self,index):
        s = self.tabText(index)
        self.status[self.prev] = False
        self.prev = index
        self.status[index] = True
        return 1
        
    def tabSizeHint(self,index):
        return self.tabSize
    
# Shamelessly stolen from this thread:
#   http://www.riverbankcomputing.com/pipermail/pyqt/2005-December/011724.html
class FingerTabWidget(QtGui.QTabWidget):
    """A QTabWidget equivalent which uses our FingerTabBarWidget"""
    def __init__(self, parent, *args):
        QtGui.QTabWidget.__init__(self, parent, *args)
        self.setTabBar(FingerTabBarWidget(self))
