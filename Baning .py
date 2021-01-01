
import mysql.connector
import  os
import getpass

def  clear():
    os.system("cls")               

usr = input("Enter your MySQL Username : ")
pas = getpass.getpass("Enter your MySQL Password : ")
try:
    mydb=mysql.connector.connect(user=usr,passwd= pas,host='localhost')

except:
    print("Failed to connect to Mysql! Please make sure that the given credentials are valid.")
    exit()

mycursor=mydb.cursor(buffered=True)
#Created Database bankDB
mycursor.execute('create database if not exists BankDB')
mycursor.execute('use BankDB')




def Menu(): #Function to display the menu
    print("*"*130)
    print("MAIN MENU".center(130))
    print("1. Insert Record/Records".center(130))
    print("2. Display Records as per Account Number".center(130))
    print(" a. Sorted as per Account Number".center(130))
    print(" b. Sorted as per Customer Name".center(130))
    print(" c. Sorted as per Customer Balance".center(130))
    print("3. Search Record Details as per the account number".center(130))
    print("4. Update Record".center(130))
    print("5. Delete Record".center(130))
    print("6. TransactionsDebit/Withdraw from theaccount".center(130))
    print(" a. Debit/Withdraw from the account".center(130))
    print(" b. Credit into the account".center(130))
    print("7. Exit".center(130))
    print("*"*130)

def MenuSort():
    print(" a. Sorted as per Account Number".center(130))
    print(" b. Sorted as per Customer Name".center(130))
    print(" c. Sorted as per Customer Balance".center(130))
    print(" d. Back".center(130))

def MenuTransaction():
    print(" a. Debit/Withdraw from the account".center(130))
    print(" b. Credit into the account".center(130))
    print(" c. Back".center(130))

def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(16),NAME varchar(50),MOBILE varchar(10),EMAIL varchar(50),ADDRESS varchar(100),CITY varchar(50),COUNTRY varchar(20),BALANCE decimal(50,2))')
        print("Table Created")
        Insert()

    except:
        print("Table Exist")
        Insert()
    

        

def Insert():
    
    while True:  #Loop for accepting records
        Acc=input("Enter account no : ")
        Name=input("Enter Name : ")
        Mob=input("Enter Mobile : ")
        email=input("Enter Email : ")
        Add=input("Enter Address : ")
        City=input("Enter City : ")
        Country=input("Enter Country : ")
        Bal=float(input("Enter Balance : "))
        #Add = Add.replace(',', '\\,')
        #Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd=f"insert into bank values('{Acc}','{Name.upper()}','{Mob}','{email}','{Add.upper()}','{City.upper()}','{Country.upper()}','{Bal}');"
        mycursor.execute(Cmd)
        mycursor.fetchall()
        mycursor.commit()
        print("The values have been entered Succesfully!")
        ch=input("Do you want to enter more records")
        if ch=='N' or ch=='n':
            break

        #Function to Display records as per ascending order of Account Number 

def DispSortAcc():
    try:
        cmd="select * from bank order by ACCNO"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETEADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

def DispSortName(): #Function to Display records as per ascending order of Name
    try:
        cmd="select * from bank order by NAME"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
        clear()
    except:
        print("Table doesn't exist")

        clear()
        
        
def DispSortBal():      #Function to Display records as per ascending order of Balance
    try:
        cmd="select * from bank order by BALANCE"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()   
        print("="*125)
    except:
        print("Table doesn't exist")


def DispSearchAcc(): #Function to Search for the Record from the Filewith respect to the account number
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the accountno to be searched")    
        for i in S:

            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
                
        else:
            print("Record Not found")
    except:
        print("Table doesn't exist")

def Update(): #Function to change the details of a customer        
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name")
                    i[1]=i[1].upper()
                    
                ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile")

                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email")
                    i[3]=i[3].upper()

                ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address")
                    i[4]=i[4].upper()

                ch=input("Change city(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City")
                    i[5]=i[5].upper()

                ch=input("Change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country")
                    i[6]=i[6].upper()
                    
                ch=input("Change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance"))
                cmd="UPDATE bank SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print("No such table")

def Delete():#Function to delete the details of a customer
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted")
                break
            
        else:
            print("Record not found")

    except:
        print("No such Table")

def Debit(): #Function to Withdraw the amount by assuring the minbalance of Rs 5000
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter the amount to be withdrawn"))
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE bank SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Debited")
                    break
                else:
                    print("There must be min balance of Rs 5000")
                    break
                    
            else:
                print("Record Not found")

    except:
        print("Table Doesn't exist")

    
def Credit(): #Function to Withdraw the amount by assuring the minvbalance of Rs 5000
    try:
            cmd="select * from bank"
            mycursor.execute(cmd)
            S=mycursor.fetchall()
            acc=input("Enter the account no from which the money is to be debited")
            for i in S:
                i=list(i)
                if i[0]==acc:
                    Amt=float(input("Enter the amount to be credited"))
                    i[7]+=Amt
                    cmd="UPDATE bank SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Credited")
                    break
            else:
                print("Record Not Found")
                
    except:
        print("Table Doesn't exist")

while True:
    Menu()
    ch=input("Enter your Choice")
    if ch=="1":
        Create()
    elif ch=="2":
        while True:
            MenuSort()
            ch1=input("Enter Choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        DispSearchAcc()
    elif ch=="4":
        Update()
    elif ch=="5":
        Delete()
    elif ch=="6":
        while True:
            MenuTransaction()
            ch1=input("Enter choice a/b/c")
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")

    elif ch=="7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")