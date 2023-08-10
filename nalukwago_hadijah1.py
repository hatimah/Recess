print("running python scripts")
print("i love python")

print("hadijah Nalukwago")

#variables
hady= 30
w ="bags"
z= 43.5 

#data structures
"""
#Numeric values are 1 -10
integer values are int
float values orsorsare float like 2.30

string values are str
'hadijah'
 mapping data types
 dictionaries

"""
#datatypes
hady= "i am a girl"
print(type(hady))
#outputs i am a girl

w = 43.5
print(type(w))

#more on lists
friends=["hady","daisy","daniel","girls","daniel","daisy"]
print(friends)
#prints the length of the list
#outputs 6 with all the duplicates counted
print(len(friends))
#prints the type of the variable friends
print(type(friends))
#access the list item
print(friends[2:5])
print(friends[:4])
print(friends[2:])
friends.append("saudah")
print(friends)
#inserting
friends.insert(0,"martha")
print(friends)
#removing an item 
friends.remove("martha")
print(friends)
friends.pop(6)
print(friends)


#tuples 
# same as lists, except that tuples are ordered and unchangeable"""
halas=('samsung','iphone,''techno','nokia') 
print(halas) 
phones=('samsung','iphone','techno','techno','samsung')
#exercises
"""
use the len() with this typle example
tuple showing different datatypes
how to access tuples
add items to a tupple[first convert it into a list eg hady= list(phones) and then convert it back
to a tuple eg
phones= tuple(hady)]"""
tuple1=('matooke','rice')
tuple2=(100,200,300,500)

#control flow 
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
    
    #Loops( while and for)
    #break and continue