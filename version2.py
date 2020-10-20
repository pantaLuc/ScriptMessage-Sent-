import xlrd
from datetime import datetime
import pandas as pd 
import requests

name = input('file: ')
wb = xlrd.open_workbook(name)

sheet = wb.sheet_by_index(0)

lookup = {
  'TeacherName': 0,
  'NoTelephone': 1,
  'HeureCours':2,
  'JourCours':3,
  'Salle':4
    
}

for rownumber in range(0, sheet.nrows-1):
  print(rownumber)
  row = sheet.row(rownumber)
  #col=sheet.col(rownumber)
  #teachername, noTelephone,heureCours,jourCours ,salle= row[lookup['TeacherName']].value, row[lookup['NoTelephone']].value ,row[lookup['HeureCours']],row[lookup['JourCours']],row[lookup['Salle']]
  df=pd.read_excel("test.xlsx")
  x = str(df['JourCours'][rownumber]).split(' ')[0] + ' ' + str(df['HeureCours'][rownumber])
  y=datetime.strptime(x,'%Y-%m-%d %H:%M:%S')
  print(abs(datetime.now() - y).seconds / 60)
  print(x)
  message="Bonjour Mr"+str(df['TeacherName'])+"Vous avez Cours de " +str(df['Cours'])+"Le " +str(df['JourCours'])+" en salle" +str(df["Salle"])
  print(message)
  #if((y-datetime.now)<=5):
   
  #print("teacherName: %s, noTelephone: %s, heureCours:%s,joursCours:%s" % (teachername,noTelephone,heureCours,jourCours))


def notification(message):
  url='http://157.230.118.14/sms/'
  with open('gautier.py','r') as f:
    nums=f.readlines()
    for i, num in enumerate(nums):
      num=num.rstrip()
      params={
        "ph"
      }
