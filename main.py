#STUDENT-GRADE

#list of names
import random

contacts = ["Dad", "Mom", "Crazy Neighbhor", "Siwon Mun", "Grandma", "Grandpa", "Auntie Susan", "Uncle Bo", "My Day 1", "Dwayne Johnson", "Vijay Aggarwal"]

#LOOP 
loop = True
while loop: 

  #CONTACT LIST 
    
    dadinfo = ("780-255-6934")
    
    #PRINT MENU
    print("MAIN MENU")

    print("1. Display Contact Names")
    print("2. Search for Contact")
    print("3. Edit Contact")
    print("4. New Contact")
    print("5. Remove Contact")
    print("6. Exit")

    #Selection From User
    select = input ("Enter Selection (1-6): ")

    #First Selection 
    if select == "1":
        print("DISPLAY ALL CONTACTS")
        print("ALL CONTACTS")
        for contactid in contacts:
          print(contactid)


    #Second Selection
    elif select == "2":
        print("SEARCH FOR CONTACT")
        searchcontact = input("WHICH CONTACT WOULD YOU LIKE TO SEARCH FOR? ") 
        for x in contacts:
          if x == searchcontact:
            print("CONTACT FOUND: ", x)
          else: 
            if x not in contacts:
              print("CONTACT NOT FOUND")  
      
          
    #Third Selection    
    elif select == "3":

        #FIND CONTACT
        searchcontact = input("WHICH CONTACT WOULD YOU LIKE TO CONTACT? ") 
        for x in contacts:
          if x == searchcontact:
            print("CONTACT FOUND: ", x)
          else: 
            if x not in contacts:
              print("CONTACT NOT FOUND")  

            #EDIT CONTACT
            editcontact = input("EDIT CONTACT: ")
            contacts = (dadinfo)
            print("Current name is", contacts)


    #Fourth Selection
    elif select == "4":
      print("ADD A CONTACT")
      chosencontact = input("ENTER A CONTACT TO ADD: ")
      if chosencontact in contacts:
        print("CONTACT ALREADY EXISTS")
      else: 
        print(chosencontact, "HAS BEEN ADDED TO CONTACT LIST")
        contacts.append(chosencontact)

    #Fifth Selection
    elif select == "5":
        print("DELETE CONTACT: ")
        chosencontact = input("WHICH CONTACT WOULD YOU LIKE TO DELETE?: ")
        if chosencontact not in contacts:
          print("CONTACT DOES NOT EXIST")
        else:
          contacts.remove(chosencontact)
          print("CONTACT HAS BEEN SUCCESFULLY DELETED")

    #Fifth Selection
    elif select == "6":
        print ("EXIT")
        loop = False