
import sqlite3
# File handling using context manger 
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()
 
with File ('file.txt', 'w') as file:
    file.write("quraan is beautiful")
print(file.closed)

print("\n====database connection")
 
class DBConnectionManager():
    def __init__(self, hostname):
        self.hostname = hostname
        self.connection = None
 
    def __enter__(self):
        self.connection = sqlite3.connect(self.hostname)
        return self.connection
 
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
        
with DBConnectionManager('localhost') as hade:
    cursor = hade.cursor()
    cursor.execute("CREATE TABLE CUSTOMERS(name VARCHAR(255), age INTEGER)")

#multithreading
import threading
 
 
def print_add(num):
    # function to print cube of given num
    print("ADD {}" .format(num + num + num))
 
 
def print_subtract(num):
    # function to print square of given num
    print("SUBTRACT: {}" .format(num - num))
 
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_subtract, args=(10,))
    t2 = threading.Thread(target=print_add, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("these are threads in python")
     
