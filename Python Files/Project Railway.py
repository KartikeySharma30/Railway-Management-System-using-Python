#Kartikey Sharma
import mysql.connector
import random
from tkinter import *
Dict_Train={"MUMBAI CENTRAL - AHMEDABAD AC DURONTO EXP":["MUMBAI CENTRAL","AHMEDABAD JN","SURENDRANAGAR","RAJKOT JN"],"AHMEDABAD - MUMBAI CENT AC DURONTO EXP":["RAJKOT JN","SURENDRANAGAR","AHMEDABAD JN","MUMBAI CENTRAL"]}
UserLog=mysql.connector.connect(host="localhost",user="root",passwd="Kartikey30",database="ProjectRailway")
C1=UserLog.cursor()
def Login():
    
    Login_User=Tk()
    Login_User.title("Login")
    e=Entry(Login_User,width=30).pack()
    Data_PasswordEnterInput=Entry(Login_User,width=30).grid(row=1,column=2)
    def SubmitClick():
        
        Label1=Label(Login,text=e.get())
        Label1.pack()
    CoustomerData_UserName_Ask=Label(Login_User,text="Enter User Name :").grid(row=0,column=0)
    CoustomerData_Password_Ask=Label(Login_User,text="Enter Password :").grid(row=1,column=0)
    Data_UserNameEnterInput=Entry(Login_User,width=30).grid(row=0,column=1)
    Data_PasswordEnterInput=Entry(Login_User,width=30).grid(row=1,column=1)
    Submit_Button_Login=Button(Login_User,text="Submit",command=SubmitClick).grid(row=2,column=1)
    
    def ChkCMD():
        Chk_U_UN=("Select user_Name From coustomer_data ")
        C1.execute(Chk_U_UN)
        UN_chk=C1.fetchall()
        for  usr_n in UN_chk:
            if(UserNameChk in usr_n):
                print("Verified User")
                break
            else:
                print("User Not Found \nPls Register First!!!")
              
    Login_User.mainloop()
def temp():
    Password_UEntered=input("Enter Passoword :-")
    Chk_U_Pass="Select password from coustomer_data where user_Name =  %s"
    C1.execute(Chk_U_Pass,(LN,))
    Pass_chk=C1.fetchone()
    for Passwd in Pass_chk:
        if(Passwd==Password_UEntered):
            Label(text="Welcome").pack()
        print('''                                             
     Enter 1 : To Book Ticket
     Enter 2 : To Cancel Ticket
     Enter 3 : Train Status
      ''')
        try:
            userInput = int(input("Please Select An Above Option:-"))
        except ValueError:
            exit("\nHy! That's Not A Number")
        else:
            print("\n")
            if(userInput==1):
                From=input("From*:-")
                From_S="Select  * from station where Station_Name like %s limit 10"
                C1.execute(From_S,("%"+From+"%",))
                From_chk=C1.fetchall()
                for Frm in From_chk:
                    print(Frm)
                To=input("To*:-")
                To_S="Select  * from station where Station_Name like %s limit 10"
                C1.execute(To_S,("%"+To+"%",))
                To_chk=C1.fetchall()
                for To in To_chk:
                    print(To)
                Date_Of_Travel=input("Enter The Date Of Travelling :- ")       
        if(userInput==2):
                    CName=input("Enter Your Name :-")
                    CPNR=int(input("Enter Your PNR :-"))
        if(userInput==3):
                    TNo=int(input("Enter the Train No. :-"))
            #else:
               # print("Incorrect User Name or Password!!! \nEnter Again")
          
customer_data=Tk()
customer_data.geometry("500x500")
customer_data.minsize(500,500)
customer_data.maxsize(500,500)
customer_data.title("Project Railway")
LnButton=Button(customer_data,text="Login",command=Login,padx=65).grid(row=0,column=0)
ReButton=Button(customer_data,text="Register",padx=65).grid(row=0,column=1)
StfButton=Button(customer_data,text="Staff",padx=65).grid(row=0,column=2)
customer_data.mainloop()

def UserData():
    print('''-----------------------------Welcome----------------------------
---------------------------------To---------------------------------
---------------------------Registration---------------------------''')
    UserName=input("Enter your User Name :-")
    password=input("Enter PASSWORD :-")#minmum 8 characters
    confpassword=input("ReEnter PASSWORD :-")
    FName=input("Enter Your First Name :-")
    LName=input("Enter Your Last Name :-")
    UAge=int(input("Enter Your Age :-"))
    UEMail=input("Enter Your Email ID :-")
    UAadharNo=int(input("Enter Your Aadhar No. :-"))
    UPhNo=int(input("Enter Your Ph.No :-"))
    UCity=input("Enter Your City Name :-")
    UPinCode=int(input("Enter Your PinCode :-"))
    if(confpassword==password):            
        S="insert into COUSTOMER_DATA (user_Name,password,First_Name,Last_Name,Age,Email,Aadhar_No,Ph_No,City,PinCode) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s,%s)"
        Regisuser=(UserName,password,FName,LName,UAge,UEMail,UAadharNo,UPhNo,UCity,UPinCode)
        C1.execute(S,Regisuser)
        UserLog.commit()
        print("Data Entered \nSuccesfully!!!")
    else:
        print("Password Incorrect \nReEnter the data")
        UserData()
UserData()


def Staff():
    Pass_to_proceed=input("Enter The Password :-")
    if(Pass_to_proceed=="Admin"):
        print("Verifed")
    print('''
Enter 1 :Update Train Status
Enter 2 :Update Ticket Price
Enter 3 : Update Station Name ''')
    try:
        userInput = int(input("Please Select An Above Option:-"))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")
    if(userInput==3):
        NewStationName=input("Do u want U to Enter ONLY one Data Y/N")
        if(NewStationName==Y or OneData==y):
            EnterStation="insert into Station (Station_Name,Station_code) values(%s,%s)"
            StationName=input("Enter Station Name")
            C1.execute(EnterStation,StationName)
            UserLog.commit()    
Staff()






(RUserName.get(),RPasswd.get(),RF_Name.get(),RL_Name.get(),RAge.get(),REmail.get(),RAdharNo.get(),RPhNo.get(),RCity.get(),RPincode.get())

