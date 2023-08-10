#regular expressions
#generators and iterators
#decoratorss
#matchers and searchers
#regex re.match(), re.search(), refinal()
# example1
#regex| Match Firstword , Match Groupword, Match all numbers
import re
text ="Hello,my name is hadijjah . I am a programmer with 15years of experience"
#match f
match =re.search(r"^\b\w+\b",text)
if match:
    print( "match:",match.group())
naji=re.findall(r"\b\d+\b",text )
print("naji:",match.group())  
#validate email address
import re
def validate_email(email):
 pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
 if re.match(pattern,email):
       return True
 else:
       return False
email=input("enter your email address")
print(validate_email(email))

print("Generators and Iterators")
def greet(f):
    if f == 0:
        yield 1
    else:
        yield f*greet(f-1)
for i in range(0,9):
  print(greet(i))    
  #example3
  # generate a function that yields the square of numbers from 1 to 10 
  def square_nmbrs():
      for j in range(1,10):  
          yield j**2
for g in square_nmbrs():
    print(g)     
print("ITERATORS")
class MyFriends:
  def __iter__(self):
    self.b = 1
    return self

  def __next__(self):
    if self.b <10:
     z = self.b
     self.b += 1
     return z
    else:
     raise StopIteration
myclass = MyFriends()
load = iter(myclass)

for x in load:
  print(x)
  
print("DECORATORS")
def funny(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I am funny and so are my friends")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I aint no ordinary person ....i am very special easy and hard to deal with so stay warned")
    
# decorate the ordinary function
decorated_func = funny(ordinary)

# call the decorated function
decorated_func()
  