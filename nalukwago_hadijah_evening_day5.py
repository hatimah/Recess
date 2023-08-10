from sys import argv
class PercentageError(Exception):
    pass
        
# Exception class for percentage > 100
class InvalidPercentageError(PercentageError):
    def __init__(self):
        super().__init__("Percentage is invalid")
        
# Exception class for percentage < 80
class LessPercentageError(PercentageError):
    def __init__(self):
        super().__init__("The Percentage is lesser than the Cut-off, Please try again!")

# class to check percentage range
class checkPercentage(PercentageError):
    def __init__(self, per):
        if per<80:
            raise LessPercentageError
        if per>100:
            raise InvalidPercentageError
        print("Congrats you're Enrolled")
        
# different cases and output
try:
    print("For Percenatge: 93")
    checkPercentage(93)
except Exception as e:
    print(e)
    
try:
    print("\nFor Percenatge: 102")
    checkPercentage(102)
except Exception as e:
    print(e)
    
try:
    print("\nFor Percenatge: 58")
    checkPercentage(58)
except Exception as e:
    print(e)
    
   # file handling 
# Open the file in write mode and write some data
with open("example.txt", "w") as file:
    file.write("Hello, yall this is me doing python yay!\n")
    file.write("This is an example of file handling in Python.")

# Open the file in append mode and add more data
with open("example.txt", "a") as file:
    file.write("\nAppending more or increased  data.")

# Open the file again in read mode and read the updated contents
with open("example.txt", "r") as file:
    added = file.read()
    #thhis line is printed here at the beginning of the file
    print("\n Hello this is me hadijah:")
    print(added)