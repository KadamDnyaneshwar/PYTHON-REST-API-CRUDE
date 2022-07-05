
from asyncio.windows_events import NULL
from urllib import response
import mysql.connector as c
from chalice import Chalice
app=Chalice(app_name="exe")
import json
import ast


# Connect to the database
try:
    con = c.connect(host="localhost",
                    user="root",
                    passwd="infeon@1432",
                    database="swapnil",
                    auth_plugin='mysql_native_password')
    cursor=con.cursor()
except Exception as e:
        print(str(e))
        
res =json.dumps({"status":"400","message":"please provode proper info"})

@app.route('/adddata',methods=["POST"])
def add_emp():
        try:         
            emp=app.current_request.json_body
        # '{emp['ename']}'-f string dont knows this string he need to tell this f string use single qoute '.' 
            query=f"INSERT INTO empdata (id,ename,salary)values({emp['id']},'{emp['ename']}',{emp['salary']})"   
            cursor.execute(query)
            con.commit()
        except Exception as ex:
            return json.dumps({"Status":"Fail","Message":str(ex)})

@app.route('/showdata',methods=['GET'])
def shoe_emp():
    try:
        cursor=con.cursor()
        query="select * from empdata"
        cursor.execute(query)
        data=cursor.fetchall()
        print(data)    
    except Exception as ex: 
        return json.dumps({"Status":"Fail","Message":str(ex)})    
@app.route('/searchdata/{id}',methods=['GET'])
def serach_emp(id):
    try:
        if(int(id)<=0):
            return res     
        else:
            query1=f"select id from empdata where id={id}"
            cursor.execute(query1)
            data=cursor.fetchone()
            if(data !=None):
                query=f"select id,ename,salary from empdata where id={id}"
                cursor.execute(query)
                data=cursor.fetchone()
            #abstract syntax trees: ast
                return json.dumps({"Status":"Success","Results":ast.literal_eval(str(data))})
            else:
                return res                   
    except Exception as ex:
        return (res)

@app.route('/updatedata/{id}',methods=['PUT'])
def update_emp(id):    
    try:
        if int(id)<=0:
            return res
        else:
            query1=f"select id from empdata where id={id}"
            cursor.execute(query1)
            data=cursor.fetchone()
            print(data)
            if(data!= None): 
                emp=app.current_request.json_body
                print(emp)
                query=f"update empdata set ename='{emp['ename']}',salary={emp['salary']} where id={id}"
                cursor.execute(query)
                con.commit()
                return json.dumps({"Status":"success","Message":ast.literal_eval(str(emp))})
            else:
                return res
    except Exception:
        return (res)
@app.route('/delete/{id}',methods=['DELETE'])
def delete_emp(id):
    try:
        if int(id)<=0:
            return res        
        else:
            query1=f"select id from empdata where id={id}"
            cursor.execute(query1)
            data=cursor.fetchone()
            print(data)
            if(data!=None):
                query=f"delete from empdata where id={id}"
                cursor.execute(query)
                return({"Status":"success","Message":"deleted success empdata"})
            else:
                return res
    except Exception:
        return (res)



 







   