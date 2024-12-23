# I wasn't sure how to create just a .py file in jupyter so I used this to create one

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userId, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        USER = userId
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31802
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            #inserts the new document
            result = self.database.animals.insert_one(data)  # data should be dictionary 
            return result.acknowledged #returns True if document created
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            #uses for loop to iterate over returned cursor looking for the right docuement
            
            animals = self.collection.find(data)
            
            return [i for i in animals]
            
            
        else:
            raise Exception("Nothing to find, because data parameter is empty")
    
    #update method for U in CRUD
    def update(self, search_data, update_data, update_many=False):
        if search_data is not None:
            #If search_data not empty then the function will search and update
            # the database
            
            #The last parameter which is has a defualt value of False
            #determines if the function uses update_one or update_many
            if update_many == False:
                result = self.collection.update_one(search_data, {"$set":update_data})
            else:
                result = self.collection.update_many(search_data, {"$set":update_data})
            
        
            #The number of update documents is returned.
            return result.matched_count
            
        else:
            raise Exception("Nothing to update, becuase update data is empty")
            
            
    #Delete method for D in CRUD
    def delete(self, data):
        if data is not None:
            #if data is not empty then the method sends delete_one command, and the 
            #fist document to match gets deleted.
            
            result = self.collection.delete_one(data)
            return result.deleted_count
            
        else:
            raise Exception("Nothing to update, becuase delete data is empty")
            
            
            
