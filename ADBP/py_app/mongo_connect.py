"""

Module for connecting to MongoDB to the proj20DB database
Applied Databases project Q 4.4
Angela Carpenter

"""
# import pymongo module
import pymongo

# create the connection to MongoDB and store in a variable, myclient

myclient = None

# make it a global variable so it can be used in different methods or functions
# give the global variable a default value of None


# define the function for connecting to the mongo database
def connect():

    global myclient
    myclient = pymongo.MongoClient()
    myclient.admin.command('ismaster')

##############################################
## define function for OPTION 6 Find Students by Address

# define function that takes an address
def findStudents(address):

    if not myclient:
        connect()
    # specify the database
    mydb = myclient["proj20DB"]
    # specify the collection in the database
    docs = mydb["docs"]
    # specify the pipeline
    pipeline = [{"$match": {"details.address":{"$eq":address}}},{"$project":{"details.name":1,"details.age":1,"qualifications":{ "$ifNull":["$qualifications"," "]}}},{"$sort":{"details.name": 1}}]
    students = docs.aggregate(pipeline)
    # return the results to the function which called this
    return students

##############################################
## define function for OPTION 7 Add New Course

def addNewCourse(ID,Name,Level):
#def addNewCourse():
    if not myclient:
        connect()

    # specify the database
    mydb = myclient["proj20DB"]
    # specify the collection in the database
    docs = mydb["docs"]
    # using the users input to update the database
    newDoc = {"_id":ID, "Name":Name, "Level":Level} 

    # catch the insert error here if the user enters an existing _id value
    try:
        docs.insert_one(newDoc)
        print("Course added to database.")
    except pymongo.errors.DuplicateKeyError as e:
        print("*** ERROR ***: _id ",ID,"already exists")
   
############   



# define the main method here
def main():
    if (not myclient):
        try:
            connect()
        except Exception as e:
            print("Error - could not connect.", e)


# tell the python program how to start
if __name__ == "__main__":
    findStudents(address)
    addNewCourse(ID,Name,Level)