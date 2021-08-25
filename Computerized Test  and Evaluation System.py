from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def Sendmail(emailid,subject,message):
    rm=MIMEMultipart()
    rm['From']= '**********@gmail.com' # enter senders email id 
    password="********" # enter senders password
    rm['To']=emailid
    rm['Subject']=subject
    rm.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(rm['From'], password)
    server.sendmail(rm['From'], emailid, rm.as_string())
    server.quit()
    print("successfully sent email to %s." % emailid)

    
    
print('Login in as: ')
print('1. Administrator \n2. Student \n3. Data Entry Operator')


s=int(input('Select yours:'))

if s==1:
    a=input('Enter your Email id: ')
    p=input('Enter your password: ')
    a_pasword="admin"

    Tryagain=True
    while Tryagain:
        
        
        if p==a_pasword:
            print('1. Add Courses \n2. Publish Result \n3. Show All Exams \n4. Show All Students \n5. Show All Courses \n6. Lock or Unlock users \n7. Change Password \n8. Exit')
                    
            press=int(input('Select from above Options: '))

            if press==1:
                new=input("Enter new course: ")
                print(new,'Course is added')

            elif press==2:
                name=input("Enter Student's name: ")
                ids=int(input("Enter student's Id.no: "))
                print(name,"Result:")

            elif press==3:
                print('All Exams:')

            elif press==4:
                print('Name of All students:')

            elif press==5:
                print('List of Courses:',)

            elif press==6:
                print('1. Lock the user \n2. Unlock the user')

                select=int(input('Select from above option'))

                if select==1:
                    name1=input("Enter Student's name: ")
                    ids=int(input("Enter student's Id.no: "))
                    print(name1,"id's is Locked")

                else:
                    name2=input("Enter Student's name: ")
                    ids=int(input("Enter student's Id.no: "))
                    print(name2,"Id's is Unlocked")

            elif press==7:
                Tryagain=True
                while Tryagain:
                    new=input('Enter new password')
                    New=input('Confirm new password')

                    if new==New:
                        print('Password is Reset')

                    else:
                        print('Try again')
                        Tryagain=False
            else:
                print('Okay Bye!')
                break
        else:
            print('Try again')
            Tryagain=False

elif s==2:
    e=input('Enter your Email:')
    p1=input('Enter your password')
    s_password="student"
    
    Tryagain=True
    while Tryagain:

        if p1==s_password:
            print('1. Change Password \n2. Check Result \n3. Give Test \n4. Exit')
            

            Select=int(input('Select from above option'))

            if Select==1:
                Tryagain=True
                while Tryagain:
                    enter=input('Enter new password:')
                    Enter=input('Confirm new password:')

                    if enter==Enter:
                        Sendmail('*********@gmail.com','Password!!',"Your Password is changed, Report if You didn't!")
                        #enter recivers emailid
                        print('Your Password is Changed')

                    else:
                        print('Try again')
                        Tryagain==False

            elif Select==2:
                Tryagain=True
                while Tryagain:
                    mail=input('Enter your Email:')

                    if e==mail:
                        print('Your Result')

                    else:
                        print('Try again')
                        Tryagain==False

            elif Select==3:
                print('Start your test')

            else:
                print('Okay Bye!')
        break
    else:
        print('Try again')
        Tryangain=False

else:
    d=input('Enter your Email:')
    p2=input('Enter your password:')
    d_password="DO"
    
    Tryagain=True
    while Tryagain:
        
        if p2==d_password:
            print('1. Schedule Exams \n2. Add Questions \n3. Enter Students Details \n4. Change Password \n5. Update Student Details \n6. Exit')
                
            press=int(input('Select from above option: '))

            if press==1:
                Sendmail('*******@gmail.com','Exam','Your Exam is Scheduled, Be prepared!')
                #enter recivers emailid
                print('Scheduled Exam')

            elif press==2:
                course=input('In which course you want to add?')
                print('Questions are added in it')

            elif press==3:
                print('Student detail are entered Successfully')

            elif press==4:
                Tryagain=True
                while Tryagain:
                    enter=input('Enter new password:')
                    Enter=input('Confirm new password:')

                    if enter==Enter:
                        print('Your Password is Changed')

                    else:
                        print('Try again')
                        Tryagain==False

            elif press==5:
                Sendmail('********@gmail.com','Data Varification','Dear Student, Your personal information is been updated by our associate, Kindly Check the information updated on our official website is valid or not, if not then report it!')
                #enter recivers emailid
                print('Varification Mail is sent to the student')
                print('Student detail is updated')

            else:
                print('okay Bye!')
        break
                    
    else:
        print('Incorrect Password \tTryagain')
        Tryagain==False    
