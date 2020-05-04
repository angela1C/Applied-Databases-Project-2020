"""
MENU FOR THE PYTHON APPLICATION 
Applied Databases project Q 4.4
Angela Carpenter

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

# write a menu to show the display options



        

############## OPTION 1 View People #############
        # if user enters 1
        if (choice =="1"):
            # call the viewPeople() function in mysql_connect module
            mysql_connect.viewPeople()
            # call display menu function
            displayMenu()
        

############# END OPTION 1 ###########

############# BEGIN OPTION 2 View Countries by Independence Year #########
        # if user enters 2
        
        elif (choice=="2"):
            print("Countries by Independence Year")
            # ask user to enter a valid year
            while True:
                # if the user does not enter a valid integer, return a value error until an integer is entered
                try:
                    year = int(input("Enter Year: "))
                    break
                except ValueError:
                    print("Invalid year entered. Please enter a valid number for the year")
            countries = mysql_connect.viewCountriesByIndependenceYear(year)
            for country in countries:
                    #print country
                print(country["Name"],":",country["Continent"],":",country["IndepYear"])
            # return to menu  
            displayMenu()

        
############# END OPTION 2 ###########

############# BEGIN OPTION 3 Add New Person  
        # if user enters 3
        elif (choice =="3"):
            # ask user to enter a Name
            name = input("Name: ")
            # ask user to enter an age
            age = input("Age: ")
            # call the addNewPerson function in the mysql_connect module
            results = mysql_connect.addNewPerson(name, age)
            # return to menu
            displayMenu()

            
############# BEGIN OPTION 4 View Countries by Name

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
            # return to menu
            displayMenu()
            
############# END OPTION 4 ###########


############# BEGIN OPTION 5 View Countries by Population

        elif (choice =="5"):
            # ask user to enter one of the following comparator operators
            cmp = input("Enter < > or = : ")
            # if user does not enter one of these, repeatedly asked until a valid choice is entered.
            while cmp not in("<",">",'='):
                cmp = input("Enter < > or = : ")
                if cmp in("<",">",'='):
                    break
                # ask the user to enter a population value, ensure the user enters a number
            while True: 
                try:  
                    pop = int(input("Enter population :"))
                    break
                except ValueError:
                    print("Invalid population value, please enter a valid number...")
                    
                except Exception as e:
                    print(e)

            # call the getCountryData function in mysql_connect module
            countries = mysql_connect.getCountryData()
                
            print("Countries by Pop \n ----------------")
            for country in countries:
                # print country details corresponding to comparator operator used and the population value
                # 
                if cmp ==">":
                    if int(country["Population"]) > int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="=":
                    if int(country["Population"]) == int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])
                elif cmp =="<":
                    if int(country["Population"]) < int(pop):
                        print(country["Code"]," : ", country["Name"]," : ", country["Continent"]," : ",country["Population"])


            # return to main menu
            displayMenu()

############# END OPTION 5 ###########

############# BEGIN OPTION 6 Find Students by Address
        # call the findStudents function in mongo_connect module
        elif (choice=="6"): 
            print("Find Students by Address")
            # ask user to enter address, The question does not ask for partial match
            address = str(input("Enter Address: "))
            # pass the address into the findStudents function
            students = mongo_connect.findStudents(address)
            # print out results returned
            for student in students:
                #print(student)
                print(student["_id"]," : ", student["details"]["name"]," : ",student["details"]["age"]," : ",student["qualifications"])
            # return to menu
            displayMenu()
   
   ############# END OPTION 6 ###########


    ##############   # BEGIN OPTION 7 Add New Course
 
    # The user is asked to enter an _id, Name and Level for a new course, which is then added to the
    # docs collection in the proj20DB database:

        elif (choice=="7"):
            print("Add New Course : ")
            # The user is asked for _id, Name and Level one at a time
            ID = str(input("_id: "))
            Name = str(input("Name :"))
            Level = str(input("Level :"))

            # call the function AddNewCourse in the mongo_connect module
            added = mongo_connect.addNewCourse(ID,Name,Level)
            # back to menu
            displayMenu()




############ END OPTION 7 ###########

############ option to exit the program is 'x' ###########
        elif (choice == "x"):
            # exit clause to break out out of the entire program and back to the command prompt
            print("Goodbye")
            break

    ## for anything else, display the menu
        else: 
            
            displayMenu()

        
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


    
if __name__ == "__main__":
    # only execute if run as a script
    main()
    