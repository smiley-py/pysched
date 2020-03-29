# -*- coding: utf-8 -*-
import requests,json,os

class Integration():
    def get_password_salt(self,security_service_url):
        response = requests.get(
            url=security_service_url +"/generatesalt"           
        )
        return json.loads(response.content)["value"]
    
    def get_password(self,security_service_url,length):
        session = requests.Session()
        
        values = {
            "length": length               
        }
        response = session.get(
            url=security_service_url+"/generatepassword",
            data=values
        )
        
        session.close()
        return json.loads(response.content)["value"]
    
    def get_password_hashed(self,security_service_url, password_salt,password):        
        session = requests.Session()
        
        values = {
            "password": password, 
            "salt": password_salt              
        }
        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
    
        url = security_service_url+"/gethashed"
        
        response = session.get(
            url=url,
            data=values
        )
        
        session.close()
        return json.loads(response.content)["value"]
    
    def upload_file(self,profile_image,user_mail,username,exportimport_service_url):
        session = requests.Session()
        exportimport_service_id_image = 0

        file_name = profile_image.filename 
        file_path = 'Images/' + str(username) + '.' +file_name.split('.')[1]
        profile_image.save(file_path)   
        f = open(file_path, 'rb')
        
        files = {'file_data':(profile_image.filename, f)}
        
        values = {
            "user_mail": user_mail,
            "description": "user profile image"                
        }
        
        response = session.post(
            url=exportimport_service_url+"/importfile",  
            files=files,
            data=values            
            )
        
        exportimport_service_id_image = json.loads(response.content)["id"]
        f.close()
        #os.remove(file_path)  
        
        session.close()
        return exportimport_service_id_image
    
    
    def send_mail(self,kwagrs):       
        session = requests.Session()
        
        headers = {
            "content-type": "application/json"
        }
        
        values = {
            "smtp" : kwagrs["media_service_smtp"],
            "port" : kwagrs["media_service_port"],
            "user_mail" : kwagrs["media_service_user"],
            "password" : kwagrs["media_service_password"],
            "tolist" : kwagrs["tolist"],
            "cclist" : kwagrs["cclist"],
            "bcclist" : kwagrs["bcclist"],
            "subject" : kwagrs["subject"],
            "body" : kwagrs["body"]
        }
    
        url =str(kwagrs["media_service_url"]) + "/sendmail"

        response = session.post(
            url=url,
            data =values
        )
        
        session.close()
        return response.content

