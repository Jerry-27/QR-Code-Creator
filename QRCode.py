import pyqrcode
import png
from io import BytesIO

class qrCode:
    error = None
    version = None
    mode = 'binary'
    scale = 3
    
    # error: L,M,Q,H
    #version
    #mode: binary, numeric, alphanumeric, kanji
    #scale
    def __init__(self,background=(255,255,255),foreground='#000000',fileName='default.png'):
        self.savedData = None
        self.savedType = None
        self.moduleColor = foreground
        self.backgroundColor = background
        self.fileName = fileName
        self.imageBuffer = BytesIO()
    def create_code(self,cardtype,data):
        self.savedData = data
        self.savedType = cardtype

        if cardtype == 'contact':
            self.create_contact_info(data)
        elif cardtype == 'email':
            self.create_email(data)
        elif cardtype == 'sms':
            self.create_SMS(data)
        elif cardtype == 'event':
            self.create_event(data)
        elif cardtype == 'wifi':
            self.create_wifi(data)
        elif cardtype == 'text':
            self.create_text(data)    
        elif cardtype == 'url':
            self.create_url(data)
        elif cardtype == 'phone':
            self.create_phone(data)
        elif cardtype == 'geolocation':
            self.create_geolocation(data)
        
        return self._get_buffer_image()
    
    def create_wifi(self,data):
        output = ""
        if ('SSID' in data) and (data['SSID'] != None):
            output +="WIFI:S:"+data['SSID']+";"

            if('networkType' in data) and (data['networkType'] != None):
                output+="T:"+data['networkType']+";"

            if('password' in data) and ( data['password'] != None):
                output+="P:"+data['password']+";"

            if('hidden' in data) and (data['hidden'] != None):
                output+="H:"+data['hidden']+";"

            output+=";"
            
            self._create_image(output)
            return 1
        return 0
        
    def create_url(self,data):
        output = None
        if('url' in data) and (data['url'] != None):
            output = data['url']
            self._create_image(output)
            return 1
        return 0

    def create_text(self,data):
        output = None
        if('text' in data) and (data['text'] != None):
            output = data['text']
            self._create_image(output)
            return 1
        return 0
        
    def create_SMS(self,data):
        output = ""
        if('phoneNumber' in data) and (data['phoneNumber'] != None):
            output +="smsto:"+data['phoneNumber']

            if('text' in data) and (data['text'] != None):
                output +=":"+data['text']
            
            self._create_image(output)
            return 1
        return 0

        
    def create_phone(self,data):
        output = None
        if ('phoneNumber' in data) and (data['phoneNumber'] != None):
            output = "tel:"+data['phoneNumber']

            self._create_image(output)
            return 1
        return 0

    def create_geolocation(self,data):
        output = ""
        if ('latitude','longitude' in data) and ( data['latitude'] and data['longitude']):
            output = "geo:"+data['latitude']+","+data['longitude']
            if ('query' in data) and (data['query'] != None):
                output+="?q="+data['query']
            self._create_image(output)
            return 1
        return 0
      

    def create_email(self,data):
        status = ""
        print("in email")
        if('mailType' in data) and (data['mailType'] != None):
            if data['mailType'] == 'mailto':
                status = self.create_email_mailto(data)
            elif data['mailType'] == 'MATMSG':
                status = self.create_email_MATMSG(data)
            else:
                return status
        return status
    
    def create_email_mailto(self,data):
        output = ""
        status = ""

        if ('email' in data) and (data['email'] != None):
            output+= "mailto:"+data['email']
        else:
            output+= "mailto:temp@gmail.com"
        
        if('subject' in data) and (data['subject'] != None):
            output+="?subject="+data['subject']
            status = 1

        if('body' in data) and (data['body'] != None):
            if(status == 1):
                output+="&body="+data['body']
            else:
                output+="?body="+data['body']

        self._create_image(output)
        

    def create_email_MATMSG(self,data):
        output = ""
        
        if ('email' in data) and (data['email'] != None):
            output = "MATMSG:TO:"+data['email']

        if('subject' in data) and (data['subject'] != None):
            output+="SUB:"+data['subject']
        
        if('body' in data) and (data['body'] != None):
            if(status == 1):
                output+="BODY:"+data['body']
            
        output += ";;"
          
        self._create_image(output)   
   
    def create_contact_info(self,data):
        status = None
        if('cardType' in data) and (data['cardType'] != None):
            if data['cardType'] == 'vCard':
                status = self.create_vCard(data)
            elif data['cardType'] == 'MECard':
                status = self.create_MECard(data)
            else:
                return status
        return status
        
       
    def create_vCard(self,data):
        output = "BEGIN:VCARD\nVERSION:3.0\n"
        if ('name' in data) and data['name'] != None:
            output+="N:"+data['name']+"\n"
            
            if ('company' in data) and data['company'] != None:
                output+="ORG:"+data['company']+"\n"
            if ('title' in data) and (data['title'] != None):
                output+="TITLE:"+data['title']+"\n"            
                #title
            
            if ('telephone' in data) and data['telephone'] != None:
                output+="TEL:"+data['telephone']+"\n"
            
            if ('url' in data) and (data['url'] != None):
                output+="URL:"+data['url']+"\n"  

            if ('email' in data) and data['email'] != None:
                output+="EMAIL:"+data['email']+"\n"
                
            if ('address1' in data) and (data['address1'] != None):
                output+="ADR:"+data['address1']
            
                if ('address2' in data) and (data['address2'] != None):
                    output+= " "+data['address2']
                output+="\n"
            if('note' in data) and (data['note']!=None):
                output+="NOTE:"+data['note']+"\n"
            output+="END:VCARD"
            
            self._create_image(output)
            return 1
        return 0

    def create_MECard(self,data):
        output = "MECARD:"
        if ('name' in data) and data['name'] != None:
            output+="N:"+data['name']+";"
            
            if ('company' in data) and (data['company'] != None):
                output+="ORG:"+data['company']+";"
            
            if ('telephone' in data) and (data['telephone'] != None):
                output+="TEL:"+data['telephone']+";"
            
            if ('url' in data) and (data['url'] != None):
                output+="URL:"+data['url']+";"  

            if ('email' in data) and data['email'] != None:
                output+="EMAIL:"+data['email']+";"
                
            if ('address1' in data) and data['address1'] != None:
                output+="ADR:"+data['address1']
            
                if ('address2' in data) and data['address2'] != None:
                    output+=data['address2']
                output+=";"
            if (('title','note') in data) and (data['note'] != None or data['title']!=None):
                output+="NOTE:"
                if data['note'] != None:
                    output += data['note']
                if data['title'] != None:
                    output+="N:"+data['title']
                output+";"
            output+=";"
        
            self._create_image(output)
            return 1
        return 0

    def create_event(self,data):
        output = "BEGIN:VEVENT\n"
        if ('event title' in data) and (data['event title'] != None):
                output+="SUMMARY:"+data['event title']+"\n"
                
        if ('start date' in data) and (data['start date'] != None):
                output+="DTSTART:"+data['start date']+"T"+data['start time']+"Z\n"
                
        if ('end date' in data) and (data['end date'] != None):
                output+="DTEND:"+data['end date']+"T"+data['end time']+"Z\n"

        if ('location' in data) and (data['location'] != None):
                output+="LOCATION:"+data['location']+"\n"
                
        if ('description' in data) and (data['description'] != None):
                output+="DESCRIPTION:"+data['description']+"\n"

        #dst is -1   time zone is invered subtraction or add
        output +='END:VEVENT'
        print(output)
        self._create_image(output)
        return 1
    
    def date_conversion(self,data):
        pass
    def color_change(self,background,foreground):
        if foreground != None:
            self.moduleColor = foreground
        if background != None:
            self.backgroundColor = background

    def settings_change():
        pass

    def _create_image(self,output):
        self.lastCode = output
        qr = pyqrcode.create(output)
        self.imageBuffer = None
        self.imageBuffer = BytesIO()
        qr.png(self.imageBuffer, scale=10, module_color=self.moduleColor, background=self.backgroundColor)

        #qr.png(self.fileName, scale=10, module_color=self.moduleColor, background=self.backgroundColor)
        

    def _get_buffer_image(self):
        return self.imageBuffer.getvalue()

    def create_file(self,fullPath):
        qr = pyqrcode.create(self.lastCode)
        qr.png(fullPath, scale=10, module_color=self.moduleColor, background=self.backgroundColor)
    def remake(self):
        self._create_image(self.lastCode)
        return self.imageBuffer.getvalue()
    
    
