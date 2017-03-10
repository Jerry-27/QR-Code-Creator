#pyuic4 input.ui -o output.py
import time
import sys
import re
from PyQt4 import QtCore, QtGui

from UI import Ui_MainWindow
from QRCode import qrCode


#Contact    tab #5b9bd5    button #d6e6f5   90%
#Email    tab #ed7d31      button #fbe1d0 
#SMS      tab   #70ad47     button  #e3f0db
#Event    tab   #f43edf     button   #fccff7  
#Wifi     tab     #ffc000   button  #fff2cc
#Text     tab   #a5a5a5    button  #e6e6e6
#Url     tab   #4472c4   button   #d8e2f3
#Phone   tab  #ff9933   button  #ffe6cc
#Geo    tab #a062d0   button #e7d8f3
#self.label_contact.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_Email.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_sms.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_event.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_wifi.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_text.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_url.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_phone.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))
#self.label_geo.setPixmap(QtGui.QPixmap(_fromUtf8("code.png")))

class Main(QtGui.QMainWindow):
   
    def __init__(self):
        super(Main, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.createButtonSetup()
        self.colorButtonsSetup()
        self.qrClassSetup()
        self.labelButtonSetup()
        self.default()

    #This function creates and places the
    #default QR Codes in the label frames
    def default(self):
        data = {'text':'Enter Stuff'}
        
        buffer = self.contactQr.create_code('text',data)
        self.updateImageLabel('Contact',buffer)
        
        self.updateImageLabel('Email',buffer)
        self.updateImageLabel('SMS',buffer)
        self.updateImageLabel('Event',buffer)
        self.updateImageLabel('Wifi',buffer)
        self.updateImageLabel('Text',buffer)
        self.updateImageLabel('Url',buffer)
        self.updateImageLabel('Phone',buffer)
        self.updateImageLabel('Geo',buffer)

        self.emailQr.create_code('text',data)
        self.smsQr.create_code('text',data)
        self.eventQr.create_code('text',data)
        self.wifiQr.create_code('text',data)
        self.textQr.create_code('text',data)
        self.urlQr.create_code('text',data)
        self.phoneQr.create_code('text',data)
        self.geoQr.create_code('text',data)
        
    #Creates classes for each QR Type
    def qrClassSetup(self):
        self.contactQr = qrCode(fileName = 'contact.png')
        self.emailQr = qrCode(fileName = 'email.png')
        self.smsQr = qrCode(fileName = 'sms.png')
        self.eventQr = qrCode(fileName = 'event.png')
        self.wifiQr = qrCode(fileName = 'wifi.png')
        self.textQr = qrCode(fileName = 'text.png')
        self.urlQr = qrCode(fileName = 'url.png')
        self.phoneQr = qrCode(fileName = 'phone.png')
        self.geoQr = qrCode(fileName = 'geo.png')
    
    #This funciton attaches each create button
    #to the function which grabs data from the
    #input fields
    def createButtonSetup(self):
        
        contact_create = self.ui.pushButton_Create_Contact
        contact_create.clicked.connect(self.retrieveContact)
        
        email_create = self.ui.pushButton_Create_Email
        email_create.clicked.connect(self.retrieveEmail)

        sms_create = self.ui.pushButton_Create_SMS
        sms_create.clicked.connect(self.retrieveSMS)
        
        event_create = self.ui.pushButton_Create_Event
        event_create.clicked.connect(self.retrieveEvent)
        
        wifi_create = self.ui.pushButton_Create_Wifi
        wifi_create.clicked.connect(self.retrieveWifi)
        
        text_create = self.ui.pushButton_Create_Text
        text_create.clicked.connect(self.retrieveText)
        
        url_create = self.ui.pushButton_Create_Url
        url_create.clicked.connect(self.retrieveUrl)
        
        phone_create = self.ui.pushButton_Create_Phone 
        phone_create.clicked.connect(self.retrievePhone)
        
        geo_create = self.ui.pushButton_Create_Geo 
        geo_create.clicked.connect(self.retrieveGeo)

        showPas = self.ui.checkBox_3
        showPas.stateChanged.connect(self.showHide)

    #Connects the background and foreground
    #buttons to the proper color dialog  
    def colorButtonsSetup(self):

        self.ui.Background_button_Contact.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Contact.clicked.connect(self.colorPickerFore)
        
        self.ui.Background_button_Email.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Email.clicked.connect(self.colorPickerFore)
        
        self.ui.Background_button_SMS.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_SMS.clicked.connect(self.colorPickerFore)

        self.ui.Background_button_Event.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Event.clicked.connect(self.colorPickerFore)

        self.ui.Background_button_Wifi.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Wifi.clicked.connect(self.colorPickerFore)
        
        self.ui.Background_button_Text.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Text.clicked.connect(self.colorPickerFore)

        self.ui.Background_button_Url.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Url.clicked.connect(self.colorPickerFore)

        self.ui.Background_button_Phone.clicked.connect(self.colorPickerBack)
        self.ui.Foreground_button_Phone.clicked.connect(self.colorPickerFore)
        
        #self.ui.Background_button_Geo.clicked.connect(self.colorPickerBack)
        #self.ui.Foreground_button_Geo.clicked.connect(self.colorPickerFore)
        #self.ui.label_contact.clicked.connect(self.fileChoose)

    #Function adds an action to each label when it is clicked
    def labelButtonSetup(self):
        self.connect(self.ui.label_contact, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_email, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_sms, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_event, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_wifi, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_text, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_url, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_phone, QtCore.SIGNAL('clicked()'), self.fileChoose)
        self.connect(self.ui.label_geo, QtCore.SIGNAL('clicked()'), self.fileChoose)

    #Function used to save the selected QR code
    #in the selected location
    def fileChoose(self):
        ui = self.ui
        index = ui.tabWidget.currentIndex()
        name = ui.tabWidget.tabText(index)
        
        self.saveDialog = QtGui.QFileDialog()
        
        location = self.saveDialog.getSaveFileName(self, "Save QR Code",
                '', "Images (*.png)")

        if location:
            if name == 'Contact':
                self.contactQr.create_file(location)
            elif name == 'Email':
                self.emailQr.create_file(location)
            elif name == 'SMS':
                self.smsQr.create_file(location)
            elif name == 'Event':
                self.eventQr.create_file(location)
            elif name == 'Wifi':
                self.wifiQr.create_file(location)
            elif name == 'Text':
                self.textQr.create_file(location)
            elif name == 'Url':
                self.urlQr.create_file(location)
            elif name == 'Phone':
                self.phoneQr.create_file(location)
            elif name == 'Geo':
                self.geoQr.create_file(location)

    #Retrieves contact information and displays qr code
    def retrieveContact(self):

        ui = self.ui
        name = ui.lineEdit_NameBox_Contact.text()
        company = ui.lineEdit_CompanyBox_Contact.text()
        title = ui.lineEdit_TitleBox_Contact.text()
        tel = ui.lineEdit_TelephoneBox_Contact.text()
        website = ui.lineEdit_WebsiteBox_Contact.text()
        email = ui.lineEdit_EmailBox_Contact.text()
        address = ui.lineEdit_AddressBox_Contact.text()
        notes = ui.plainTextEdit_NotesBox_Contact.toPlainText()

        ctype = ui.comboBox_CardType_Contact.currentText()
        
        correction = ui.comboBox_Correction_Contact.currentText()
        encoding = ui.comboBox_Encoding_Contact.currentText()
        size = ui.comboBox_Size_Ciontact.currentText()

        #self.getButtonColor(self.ui.Background_button_Contact)
        #self.getButtonColor(self.ui.Foreground_button_Contact)

        settings = {'correction':correction,'encoding':encoding,'size':size}
        contact = {'cardType':ctype,'name':name,'company':company,'title':title,'telephone':tel,'url':website,
                  'email':email,'address1':address,'address2':'','note':notes}
        self.createQr(contact)
        
    #Retrieves email info and displays qr code
    def retrieveEmail(self):
        ui = self.ui
        mailtype = ui.comboBox_MailType_Email.currentText()
        recipient = ui.lineEdit_RecipientBox_Email.text()
        subject = ui.lineEdit_SubjectBox_Email.text()
        message = ui.plainTextEdit_Email.toPlainText()

        correction = ui.comboBox_Correction_Email.currentText()
        encoding = ui.comboBox_Encoding_Email.currentText()
        size = ui.comboBox_Size_Email.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        email ={'mailType':mailtype,'email':recipient,'name':subject,'body':message}
        self.createQr(email)

    #Retrieves sms info and displays qr code    
    def retrieveSMS(self):
        ui = self.ui

        recipientnumber = ui.lineEdit_TelephoneBox_SMS.text()
        message = ui.plainTextEdit_SMS.toPlainText()

        correction = ui.comboBox_Correction_SMS.currentText()
        encoding = ui.comboBox_Encoding_SMS.currentText()
        size = ui.comboBox_Size_SMS.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        sms = {'phoneNumber':recipientnumber,'text':message}
        self.createQr(sms)

    #Retrieves event informtion and displays qr code 
    def retrieveEvent(self):
        ui = self.ui
        timezone = ui.comboBox_Event.currentText()
        dst = ui.checkBox_Event.isChecked()
        title = ui.lineEdit_EventTitle_Event.text()
        location = ui.lineEdit_Location_Event.text()
        description = ui.plainTextEdit_Event.toPlainText()
        startPart= ui.dateTimeEdit_Event.dateTime()
        endPart = ui.dateTimeEdit_Event_2.dateTime()
        
        startDate = startPart.toString('yyyyMMdd')
        startTime = startPart.time()
        
        endDate = endPart.toString('yyyyMMdd')
        endTime = endPart.time()
        
        if dst:
            dst = -1*60*60   #-1 hour
        else:
            dst = 0
        
        timeZoneNumber = self.parseTZ(timezone)
        
        startTime = startTime.addSecs(timeZoneNumber+dst)
        endTime = endTime.addSecs(timeZoneNumber+dst)
        startTime = startTime.toString('hhmmss')
        endTime = endTime.toString('hhmmss')
        
        event = {'summary':title,'start date':startDate,'end date':endDate,
                 'start time':startTime,'end time':endTime,
                 'location':location,'description':description}

        self.createQr(event)

    #Gets the selection timezone and
    #returns a positive or negative number
    def parseTZ(self,timezone):

        p = re.compile('[+-]?\d')
        value = re.findall(p,timezone)

        if value:
            parse = value[0]
            parse2 = value[1] 

            hour = int(parse[1:len(parse)])
            minutes = int(parse2)*10
            
            if parse[0] =='+':
                number = (hour*-1*60*60)+(minutes*-1*60)
            elif parse[0] =='-':
               number = (hour*60*60)+(minutes*60) 
        else:
            number = 0
        
        return number
        
    #Retrieves wifi information and displays qr code  
    def retrieveWifi(self):
        ui = self.ui
        ssid = ui.lineEdit_SSID_Wifi.text()
        pas = ui.lineEdit_PasswordBox_Wifi.text()
        protect = ui.comboBox_Protection_Wifi.currentText()
        hidden = ui.checkBox_hidden_Wifi.isChecked()
        
        correction = ui.comboBox_Correction_Wifi.currentText()
        encoding = ui.comboBox_Encoding_Wifi.currentText()
        size = ui.comboBox_Size_Wifi.currentText()
        
        settings = {'correction':correction,'encoding':encoding,'size':size}
        wifi = {'SSID':ssid,'password':pas,'networkType':protect}
        self.createQr(wifi)
        
    #Retrieves text information and displays qr code   
    def retrieveText(self):
        ui = self.ui
        plaintext = ui.plainTextEdit_Text.toPlainText()

        correction = ui.comboBox_Correction_Text.currentText()
        encoding = ui.comboBox_Encoding_Text.currentText()
        size = ui.comboBox_Size_Text.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        text ={'text':plaintext}
        self.createQr(text)
        
    #Retrieves url information and displays qr code  
    def retrieveUrl(self):
        ui = self.ui
        plainurl = ui.lineEdit_Url.text()

        correction = ui.comboBox_Correction_Url.currentText()
        encoding = ui.comboBox_Encoding_Url.currentText()
        size = ui.comboBox_Size_Url.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        url = {'url':plainurl}
        self.createQr(url)
       
    #Retrieves phone information and displays qr code 
    def retrievePhone(self):
        ui = self.ui
        number = ui.lineEdit_PhoneNumber_Phone.text()

        correction = ui.comboBox_Correction_Phone.currentText()
        encoding = ui.comboBox_Encoding_Phone.currentText()
        size = ui.comboBox_Size_Phone.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        phone = {'phoneNumber':number}
        self.createQr(phone)
        
    #Retrieves geo information and displays qr code    
    def retrieveGeo(self):
        ui = self.ui
        lat = ui.lineEdit_Latitude_Geo.text()
        long = ui.lineEdit_Longitude_GEO.text()
        query = ui.lineEdit_Query_Geo.text()

        correction = ui.comboBox_Correction_Phone.currentText()
        encoding = ui.comboBox_Encoding_Phone.currentText()
        size = ui.comboBox_Size_Phone.currentText()

        settings = {'correction':correction,'encoding':encoding,'size':size}
        geo = {'lat':lat,'long':long,'query':query}
        self.createQr(geo)
        
    #Function updates the background button color
    def colorPickerBack(self):
        
        sender = self.sender()
        colorSelection = self.getButtonColor(sender)
        color = self.setButtonColor(colorSelection,sender)
        if color != None:
            self.updateImageColor('back',color)
         
    #Function updates the foreground button color
    def colorPickerFore(self):
        
        sender = self.sender()
        colorSelection = self.getButtonColor(sender)
        color = self.setButtonColor(colorSelection,sender)
        if color != None:
            self.updateImageColor('fore',color)

    #Function gets and return the current button color
    #by parseign the stylesheet(easiest/quickest way I found).
    def getButtonColor(self,button):
        text = button.styleSheet().split('QPushButton{background-color:')
        color = text[1][0:7]
        return color

    #Sets the color fo the button based on the colorDialog selection
    def setButtonColor(self,colorSelection,button):
        if colorSelection:
           color = QtGui.QColorDialog.getColor(QtGui.QColor(colorSelection))
           
        else:
            color = QtGui.QColorDialog.getColor()
        if color.isValid():
            colorName = color.name()
            button.setStyleSheet(("QPushButton{background-color:"+color.name()+";border-style:solid;border-width:1px;border-color: #999999;}\n"
"\n"
"QPushButton::hover{border-width:1px;border-style:solid;border-radius:1px;border-color:#000000;height:40;width:40;}"))
        else:
            colorName = None
        return colorName

    #Function updates the color of the button
    #and the qr code   
    def updateImageColor(self,backFore,color):
        ui = self.ui
        index = ui.tabWidget.currentIndex()
        name = ui.tabWidget.tabText(index)
        
        # Logic to determine whether fore/back
        # didn't want to retype 'fore' and 'back'
        if backFore == 'back':
            flag = 1
        elif backFore == 'fore':
            flag = 2
        else:
            flag = 0

        #Logic is used to determine which QR code class's colors are updated
        if name == 'Contact':

            #Logic is used to determine whether foreground or background
            #color is updated
            if flag == 1:
                self.contactQr.color_change(background=color,foreground=None) 
            elif flag == 2:
                self.contactQr.color_change(background=None,foreground=color)
            buffer = self.contactQr.remake() 
            self.updateImageLabel(name,buffer)

        elif name == 'Email':
            if flag == 1:
                self.emailQr.color_change(background=color,foreground=None)
            elif flag == 2:
                self.emailQr.color_change(background=None,foreground=color)
            buffer = self.emailQr.remake() 
            self.updateImageLabel(name,buffer)

        elif name == 'SMS':
            if flag == 1:
                self.smsQr.color_change(background=color,foreground=None) 
            elif flag == 2:
                self.smsQr.color_change(background=None,foreground=color)
            buffer = self.smsQr.remake()
            self.updateImageLabel(name,buffer)
            

        elif name == 'Event':
            if flag == 1:
                self.eventQr.color_change(background=color,foreground=None)
            elif flag == 2:
                self.eventQr.color_change(background=None,foreground=color)
            buffer = self.eventQr.remake()
            self.updateImageLabel(name,buffer)

        elif name == 'Wifi':
            if flag == 1:
                self.wifiQr.color_change(background=color,foreground=None)
            elif flag == 2:
                self.wifiQr.color_change(background=None,foreground=color)
            buffer = self.wifiQr.remake()
            self.updateImageLabel(name,buffer)

        elif name == 'Text':
            if flag == 1:
                self.textQr.color_change(background=color,foreground=None)
            elif flag == 2:
                self.textQr.color_change(background=None,foreground=color)
            buffer = self.textQr.remake()
            self.updateImageLabel(name,buffer)

        elif name == 'Url':
            if flag == 1:
                self.urlQr.color_change(background=color,foreground=None) 
            elif flag == 2:
                self.urlQr.color_change(background=None,foreground=color)
            buffer = self.urlQr.remake()
            self.updateImageLabel(name,buffer)

        elif name == 'Phone':
            if flag == 1:
                self.phoneQr.color_change(background=color,foreground=None) 
            elif flag == 2:
                self.phoneQr.color_change(background=None,foreground=color)
            buffer = self.phoneQr.remake()
            self.updateImageLabel(name,buffer)

        elif name == 'Geo':
            if flag == 1:
                self.geoQr.color_change(background=color,foreground=None) 
            elif flag == 2:
                self.geoQr.color_change(background=None,foreground=color)
            buffer = self.geoQr.remake()
            self.updateImageLabel(name,buffer)
            

    def updateImageLabel(self,tabName,imageBuffer):
        ui = self.ui
        
        img = QtGui.QImage()
        img.loadFromData(imageBuffer)
        
        if tabName == 'Contact':
            ui.label_contact.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Email':
            ui.label_email.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'SMS':
            ui.label_sms.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Event':
            ui.label_event.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Wifi':
            ui.label_wifi.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Text':
            ui.label_text.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Url':
            ui.label_url.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Phone':
            ui.label_phone.setPixmap(QtGui.QPixmap(img))
        elif tabName == 'Geo':
            ui.label_geo.setPixmap(QtGui.QPixmap(img))

    #This function grabs the for/back button colors
    #and data and updates the proper qr label 
    def createQr(self,data):
        ui = self.ui
        index = ui.tabWidget.currentIndex()
        name = ui.tabWidget.tabText(index)

        #Logic determines which colors to grab based on the selected tab
        if name == 'Contact':
            backColor = self.getButtonColor(ui.Background_button_Contact)
            foreColor = self.getButtonColor(ui.Foreground_button_Contact)
            self.contactQr.color_change(backColor,foreColor)
            buffer = self.contactQr.create_code('contact',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Email':
            backColor = self.getButtonColor(ui.Background_button_Email)
            foreColor = self.getButtonColor(ui.Foreground_button_Email)
            self.emailQr.color_change(backColor,foreColor)
            buffer = self.emailQr.create_code('email',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'SMS':
            backColor = self.getButtonColor(ui.Background_button_SMS)
            foreColor = self.getButtonColor(ui.Foreground_button_SMS)
            self.smsQr.color_change(backColor,foreColor)
            buffer = self.smsQr.create_code('sms',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Event':
            backColor = self.getButtonColor(ui.Background_button_Event)
            foreColor = self.getButtonColor(ui.Foreground_button_Event)
            self.eventQr.color_change(backColor,foreColor)
            buffer = self.eventQr.create_code('event',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Wifi':
            backColor = self.getButtonColor(ui.Background_button_Wifi)
            foreColor = self.getButtonColor(ui.Foreground_button_Wifi)
            self.wifiQr.color_change(backColor,foreColor)
            buffer = self.wifiQr.create_code('wifi',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Text':
            backColor = self.getButtonColor(ui.Background_button_Text)
            foreColor = self.getButtonColor(ui.Foreground_button_Text)
            self.textQr.color_change(backColor,foreColor)
            buffer = self.textQr.create_code('text',data)
            self.updateImageLabel(name, buffer)
            
        elif name == 'Url':
            backColor = self.getButtonColor(ui.Background_button_Url)
            foreColor = self.getButtonColor(ui.Foreground_button_Url)
            self.urlQr.color_change(backColor,foreColor)
            buffer = self.urlQr.create_code('url',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Phone':
            backColor = self.getButtonColor(ui.Background_button_Phone)
            foreColor = self.getButtonColor(ui.Foreground_button_Phone)
            self.phoneQr.color_change(backColor,foreColor)
            buffer = self.phoneQr.create_code('phone',data)
            self.updateImageLabel(name,buffer)
            
        elif name == 'Geo':
            backColor = self.getButtonColor(ui.Background_button_Geo)
            foreColor = self.getButtonColor(ui.Foreground_button_Geo)
            self.geoQr.color_change(backColor,foreColor)
            buffer = self.geoQr.create_code('geo',data)
            self.updateImageLabel(name,buffer)
        else:
            print("Somthing went wrong...")

    #This function is used to show/hide the wifi password
    def showHide(self):
        if self.ui.checkBox_3.isChecked():
            self.ui.lineEdit_PasswordBox_Wifi.setEchoMode(QtGui.QLineEdit.Password)
        else:      
            self.ui.lineEdit_PasswordBox_Wifi.setEchoMode(QtGui.QLineEdit.Normal)  

    #This function gets the mouse position
    def mousePressEvent(self, event):
        self.offset = event.pos()

    #This function is used to move the window 
   # def mouseMoveEvent(self, event):
    #    x = event.globalX()
     #   y = event.globalY()
      #  x_w = self.offset.x()
       # y_w = self.offset.y()
        #self.move(x-x_w, y-y_w)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
