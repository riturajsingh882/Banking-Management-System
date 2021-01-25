import mysql.connector
import  os
import getpass

def  clear():
    if os.name == "nt":
        os.system("cls") 

    else:
        os.system("clear")

usr = input("Enter your MySQL Username(root) : ")

if usr=='':
    usr="root"

pas = getpass.getpass("Enter your MySQL Password : ")

try:
    mydb=mysql.connector.connect(user=usr,passwd= pas,host='localhost')

except:
    print("Failed to connect to Mysql! Please make sure that the given credentials are valid.")
    exit()

mycursor = mydb.cursor(buffered=True)
#Created Database bankDB
mycursor.execute('create database if not exists BankDB')
mycursor.execute('use BankDB')

            
def password():
    try: 
        mycursor.execute("select pass from password")
        data = mycursor.fetchall()
        return data[0][0]

    except:
        while True:
            print("Enter your new authentication password : ")
            pas = getpass.getpass()
            print("Confirm your password : ")
            pas2 = getpass.getpass()

            if pas != pas2:
                print("The two passwords did not match, please try again!")

            else:
                mycursor.execute("create table if not exists password(pass varchar(100));")
                mycursor.execute(f"insert into password values('{pas}');")
                mydb.commit()
                print("Password added successfully!")
                break
        
password()


#Function to display the menu
def Menu(): 
    clear()
    print("*"*130)
    print("MAIN MENU\n".center(130))
    print("1. Insert Record/Records".center(130))
    print("2. Display Records as per Account Number".center(130))
    print("3. Search Record Details as per the account number".center(130))
    print("4. Update Record".center(130))
    print("5. Delete Record".center(130))
    print("6. TransactionsDebit/Withdraw from the account".center(130))
    print("7. Change Password".center(130))
    print("8. Exit".center(130))
    print("*"*130)


#Function to display the menu sorted-ly
def MenuSort():
    clear()
    print("*"*130)
    print("MAIN MENU>>>DISPLAY RECORDS\n".center(130))
    print(" a. Sorted as per Account Number".center(130))
    print(" b. Sorted as per Customer Name".center(130))
    print(" c. Sorted as per Customer Balance".center(130))
    print(" d. Back".center(130))
    print("*"*130)
    

#Function to display the transactions menu
def MenuTransaction():
    clear()
    print("*"*130)
    print("MAIN MENU>>>TRANSACTIONS\n".center(130))
    print(" a. Debit/Withdraw from the account".center(130))
    print(" b. Credit into the account".center(130))
    print(" c. Back".center(130))
    print("*"*130)


#Function to create the main table
def Create():
    mycursor.execute('create table if not exists bank(ACCNO varchar(16),NAME varchar(50),MOBILE varchar(10),EMAIL varchar(50),ADDRESS varchar(100),CITY varchar(50),COUNTRY varchar(20),BALANCE decimal(50,2))')
    Insert()

#Function to insert records into the table
def Insert():
    clear()
    print("*"*130)
    print("MAIN MENU>>>INSERT RECORDS".center(130))
    print("*"*130)
    print("Please enter your authentication password to continue!")
    pas = getpass.getpass()
    if pas == password():
        print("Authentication successful!")
    
    else:
        input("The given password is incorrect! Please press enter to return to main menu.")
        return
    #Loop for accepting records
    while True:  
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
        #mycursor.fetchall()
        mydb.commit()
        print("The values have been entered Successfully!")
        ch=input("Do you want to enter more records(Y/n) : ")
        if ch=='y' or ch=='Y':
            continue
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


#Function to Display records as per ascending order of Name
def DispSortName(): 
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
    except:
        print("Table doesn't exist")


#Function to Display records as per ascending order of Balance
def DispSortBal():      
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


 #Function to Search for the Record from the Filewith respect to the account number
def DispSearchAcc():
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the account no to be searched")    
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

#Function to change the details of a customer    
def Update(): 
    print("*"*130)
    print("MAIN MENU>>>UPDATE RECORDS\n".center(130))  
    print("*"*130)
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the account no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N) : ")
                if ch=='y' or ch=='Y':  
                    i[1]=input("Enter Name : ")
                    i[1]=i[1].upper()
                    
                ch=input("Change Mobile(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile : ")

                ch=input("Change Email(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email : ")
                    i[3]=i[3].upper()

                ch=input("Change Address(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address : ")
                    i[4]=i[4].upper()

                ch=input("Change city(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City : ")
                    i[5]=i[5].upper()

                ch=input("Change Country(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country : ")
                    i[6]=i[6].upper()
                    
                ch=input("Change Balance(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance : "))
                cmd=f"UPDATE bank SET NAME='{i[1]}',MOBILE='{i[2]}',EMAIL='{i[3]}',ADDRESS='{i[4]}',CITY='{i[5]}',COUNTRY='{i[6]}',BALANCE={i[7]} WHERE ACCNO='{i[0]}';"
                #val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd)
                mydb.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print("No such table")


#Function to delete the details of a customer
def Delete():
    try:
        cmd="select * from bank"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the account no whose details to be removed: ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno={A}"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted")
                break
            
        else:
            print("Record not found")

    except:
        print("No such Table")


#Function to Withdraw the amount by assuring the minbalance of Rs 5000
def Debit(): 
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
                    cmd=f"UPDATE bank SET BALANCE={Amt} WHERE ACCNO={acc}"
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


#Function to Withdraw the amount by assuring the minvbalance of Rs 5000   
def Credit(): 
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
                    cmd=f"UPDATE bank SET BALANCE={Amt} WHERE ACCNO={acc}"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Credited")
                    break
            else:
                print("Record Not Found")
                
    except:
        print("Table Doesn't exist")


#while loop that calls the main menu!
while True:
    Menu()
    ch=input("Enter your Choice : ")
    if ch=="1":
        Create()

    elif ch=="2":
        #while True:
            MenuSort()
            ch1=input("Enter Choice a/b/c/d : ")
            clear()
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                break
            else:
                print("Invalid choice")
            input("Press enter to continue.")

    elif ch=="3":
        clear()
        print("*"*130)
        print("MAIN MENU>>>SEARCH RECORDS\n".center(130))
        print("*"*130)
        DispSearchAcc()
        
    elif ch=="4":
        clear()
        print("*"*130)
        print("MAIN MENU>>>UPDATE RECORDS\n".center(130))
        print("*"*130)
        print("Please enter your authentication password to continue!")
        pas = getpass.getpass()
        if pas == password():
            Update()
        
        else:
            input("The given password is incorrect! Please press enter to return to main menu.")

    elif ch=="5":
        clear()
        print("*"*130)
        print("MAIN MENU>>>DELETE RECORDS\n".center(130))
        print("*"*130)
        print("Please enter your authentication password to continue!")
        pas = getpass.getpass()
        if pas == password():
            Delete()
        
        else:
            input("The given password is incorrect! Please press enter to return to main menu.")

    elif ch=="6":
        while True:
            MenuTransaction()
            ch1=input("Enter choice a/b/c : ")
            clear
            if ch1 in ['a','A']:
                print("*"*130)
                print("MAIN MENU>>>TRANSACTIONS>>>DEBIT\n".center(130))
                print("Please enter your authentication password to continue!")
                pas = getpass.getpass()
                if pas == password():
                    Debit()
                
                else:
                    input("The given password is incorrect! Please press enter to return to main menu.")

            elif ch1 in ['b','B']:
                print("*"*130)
                print("MAIN MENU>>>TRANSACTIONS>CREDIT\n".center(130))
                print("Please enter your authentication password to continue!")
                pas = getpass.getpass()
                if pas == password():
                    Credit()
                
                else:
                    input("The given password is incorrect! Please press enter to return to main menu.")

            elif ch1 in ['c','C']:
                break

            else:
                print("Invalid choice")
            input("Press enter to continue.")

    elif ch=="7":
        clear()
        print("*"*130)
        print("MAIN MENU>>>CHANGE PASSWORD\n".center(130))
        print("*"*130)
        x=input("Do you want to update your authentication password? Y/N: ")
        if x.lower()=='y':
            print("Please enter your current password.")
            pas = getpass.getpass()
            if pas == password():
                print("Enter your new authentication password.")
                npas = getpass.getpass()
                print("Confirm your password.")
                npas2 = getpass.getpass()

                if npas != npas2:
                    print("The two passwords did not match, please try again later!")
                    continue
            
                else:
                    mycursor.execute(f"update password set pass = '{npas}' where pass = '{pas}';")
                    mydb.commit()
                
            else:
                print("The entered password is incorrect! Please enter the correct password and try again!")
                
        elif x.lower()=='n':
            print("Ok!")
            continue

        else:
            print("Wrong Choice Entered")
            continue
        input("Press enter to continue.")

    elif ch=="8":
        print("Exiting...")
        break

    else:
        print("Wrong Choice Entered")
        continue