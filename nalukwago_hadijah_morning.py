#control flow 
#An "if statement" is written by using the if keyword.
#if condition1:
    # code block executed if condition1 is true
#elif condition2:
    # code block executed if condition2 is true and condition1 is false
#else:
    # code block executed if both condition1 and condition2 are false
"""if statements:
     print('male')
elif conditions2:
    print('female')
    else
    """
age= 20
if (age<18):
    print("you are underage")
elif (age>=18 and age<=65):
    print("you are   an adult")
else:
    print("you are a senior citizen")     
     #while loops
    #break and continue statements
    # Break jumps out of a loop when a condition is reached 
    
#Loops( while and for) 
#The while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# It keeps executing the code block until the condition becomes false.
hady = 10
while hady > 0:
    print(hady)
    if hady==4:
        break
    hady-=1 
    if hady ==6:
        continue
    hady-=1

    #for loop example  with a continue# for loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
# It executes a block of code for each element in the sequence.
    
for c in range(1,10):
  print(c)
  if c==5:
      continue
girls=['dija','hady','mariam','julius']
for c in girls:
      print(c)
      #EXCEPTION HANDLING# Exception handling(try, except, finally)
# except is used to handle specific type of exceptions when they occur.
#try:
    # code that may raise an exception
    # It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.
#except SomeException:
    # code executed if SomeException is raised
#except AnotherException:
    # code executed if AnotherException is raised
#else:
    # code executed if no exceptions are raised
#finally:
    # code executed regardless of whether an exception occurred or not
#try:
     #x = int(input("Enter a number: "))a = ["Python", "Exceptions", "try and except"]
     
a = ["hadijah", "eats", "food"]       
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
#if an error occurs in the try block, then except block will be executed by the Python interpreter       
except:  
    print ("Index out of range")  
#Exercise: write a program to ask students about their mental health, prompt students on a scale of 1 to 10 to rate their mental health
health_issues={
    1:"Sad",
    2:"Anxious",
    3:"Disgust",
    4:"Fear",
    5:"Confused",
    6:"Shame",
    7:"scared",
    8:"mixed emotions",
    9:"loving",
    10:"Happy",
    }
mentalHealth=int(input("How can you rate your mental Health on a scale of 1-10?"))
if mentalHealth in health_issues.keys():
    print(health_issues[mentalHealth])


#functions
#holds blocks of code
def function_name (first_name,last_name):
    print("class starts in the afteernoon")
    print("")
    print("attenders are close to 100 including {first_name} {last_name}")
    
    #calling a function
    function_name("hadijah","Nalukwago")
    #Arguments and parameters
    #Arguments are specified after the function
    #parameters are
