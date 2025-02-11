import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vr1#%!)%(!!!!$",database="job")
mycursor = mydb.cursor()

from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import ttk
import webbrowser

top=Tk()
top.title("MOVIE SEARCH APP")
top.geometry("1250x600")
top.configure(bg="white")
ent=Entry(top)


#signup
def signup_display():
    addun_screen=Toplevel(top)
    addun_screen.title("Signup")
    addun_screen.geometry("450x375")
    addun_screen.configure(bg="white")

    global first_name
    global last_name
    global user_id
    global pswd
    Label(addun_screen,text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",bg="blue",width=300).pack()
    first_name=StringVar()
    last_name=StringVar()
    user_id=StringVar()
    pswd=StringVar()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="First Name:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=first_name).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="Last Name:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=last_name).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="User-ID:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=user_id).pack()
    Label(addun_screen, text="",bg="white").pack()
    Label(addun_screen, text="Password:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(addun_screen, textvariable=pswd,show="*").pack()
    Label(addun_screen, text="",bg="white").pack()
    Button(addun_screen, text="Signup", bg="blue", fg='white', relief="groove", font=('calibri', 14, 'bold'),command=usinfo).pack()
    Label(addun_screen, text="",bg="white")
    
def usinfo():
    fname=first_name.get()
    lname=last_name.get()
    ui=user_id.get()
    pw=pswd.get()
    if(fname=="" or lname=="" or ui=="" or pw==""):
        MessageBox.showerror("Profile","All fields are required")
    else:
        try:
            sql="insert into signup(firstname,lastname,userid,passwd) values('{}','{}','{}','{}')".format(fname,lname,ui,pw)
            mycursor.execute(sql)
            mydb.commit()        
            
        
            MessageBox.showinfo("Showinfo","Successfully signed up")
            movies()
      
            
        except mysql.connector.errors.IntegrityError:
            MessageBox.showinfo("Showinfo","Userid or Password already in use!")

def Exit():
    wayOut = MessageBox.askyesno("Signup System", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return

#login
def login_screen():
    login_screen=Toplevel(top)
    login_screen.title("Login")
    login_screen.geometry("450x375")
    login_screen.configure(bg="white")

    global userid
    global ps_wd
    Label(login_screen,text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",bg="blue",width=300).pack()
    userid=StringVar()
    ps_wd=StringVar()
    Label(login_screen, text="",bg="white").pack()
    Label(login_screen, text="User-ID:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(login_screen, textvariable=userid).pack()
    Label(login_screen, text="",bg="white").pack()
    Label(login_screen, text="Password:",fg="black", font=('calibri', 14, 'bold')).pack()
    Entry(login_screen, textvariable=ps_wd,show="*").pack()
    Button(login_screen, text="Submit", bg="blue", fg='white', relief="groove", font=('calibri', 14, 'bold'),command=log).pack()
    Label(login_screen, text="",bg="white")

def log():
    usi=userid.get()
    pd=ps_wd.get()
    if(usi=="" or pd==""):
        MessageBox.showerror("Profile","All fields are required")
    else:
        sql3="insert into login(userid,passwd) values('{}','{}')".format(usi,pd)  
        mycursor.execute(sql3)
        mydb.commit()
        login()
        
               
def login():
    usi=userid.get()
    pd=ps_wd.get()
    sql4='select userid,passwd from signup'
    mycursor.execute(sql4)
    data=mycursor.fetchall()
    mydb.commit()
    for row in data:
        if(row[0]==usi) and (row[1]==pd):
            MessageBox.showinfo("showinfo","Successfully Logged In")
            movies()
            break
        
    else:
         MessageBox.showinfo("showinfo","Profile Not Found")
              
            
def Exit2():
    wayOut = MessageBox.askyesno("Login System", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 


def Exit3():
    wayOut = MessageBox.askyesno("Personal Info", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 

#delete profile        
def rem_pro():
    global temp_userid
    global temp_pswd
    rempro_screen=Toplevel(top)
    rempro_screen.title("Remove Profile")
    rempro_screen.config(bg="white")
    rempro_screen.geometry("500x500")

    
    Label(rempro_screen,text="User-ID:",font=('calibri',14,"bold"),width=20,fg="black").grid(row=2,sticky=W,pady=10)
    Label(rempro_screen,text="Password:",font=('calibri',14,"bold"),width=20,fg="black").grid(row=3,sticky=W,pady=10)

    
    Button(rempro_screen,text="SUBMIT",font=("calibri",14,"bold"),fg="white",bg="blue",width=10,command=rempro).grid(row=5,sticky=E,pady=10)

    
    temp_userid=Entry(rempro_screen)
    temp_userid.grid(row=2,column=10,sticky=E,pady=10)
    temp_pswd=Entry(rempro_screen,show='*')
    temp_pswd.grid(row=3,column=10,sticky=E,pady=10)

def rempro():
    c=temp_userid.get()
    r=temp_pswd.get()
    if(c=="" or r==""):
        MessageBox.showerror("Removing profile","All fields are required")
    else:
        data=(c,r)
        sql='delete from signup where userid=%s and passwd=%s'
        mycursor.execute(sql,data)
        mydb.commit()
        

        MessageBox.showinfo("Showinfo","Profile deleted")

def Exit4():
    wayOut = MessageBox.askyesno("Remove Profile", "Do you want to exit the system?")
    if wayOut > 0:
        root.destroy()
        return 

frame= Frame(top)
def movies():
    webbrowser.open("file:///C:/Users/Dhiyazhini/OneDrive/Desktop/Movie_Search_App/index.html")

    
   
#main display
Label(top,text="MOVIE SEARCH APP",bd=20,font=('calibri',25,"bold"),relief="raised",width=30,fg="blue").grid(row=0,sticky=N,pady=10)


Button(top,text="SIGNUP",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=signup_display).grid(row=2,sticky=W,pady=10)
Button(top,text="LOGIN",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=login_screen).grid(row=3,sticky=W,pady=10)
Button(top,text="REMOVE PROFILE",bd=10,font=('calibri',20,"bold"),relief="groove",width=20,bg="blue",fg="white",command=rem_pro).grid(row=4,sticky=W,pady=10)

top.mainloop()


