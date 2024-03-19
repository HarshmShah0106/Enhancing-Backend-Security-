from flask import Flask,render_template,Response,request
import hashlib
import random
import base64
import uuid
import mysql
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
     host="",
     user="",
     passwd="",
     database = ""
 )
mycursor = mydb.cursor()

def hash_password(password):
    hashed_password = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
    return hashed_password

#Salt ID creation
salt_ID_1 = "b'2_JcLfvfRl-Ho9dEwwo70Q"
salt_ID_2 = "b'ub98OngPT3Sj3gDOdEvHFw"
salt_ID_3 = "b'KlpN-ueSTKiG33ADkxF63w"
salt_ID_4 = "b'HP-8ljICR9mBV237yC3rwQ"
salt_ID_5 = "b'gIDPEm5JSf6S68n0hoxAbg"
salt_ID_6 = "b'FCRXdx2HTw6017ywsxb3CQ"
salt_ID_7 = "b'ulnUMSRmQtOooXU6aa0hVw"
salt_ID_8 = "b'VKnsuoKnQq6lMfFK7HFiaA"
salt_ID_9 = "b'9KL-_CKURkeRcIzDiMMYvg"
salt_ID_10 = "b'dN3Lsem1Tk6L8X9o9wvgiA"
salt_ID_11 = "b'-gpKagi2Qd2UKuFFHgqsaQ"
salt_ID_12 = "b'G7IRG0SjRn6pVk4Tv51iWQ"
salt_ID_13 = "b'en5ckxsJTTOHhun9C44duA"
salt_ID_14 = "b'm2MXKiTZS5SCGW1DAjjYWQ"
salt_ID_15 = "b'h_ypKnfOQ0mBdRVmzOc4Tw"
salt_ID_16 = "b'SDy-feA6Q-Shntvf-nYs0g"
salt_ID_17 = "b'6X-3ihwfQc-YqJlcF32tFw"
salt_ID_18 = "b'JLJyO2qpRQKJfEVQDr5z4A"
salt_ID_19 = "b'KCs9p3bIQ9q5qW8BZwHQYw"
salt_ID_20 = "b'NIeAqAZBSeeyiYESkc_9ug"

# Grouping of Salt IDs
salt_ID = [salt_ID_1,salt_ID_2,salt_ID_3,salt_ID_4,salt_ID_5,salt_ID_6,salt_ID_7,salt_ID_8,salt_ID_9,salt_ID_10,salt_ID_11,salt_ID_12,salt_ID_13,salt_ID_14,salt_ID_15,salt_ID_16,salt_ID_17,salt_ID_18,salt_ID_19,salt_ID_20]

List_salt_ID = ["Salt_ID_1","Salt_ID_2","Salt_ID_3","Salt_ID_4","Salt_ID_5","Salt_ID_6","Salt_ID_7","Salt_ID_8","Salt_ID_9","Salt_ID_10","Salt_ID_11","Salt_ID_12","Salt_ID_13","Salt_ID_14","Salt_ID_15","Salt_ID_16","Salt_ID_17","Salt_ID_18","Salt_ID_19","Salt_ID_20"]


def register(username, password):

    #Random Salt ID Allocation to UserName
    random_salt_id = random.choice(salt_ID)
    username_stored = random_salt_id + username
    hashed_username = hash_password(username)

    password_usedto_hash = random_salt_id + password
    hashed_password = hash_password(password_usedto_hash)

    #Code to find out salt id used
    salt_ID_used = username_stored.replace(username,"")

    if salt_ID_used == salt_ID_1:
        # print("Salt id 1 is used")
        salt_ID_Stored = "Salt_ID_1"

    elif salt_ID_used == salt_ID_2:
        # print("Salt id 2 is used")
        salt_ID_Stored = "Salt_ID_2"

    elif salt_ID_used == salt_ID_3:
        # print("Salt id 3 is used")
        salt_ID_Stored = "Salt_ID_3"

    elif salt_ID_used == salt_ID_4:
        # print("Salt id 4 is used")
        salt_ID_Stored = "Salt_ID_4"

    elif salt_ID_used == salt_ID_5:
        # print("Salt id 5 is used")
        salt_ID_Stored = "Salt_ID_5"

    elif salt_ID_used == salt_ID_6:
        # print("Salt id 6 is used")
        salt_ID_Stored = "Salt_ID_6"

    elif salt_ID_used == salt_ID_7:
        # print("Salt id 7 is used")
        salt_ID_Stored = "Salt_ID_7"

    elif salt_ID_used == salt_ID_8:
        # print("Salt id 8 is used")
        salt_ID_Stored = "Salt_ID_8"

    elif salt_ID_used == salt_ID_9:
        # print("Salt id 9 is used")
        salt_ID_Stored = "Salt_ID_9"

    elif salt_ID_used == salt_ID_10:
        # print("Salt id 10 is used")
        salt_ID_Stored = "Salt_ID_10"

    elif salt_ID_used == salt_ID_11:
        # print("Salt id 11 is used")
        salt_ID_Stored = "Salt_ID_11"

    elif salt_ID_used == salt_ID_12:
        # print("Salt id 12 is used")
        salt_ID_Stored = "Salt_ID_12"

    elif salt_ID_used == salt_ID_13:
        # print("Salt id 13 is used")
        salt_ID_Stored = "Salt_ID_13"

    elif salt_ID_used == salt_ID_14:
        # print("Salt id 14 is used")
        salt_ID_Stored = "Salt_ID_14"

    elif salt_ID_used == salt_ID_15:
        # print("Salt id 15 is used")
        salt_ID_Stored = "Salt_ID_15"

    elif salt_ID_used == salt_ID_16:
        # print("Salt id 16 is used")
        salt_ID_Stored = "Salt_ID_16"

    elif salt_ID_used == salt_ID_17:
        # print("Salt id 17 is used")
        salt_ID_Stored = "Salt_ID_17"

    elif salt_ID_used == salt_ID_18:
        # print("Salt id 18 is used")
        salt_ID_Stored = "Salt_ID_18"

    elif salt_ID_used == salt_ID_19:
        # print("Salt id 19 is used")
        salt_ID_Stored = "Salt_ID_19"

    elif salt_ID_used == salt_ID_20:
        # print("Salt id 20 is used")
        salt_ID_Stored = "Salt_ID_20"

    print(f"Username : {hashed_username}")
    print(f"Password : {hashed_password}")
    print(f"Salt_ID : {salt_ID_Stored}")

    sqlformula = "Insert into Database (UserName,Password,Salt_ID) values (%s,%s,%s)"

    Values = [(hashed_username,hashed_password,salt_ID_Stored)]

    mycursor.executemany(sqlformula,Values)

    mydb.commit()

def check_user(result):
     if result == ('No matching records found',):
        return False
     else:
         return True
     

def Login(username_entered, password_entered):

    hashed_username = hash_password(username_entered)

    mycursor = mydb.cursor()

    # Select data with condition
    sql_username = "SELECT IFNULL((SELECT Username FROM Database WHERE Username = %s), 'No matching records found') AS Result"
    val = [(hashed_username)]
    mycursor.execute(sql_username, val)
    myresult = mycursor.fetchall()
    for result in myresult:
        if result == ('No matching records found',):
            user_found = "Login Details not found !"
            return user_found
        else:
            user_found = "Login Details found"
            return user_found, result
        

        
    if check_user(result) == True:
    
        sql_password = "SELECT Salt_ID from Database where Username = %s;"
    
        mycursor.execute(sql_password,val)
        myresult_password = mycursor.fetchall()

        for salt_result in myresult_password:
            Salt_ID_in_DB = salt_result
            break

    Salt_ID_in_DB = str(Salt_ID_in_DB)
    Salt_ID_in_DB = Salt_ID_in_DB.replace("'","")
    Salt_ID_in_DB = Salt_ID_in_DB.replace(",","")
    Salt_ID_in_DB = Salt_ID_in_DB.replace("(","")
    Salt_ID_in_DB = Salt_ID_in_DB.replace(")","")

    
    if Salt_ID_in_DB == "Salt_ID_1":
        Salt_ID_password = salt_ID_1

    elif Salt_ID_in_DB == "Salt_ID_2":
        Salt_ID_password = salt_ID_2

    elif Salt_ID_in_DB == "Salt_ID_3":
        Salt_ID_password = salt_ID_3    
        
    elif Salt_ID_in_DB == "Salt_ID_4":
        Salt_ID_password = salt_ID_4    

    elif Salt_ID_in_DB == "Salt_ID_5":
        Salt_ID_password = salt_ID_5   

    elif Salt_ID_in_DB == "Salt_ID_6":
        Salt_ID_password = salt_ID_6    

    elif Salt_ID_in_DB == "Salt_ID_7":
        Salt_ID_password = salt_ID_7   

    elif Salt_ID_in_DB == "Salt_ID_8":
        Salt_ID_password = salt_ID_8   

    elif Salt_ID_in_DB == "Salt_ID_9":
        Salt_ID_password = salt_ID_9  

    elif Salt_ID_in_DB == "Salt_ID_10":
        Salt_ID_password = salt_ID_10   

    elif Salt_ID_in_DB == "Salt_ID_11":
        Salt_ID_password = salt_ID_11  

    elif Salt_ID_in_DB == "Salt_ID_12":
        Salt_ID_password = salt_ID_12   

    elif Salt_ID_in_DB == "Salt_ID_13":
        Salt_ID_password = salt_ID_13

    elif Salt_ID_in_DB == "Salt_ID_14":
        Salt_ID_password = salt_ID_14   

    elif Salt_ID_in_DB == "Salt_ID_15":
        Salt_ID_password = salt_ID_15   

    elif Salt_ID_in_DB == "Salt_ID_16":
        Salt_ID_password = salt_ID_16    

    elif Salt_ID_in_DB == "Salt_ID_17":
        Salt_ID_password = salt_ID_17   

    elif Salt_ID_in_DB == "Salt_ID_18":
        Salt_ID_password = salt_ID_18   

    elif Salt_ID_in_DB == "Salt_ID_19":
        Salt_ID_password = salt_ID_19   

    elif Salt_ID_in_DB == "Salt_ID_20":
        Salt_ID_password = salt_ID_20 


    password_compare = Salt_ID_password + username_entered + password_entered
    password_compare = hash_password(password_compare)

    sql_password_compare = "Select Password from Database Where Username = %s and Salt_ID = %s"
    val_Password_compare = (hashed_username,Salt_ID_in_DB)
    mycursor.execute(sql_password_compare, val_Password_compare)
    myresultforpass = mycursor.fetchone()
    for passwd_result in myresultforpass:
        if passwd_result == password_compare :
            value_pass = "Login Successful"
            return value_pass
        elif passwd_result != password_compare :
            value_pass = "Wrong Password"
            return value_pass
        else:
            value_pass = "Error Occured !!!"
            return value_pass



@app.route("/", methods = ['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        register(username, password)

    return render_template("Register.html")


@app.route("/Login", methods = ['GET', 'POST'])
def SignIn():
    user_found = ""
    result = ""
    pass_found = ""

    if request.method == 'POST':
        username_entered = request.form.get('username_entered')
        password_entered = request.form.get('password_entered')

        user_found, result, pass_found = Login(username_entered,password_entered) 

    return render_template("Login.html", user_found = user_found,result = result, pass_found = pass_found)
    

if __name__=='__main__':
    app.run(debug = True)
