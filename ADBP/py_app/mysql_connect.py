"""
Rough work for functions - all working for now. Just saving work so far
option 4 - view countries by name should work with lower and uppercase so fix this

set password before running.

"""
passwd = "add password here"

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
            print(conn)
            # once connected can break out of this function
            break
        except Exception as e:
            print("problem connecting ", e)

##############################################
## OPTION 1

def viewPeople():

    if not conn:
        connect()

    # conn= pymysql.connect(host="localhost", user="root", password =passwd,db="world", cursorclass=pymysql.cursors.DictCursor)
    sql = "select * from person"

    with conn:
        try:
            cursor = conn.cursor()
            print("Connected to database")
            cursor.execute(sql,)

            while True:
                result = cursor.fetchmany(2)
                # not sure if I should have this part in the menu program or not. it is working this way
                # # trying to stop it printing where no more persons
                if not result:
                    print("No more people in the Database.")
                    break
                
                for person in result:
                    
                    
                    print(person["personname"],":",person["age"])

                quit = input("quit<q>")
                # need to stop printing when there are no more people
                
                

                if quit == "q":
                    break  


        except pymysql.IntegrityError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)      

        except Exception as e:
            print("other error", e)

################################################################
# OPTION 2
# 2 View countries by independence year - this is from the country table
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
            cursor.execute(sql,year)
            return cursor.fetchall()

        except pymysql.IntegrityError as e:
            print(e)
        except pymysql.InternalError as e:
            print(e)      

        except Exception as e:
            print("other error", e)

################################################################
# OPTION 3

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
            cursor = conn.cursor()
            cursor.execute(sql,(name,age))
            conn.commit()
            print("Insert Successful")
        except pymysql.IntegrityError as e:
            print("*** ERROR ***:",name, " already exists")


################################################################
# option 4 and option 5

# a general function to return all the countries so it can be used again

def getCountryData():

    global country_data    

    if not country_data:
        print("Country data has not been fetched yet, Getting country data from database...")
    else:
        print("country data previously retrieved - getting from store...")

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


