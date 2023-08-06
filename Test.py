from tkinter import *
from tkinter import ttk
import random
import datetime
import mysql.connector
from tkcalendar import *
UserLog=mysql.connector.connect(host="localhost",user="root",passwd="Kartikey30",database="projectrailway")
C1=UserLog.cursor()
import csv
def book():
    BookMenu= Tk() 
    BookMenu.title('Book Menu') 
    BookMenu.geometry('600x500')
    BookMenu.minsize(600,500)
    BookMenu.maxsize(600,500)
    BookMenu.iconbitmap("favicon.ico")
    Frm = StringVar()
    To = StringVar()
    Label(BookMenu,text="From :").grid(row=0,column=0,pady=10)
    Label(BookMenu,text="To:").grid(row=1,column=0,pady=10)   
    FromTicket = ttk.Combobox(BookMenu, width = 27, textvariable = Frm)
    ToTicket = ttk.Combobox(BookMenu, width = 27, textvariable = To)
    From_Chk="Select Station_Name From station"
    C1.execute(From_Chk)
    F1=C1.fetchall()
    b=[]
    for c in F1:
        c=list(c)
        b.append(c)
    b=tuple(b)
    FromTicket['values']=b
    ToTicket['values']=b
    FromTicket.grid(column = 1, row = 0)
    ToTicket.grid(column = 1, row = 1)
    FromTicket.current()
    ToTicket.current()
    def Findtrain():
        x=FromTicket.get()
        y=ToTicket.get()
        if(x==""):
            Label(BookMenu,text="Field is Empty",fg="red").grid(row=0,column=2,pady=10)
        else:
            Label(BookMenu,text="                                                   ").grid(row=0,column=2,pady=10)
        if(y==""):
            Label(BookMenu,text="Field is Empty",fg="red").grid(row=1,column=2,pady=10)
        else:
            Label(BookMenu,text="                                                   ").grid(row=1,column=2,pady=10)
            lenM=len(x)
            lenD=len(y)
            k=""
            m=""
            for i in range(1,lenD-2): #{ DELHI CANT  }
                k+=y[i]
            for i in range(1,lenM-2):
                m+=x[i]
            k=str(k)
            m=str(m)
            m.capitalize()
            SearchName=k
            SearchName.capitalize() 
            f=open("book2.csv","r+")
            r=csv.DictReader(f)
            FTrains = StringVar()
            Trains = ttk.Combobox(BookMenu, width =50, textvariable = FTrains)# {S:[a,b,c,d]}
            FindT=[]
            Var=0
            Var1=0
            for c in r:
                Var1+=1
                g=c.get('Stations')
                if(SearchName in g and m in g):
                    FindT.append(c.get('TRAIN NAME'))
                    Var+=1
                if(SearchName not in g and m not in g):
                    if(Var==0 and Var1==26):
                        TrainNotFound=Tk()
                        TrainNotFound.iconbitmap("favicon.ico")
                        TrainNotFound.title("Not Found")
                        def YesMore():
                            TrainNotFound.destroy()
                        def NoMore():
                            TrainNotFound.destroy()
                            BookMenu.destroy()
                        Label(TrainNotFound,text="No Train Available at this Route ").grid(row=0,column=0,pady=10)
                        Label(TrainNotFound,text="Do You Want To Search More Trains?? ").grid(row=1,column=0,pady=10)
                        Button(TrainNotFound,text="Yes",command=YesMore,padx=30).grid(row=2,column=0)
                        Button(TrainNotFound,text="No",command=NoMore,padx=30).grid(row=2,column=1)
                        TrainNotFound.mainloop()                                   
            FindT=tuple(FindT)
            Trains['values']=FindT
            
            def GenerateTicket():
                D=cal.selection_get()
                D=str(D)
                GenerateTicket=Tk()
                GenerateTicket.geometry("800x700")
                GenerateTicket.iconbitmap("favicon.ico")
                GenerateTicket.title("Booking")
                NameTicket_Label=Label(GenerateTicket,text="Enter Name :").grid(row=0,column=0)
                NameTicket_Variable=StringVar()
                NameTicket_Entry=Entry(GenerateTicket,textvariable=NameTicket_Variable,width=50)
                NameTicket_Entry.grid(row=0,column=1,columnspan=1,padx=50,pady=10)
                AgeTicket_Label=Label(GenerateTicket,text="Enter Age :")
                AgeTicket_Label.grid(row=1,column=0)
                AgeTicket_Variable=StringVar()
                AgeTicket_Entry=Entry(GenerateTicket,textvariable=AgeTicket_Variable,width=50)
                AgeTicket_Entry.grid(row=1,column=1,columnspan=1,padx=50,pady=10)
                Label(GenerateTicket,text="Select Gender :").grid(row=2,column=0)
                GenderVar = StringVar()
                GenderTk= ttk.Combobox(GenerateTicket, width=35, textvariable = GenderVar)
                GenderTk['values']=('Male','Female','Other')
                GenderTk.grid(column = 1, row = 2) 
                GenderTk.current()
                FoodVar = StringVar()
                FoodonRailTk= ttk.Combobox(GenerateTicket, width=35, textvariable =FoodVar)
                FoodonRailTk['values']=('Yes','N/A')
                FoodonRailTk.grid(column = 1, row = 4) 
                FoodonRailTk.current()
                Label(GenerateTicket,text="Food on Rail :").grid(row=4,column=0,pady=10)
                PNRNo=random.randint(100000,99999999)
                StoreTrainName=Trains.get()
                def BookNow():
                    Name_ofPassenger=NameTicket_Entry.get()
                    Age_ofPassenger=AgeTicket_Entry.get()
                    for c in Age_ofPassenger:
                        if c!='1' and c!='2' and c!='3' and c!='4' and c!='5' and c!='6' and c!='7' and c!='8' and c!='9' and c!='0':  
                            Label(GenerateTicket,text="Only Intergers Allowed",fg="red").grid(row=1,column=2)
                            Label(GenerateTicket,text="CAUTION : Please Close The Window And Retry",fg="red").grid(row=8,column=1,pady=10)
                    FoodonRail=FoodonRailTk.get()  
                    PassengerGender=GenderTk.get()
                    Train_Name=StoreTrainName
                    Ticket=(Name_ofPassenger,Age_ofPassenger,FoodonRail,D,PassengerGender,Train_Name,USERNAME,PNRNo)
                    try:
                        TicketReservation="INSERT INTO reservation(Name_Of_Traveller,Age_Of_Traveller,Food_on_rail,Date_of_travel,Gender_of_Traveller,TrainName,user_Name,PNR_No) Value(%s,%s,%s,%s,%s,%s,%s,%s)"
                        C1.execute(TicketReservation,Ticket)
                        UserLog.commit()
                    except:
                        pass
                    else:
                        Label(GenerateTicket,text= "Successfully Booked",fg="green").grid(row=8,column=1,pady=10)
                        Label(GenerateTicket,text= "Name Of Traveller :").grid(row=9,column=0,pady=10)
                        Label(GenerateTicket,text=Name_ofPassenger).grid(row=9,column=1,pady=10)
                        Label(GenerateTicket,text="Age Of Traveller :").grid(row=10,column=0,pady=10)
                        Label(GenerateTicket,text=Age_ofPassenger).grid(row=10,column=1,pady=10)
                        Label(GenerateTicket,text="Food On Rail :").grid(row=11,column=0,pady=10)
                        Label(GenerateTicket,text=FoodonRail).grid(row=11,column=1,pady=10)
                        Label(GenerateTicket,text="Date Of Travell :").grid(row=12,column=0,pady=10)
                        Label(GenerateTicket,text=D).grid(row=12,column=1,pady=10)
                        Label(GenerateTicket,text="Gender :").grid(row=13,column=0,pady=10)
                        Label(GenerateTicket,text=PassengerGender).grid(row=13,column=1,pady=10)
                        Label(GenerateTicket,text="Train Name :").grid(row=14,column=0,pady=10)
                        Label(GenerateTicket,text=Train_Name).grid(row=14,column=1,pady=10)
                        Label(GenerateTicket,text="PNR No :").grid(row=15,column=0,pady=10)
                        Label(GenerateTicket,text=PNRNo).grid(row=15,column=1,pady=10)
                        Label(GenerateTicket,text="PLEASE RECORD THE DETAILS FOR FUTHER INQUIRY ",fg="red").grid(row=17,column=1,pady=10)              
                Button(GenerateTicket,text="Book Now",command=BookNow).grid(row=7,column=1)
                GenerateTicket.mainloop()
            Label(BookMenu,text="Choose Train :").grid(column = 0, row = 4)
            Label(BookMenu,text="Select Date of Travell :").grid(column = 0, row = 5)
            cal=Calendar(BookMenu,font="Arial 14",selectmode="day",cursor="hand1")
            cal.grid(row=5,column=1,pady=10)
            Button(BookMenu,text="Submit",command=GenerateTicket).grid(row=6,column=1,pady=10)
            Trains.grid(column = 1, row = 4)
            Trains.current()
    Button(BookMenu,text="FindTrains",command=Findtrain).grid(row=3,column=1,pady=10)
    
    BookMenu.mainloop()
def cancel():
    CancelBooking=Tk()
    CancelBooking.geometry("400x200")
    CancelBooking.iconbitmap("favicon.ico")
    CancelBooking.title("Cancel Ticket")
    Cancel=StringVar()
    Cancel_Label=Label(CancelBooking,text="Enter PNR NO:")
    Cancel_Label.grid(row=0,column=0)
    PNR_Cancel=Entry(CancelBooking,width=50,textvariable=Cancel)
    PNR_Cancel.grid(row=0,column=1,pady=10)
    def Confirm_Cancel():
        Confirm_Cancel1=Tk()
        Confirm_Cancel1.geometry("350x200")
        Confirm_Cancel1.minsize(350,200)
        Confirm_Cancel1.maxsize(350,200)
        Confirm_Cancel1.iconbitmap("favicon.ico")
        Confirm_Cancel1.title("Confirm Canceling")
        CancelBooking.iconbitmap("favicon.ico")
        def yes_Cancel():
            PNRConf_cancel=PNR_Cancel.get()
            Canceling="DELETE  FROM reservation WHERE PNR_No = '"+PNRConf_cancel+"' and user_Name ='"+USERNAME+"' "
            C1.execute(Canceling)
            UserLog.commit()
            CancelBooking.destroy()
            Confirm_Cancel1.destroy()
        Label(Confirm_Cancel1,text="Are you sure you want to cancel?").grid(row=0,column=0,pady=10)    
        Confirm_Cancel_Button=Button(Confirm_Cancel1,text="Yes",command=yes_Cancel,padx=20).grid(row=1,column=0,pady=10)
        No_Cancel_Button=Button(Confirm_Cancel1,text="No",command=lambda:Confirm_Cancel1.destroy(),padx=20).grid(row=1,column=1,pady=10)
        Confirm_Cancel1.mainloop()       
    Cancel_Button=Button(CancelBooking,text="Cancel",command=Confirm_Cancel)
    Cancel_Button.grid(row=2,column=1)
 
    CancelBooking.mainloop()
def ShowReservation():
    ShowingReservation=Tk()
    ShowingReservation.iconbitmap("favicon.ico")
    ShowingReservation.title("Tickets")
    Label(ShowingReservation,text="Your Past Booking's",fg="green").grid(row=0,column=5,pady=10)
    Label(ShowingReservation,text="S.No",fg="orange").grid(row=1,column=1,padx=20)
    Label(ShowingReservation,text="Name Of Traveller",fg="orange").grid(row=1,column=2,padx=40)
    Label(ShowingReservation,text="User Name",fg="orange").grid(row=1,column=3,padx=40)
    Label(ShowingReservation,text="Age of Traveller",fg="orange").grid(row=1,column=4,padx=20)
    Label(ShowingReservation,text="Gender Of Traveller",fg="orange").grid(row=1,column=5,padx=20)
    Label(ShowingReservation,text="Food on Rail",fg="orange").grid(row=1,column=6,padx=20)
    Label(ShowingReservation,text="Date Of Travel",fg="orange").grid(row=1,column=7,padx=20)
    Label(ShowingReservation,text="Train Name",fg="orange").grid(row=1,column=8,padx=20)
    Label(ShowingReservation,text="PNR No",fg="orange").grid(row=1,column=9,padx=30)
    showreserv="SELECT * FROM reservation "
    C1.execute(showreserv)
    CE=C1.fetchall()
    j=1
    Rowcount=2
    for t in CE:
        if(t[1]==USERNAME):
            Label(ShowingReservation,text=j).grid(row=Rowcount,column=1)
            Label(ShowingReservation,text=t[0]).grid(row=Rowcount,column=2)
            Label(ShowingReservation,text=t[1]).grid(row=Rowcount,column=3)
            Label(ShowingReservation,text=t[2]).grid(row=Rowcount,column=4)
            Label(ShowingReservation,text=t[3]).grid(row=Rowcount,column=5)
            Label(ShowingReservation,text=t[4]).grid(row=Rowcount,column=6)
            Label(ShowingReservation,text=t[5]).grid(row=Rowcount,column=7)
            Label(ShowingReservation,text=t[6]).grid(row=Rowcount,column=8)
            Label(ShowingReservation,text=t[7]).grid(row=Rowcount,column=9)
            Rowcount+=1
            j+=1
    ShowingReservation.mainloop()            
def ManageProf():
    ManageProfile=Tk()
    ManageProfile.iconbitmap("favicon.ico")
    ManageProfile.title("Update Profile")
    def UpdateProf():
        NewCS=NewCityName.get()
        NewPhno=NewPhnNo.get()
        UpProfile="UPDATE coustomer_data SET City = %s, Ph_No = %s WHERE user_Name = %s "
        NewUP=(NewCS,NewPhno,USERNAME)
        C1.execute(UpProfile,NewUP)
        UserLog.commit()
        Label(ManageProfile,text="Successfully Entered",fg="green").grid(row=3,column=1)
    Label(ManageProfile,text="Enter New City Name").grid(row=0,column=0)
    Label(ManageProfile,text="Enter New Mobile No.").grid(row=1,column=0)
    NewCity=StringVar()
    NewPhn=StringVar()
    NewCityName=Entry(ManageProfile,width=50,textvariable=NewCity)
    NewCityName.grid(row=0,column=1)
    NewPhnNo=Entry(ManageProfile,width=50,textvariable=NewPhn)
    NewPhnNo.grid(row=1,column=1)
    UpdatePrf=Button(ManageProfile,text="Update Profile ",command=UpdateProf,padx=16).grid(row=2,column=1,padx=35)
    ManageProfile.mainloop()
def Login():
    Login_User=Tk()
    Login_User.title("Login")
    Login_User.iconbitmap("favicon.ico")
    CoustomerData_UserName_Ask=Label(Login_User,text="Enter User Name :").grid(row=0,column=0)
    CoustomerData_Password_Ask=Label(Login_User,text="Enter Password :").grid(row=1,column=0)
    def New_Pass():
        New_Pass=Tk()
        New_Pass.title("Change Password")
        New_Pass.iconbitmap("favicon.ico")
        Label(New_Pass,text="Enter New Password").grid(row=0,column=0)
        Label(New_Pass,text="Confirm New Password").grid(row=1,column=0)
        newpass1=StringVar()
        newpass2=StringVar()
        Entry1=Entry(New_Pass,width=50,textvariable=newpass1)
        Entry1.grid(row=0,column=1)
        Entry2=Entry(New_Pass,width=50,textvariable=newpass2,show="*")
        Entry2.grid(row=1,column=1)
        def Save_newpass():
            NewPass1=Entry1.get()
            NewPass2=Entry2.get()
            UN=Data_UserNameEnter.get()
            if NewPass1==NewPass2 :
                NewPassRec="UPDATE coustomer_data SET password ='"+NewPass1+"' WHERE user_Name='"+UN+"'"
                C1.execute(NewPassRec)
                UserLog.commit()
                Label(New_Pass,text="Password Changed Successfully",fg="Blue").grid(row=3 ,column=1)                
            else:
                Label(New_Pass,text="Both Password Do Not Match",fg="red").grid(row=3 ,column=1)
        Forgot_Pass=Button(New_Pass,text="Submit",command=Save_newpass).grid(row=2,column=1)
        New_Pass.mainloop()
    Forgot_Pass=Button(Login_User,text="Forgot Password",command=New_Pass).grid(row=2,column=0)
    Data_UserNameEnterStore=StringVar()
    Data_PasswordEnterStore=StringVar()
    Data_UserNameEnter=Entry(Login_User,width=50,textvariable=Data_UserNameEnterStore)
    Data_UserNameEnter.grid(row=0,column=1,columnspan=1,padx=50)
    Data_PasswordEnter=Entry(Login_User,show="*",width=50,textvariable=Data_PasswordEnterStore)
    Data_PasswordEnter.grid(row=1,column=1,columnspan=1,padx=50)
    

    def MainMenu():
        global USERNAME
        USERNAME=Data_UserNameEnter.get()
        PASSWORD=Data_PasswordEnter.get()
        Chk_USERPASS=(USERNAME,PASSWORD)
        Chk="SELECT user_Name,password FROM coustomer_data"
        C1.execute(Chk)
        r=C1.fetchall()
        var2=0
        for i in r:
            var2+=1
            if(i==Chk_USERPASS ):
                Login_User.destroy()
                Main_Menu=Tk()
                Main_Menu.iconbitmap("favicon.ico")
                Main_Menu.title("Options")
                Label(Main_Menu,text="Choose Option",fg="blue").grid(row=0,column=0,columnspan=2,padx=50)
                Book_Ticket=Button(Main_Menu,text="Book Ticket",command=book,padx=40).grid(row=1,column=0,columnspan=2,padx=50)
                Cancel_Ticket=Button(Main_Menu,text="Cancel_Ticket",command=cancel,padx=35).grid(row=2,column=0,columnspan=2,padx=35)
                Show_Ticket=Button(Main_Menu,text="Show Past Bookings ",command=ShowReservation,padx=16).grid(row=3,column=0,columnspan=2,padx=35)
                ManagePrf=Button(Main_Menu,text="Manage Profile ",command=ManageProf,padx=29).grid(row=4,column=0,columnspan=2,padx=35)
                Main_Menu.mainloop()
                break
            if i!=Chk_USERPASS:
                if var2==len(r):
                    Label(Login_User,text="Username or Password Is Incorrect",fg="red").grid(row=3,column=1)
    Submit_Button_Login=Button(Login_User,text="Submit",command=MainMenu).grid(row=2,column=1)
    Login_User.mainloop()
def Staff():
    Staff=Tk()
    Staff.geometry("200x200")
    Staff.minsize(400,200)
    Staff.maxsize(400,200)
    Staff.title("Staff")
    Staff.iconbitmap("favicon.ico")
    def Staff_Btn():
        Staff_Btn=Tk()
        Staff_Btn.geometry("300x150")
        Staff_Btn.title("Staff Button")
        Staff_Btn.iconbitmap("favicon.ico")
        SU=StaffUserName.get()
        SP=StaffPasswd.get()
        def AddStation():
            AddStationN=Tk()
            AddStationN.iconbitmap("favicon.ico")
            AddStationN.geometry("500x100")
            AddStationN.minsize(500,100)
            AddStationN.maxsize(500,100)
            AddStationN.title("ADD Station")
            NStationName=StringVar()
            NewStationName=Entry(AddStationN,width=30,textvariable=NStationName)
            NewStationName.grid(row=0,column=1)
            NewStationName_label=Label(AddStationN,text="Enter The New Station Name :")
            NewStationName_label.grid(row=0,column=0)
            
            def SubmitStation():
                NSN=NewStationName.get()
                NSN=str(NSN)
                SubmitName="INSERT INTO Station VALUES('"+NSN+"')"
                C1.execute(SubmitName,NSN)
                UserLog.commit()
                SEntered=Label(AddStationN,text="Successfully Entered")
                SEntered.grid(row=1,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
            AddRecBtn=Button(AddStationN,text="Add Station Record",command=SubmitStation)
            AddRecBtn.grid(row=2,column=1,padx=20,pady=10)
            AddStationN.mainloop()
        def Deletestation():
            DelStationN=Tk()
            DelStationN.geometry("500x100")
            DelStationN.minsize(500,100)
            DelStationN.maxsize(500,100)
            DelStationN.title("DEL Station")
            DelStationN.iconbitmap("favicon.ico")
            DStationName=StringVar()
            DelStationName=Entry(DelStationN,width=30,textvariable=DStationName)
            DelStationName.grid(row=0,column=1)
            DelStationName_label=Label(DelStationN,text="Enter the Station Name :")
            DelStationName_label.grid(row=0,column=0)
            def SubmitDelStation():
                DSN=DelStationName.get()
                SubmitDelName="DELETE FROM Station WHERE Station_Name = '"+DSN+"'"
                C1.execute(SubmitDelName,DSN)
                UserLog.commit()
                DelStation_Label=Label(DelStationN,text="Record Successfully Deleted")
                DelStation_Label.grid(row=1,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
            DelStation_Btn=Button(DelStationN,text="DELETE Station Record",command=SubmitDelStation)
            DelStation_Btn.grid(row=2,column=1,padx=20,pady=10)
            DelStationN.mainloop()
        def ShowRes():##############################
            ShowingReserv=Tk()
            ShowingReserv.iconbitmap("favicon.ico")
            ShowingReserv.title("All Bookings")
            Label(ShowingReserv,text="All Booking's",fg="green").grid(row=0,column=5,pady=10)
            Label(ShowingReserv,text="S.No",fg="orange").grid(row=1,column=1,padx=20)
            Label(ShowingReserv,text="Name Of Traveller",fg="orange").grid(row=1,column=2,padx=40)
            Label(ShowingReserv,text="User Name",fg="orange").grid(row=1,column=3,padx=40)
            Label(ShowingReserv,text="Age of Traveller",fg="orange").grid(row=1,column=4,padx=20)
            Label(ShowingReserv,text="Gender Of Traveller",fg="orange").grid(row=1,column=5,padx=20)
            Label(ShowingReserv,text="Food on Rail",fg="orange").grid(row=1,column=6,padx=20)
            Label(ShowingReserv,text="Date Of Travel",fg="orange").grid(row=1,column=7,padx=20)
            Label(ShowingReserv,text="Train Name",fg="orange").grid(row=1,column=8,padx=20)
            Label(ShowingReserv,text="PNR No",fg="orange").grid(row=1,column=9,padx=30)
            showreserv="SELECT * FROM reservation "
            C1.execute(showreserv)
            CE=C1.fetchall()
            j=1
            Rowcount=2
            for t in CE:
                Label(ShowingReserv,text=j).grid(row=Rowcount,column=1)
                Label(ShowingReserv,text=t[0]).grid(row=Rowcount,column=2)
                Label(ShowingReserv,text=t[1]).grid(row=Rowcount,column=3)
                Label(ShowingReserv,text=t[2]).grid(row=Rowcount,column=4)
                Label(ShowingReserv,text=t[3]).grid(row=Rowcount,column=5)
                Label(ShowingReserv,text=t[4]).grid(row=Rowcount,column=6)
                Label(ShowingReserv,text=t[5]).grid(row=Rowcount,column=7)
                Label(ShowingReserv,text=t[6]).grid(row=Rowcount,column=8)
                Label(ShowingReserv,text=t[7]).grid(row=Rowcount,column=9)
                Rowcount+=1
                j+=1
            ShowingReserv.mainloop()            

        def ShowCoust():
            ShowingCD=Tk()
            ShowingCD.iconbitmap("favicon.ico")
            ShowingCD.title("Coustomer Data")
            Label(ShowingCD,text="COUSTOMER DATA",fg="green").grid(row=0,column=5,pady=10)
            Label(ShowingCD,text="S.No",fg="orange").grid(row=1,column=1,padx=20)
            Label(ShowingCD,text="User Name",fg="orange").grid(row=1,column=2,padx=40)
            Label(ShowingCD,text="Password",fg="orange").grid(row=1,column=3,padx=40)
            Label(ShowingCD,text="First Name",fg="orange").grid(row=1,column=4,padx=20)
            Label(ShowingCD,text="Last Name",fg="orange").grid(row=1,column=5,padx=20)
            Label(ShowingCD,text="Age",fg="orange").grid(row=1,column=6,padx=20)
            Label(ShowingCD,text="Email",fg="orange").grid(row=1,column=7,padx=20)
            Label(ShowingCD,text="ADHAR No.",fg="orange").grid(row=1,column=8,padx=20)
            Label(ShowingCD,text="Ph No.",fg="orange").grid(row=1,column=9,padx=30)
            Label(ShowingCD,text="City",fg="orange").grid(row=1,column=10,padx=30)
            Label(ShowingCD,text="Pincode",fg="orange").grid(row=1,column=11,padx=10)
            showreserv="SELECT * FROM coustomer_data "
            C1.execute(showreserv)
            CE=C1.fetchall()
            j=1
            Rowcount=2
            for t in CE:
                Label(ShowingCD,text=j).grid(row=Rowcount,column=1)
                Label(ShowingCD,text=t[0]).grid(row=Rowcount,column=2)
                Label(ShowingCD,text=t[1]).grid(row=Rowcount,column=3)
                Label(ShowingCD,text=t[2]).grid(row=Rowcount,column=4)
                Label(ShowingCD,text=t[3]).grid(row=Rowcount,column=5)
                Label(ShowingCD,text=t[4]).grid(row=Rowcount,column=6)
                Label(ShowingCD,text=t[5]).grid(row=Rowcount,column=7)
                Label(ShowingCD,text=t[6]).grid(row=Rowcount,column=8)
                Label(ShowingCD,text=t[7]).grid(row=Rowcount,column=9)
                Label(ShowingCD,text=t[8]).grid(row=Rowcount,column=10)
                Label(ShowingCD,text=t[9]).grid(row=Rowcount,column=11)
                Rowcount+=1
                j+=1
            ShowingCD.mainloop()
        def DelCoust():
            DelCData=Tk()
            DelCData.iconbitmap("favicon.ico")
            def ConfDel():
                usernameget=DelCD.get()
                print(usernameget)
                DelCostomerD="DELETE FROM coustomer_data WHERE user_Name = '"+usernameget+"' "
                C1.execute(DelCostomerD)
                UserLog.commit()
                Label(DelCData,text="Successfully DELETED",fg="green").grid(row=2,column=1)
            Label(DelCData,text="Enter UserName").grid(row=0,column=0)
            CDDel=StringVar()
            DelCD=Entry(DelCData,width=50,textvariable=CDDel)
            DelCD.grid(row=0,column=1)
            DELCD=Button(DelCData,text="DELETE",command=ConfDel,padx=30)      
            DELCD.grid(row=1,column=1,padx=10)
            DelCData.mainloop()
        if(SU=="Admin" and SP=="IRCTC"):
            Label(Staff_Btn,text="Choose Option",fg="blue").grid(row=0,column=0,padx=100)
            ADDREC=Button(Staff_Btn,text="Add Station Record",command=AddStation,padx=30)      
            ADDREC.grid(row=1,column=0,padx=10)
            DELREC=Button(Staff_Btn,text="Delete Station Record",command=Deletestation,padx=25)
            DELREC.grid(row=2,column=0,padx=10)
            ShowallReserve=Button(Staff_Btn,text="Show All Booking",command=ShowRes,padx=35)
            ShowallReserve.grid(row=3,column=0,padx=10)
            ShowCoustomerData=Button(Staff_Btn,text="Coustomer Data",command=ShowCoust,padx=38)
            ShowCoustomerData.grid(row=4,column=0,padx=10)
            DelCoustomerData=Button(Staff_Btn,text="Delete Coustomer Data",command=DelCoust,padx=20)
            DelCoustomerData.grid(row=5,column=0,padx=10)
        else:
            WrongEntry=Label(Staff_Btn,text="Incorrect User Name OR Password")
            WrongEntry.grid(row=2,column=0)
        Staff_Btn.mainloop()
    StaffUserName= StringVar()
    StaffPasswd= StringVar()
    StaffUserName=Entry(Staff,width=30,textvariable=StaffUserName)
    StaffUserName.grid(row=0,column=1,padx=20)
    StaffPasswd=Entry(Staff,width=30,textvariable=StaffPasswd,show="*")
    StaffPasswd.grid(row=1,column=1,padx=20)
    Staff_Btn=Button(Staff,text="Submit",command=Staff_Btn).grid(row=3,column=1,columnspan=2,padx=10,pady=10,ipadx=100)
    StaffUserName_label=Label(Staff,text="Enter a UserName :").grid(row=0,column=0)
    StaffPasswd_label=Label(Staff,text="Enter a Password :").grid(row=1,column=0)
    Staff.mainloop()
#REGISTRATION WINDOW(WIN#1->2)    
def Register():
    Register=Tk()
    Register.geometry("800x500")
    
    Register.title("Registration")
    Register.iconbitmap("favicon.ico")
    #Registeration Button Func
    def Registeration_Btn():
        S="INSERT INTO coustomer_data (user_Name,password,First_Name,Last_Name,Age,Email,Aadhar_No,Ph_No,City,PinCode) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s,%s)" 
        
        A=EntryUser.get()
        B=EPass.get()
        C=EF.get()
        D=EL.get()           
        E=EAge.get()
        for d in E:
             if d!='1' and d!='2' and d!='3' and d!='4' and d!='5' and d!='6' and d!='7' and d!='8' and d!='9' and d!='0':  
                Label(Register,text="#Wrong Data Input For Age",fg="red").grid(row=5,column=2)
                Label(Register,text="CAUTION : Please Close The Window And Retry",fg="red").grid(row=12,column=0,pady=10)
        F=EMail.get()
        G=EAdhr.get()
        for e in G:
             if e!='1' and e!='2' and e!='3' and e!='4' and e!='5' and e!='6' and e!='7' and e!='8' and e!='9' and e!='0':
                Label(Register,text="#Digits of Adhar are Not Matching(10 digit)",fg="red").grid(row=7,column=2)
                Label(Register,text="CAUTION : Please Close The Window And Retry",fg="red").grid(row=12,column=0,pady=10)
        H=EPhn.get()
        for f in H:
            if f!='1' and f!='2' and f!='3' and f!='4' and f!='5' and f!='6' and f!='7' and f!='8' and f!='9' and f!='0':
                Label(Register,text="#Digit of Phone Number Not Matching(10 digit)",fg="red").grid(row=8,column=2)
                Label(Register,text="CAUTION : Please Close The Window And Retry",fg="red").grid(row=12,column=0,pady=10)
        I=ECity.get()
        J=EPin.get()
        for g in J:
            if g!='1' and g!='2' and g!='3' and g!='4' and g!='5' and g!='6' and g!='7' and g!='8' and g!='9' and g!='0':
                Label(Register,text="#Wrong Data Input For Pincode",fg="red").grid(row=10,column=2)
                Label(Register,text="CAUTION : Please Close The Window And Retry",fg="red").grid(row=12,column=0,pady=10)
        Reguser=(A,B,C,D,E,F,G,H,I,J)
        try:
            C1.execute(S,Reguser)
            UserLog.commit()
        except:
            pass
        else:
            Label(Register,text="Successfully Entered",fg="green").grid(row=12,column=0,padx=10,pady=10,ipadx=100)
#Creating Registration Entry Box
    RUserName= StringVar()
    RPasswd= StringVar()
    RF_Name= StringVar()
    RL_Name= StringVar()
    RAge= IntVar()
    REmail= StringVar()
    RAdharNo= IntVar()
    RPhNo= IntVar()
    RCity= StringVar()
    RPincode= IntVar()
    EntryUser=Entry(Register,width=30,textvariable=RUserName)
    EntryUser.grid(row=0,column=1,padx=20)
    EPass=Entry(Register,width=30,textvariable=RPasswd)
    EPass.grid(row=1,column=1,padx=20)
    EF=Entry(Register,width=30,textvariable=RF_Name)
    EF.grid(row=3,column=1,padx=20)
    EL=Entry(Register,width=30,textvariable=RL_Name)
    EL.grid(row=4,column=1,padx=20)
    EAge=Entry(Register,width=30,textvariable=RAge)
    EAge.grid(row=5,column=1,padx=20)
    EMail=Entry(Register,width=30,textvariable=REmail)
    EMail.grid(row=6,column=1,padx=20)
    EAdhr=Entry(Register,width=30,textvariable=RAdharNo)
    EAdhr.grid(row=7,column=1,padx=20)
    EPhn=Entry(Register,width=30,textvariable=RPhNo)
    EPhn.grid(row=8,column=1,padx=20)
    ECity=Entry(Register,width=30,textvariable=RCity)
    ECity.grid(row=9,column=1,padx=20)
    EPin=Entry(Register,width=30,textvariable=RPincode)
    EPin.grid(row=10,column=1,padx=20)
    #Creating Lable For Entry Box
    User_Name_label=Label(Register,text="Enter a UserName :").grid(row=0,column=0)
    Passw_label=Label(Register,text="Enter a Password :").grid(row=1,column=0)
    F_Name_label=Label(Register,text="First Name :").grid(row=3,column=0)
    L_Name_label=Label(Register,text="Last Name :").grid(row=4,column=0)
    Age_label=Label(Register,text="Age :").grid(row=5,column=0)
    Email_label=Label(Register,text="Email :").grid(row=6,column=0)
    AdharNo_label=Label(Register,text="Adhar No. :").grid(row=7,column=0)
    PhoneNo_label=Label(Register,text="Phone No. :").grid(row=8,column=0)
    City_Name_label=Label(Register,text="City Name :").grid(row=9,column=0)
    Pincode_Name_label=Label(Register,text="Pincode :").grid(row=10,column=0)
    #Creating Register Btn
    Register_Btn=Button(Register,text="Register",command=Registeration_Btn).grid(row=11,column=0,padx=10,pady=10,ipadx=100)
    Register.mainloop()
#MAIN WINDOW(WIN#1)
customer_data=Tk()
customer_data.geometry("500x290")
customer_data.minsize(513,290)
customer_data.maxsize(513,290)
customer_data.iconbitmap("favicon.ico")
photo=PhotoImage(file="BackGround1.gif")
La=Label(customer_data,image=photo,padx=100).place(relx=0.5,anchor="n")
customer_data.title("Project Railway")
customer_data.configure(bg=La)
LnButton=Button(customer_data,text="Login",command=Login,padx=66).grid(row=0,column=0)
ReButton=Button(customer_data,text="Register",command=Register,padx=60).grid(row=0,column=1)
StfButton=Button(customer_data,text="Staff",command=Staff,padx=69).grid(row=0,column=2)
ExitBtton=Button(customer_data,text="Quit",command=quit,padx=69).grid(row=6,column=1,pady=230)
customer_data.mainloop()
