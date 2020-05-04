"""
Module for connecting to MySQL using pymysql module
 to the World database

Applied Databases project Q 4.4
Angela Carpenter

Note: Please note that the password needs to be set password in the passwd field at the top of the script 
before running the program if your password different to "root".

"""
# please enter password here if different to root
passwd = "root"

import pymysql

# create global variable for connections, assign default value for now
conn = None

# create a global variable for the country data, assign a default value at the start
country_data = None

# define connection function

def connect():
    # use global variable, can be used by all read and write functions and modules here
    global conn

    while True:
        # connect to database
        try:
            conn = pymysql.connect(host="localhost", user="root", password = passwd,db="world", cursorclass=pymysql.cursors.DictCursor)
            #print(conn)
            # once connected can break out of this function
            break
        except Exception as e:
            print("Sorry - there is a problem connecting to the database...", e)

##############################################
## define function for OPTION 1

def viewPeople():

    if not conn:
        connect()

    # conn= pymysql.connect(host="localhost", user="root", password =passwd,db="world", cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from person"

    with conn:
        try:
            cursor = conn.cursor()
            #print("Connected to database")
            cursor.execute(sql,)

            while True:
                # this returns the next 2 sets of rows of a query result
                result = cursor.fetchmany(2)
                # it will return an empty list if no other rows are available
                if not result:
                    #print("There are no more people in the Database.")
                    break
                for person in result:
                                        
                    print(person["personname"],":",person["age"])
                # takes user input
                quit = input("quit<q>")
                # if user presses any other key except 'q' the next two people in the database are shown
                if quit == "q":
                    # whenever user presses q, the user is brought back to the main menu
                    break  

        # print any exception errors
        except pymysql.IntegrityError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)      

        except Exception as e:
            print("Error - please try again", e)

################################################################
# define function for OPTION 2
# 2 View countries by independence year - this is from the country table
# function takes a year as the input - as entered by user in menu option 2  
def viewCountriesByIndependenceYear(year):

    if not conn:
        connect()
    
    sql = """
        select Name, IndepYear, Continent, Population
        from country
        where IndepYear = %s
        """

    with conn:
        try:

            cursor = conn.cursor()
            # execute sql query taking the year input by the user
            cursor.execute(sql,year)
            #fetch all the rows of the query result
            return cursor.fetchall()
        # error exception handling
        except pymysql.IntegrityError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)      
        
        except Exception as e:
            print("Error - please try again.", e)
        

################################################################
# define function for OPTION 3
# function takes a name and age as entered by the user in menu option 3
def addNewPerson(name, age):
    if not conn:
        connect()
  
    sql = """
    INSERT INTO person
    (personname, age) 
    VALUES (%s, %s)
    """

    with conn:
        try:
            # create a cursor object with which to execute the sql queries
            cursor = conn.cursor()
            # execute the sql query using the name and age input by the user
            cursor.execute(sql,(name,age))
            conn.commit()
            print("Insert Successful")
        except pymysql.IntegrityError as e:
            # if the user has entered a name that already exists, do not add to the database and print error message
            print("*** ERROR ***:",name, " already exists")
        # any other exceptions
        except Exception as e:
            print("Error - please try again.", e)

################################################################
# option 4 and option 5

# a general function to return all the countries so it can be used again

def getCountryData():

    global country_data    

    # for testing - remove
    #if not country_data:
    #    print("Country data has not been fetched yet, Getting country data from database...")
    #else:
    #    print("country data previously retrieved - getting from store...")

    if not conn:
            connect()

    sql = "select * from country"


# select all the data from the country table     
    with conn:
        try:

            cursor = conn.cursor()
            cursor.execute(sql,)
            country_data = cursor.fetchall()
            return country_data

        except pymysql.IntegrityError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)      

        except Exception as e:
            print("other error", e)
##########################



    

########################################################
# call the main program
if __name__ == "__main__":
    main()
    connect()
    viewPeople()
    viewCountriesByIndependenceYear()
    addNewPerson(name, age)
    getCountryData()
    viewCountriesByName()


