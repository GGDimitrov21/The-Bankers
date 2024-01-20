import webbrowser #web page url library
import os #system
import time #sleep()
<<<<<<< HEAD
import json #Convert from JSON to Python
from urllib.request import urlopen

with open('LoginForm.js') as f: #open LoginForm.js to get the data
    data=json.load(f) #get the data

for state in data['states']:
    print(state['E-mail'], state['password']) #some JSON: x =  '{ "E-mail":"...@codingburgas.bg", "password":"...45667"}'

with open('Data.txt', 'w') as f: #open Data.txt to write
    f.write(data, f, indent=2) #takes the data and puts it in the text file

with urlopen("url_on_web_page") as responce:
    source=responce.read() 
data = json.loads(source) #gets all the data

url = "url_on_web_page"
responce = urlopen(url)
data = json.loads(responce.read().decode('utf-8'))
print(data)
=======
#import json #Convert from JSON to Python

#with open('../pages/LoginForm.js') as f: #open LoginForm.js to get the data
#    data=json.load(f) #get the data

#for state in data['states']:
#    print(state['Username'], state['password']) #some JSON: x =  '{ "Username":"ATSivkov21", "password":"...45667"}'

#with open('Data.txt', 'w') as f: #open Data.txt to write
#    f.write(data, f, indent=2) #takes the data and puts it in the text file

#with urlopen("url_on_web_page") as responce:
#    source=responce.read() 
#data = json.loads(source) #gets all the data

#url = "url_on_web_page"
#responce = urlopen(url)
#data = json.loads(responce.read().decode('utf-8'))
#print(data)
>>>>>>> 880d9d5cef434efed0ed8163f078071d81fa3450

#Example
#Convert from JSON to Python:

#import json

# some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["age"])

#x=json.loads(y) 

def open_web_page():
   uniform_resource_locator=str('../pages/LoginForm.html')
   webbrowser.open_new_tab(uniform_resource_locator) 

count_profiles_passwords = 1
profiles_passwords_file = open("../python/Data.txt", "r")
list_profiles_passwords = profiles_passwords_file.readlines()
count_profiles_passwords = list_profiles_passwords[len(list_profiles_passwords)-1][0]
count_profiles_passwords_1 = int(count_profiles_passwords)
count_profiles_passwords = count_profiles_passwords_1 + 1
profiles_passwords_file.close()
print(f"rows_profiles_passwords - {len(list_profiles_passwords)}")
print(f"profiles_passwords - {list_profiles_passwords}")
print(f"Profiles - {count_profiles_passwords-1}")

#function print all profiles and passwords in text document
def p_p():
    profiles_passwords_file = open("Data.txt", "r")
    print(profiles_passwords_file.read())
    time.sleep(5)
    profiles_passwords_file.close()

#function to check data in a text document
def log_in():
    true_or_false_log_in = False
    profiles_passwords_file = open("Data.txt", "a")

    #enter an email
    Email_addres=input(str("Write your E-mail : "))

    #enter an password
    Passwords=input(str("Write your password : "))

    #the for loop to search for data in a text 
    for i in range(2, len(list_profiles_passwords)):
        if(list_profiles_passwords[i].find("Pr-"+Email_addres)>0 and list_profiles_passwords[i].find("Pa-"+Passwords)>0 and true_or_false_log_in == False):
            print(f"It is line {i}")
            true_or_false_log_in = True
            print("True")
        #(i == len(list_profiles_passwords) and true_or_false_log_in == False)
            
        elif(true_or_false_log_in==False and i==len(list_profiles_passwords)-1):
            print("False")
            #sign_up()
            profiles_passwords_file.write(f"\n{count_profiles_passwords} :    " + "Pr-" + Email_addres + "   " + "Pa-" + Passwords)
        #else:
        #    print("Error")
    profiles_passwords_file.close()

#function to enter data into a text document
def sign_up():

    #enter an email
    Email_addres=input(str("Write your E-mail : "))

    #enter a password
    Passwords=input(str("Write your password : "))

    #enter an age 
    Age_person=input(int("Write your age : "))

    #the condition checks the entered email
    if(Email_addres.find("@abv.bg")>0 or Email_addres.find("@codingburgas.bg")>0 or Email_addres.find("@gmail.com")>0):
        #the condition checks the length of the password
        if(len(Passwords)>=8):
            #the while loop checks the entered age
            while(Age_person<18):
                Age_person=input(int("Write your age : "))
            profiles_passwords_file = open("Data.txt", "a")
            profiles_passwords_file.write(f"\n{count_profiles_passwords} :    " + "Pr-" + Email_addres + "   " + "Pa-" + Passwords)
            profiles_passwords_file.close()

        else:
            #the while loop checks the length of the password
            while(len(Passwords)<8):
                Passwords=input(str("Write your password : "))

    else:
        #while loop returns print
        while(Email_addres.find("@abv.bg")<0 or Email_addres.find("@codingburgas.bg")<0 or Email_addres.find("@gmail.com")<0):
            Email_addres=input(str("Write your E-mail : "))

#function to delete data in text document
def delete():
    profiles_passwords_file = open("Data.txt", "r")
    list_profiles_passwords = profiles_passwords_file.readlines()
    profiles_passwords_file.close()

    num_delete_account = input("Write number for delete : ")
    while(int(num_delete_account)<=1):
        num_delete_account = input("Write number for delete : ")
    list_profiles_passwords.pop(int(num_delete_account))
    os.remove("Data.txt")
    profiles_passwords_file = open("Data.txt", "a")
    for i in range(0, len(list_profiles_passwords)):
        if(i>=int(num_delete_account)):
            num_minus = int(list_profiles_passwords[i][0])
            num_minus = int(num_minus) - 1
            list_profiles_passwords[i][0]=str(num_minus)
           
        profiles_passwords_file.write(str(list_profiles_passwords[i]))

#main function
def main():
    chouse=" "
    while(chouse!="exit" or chouse!="stop"):
        menu = [
            "|  page |",
            "| p _ p |",
            "|log  in|",
            "|sign up|",
            "|del ete|"
        ]

        #print menu
        for i in range(0,5):
            print(menu[i])
 
        chouse=input(str(" - "))
        while(chouse!="p_p" and chouse!="log_in" and chouse!="log in" and chouse!="sign_up" and chouse!="sign up" and chouse!="delete" and chouse!="exit" and chouse!="stop"):

            os.system("cls")

            menu = [
                "|  page |",
                "| p _ p |",
                "|log  in|",
                "|sign up|",
                "|del ete|"
            ]

            #print menu
            for i in range(0,5):
                print(menu[i])
    
            chouse=input(str(" - "))

        #the conditions check the entered value
        if(chouse=="page" or chouse=="pages"):
            open_web_page()  

        if(chouse=="p_p" or chouse=="profiles" or chouse=="passwords"):
            p_p()
            time.sleep(10)

        if(chouse=="log_in" or chouse=="log in" or chouse=="login"):
            log_in()
            time.sleep(2)

        if(chouse=="sign_up" or chouse=="sign up" or chouse=="signup"):
            sign_up()
            time.sleep(2)

        if(chouse=="delete" or chouse=="del"):
            delete()
            time.sleep(2)

        if(chouse=="exit" or chouse=="stop"):
            with open('python.py','r') as firstfile, open('Profile_Password_Python_Code.txt','a') as secondfile: 
      
                # read content from first file 
                for line in firstfile: 
                            
                    # append content to second file 
                    secondfile.write(line)

            file_profiles_passwords_txt=open('Profile_Password_Python_Code.txt','a')
            file_profiles_passwords_txt.write("\n----------------------------------------\n----------------------------------------")
            file_profiles_passwords_txt.close()

            #code exit
            exit()

        #clear the system window
        os.system("cls")

    #code exit
    exit()

#performs the main function
main()