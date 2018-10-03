import os
def create_account():
    file= open ("account_list.txt","r+")
    global s_no, name, address, phone, balance, a_num
    a= file.readlines()
    b=len(a)
    s_num = b+1
    print( " * * * * * * * * * * * * * * * * ")
    name = input("ENTER YOUR NAME : ")
    phone = input("ENTER YOUR CONTACT NUMBER : ")
    balance = 0
    a_num = 2373648 * 10 + s_num
    rec = str(a_num) + "," + str(name) + "," + str(phone) + "," + str(balance) + "\n"
    print("******* ACCOUNT SUCCESSFULLY CREATED *******")
    print("ACCOUNT NUMBER : ", a_num)
    print("NAME : ", name)
    print("CONTACT NUMBER : ", phone)
    print("BALANCE : ", balance)
    print(" kindly note your account number for further use ")
    file.write(rec)
    file.close()

def credit(x):
    global b
    file= open ("account_list.txt","r+")
    a_num = x
    a = file.readlines() # read the whole file as a list of strings
    for i in range(0, len(a)): # split the list into elements
        rec = a[i] # element of the list [  WORKING FINE  ]
        n = rec.rstrip('\n') # remove new line character form the end
        record = n.split(',') # separate each record accd to delimiter
        b = record [0] # b = account number
        if b == str(a_num):
            c = i # index of the element where the account number matched
            print(c)
            break
    d = a[c] # record of matched account number
    e = d.split(',') # split the record into another list
    print( " * * * * * * * * * * * * * * * * ")
    add = int( input ( "ENTER THE AMOUNT TO BE DEPOSITED : "))
    f=e[3] # initializing 'f' with the balance
    f= int(f) 
    f += add # updating the balance
    e[3] = f # updating the record
    g = str(e[0]) + "," + str(e[1]) + "," + str(e[2]) + "," + str(e[3]) + "\n"
    a[c] = g
    file2 = open("abc.txt", "w")
    file2.writelines(a)
    file.close()
    file2.close()
    os.remove("account_list.txt")
    os.rename("abc.txt","account_list.txt")
    print (" ******* MONEY SUCCESSFULLY DEPOSITED *******")
    
def debit(x):
    file= open ("account_list.txt","r+")
    a_num = x
    a = file.readlines() # read the whole file as a list of strings
    c = 0
    for i in range(0, len(a)): # split the list into elements
        rec = a[i] # element of the list [  WORKING FINE  ]
        n = rec.rstrip('\n') # remove new line character form the end
        record = n.split(',') # separate each record accd to delimiter
        b = record [0] # b = account number
        if b == str(a_num):
            c = i # index of the element where the account number matched
            print(c)
            break
    d = a[c] # record of matched account number
    e = d.split(',') # split the record into another list
    print( " * * * * * * * * * * * * * * * * ")
    add = int( input ( "ENTER THE AMOUNT TO BE WITHDRAWN : "))
    f=e[3] # initializing 'f' with the balance
    f= int(f) 
    f -= add# updating the balance
    if f < 0 :
        print("INSUFFICIENT FUNDS !!" )
        print("WITHDRAWAL DECLINED" )
    else:
        e[3] = f # updating the record
        g = str(e[0]) + "," + str(e[1]) + "," + str(e[2]) + "," + str(e[3]) + "\n"
        a[c] = g 
        file2 = open("abc.txt", "w")
        file2.writelines(a)
        file.close()
        file2.close()
        os.remove("account_list.txt")
        os.rename("abc.txt","account_list.txt")
        print ("******* MONEY SUCCESSFULLY WITHDRAWAL *******")
def show(x):
    file= open ("account_list.txt","r+")
    a_num = x
    a = file.readlines() # read the whole file as a list of strings
    c = 0
    for i in range(0, len(a)): # split the list into elements
        rec = a[i] # element of the list [  WORKING FINE  ]
        n = rec.rstrip('\n') # remove new line character form the end
        record = n.split(',') # separate each record accd to delimiter
        b = record [0] # b = account number
        if b == str(a_num):
            c = i # index of the element where the account number matched
            print(c)
            break
    d = a[c] # record of matched account number
    e = d.split(',') # split the record into another list
    print( " * * * * * * * * * * * * * * * * ")
    print("******* YOUR ACCOUNT DETAILS *******")
    print(" ACCOUNT NUMBER : ", e[0])
    print(" NAME : ", e[1])
    print(" CONTACT NUMBER : ", e[2])
    print(" BALANCE : ", e[3])

# MAIN

while True:
    print("********** PYTHON ACCOUNTING APPLICATION **********")
    print("KINDLY CHOOSE AN APPROPRIATE OPTION")
    print("PRESS 1 IF YOU WANT TO CREATE A NEW ACCOUNT ")
    print("PRESS 2 IF YOU ALREADY HAVE AN EXISTING ACCOUNT ")
    opt = int(input("    ENTER YOUR CHOICE : "))
    if opt == 1:
        create_account()
        print("KINDLY CHOOSE AN APPROPRIATE OPTION")
        print("PRESS 1 TO MOVE TO THE PREVIOUS MENU")
        print("PRESS 2 TO MOVE TO THE APPLICATION WINDOW")
        print("PRESS 3 TO EXIT THE APPLICATION")
        opt1 = int(input(" ENTER YOUR CHOICE : "))
        if opt1 == 1:
            continue
        elif opt1 == 3:
            break
        elif opt1 == 2:
            print("********** PYTHON ACCOUNTING APPLICATION **********")
            print("**********       APPLICATION MENU        **********")
            h = int(input("ENTER ACCOUNT NUMBER (incase you dont have an account, move to the main menu by pressing '0000':"))
            if h == 0000:
                continue
            file= open ("account_list.txt","r+")
            a = file.readlines() # read the whole file as a list of strings
            c = 0
            for i in range(0, len(a)): # split the list into elements
                rec = a[i] # element of the list [  WORKING FINE  ]
                n = rec.rstrip('\n') # remove new line character form the end
                record = n.split(',') # separate each record accd to delimiter
                b = record [0] # b = account number
                if b == str(h):
                   c=1
            if c==0:
                print("INVALID ACCOUNT NUMBER !!!")
                print("TRY AGAIN !!!")
                continue
            print("KINDLY CHOOSE AN APPROPRIATE OPTION")
            print("PRESS 1 TO DEPOSIT MONEY ")
            print("PRESS 2 TO WITHDRAW MONEY ")
            print("PRESS 3 TO SHOW ACCOUNT DETAILS ")
            print("PRESS 4 TO RETURN TO MAIN MENU ")
            print("PRESS 5 TO EXIT THE APPLICATION ")
            opt2 = int(input(" ENTER YOUR CHOICE : "))
            if opt2 == 1:
                credit(h)
            elif opt2 == 2:
                debit(h)
            elif opt2 == 3:
                show(h)
            elif opt2 == 4:
                continue
            elif opt2 == 5:
                break
    elif opt == 2:
        print("********** PYTHON ACCOUNTING APPLICATION **********")
        print("**********       APPLICATION MENU        **********")
        h = int(input("ENTER ACCOUNT NUMBER (incase you dont have an account, move to the main menu by pressing '0000':"))
        if h == 0000:
            continue
        file= open ("account_list.txt","r+")
        a = file.readlines() # read the whole file as a list of strings
        c = 0
        file.close()
        for i in range(0, len(a)): # split the list into elements
            rec = a[i] # element of the list [  WORKING FINE  ]
            n = rec.rstrip('\n') # remove new line character form the end
            record = n.split(',') # separate each record accd to delimiter
            b = record [0] # b = account number
            if b == str(h):
               c=1
               
        if c==0:
            print("INVALID ACCOUNT NUMBER !!!")
            print("TRY AGAIN !!!")
            continue
        print("KINDLY CHOOSE AN APPROPRIATE OPTION")
        print("PRESS 1 TO DEPOSIT MONEY ")
        print("PRESS 2 TO WITHDRAW MONEY ")
        print("PRESS 3 TO SHOW ACCOUNT DETAILS ")
        print("PRESS 4 TO RETURN TO MAIN MENU ")
        print("PRESS 5 TO EXIT THE APPLICATION ")
        opt2 = int(input("   ENTER YOUR CHOICE : "))
        if opt2 == 1:
            credit(h)
        elif opt2 == 2:
            debit(h)
        elif opt2 == 3:
            show(h)
        elif opt2 == 4:
            continue
        elif opt2 == 5:
            break
        
    
            
    
    

