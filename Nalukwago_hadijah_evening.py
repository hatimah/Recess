    #dictionaries
    #dictionaries dont contain duplicates
    #EXAMPLE1: dictionary
friends ={
            "hady": "i am a girl",
            "daisy": "i am a girl",
            "daniel": "i am a girl",
            "girls": "i am a girl",
            "daniel": "i am a boy",
            "daisy": "i am a girl"
        }
print(friends)
# length of a dictionary
print(len(friends))
#access a dictionary
s=friends["hady"]
print(s)
g=friends.get("daniel")
print(g)
#change the value of a key
friends["hady"] = "i am a boy"
print(friends)
#loop through a dictionary 
for h in friends:
 print(h)
 print(friends[h])
    #here we are printing each values with its value
    #print(friends[f])
    #add items in the dictionary
friends["forna"] = "i am a girl"
print(friends)
    #remove items from the dictionary
    #friends.pop("daniel")
    #print(friends)
    #check if a key is in the dictionary
if "girls" in friends:
        print("yes")
else:
        print("no")
#NUMBERS
s=20 
w=38.99
y= 2j
print(type(y))
print(type(s))
print(type(w))

#complex numbers
f =6+2j
z= complex(s)
print(z)
print (type(z))
h =complex(w)
print(type(h))
a =int(12)
b =int(32000)
c =int(3.5)
d =int('4')
print(a,b,c,d)
               
#STRINGS
print("i am hadijah")
print ('this is hadijah')
#assigning string to a variable
hady ="hadijah"
print (hady)
#multiline strings
k ="""
 i am hadijah
 and i learn datascience
 and my best language is python
 """
print(k)
#strings as arrays
hady ="hadijah"
print(hady[4])
#exercise1
print(len(hady))
#exercise2
for i in hady:
    print(i)
 #exercise3
 #slicing in strings  
  #modify a string
print(hady.lower())
print(hady.upper())
# removing whitespace we use the strip()method
# string concatenation
#FORMAT SRTING
#works when one wantsto combine a string to a number
age = 21
name = "my name is hadijah and i am {} years old"
print(name.format(age))
        
#EXERCISE
#excercise 1 : use the values( methos to reurn a list of all values in the dictionary
#excercise 2: check if a key exists in a dictionary
#exercise3:give an example on how to change dictionary items,how to update 
# #exercise4 Give an example of how to add items to a dictionary and how to remove dictionary items
 #exercise5 give an example how toloop through dictionary and how to nest a dictionary   
family={
      "abdu": " first",
      "hady": "second",
      "daniel": " third",
      "jati": " fourth",
      "soda": " fifth",
  } #exercise1
for x in family.values():
          print (x)  
          #exercise2
if "hady" in family:
     print("yes")
else:
    print("no")
#exercise3
#one can change a dictionary item by  changing it's key value
family["soda"] = "sixth"
print(family)
#exercise4
# adding another item to a dictionary
family["pretty"] = " last"
print(family)
# removing a dictionary item
family.pop("daniel")
print(family)
#exercise5 
for x,y in family.items():
    print(x,y)
 #nesting dictionaries
jail ={
  "adam" : {
    "name" : "jati",
    "year" : 1994
  },
  "mariam"  : {
    "name" : "daniel",
    "year" : 1995
  },
  "hadijah" : {
    "name" : "adam",
    "year" : 1998
  }
}
print(jail)
 
