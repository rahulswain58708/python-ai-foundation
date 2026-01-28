#Contacts Manager App
print("---------------Welcome To Contacts Manager App---------------")
#Show Menu
print("1.Create Contact")
print("2.View All Contacts")
print("3.Update Contact")
print("4.Search Contact")
print("5.Delete Contact")
print("6.Exit")
contacts = {}
while True:
    option = input("Enter One Option:-")
    #Create Contact
    if option == "1":
        print("-------------Create An Contact-----------")
        user_name = input("Enter UserName:-")
        ph = int(input("Enter Phone Number:-"))
        if user_name in contacts:
            print("Contact already exists")
        else:
            contacts[user_name] = ph
            print("Contact saved")
    #view all contacts
    elif option == "2":
        print("-------Contacts-------")
        if not contacts:
            print("No Contacts Available")
        else:
            for name,num in contacts.items():
                print(f"Name:{name}|phone:{num}")
    #Update Contact
    elif option == "3":
        print("-------Update Contact-------")
        update_name = input("Enter Update UserName:-")
        if update_name in contacts:
            pho = int(input("Enter Phone Number:-"))
            contacts[update_name] = pho
            print("Update successful")
        else:
            print("UserName Not Exist❌")
    #search Contact
    elif option == "4":
        print("-------Search Contact--------")
        search_name = input("Enter UserName:-")
        if search_name in contacts:
             print(f"Phone:{contacts[search_name]}")
        else:
            print("Search Name Not Exist....")
    #Delete Contact
    elif option == "5":
        print("-------Delete Contact-------")
        del_name = input("Enter UserName:")
        if del_name not in contacts:
            print("Enter Correct UserName Want delete contact")
        else:
            del contacts[del_name]
            print("Delete Successful")
    elif option == "6":
        print("Exit............🤗")
        break
    else:
        print("Please Enter Valid Option❌")
