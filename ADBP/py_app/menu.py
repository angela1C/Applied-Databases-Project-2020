"""
MENU FOR THE PYTHON APPLICATION

- fix option 2 so that when there are no more people, it will not return 'q'. Using an if not to get out.
- make the country names case insensitive so it looks up lower case and upper case. Using str.casefold for caseless matching
- add the try and exception errors.
- remove all connection messages - just there for testing
- don't want to print the memory location
- password!
"""

import mysql_connect
import mongo_connect

# main program
def main():
    # call the function to display the menu
    displayMenu()
    # calls the menu
    while True:
        #displayMenu()
        
        choice = input("Choice:")



############## OPTION 1 #############
        if (choice =="1"):
            mysql_connect.viewPeople()
            displayMenu()
        

############# END OPTION 1 ###########

############# BEGIN OPTION 2 #########

        elif (choice=="2"):
            print("Countries by Independence Year")
            year = input("Enter Year: ")
            print("Looking for matches for year",year)
            ## call the function in the q44db module
            countries = mysql_connect.viewCountriesByIndependenceYear(year)
            for country in countries:
                #print country
                print(country["Name"],":",country["Continent"],":",country["IndepYear"])
            
            displayMenu()

        
############# END OPTION 2 ###########

############# BEGIN OPTION 3 ###########

        elif (choice =="3"):
            name = input("Name: ")
            age = input("Age: ")

            results = mysql_connect.addNewPerson(name, age)
        
            displayMenu()

            
############# BEGIN OPTION 4 ###########

#### must make this case insensitive!

        elif (choice == "4"):
            # ask user for input, convert to a string
            country_name = str(input("Enter Country Name: "))
            # get the country data
            countries = mysql_connect.getCountryData()
             # loop through all the countries returned 
            for country in countries:
            # check if the string entered is in the country name, this will pick up partial matches also
            # using string fold for caseless matching
                if str.casefold(country_name) in str.casefold(country["Name"]):
                    print(country["Name"],":",country["Continent"],":",country["Population"],":",country["HeadOfState"])

            displayMenu()
            
############# BEGIN OPTION 4 ###########


############# BEGIN OPTION 5 ###########

        elif (choice =="5"):
            cmp = input("Enter < > or = : ")
            # if user does not enter one of these, repeatedly asked until a valid choice is entered.
            while cmp not in("<",">",'='):
                cmp = input("Enter < > or = : ")
                if cmp in("<",">",'='):
                    break
            while True: 
                try:  
                    pop = int(input("Enter population :"))
                    break
                except ValueError:
                    print("Invalid population value, please enter a valid number...")
                    
                except Exception as e:
                    print(e)
            
                    


            
            countries = mysql_connect.getCountryData()
                
            print("Countries by Pop \n ----------------")
            for country in countries:
                # print country details
                
                if cmp ==">":
                    if int(country["Population"]) > int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="=":
                    if int(country["Population"]) > int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="<":
                    if int(country["Population"]) < int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])


            # back to main program
            displayMenu()


        elif (choice=="6"): 
            print("Find Students by Address")
            address = str(input("Enter Address: "))
            # pass the address into the function
            students = mongo_connect.findStudents(address)
            
            for student in students:
                #print(student)
                print(student["_id"]," : ", student["details"]["name"]," : ",student["details"]["age"]," : ",student["qualifications"])
            
            displayMenu()
   


    ########################################################## option 7
    # BEGIN OPTION 7

    # The user is asked to enter an _id, Name and Level for a new course, which is then added to the
    # docs collection in the proj20DB database:

        elif (choice=="7"):
            print("Add New Course : ")
            ID = str(input("_id: "))
            Name = str(input("Name :"))
            Level = str(input("Level :"))

            added = mongo_connect.addNewCourse(ID,Name,Level)
            # Just checking for now that course has been updated
            courses = mongo_connect.findCourse()
            for course in courses:
                print(course)
            
            
            # back to main program
            displayMenu()

    ##  using this for testing
        elif (choice =="t"):
            print("Just for testing")

            # back to main program

        elif (choice == "x"):
            # exit clause to break out out of the entire program and back to the command prompt
            print("Goodbye")
            break






    ## for anything else, display the menu
        else: 
            
            displayMenu()





        
# write a menu to show the display options
def displayMenu():
    print("")
    print("World DB")
    print("--------")
    print("")
    print("MENU")
    print("====")
    print("1 - View People")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by population")
    print("6 - Find Students by Address")
    print("7 - Add New Course")
    print("x - Exit application")
    print("t  - testing a function")



        
    
if __name__ == "__main__":
    main()
    