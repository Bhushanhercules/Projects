# Enter our own details According to your preferences Where ever there are '*'

#Time
import time

#Calling MySQL and taking data
import mysql.connector as cn
conn=cn.connect(host='localhost',user='******',password='****',database='******')
bd=conn.cursor()
s="INSERT INTO ad(Card_no,PIN,Balance,Debited,CB) VALUES(%s,%s,%s,%s,%s)"

#Email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Email function base
def SendEMail(emailid,subject,message):
    try:
        msg=MIMEMultipart()
        msg['From'] = "********@gmail.com"
        password="*********"
        msg['To']=emailid
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], emailid ,msg.as_string())
        server.quit()
        print ("successfully sent email to %s." % emailid)

    except:
        print('Error in sending Mail')


def User_Login():
    #Greeting    
    print('\n\n\n \t\t\t\t\t\t**WELLCOME TO A.B.C BANK**')


    #Main Loop
    Tryagain = 1
    while Tryagain != 4:
        try:
            #User Interface
            #Checking Details of User
            Card_No=int(input('Enter Card Number: '))
            PIN =int(input('Enter Your PIN Number: '))
            password=1234
            balance=1000000

            if PIN != password:
                print('Tryagain')
                time.sleep(1) #To take 1sec of pause
                Tryagain = Tryagain + 1 #by this Loop will automatically ends after 3 wrong attempts
                        
                        
            else:
                time.sleep(1)
                print('1. Balance Inquiry')
                print('2. Withdraw')
                print('3. Fund Transfer')
                print('4. Change PIN')
                

                press=int(input('choose from above option: '))

                if (press==1):
                    time.sleep(1)
                    print('Your current balance is:', balance)#Showing the current balance
                            
                elif (press==2):
                    withdraw=int(input('Enter amount: '))
                    balance1=balance-withdraw
                            
                    if withdraw >= 20000 or withdraw <= 100:
                        print('You cannot withdraw such amount')
                                
                    else:
                        time.sleep(1)
                        print('The amount:%s is deducted from your account' % withdraw)

                        #show the balance after calculateing
                        print('Your updated balance is:', balance1)

                        #Will send the mail to the user 
                        SendEMail('********@gmail.com','Amount Deducted','Your ATM card is used in ABC Bank ATM Machine')    

                        #will save data automatically in MySQl data in RDBMS
                        j=(Card_No,PIN,balance,withdraw,balance1)
                        bd.execute(s,j)
                        conn.commit()
                        
                elif (press==3):
                    time.sleep(1)

                    #Funds transfer
                    fund=int(input('How much amount you want to Transfer: '))
                    balance2=balance-fund
                    print('The Funds are Tranferd')

                    #show the balance after calculateing
                    print('And your Current Balance is:',balance2)

                    #Will send the mail to the user
                    SendEMail('********@gmail.com','Amount Deducted','Your ATM card is used in ABC Bank ATM Machine')

                    #will save data automatically in MySQl data in RDBMS
                    j1=(Card_No,PIN,balance,fund,balance2)
                    bd.execute(s,j1)
                    conn.commit()
                    
                else:
                    Try = 1
                    while Try != 4:
                        New=int(input('Enter new PIN'))
                        new=int(input('Confirm Your new PIN'))

                        if New==new:
                            print('Your PIN is Changed Sucesfully')
                            SendEMail('******@gmail.com','PIN CHANGED','Your ATM card PIN is Changed in ABC Bank ATM Machine')
                        else:
                            print('Try Again')
                            time.sleep(1) #To take 1sec of pause
                            Try = Try + 1 #by this Loop will automatically ends after 3 wrong attempts
        
        
        except:
            print('Error in the process')
            
    #it will appear in case of 3 wrong attempt of passwords       
    print('Your card is Locked \nTo unlock card Admin login requried')
    print('Please Contact Admin!, And ask for help')


def Admin_Login():
    print('\n\n\n \t\t\t\t\t\t**WELLCOME TO A.B.C BANK**')

    #Admin interface
    #Will send the mail to the user
    SendEMail('********@gmail.com','login OTP','your OTP :8937')
    num=8937

    Tryagain = 1
    while Tryagain != 4:

        OTP=int(input('For admin login please enter the given OTP: '))
        if OTP!=num:
                print('Tryagain')
                time.sleep(1) #To take 1sec of pause
                Tryagain = Tryagain + 1 #by this Loop will automatically ends after 3 wrong attempts


        else:
            print('Admin Login sucesful')
            print('1. Open New Account')
            print('2. Issue New Card')
            print('3. Close account')
            print('4, Lock or Unlock card')
            print('5. Generate Transaction report')
            print('6. Monthly teansaction analysis')
            print('7. Change Password')

            Enter=int(input('Enter Your Option: '))

            if (Enter==1):
                de=input("Enter costumer's personal details: ")
                print(de, "New Account is created Successfully")
            
            elif (Enter==2):
                acc=int(input("Enter Account Number: "))
                print(acc, "application for new card is been proceeded \nThe new card will be delivered to as soon as possible")

            elif (Enter==3):
                ac=int(input("Enter Account number: "))
                print(ac, "application for closing an account is under surviliance, it will take 2 to 3 working days")

            elif (Enter==4):
                print('To Unlock Your Card Enter Account details')
                card_no=int(input('Enter Your card_no: '))

                if card_no==Card_No:
                    print('Your Card is Unlocked')

                else:
                    print('Your card is still Locked')

            elif (Enter==5):
                acn=int(input("Enter Account number: "))
                print(acn, "Transaction Report")

            elif (Enter==6):
                ac=int(input("Enter account number: "))
                print(ac, "Monthly Transaction")
                
            else:
                old=input('Enter your old password')
                ne=input('Enter your new password')
                print('Your Password is changed Successfull \nHave a Good Day')

    print('You have completed your 3 attempts try after 24 hours')



print('Welcome \nSelect from below option')
print('1. Costumer Login')
print('2. Admin Login')
Des=int(input('Enter from above option: '))
if Des==1:
    User_Login()
else:
    Admin_Login()
