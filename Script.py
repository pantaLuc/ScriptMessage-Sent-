from __future__ import unicode_literals

import xlrd
from datetime import datetime
import pandas as pd 
import requests

fichier=xlrd.open_workbook("test.xlsx")
sheet = fichier.sheet_by_index(0)

Columns = {
  'TeacherName': 0,
  'NoTelephone': 1,
  'HeureCours':2,
  'JourCours':3,
  'Salle':4
    
}

rownumber=0
print(rownumber)
dateNow=datetime.now()
while(rownumber<sheet.nrows-1):
  df=pd.read_excel("test.xlsx")
  x = str(df['JourCours'][rownumber]).split(' ')[0] + ' ' + str(df['HeureCours'][rownumber])
  y=datetime.strptime(x,u'%Y-%m-%d %H:%M:%S')
  message="Bonjour Mr "+str(df['TeacherName'][rownumber])+u" Vous avez Cours de " +str(df['Cours'][rownumber])+" Le " +x +" en salle " +str(df["Salle"][rownumber])
  print(message)
  number=str(df["NoTelephone"][rownumber])
  print(number)
  if((y-dateNow).seconds/60<5):
    url='http://157.230.118.14/sms/'
    params={
      "phone":number.rstrip().encode("utf8"),
      "message":message.rstrip().encode("utf8")
    }
    
    responses=requests.get(url,params=params)
    print("sending message{} to {}".format(message,number))
    print(responses.status_code)
    print(responses.text)
  rownumber+=1