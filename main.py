from data_structures import *
from validate import *
from process_sequence import *
import sys

def main():
    file_read = file()
    file_write = file()
    database = db_class()

    print("Press Enter to Skip Input")
    file_read.openFile("File to read: ", 'r')
    file_write.openFile("File to write: ", 'w')
    database.openDBInstance("URL: ", "Database Name: ", "Collection Name: ")
    
    while(True):
        print('0 - Exit')
        print('1 - Input File Settings')
        print('2 - Output File Settings')
        print('3 - Database Settings')
        print('4 - Process Next Sequence')
        response = getInt()

        if(response == 0):
            if(file_read.valid == 1):
                file_read.closeFile()
            if(file_write.valid == 1):
                file_write.closeFile()
            if(database.valid == 1):
                database.closeClient()
            sys.exit()  
        elif(response == 1):
            print('1 - Close File')
            print('2 - Open File')
            print('Else - Back')
            response = getInt()
            if(response == 1):
                if(file_read.valid == 1):
                    file_read.closeFile()
            elif(response == 2):
                if(file_read.valid == 1):
                    file_read.closeFile()
                file_read.openFile("File to read: ",'r')
            else:
                pass
        elif(response == 2):
            print('1 - Close File')
            print('2 - Open File')
            print('Else - Back')
            response = getInt()
            if(response == 1):
                if(file_write.valid == 1):
                    file_write.closeFile()
            elif(response == 2):
                if(file_write.valid == 1):
                    file_write.closeFile()
                file_write.openFile("File to write: ", 'w')
            else:
                pass
        elif(response == 3):
            print('1 - Close Database')
            print('2 - Open Database')
            print('3 - Delete Database')
            print('4 - Delete Collection')
            print('Else - Back')
            response = getInt()
            if(response == 1):
                if(database.valid == 1):
                    database.closeClient()
            elif(response == 2):
                if(database.valid == 1):
                    database.closeClient()
                database.openDBInstance("URL: ","Database Name: ","Collection Name: ")
            elif(response == 3):
                if(database.valid == 1):
                    database.dBDeleteDatabase()
            elif(response == 4):
                if(database.valid == 1):
                    database.dBDeleteCollection()
            else:
                pass
        elif(response == 4):
            processNextSequence(file_read, file_write, database)
        else:
            print('Please Enter Nos. between 0-4')

    return

if __name__ == "__main__":
    main()
