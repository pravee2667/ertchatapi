from flask import Flask,request
import mysql.connector
import json
from bs4 import BeautifulSoup
import string
import random
app = Flask(__name__)


mydb = mysql.connector.connect(
  host="40.77.22.5",
  user="preptalk-gi",
  passwd="Pact@1234",
  database="PrepTalk_GI"
)

@app.route("/")
def hello():
    return "Hello, SmartNinja!"

@app.route('/ertresponse',methods=['POST'])
def ertresponse():
    if request.method=='POST':
        result=request.get_json(force=True)
        
        
        res_botresponse=result['botResponse']
        lst = [random.choice(string.ascii_uppercase + string.digits) for n in range(8)]
        session_id = "".join(lst)
        ex_params=result['extractedParams']
        insert_userparams(session_id,ex_params)
        
        
        
        mycursor = mydb.cursor()
        sql = "insert into prepchat_dum(response,result) values (%s, %s)"
        val = ("High", "Low")
        mycursor.execute(sql, val)
        mydb.commit()
        
        
        
        
        return session_id
    return "Smart_Ninja2"

def insert_regparams(session_id,health_check,final_response,user_message):
    try:
        mycursor = mydb.cursor()
        sql = "insert into ert_regparams(sessionid,ert_check,health_status,bot_response) values (%s,%s,%s,%s)"
        val = (session_id,health_check,final_response,user_message)
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print(e)
        
def insert_userparams(session_id,ex_params):
    try:
        try:
            age=int(ex_params['age'])
        except Exception as e:
            print(e)
            age=27
            
        
        name=ex_params['name']
        fever=ex_params['fever']
        gender=ex_params['gender']
        
        travel=ex_params['travel']
        travel_period=int(ex_params['travel_period'])
        medical_history=ex_params['medical_history']
        travelled_country=ex_params['travelled_country']
        symptom_progression=ex_params['symptom_progression']
        
        mycursor = mydb.cursor()
        sql = "insert into ert_userparams(sessionid,age,name ,gender ,fever_status,travel,travel_period,medical_history,travelled_country,symptoms_progression) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (session_id,age,name ,gender ,fever,travel,travel_period,medical_history,travelled_country,symptom_progression)
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print(e)

        

def insert_healthparams(session_id,ex_params):
    symptoms=ex_params['symptoms']
    medical_condition=ex_params['medical_condition']
    
        
        
    
    

@app.route('/home')
def home():
    return "Smart_Ninja2"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
