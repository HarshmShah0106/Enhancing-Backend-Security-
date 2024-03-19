import hashlib
import random
import mysql
import mysql.connector

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
salt_ID_16 = "b'IDy-feA6Q-Shntvf-nYs0g"
salt_ID_17 = "b'6X-3ihwfQc-YqJlcF32tFw"
salt_ID_18 = "b'JLJyO2qpRQKJfEVQDr5z4A"
salt_ID_19 = "b'KCs9p3bIQ9q5qW8BZwHQYw"
salt_ID_20 = "b'NIeAqAZBSeeyiYESkc_9ug"

def check_user(result):
     if result == ('No matching records found',):
        return False
     else:
         return True
     

    


def hash_password(password):
    hashed_password = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
    return hashed_password



mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database = "",
)

username_entered = input("Enter Username :")
hashed_username = hash_password(username_entered)



mycursor = mydb.cursor()

#Select data with condition
sql_username = "SELECT IFNULL((SELECT Username FROM Database WHERE Username = %s), 'No matching records found') AS Result"
val = [(hashed_username)]
mycursor.execute(sql_username, val)
myresult = mycursor.fetchall()
for result in myresult:
    if check_user(result) == False:
        print("No Login Details...")
        break
    break



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


password_entered = input("Enter Password: ")



Salt_ID_password = salt_ID_1
if Salt_ID_in_DB == "Salt_ID_1":
    Salt_ID_password=salt_ID_1
    
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
        print("Login Successful")
    elif passwd_result != password_compare :
        print("Wrong Password")
    else:
        print("Error Occured !!!")
