import os #system(), remove()
import json #save data
import time #sleep()
import webbrowser #web page url library

name=str(input("Name - "))
e_mail=str(input("E-mail - "))
while(e_mail.find("@codingburgas.bg")<0 and e_mail.find("@abv.bg")<0 and e_mail.find("@gmail.bg")<0):
    e_mail=str(input("E-mail - "))
    os.system("cls")

password=str(input("Password - "))
while(len(password)<8):
    password=str(input("Password - "))
    os.system("cls")

phone_number=int(input("Phone number 089- "))
while(len(str(phone_number))<7 or len(str(phone_number))>7):
    phone_number=int(input("Phone number 089- "))
    os.system("cls")

money=int(input("Money - "))
os.system("cls")

dir=os.getcwd()

choose_log_in_sign_up=0

menu=[
    "________________",
    "|              |",
    "|  1-Log in    |",
    "|  2-Sing up   |",
    "|______________|" 
]

menu1=[
    "________________",
    "|              |",
    "|     Menu     |",
    "|  1-profiles  |",
    "|  2-data      |",
    "|  3-delete    |",
    "|  4-open web  |",
    "|  5-exit      |",
    "|______________|"
]

#Main function
def main():
    for row in menu:
        print(row+"\n")

    choose_log_in_sign_up=int(input("Write number on function - "))

    if(choose_log_in_sign_up==1):
        log_in()
    if(choose_log_in_sign_up==2):
        sign_up()

    for row in menu1:
        print(row+"\n")

    choose_functions=int(input("Write number on function - "))

    while(choose_functions!=1 and choose_functions!=2 and choose_functions!=3 and choose_functions!=4 and choose_functions!=5):
        choose_functions=int(input("Write number on function - "))
        os.system("cls")

    if(choose_functions==1):
        os.system("cls")
        profiles()
        time.sleep(5)
        os.system("cls")
        main()
    if(choose_functions==2):
        os.system("cls")
        data()
        time.sleep(5)
        os.system("cls")
        main()
    if(choose_functions==3):
        os.system("cls")
        delete()
        time.sleep(2)
        os.system("cls")
        main()
    if(choose_functions==4):
        os.system("cls")
        open_web_page()
    if(choose_functions==5):
        exit()
    
def open_web_page():
   uniform_resource_locator=str(f'{dir}\website\pages\LoginForm.html')
   print(uniform_resource_locator)
   webbrowser.open_new_tab(uniform_resource_locator)

#Sign up
def sign_up():
    file_path = f"{dir}\website\python\{name}.json"
    if(os.path.exists(file_path)):
        f=open(f"{dir}\website\python\{name}.json", "r")
        row_e_mail=f.readlines()
        row_e_mail=row_e_mail[2]

        if(row_e_mail.find(e_mail)):
            print("You have acount.")

        else:
            f=open(f"{dir}\website\python\{name}.json", "a")
            f.write("{"+"\n"+'  "person": ['+"\n"+"     {"+"\n"+f'      "e-mail": "{e_mail}",'+"\n"+f'      "password": "{password}",'+"\n"+f'      "phone_number": "089{phone_number}",'+"\n"+f'      "money": "{bin(money)}"'+"\n"+"     }"+"\n"+"  ]"+"\n"+"}"+"\n")
            f.close()

            f=open(f"{dir}\website\python\{name}", "r")
            rows=f.readlines()
            row_3="        },\n"
            f.close()
            rows[-3]=row_3
            rows.remove("    ]")
            rows.remove("}")

            file_path = f"{dir}\website\python\Data.json"
            if(os.path.exists(file_path)):
                os.remove(file_path)
            else:
                print("Errro data.")

            f=open(f"{dir}\website\python\Data.json", "w")
            for i in rows:
                f.write(i)
            
            print(f"1-{rows}")

            f=open(f"{dir}\website\python\Data.json", "a")
            f.write("        {"+"\n"+f'            "name": "{name}",'+"\n"+f'            "e-mail": "{e_mail}",'+"\n"+f'            "password": "{password}",'+"\n"+f'            "phone_number": "089{phone_number}",'+"\n"+f'            "money": "{bin(money)}"'+"\n"+"        }"+"\n")
            f.close()

            f=open(f"{dir}\website\python\Data.json", "a")
            f.write("    ]"+"\n"+"}")
            f.close()
    else:
        f=open(f"{dir}\website\python\{name}.json", "a")
        f.write("{"+"\n"+'  "person": ['+"\n"+"     {"+"\n"+f'      "e-mail": "{e_mail}",'+"\n"+f'      "password": "{password}",'+"\n"+f'      "phone_number": "089{phone_number}",'+"\n"+f'      "money": "{bin(money)}"'+"\n"+"     }"+"\n"+"  ]"+"\n"+"}"+"\n")
        f.close()

        f=open(f"{dir}\website\python\Data.json", "r")
        rows=f.readlines()
        row_3="        },\n"
        f.close()
        rows[-3]=row_3
        rows[-1]="        "
        rows[-2]="        {"

        file_path = f"{dir}\website\python\Data.json"

        if(os.path.exists(file_path)):
            os.remove(file_path)

        else:
            print("Errro data.")

        f=open(f"{dir}\website\python\Data.json", "w")

        for i in rows:
            f.write(i)

        f.close()
        

        f=open(f"{dir}\website\python\Data.json", "a")
        f.write("\n"+f'            "name": "{name}",'+"\n"+f'            "e-mail": "{e_mail}",'+"\n"+f'            "password": "{password}",'+"\n"+f'            "phone_number": "089{phone_number}",'+"\n"+f'            "money": "{bin(money)}"'+"\n"+"        }"+"\n")
        f.close()

        f=open(f"{dir}\website\python\Data.json", "a")
        f.write("    ]"+"\n"+"}")
        f.close()

#Log in
def log_in():
    file_path = f"{dir}\website\python\{name}.json.json"
    file_path1 = f"{dir}\website\python\{e_mail}.json"

    if(os.path.exists(file_path) or os.path.exists(file_path1)):
        f=open(f"{dir}\website\python\{name}.json", "r")
        row_e_mail=f.readlines()
        row_e_mail=row_e_mail[2]

        if(row_e_mail.find(e_mail)):
            print("You have acount.")

        else:
            sign_up()

    else:
        print("Errro data.")

#Delete profile
def delete():
    file_path = f"{dir}\website\python\{name}.json"
    file_path1 = f"{dir}\website\python\{e_mail}.json"

    if(os.path.exists(file_path)):
        os.remove(file_path)

    elif(os.path.exists(file_path1)):
        os.remove(file_path1)

    else:
        print("Error data.")

#Prints all profiles
def profiles():
    directory_path = f"{dir}\website\python"
    all_files = os.listdir(directory_path)
    list_json_files = []

    for json_file in all_files:
        if(json_file.endswith("json")):
            list_json_files.append(json_file)

    print("\nProfiles\n")

    for json_files in list_json_files:
        len_json_files=len(json_files)
        print(f"-{json_files[0:len_json_files-5]}")


#Prints all profile information
def data():
    file_path = f"{dir}\website\python\{name}.json"
    file_path1 = f"{dir}\website\python\{e_mail}.json"

    if(os.path.exists(file_path) or os.path.exists(file_path1)):
        f=open(f"{dir}\website\python\{name}.json", "r")
        row_e_mail=f.readlines()
        row_e_mail=row_e_mail[2]

        if(row_e_mail.find(e_mail)):
            with open(f'{dir}\website\python\{name}.json') as f:
                data=json.load(f)

            for person in data['person']:
                time.sleep(2)
                print(person)

        else:
            print("You don't have acount.")

    else:
        print("Error data.")

print("Dir-"+dir+"\website\pages")
main()