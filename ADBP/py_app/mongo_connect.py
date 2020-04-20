"""

Module for connecting to mongo db
 - tidy up
 - remove connection messages etc

"""

import pymongo

# create the connection to MongoDB and store in a variable, myclient

myclient = None

# make it a global variable so it can be used in different methods or functions
# give the global variable a default value of None



def connect():

    global myclient
    print("In connect() function")
    # just to see the connection variable before and after the connection
    print("1:", myclient)

    myclient = pymongo.MongoClient()
    print("2:", myclient)
    myclient.admin.command('ismaster')




def findStudents(address):

    if not myclient:
        connect()
    # specify the database
    mydb = myclient["proj20DB"]
    # specify the collection in the database
    docs = mydb["docs"]
    pipeline = [{"$match": {"details.address":{"$eq":address}}},{"$project":{"details.name":1,"details.age":1,"qualifications":{ "$ifNull":["$qualifications"," "]}}},{"$sort":{"details.name": 1}}]
    students = docs.aggregate(pipeline)
    return students
# This returns what I want in Mongo DB itself
# db.docs.aggregate([{$match: {"details.address":{$eq:"Dublin"}}},{$project:{"details.name":1,_id:0,qualifications:{ $ifNull:["$qualifications","None"]}}},{$sort:{"details.name": 1}}])
# { "details" : { "name" : "Brian Collins" }, "qualifications" : [ "ENG", "SW" ] }
# { "details" : { "name" : "Tom Kenna" }, "qualifications" : "None" }


def addNewCourse(ID,Name,Level):
#def addNewCourse():
    if not myclient:
        connect()

    # specify the database
    mydb = myclient["proj20DB"]
    # specify the collection in the database
    docs = mydb["docs"]

    newDoc = {"_id":ID, "Name":Name, "Level":Level} 

    # catch the insert error here 
    try:
        docs.insert_one(newDoc)
    except pymongo.errors.DuplicateKeyError as e:
        print("*** ERROR ***: _id ",ID,"already exists")
   
    
  
def findCourse():

    if not myclient:
        connect()
    # specify the database
    mydb = myclient["proj20DB"]
    # specify the collection in the database
    docs = mydb["docs"]
    query={}
    courses = docs.find(query)
    return courses

# define the main method here
def main():
    print("here")
    if (not myclient):
        try:
            connect()
        except Exception as e:
            print("Error - could not connect.", e)

        
        find2()

        



# tell the python program how to start
if __name__ == "__main__":
    main()