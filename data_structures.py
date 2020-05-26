from pymongo import *

class file:
    def __init__(self):
        self.file = None
        self.filename = None
        self.valid = 0
    def getFileName(self, message):
        self.filename = input(message)
        return
    def openFile(self, message, mode):
        try:
            self.getFileName(message)
            if(self.filename == ""):
                self.filename = None
                return
            self.file = open(self.filename, mode)
        except:
            print('File Not Found Error. Re-enter File Name.')
            self.openFile(message, mode)
        finally:
            if(self.filename != None):
                self.valid = 1
            return
    def addToFile(self, data):
        self.file.write(data)
        return
    def closeFile(self):
        self.file.close()
        self.valid = 0
        return


class db_class:
    def __init__(self):
        self.client = None
        self.db_instance = None
        self.col_instance = None
        self.conn_url = None
        self.db_name = None
        self.collection_name = None
        self.valid = 0
        self.doc_count = 0
    def getConnURL(self, message):
        self.conn_url = input(message)
        return
    def getDBName(self, message):
        self.db_name = input(message)
        return
    def getCollectionName(self, message):
        self.collection_name = input(message)
        return
    def openDBInstance(self, message_url, message_db, message_col):
        try:
            self.getConnURL(message_url)
            if(self.conn_url == ""):
                self.conn_url = None
                return
            self.getDBName(message_db)
            self.getCollectionName(message_col)
            self.client = MongoClient(self.conn_url)
            self.client.admin.command("ismaster")
            self.db_instance = self.client[self.db_name]
            if self.collection_name in self.db_instance.list_collection_names():
                self.db_instance[self.collection_name].drop()
            self.col_instance = self.db_instance[self.collection_name]
        except:
            print('Connection Error. Re-enter Details.')
            self.openDBInstance(message_url, message_db, message_col)
        finally:
            if(self.conn_url != None):
                self.valid = 1
            return
    def dBInsertOne(self, data_dict):
        self.col_instance.insert_one(data_dict)
        return
    def dBInsertMultiple(self, data_dict_list):
        self.col_instance.insert_many(data_dict_list)
        return
    def dBDeleteCollection(self):
        self.col_instance.drop()
        self.valid = 0
        return
    def dBDeleteDatabase(self):
        self.client.drop_database(self.db_name)
        self.valid = 0
        return
    def dBDisplayCollection(self):
        for i in self.col_instance.find():
            print(i)
        return
    def closeClient(self):
        self.client.close()
        self.valid = 0
        return
