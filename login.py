user_id='volly@admin'
passw='admin@123'
Choice='Y'
t_id='tvolly@admin'
passwt='tadmin@123'

a= input("Login as Teacher or User ")
if a=='teacher'or a=='Teacher':
    while (Choice=='Y'):
        login=input("Please enter Teacher ID: ")
        password=input("Please enter password: ")

        if login != t_id or password !=passwt:
            print("Wrong Teacher ID or Password! ")
            Choice=input("Do you want to try again? Y/N : ")

        if Choice== 'N':
            print("Bye!")

        elif login==t_id and password==passwt:
            print("Login successful!")
            break

else:
    while (Choice=='Y'):
        login=input("Please enter User ID: ")
        password=input("Please enter password: ")

        if login != user_id or password !=passw:
            print("Wrong User ID or Password! ")
            Choice=input("Do you want to try again? Y/N : ")

        if Choice== 'N':
            print("Bye!")

        elif login==user_id and password==passw:
            print("Login successful!")
            break
    
    
        


        
