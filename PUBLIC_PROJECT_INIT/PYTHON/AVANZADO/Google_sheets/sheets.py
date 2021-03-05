"""
Acceder y editar a los APIs de Google Sheets usando el modulo 'gspread'.
Revisar la documentacion para tener un panomara más amplio:
link: 'https://gspread.readthedocs.io/en/latest/'
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Google_sheets/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Practice").sheet1
data = sheet.get_all_records()

#update = sheet.cell(1,1).value
update = sheet.update("A2","AJI AMARILLO")
pprint(update)