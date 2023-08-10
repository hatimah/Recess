class love:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def care(self):
        print("Hello, my name is " + self.name  + "and i love myself  ")
        print("My age is " + str(self.age))  # Converted age to string
wubai = love("hady", 45)
wubai.care()
    
class Student:
  def __init__(self,name,year,course):
        self.name =name
        self.year= year
        self.course =course
  def display_details(self): 
    print("Name:",self.name)
    print("Year:",self.year)
    print("course:",self.course)
hady = Student ("jeff geoff",3,"software Engineering")
hady.display_details()    
            
#EXERCISE
#calculate the area and circumference of a circle
#calculate the area and perimeter of a rectangle
class rectangle:
  def __init__(self,length,breadth):
       self.length = length
       self.breadth = breadth
  def area(self):
       return 2 * (self.breadth*self.length)
     
  def perimeter(self):
      return 2 * (self.length + self.breadth)
dijah =rectangle(5.0,6.0)
print(dijah.area())
print(dijah.perimeter())
#example2
class circle:
  def __init__(self,radius): 
     self.radius = radius
  def area(self):
       return 2 * 3.14 *(self.radius*self.radius)
  def circumference(self):
        return 2 * 3.14 * self.radius
rad = circle(4.0)
print (rad.area())
print (rad.circumference())     

class Bonus:
  def __init__(self,percentage,salary):
    self.percentage= percentage
    self.salary = salary
  def bonus_money(self):
      return self.salary * self.percentage
  def print_bonus(self):
        # Convert bonus to string
        print("The actual bonus amount is: " +
              str(self.salary + (self.bonus_money())))
employee1 = Bonus(0.15, 150000)
employee1.print_bonus()

#temperature example
class Temperature:
    def _init_(self):
        self.celsius = 0.0
        self.fahrenheit = 0.0

    def set_celsius(self, celsius):
        self.celsius = celsius

    def get_celsius(self):
        return self.celsius

    def convert_to_fahrenheit(self):
        self.fahrenheit = (self.celsius * 9/5) + 32

    def get_fahrenheit(self):
        return self.fahrenheit


# Create an instance of the TemperatureConverter class
converter = Temperature()

# Set the temperature in Celsius
celsius = float(input("Enter temperature in degrees Celsius: "))
converter.set_celsius(celsius)

# Convert Celsius to Fahrenheit
converter.convert_to_fahrenheit()

# Get the converted temperature in Fahrenheit
fahrenheit = converter.get_fahrenheit()

# Display the result
print("Temperature in degrees Fahrenheit: ", fahrenheit)
      
      
      #ENCAPSULATION
      #bankAccount
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__salary

    def set_amount(self, new_salary):
        self.__salary = new_salary

    def increment_pay(self, increment_amount):
        self.__salary += increment_amount


# Create an employee object
employee = Employee("Jati", 850000)

# Display the initial salary
print("Initial Amount:", employee.get_salary())

# Increment the pay by 150000
employee.increment_pay(150000)

# Display the new salary
print("New Amount:", employee.get_salary())
              