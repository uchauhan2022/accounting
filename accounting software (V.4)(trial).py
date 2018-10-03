#IMPORTING REQUIRED MODULES

import os,pickle,time,sys,random

# CLASS "ACCOUNT_HOLDER" WHICH CONTAINS ALL DETAILS OF THE ACCOUNT HOLDER.

class account_holder():
    def __init__(self): 
        self.acc_num = 0
        self.name = ""
        self.phone = 0
        self.password = 0
        self.balance = 0
        self.aadhaar_id = 0
        self.count = 23776383

# MEMBER FUNCTION TO CREATE A NEW ACCOUNT.

    def create_account(self):
        global c
        print( " * * * * * * * * * * * * * * * * ")
            #TAKING DETAILS FROM THE USER.
        self.name = input("ENTER YOUR NAME : ")
        self.phone = int(input("ENTER YOUR CONTACT NUMBER : "))
        self.aadhaar_id = int(input("ENTER YOUR AADHAAR ID : "))
        print("CREATING YOUR ACCOUNT...")
        time.sleep(1)
            #GENERATING ACCOUNT NUMBER.
        self.acc_num = self.count+c
        c+=3
        print("******* ACCOUNT SUCCESSFULLY CREATED *******")
        print("ACCOUNT NUMBER : ", self.acc_num)
        print("NAME : ", self.name)
        print("CONTACT NUMBER : ", self.phone)
        print("BALANCE : ", self.balance)
        print("AADHAAR ID : ", self.aadhaar_id)
            #GENERATING A RANDOM 4 DIGIT PASSWORD
        self.password = random.randint(1000,9999)
        print("YOUR 4 DIGIT PIN IS : ", self.password)
        print(" kindly note your ACCOUNT NUMBER and PASSWORD for further use ")
            #INCREMENTING THE COUNT VARIABLE AND STORING IT INTO A TEXT FILE FOR FURTHER USE.
        file3 = open("c.txt" , "w")
        file3.write(str(c))
        file3.close()

#MEMBER FUNCTION TO CREATE A REFERENCE LIST.        

    def file_out(self):
        rec ="ACCOUNT HOLDER'S NAME : "+str(self.name)+" , ACCOUNT NUMBER : "+str(self.acc_num) +  " , PASSWORD : "+str(self.password)+"\n"
            #CREATING A REFERENCE FILE WHICH CONTAINS ACCOUNT NUMBERS AND PASSWORDS OF ALL ACCOUNTS. 
        file4 = open("REFERENCE FILE.txt", "a+")
        file4.write(rec)
        file4.close()

#MEMBER FUNCTION TO VERIFY THE PASSWORD.

    def password_check(self,pword): # INTRODUCING A PARAMETER = 'pword' (USER INPUT).
        if self.password == pword:
            return True
        else:
            return False

#MEMBER FUNCTION TO CREDIT AMOUNT INTO THE ACCOUNT.


    def credit(self):
        print( " * * * * * * * * * * * * * * * * ")
        add = int( input ( "ENTER THE AMOUNT TO BE DEPOSITED : "))
            #UPDATING THE BALANCE.
        self.balance += add
        print(self.balance)
        print (" ******* MONEY SUCCESSFULLY DEPOSITED *******")

#MEMBER FUNCTION TO DEBIT AMOUNT FROM THE ACCOUNT.

    def debit(self):
        print( " * * * * * * * * * * * * * * * * ")
        sub = int( input ( "ENTER THE AMOUNT TO BE WITHDRAWN : "))
            #CHECKING IF THE AMOUNT TO BE WITHDRAWN IS LESS THAN THE BALANCE.
        if self.balance >= sub:
            self.balance -= sub
            print (" ******* MONEY SUCCESSFULLY WITHDRAWN *******")
        else:
            #IF AMOUNT TO BE WITHDRAWN > BALANCE.
            print("INSUFFICIENT FUNDS !!" )
            print("WITHDRAWAL DECLINED" )

#MEMBER FUNCTION TO SHPW THE DETAILS OF ACCOUNT HOLDER.

    def show(self):
        print( " * * * * * * * * * * * * * * * * ")
        print("******* YOUR ACCOUNT DETAILS *******")
        print(" ACCOUNT NUMBER : ", self.acc_num)
        print(" NAME : ", self.name)
        print(" CONTACT NUMBER : ", self.phone)
        print(" BALANCE : ", self.balance)
        print(" AADHAAR ID : ", self.aadhaar_id)
#CLASS ENDS.

#CREATING A FUNCTION TO WRITE THE ACCOUNT DETAILS ON TO A BINARY FILE.
        
def store_new():
        #CREATING A UNIQUE FILE NAME.
    path = "account_data_" + str(user.acc_num) + ".log"
    file = open(path,"w+b")
        #DUMPING THE DATA INTO THE FILE.
    pickle.dump(user,file)
    file.close()

#CREATING A FUNCION TO UPDATE THE ACCOUNT DETAILS(BALANCE) AFTER A TRANSACTION.
    
def update():
        #ACCESSING THE GLOBAL VARIABLE = 'user'.
    global user
    path = "account_data_" + str(user.acc_num) + ".log"
        #DUMPING THE NEW DATA IN A NEW FILE.
    file2 = open("abc.log", "wb+")
    pickle.dump(user,file2)
    file2.close()
        #DELETING THE ACTUAL FILE.
    os.remove(path)
        #RENAMING THE NEW FILE TO THE ACTUAL FILE NAME.
    os.rename("abc.log",path)

#CREATING A FUNCTION TO EXIT THE APPLICATION.
    
def _exit():
    print("THANK YOU ")
    time.sleep(10)
    sys.exit()

#CREATING A FUCTION THE CONTAINS THE MAIN PROGRAM RUN FOR CREATING A NEW ACCOUNT.

def create():
        #ACCESSING THE GLOBAL VARIABLE = 'user','c'.   
    global user,c
        #CREATING A NEW OBJECT FOR THE ACCOUNT HOLDER.
    user = account_holder()
        #CALLING THE 'create_account()' MEMBER FUNCTION.
    user.create_account()
        #CALLING THE 'store_new()' FUNCTION TO STORE THE ACCOUNT DETAILS. 
    store_new()
        #CALLING THE 'file_out()' MEMBER FUNCTION TO UPDATE REFERENCE FILE.
    user.file_out()
        #DISPLAYING AVAILABLE OPTIONS.
    print("KINDLY CHOOSE AN APPROPRIATE OPTION")
    print("PRESS 1 TO MOVE TO THE PREVIOUS MENU")
    print("PRESS 2 TO MOVE TO THE APPLICATION WINDOW")
    print("PRESS 3 TO EXIT THE APPLICATION")
    opt1 = int(input(" ENTER YOUR CHOICE : "))
    if opt1 == 1:
        #GETTING BACK TO THE MAIN MENU.
        main()        
    elif opt1 == 3:
        #EXITING FROM THE PROGRAM.
        _exit()
    elif opt1 == 2:
        #MOVING TO THE APPLICATION MENU.
        app_menu()

#CREATING A FUCTION THE CONTAINS THE MAIN PROGRAM RUN FOR APPLICATION MENU.

def app_menu():
        #ACCESSING THE GLOBAL VARIABLE = 'user'.
    global user
    print("********** PYTHON ACCOUNTING APPLICATION **********")
    print("**********       APPLICATION MENU        **********")
        #ASKING THE USER FOR ACCOUNT NUMBER.
    h = int(input("ENTER ACCOUNT NUMBER (incase you dont have an account, move to the main menu by pressing '0000':"))
        #CHECKING THE CONDITION TO MOVE TO MAIN MENU.
    if h == 0000:
        #MOVING TO MAIN MENU.
        main()
    path = "account_data_" + str(h) + ".log"
        #CHECKING WHETHER THE ACCOUNT EXISTS.
    if not os.path.exists(path):
        #SWITCHHING BACK TO APPLICATION MENU IF ACCOUNT DOES NOT EXIST.
        print("INVALID ACCOUNT NUMBER")
        print("PLEASE TRY AGAIN")
        app_menu()
    else:
        #USING TRY BLOCK TO READ THE ACCOUNT DETAILS FROM THE ACCOUNT BINARY FILE.
        try:
            file=open(path,'rb')
            file.seek(0)
            user=pickle.load(file)
        #EXCEPTING END OF FILE ERROR.
        except EOFError:
            pass
        file.close()
        #ASKING USER FOR THE ACCOUNT PASSWORD.
        pword= int(input("ENTER YOUR 4 - DIGIT PIN : "))
                #VERIFFYING THE PASSWORD
        if user.password_check(pword):
            print("ACCESS GRANTED")
                #DISPLAYING AVAILABLE OPTIONS.
            print("KINDLY CHOOSE AN APPROPRIATE OPTION")
            print("PRESS 1 TO DEPOSIT MONEY ")
            print("PRESS 2 TO WITHDRAW MONEY ")
            print("PRESS 3 TO SHOW ACCOUNT DETAILS ")
            print("PRESS 4 TO SIGN OUT AND RETURN TO MAIN MENU ")
            print("PRESS 5 TO EXIT THE APPLICATION ")
            opt2 = int(input(" ENTER YOUR CHOICE : "))
            if opt2 == 1:
                #CALLING THE 'credit()' MEMBER FUNCTION FOLLOWED BY THE 'update' FUNCTION.
                user.credit()
                update()
            elif opt2 == 2:
                #CALLING THE 'debit()' MEMBER FUNCTION FOLLOWED BY THE 'update' FUNCTION.
                user.debit()
                update()
            elif opt2 == 3:
                #CALLING THE 'show()' MEMBER FUNCTION.
                user.show()                
            elif opt2 == 4:
                #MOVING TO THE MAIN MENU BY CALLING 'main()' FUNCTION.
                main()
            elif opt2 == 5:
                #EXITING THE PROGRAM BY CALLING '_exit()' FUNCTION.
                _exit()
        else:
            #IF THE ENTERED PASSWORD DOES NOT MATCH.
            print("INCORRECT PASSWORD! \n ACCESS DENIED \n PLEASE TRY AGAIN !")
            app_menu()
    app_menu_2()
def app_menu_2():
    global user

        #DISPLAYING AVAILABLE OPTIONS.
    print("KINDLY CHOOSE AN APPROPRIATE OPTION")
    print("PRESS 1 TO DEPOSIT MONEY ")
    print("PRESS 2 TO WITHDRAW MONEY ")
    print("PRESS 3 TO SHOW ACCOUNT DETAILS ")
    print("PRESS 4 TO SIGN OUT AND RETURN TO MAIN MENU ")
    print("PRESS 5 TO EXIT THE APPLICATION ")
    opt2 = int(input(" ENTER YOUR CHOICE : "))
    if opt2 == 1:
        #CALLING THE 'credit()' MEMBER FUNCTION FOLLOWED BY THE 'update' FUNCTION.
        user.credit()
        update()
    elif opt2 == 2:
        #CALLING THE 'debit()' MEMBER FUNCTION FOLLOWED BY THE 'update' FUNCTION.
        user.debit()
        update()
    elif opt2 == 3:
        #CALLING THE 'show()' MEMBER FUNCTION.
        user.show()                
    elif opt2 == 4:
        #MOVING TO THE MAIN MENU BY CALLING 'main()' FUNCTION.
        main()
    elif opt2 == 5:
        #EXITING THE PROGRAM BY CALLING '_exit()' FUNCTION.
        _exit()
    app_menu_2()

    
 
# MAIN
#CREATING GLOBAL VARIABLES : 'user','c'.
global user,c
#READING THE CALUE OF 'c' FROM THE SOURCE TEXT FILE.
file3 = open("c.txt","r")
c=file3.read()
c=int(c)
file3.close()

#CREATING A FUNCTION FOR ACCESSING THE MAIN MENU OF THE PROGRAM.

def main():
    #CREATING A USER DEFINED EXCEPTION.
    class Error(Exception):
        pass
    error1 = Error
    #INFINITE LOOP.
    while True:
        print("********** PYTHON ACCOUNTING APPLICATION **********")
        print("KINDLY CHOOSE AN APPROPRIATE OPTION")
        print("PRESS 1 IF YOU WANT TO CREATE A NEW ACCOUNT ")
        print("PRESS 2 IF YOU ALREADY HAVE AN EXISTING ACCOUNT ")
        first_choice()
#CREATING A UNCTION WHICH USES AN USER DEFINED EXCEPTION BLOCK TTO INPUT CHOICE.
def first_choice():
    try:
        opt = int(input("    ENTER YOUR CHOICE : "))
        if opt == 1:
            #CREATING NEW ACCOUNT BY CALLING 'creat()' FUNCTION.
            create()
        elif opt == 2:
            #MOVING TO THE APPLICATION MENU USING 'app_menu' FUNCTION.
            app_menu()
        else:
            raise error1
    except:
        #IF EXCEPTION IS RAISED.
        print("PLEASE ENTER YOUR CHOICE ONLY AS 1 OR 2 (WITHOUT SPACE OR ANY SPECIAL CHARACTER)")           
        first_choice()

#STARTING THE PROGRAM.
            
main()   
        

        
        
        
