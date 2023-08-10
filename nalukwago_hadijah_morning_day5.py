class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Cow(Animal):
    def meow(self):
        print(f"{self.name} is mooowing")


# create Animal objects
animal= Animal("animalia")

dog = Dog("chama")
cat = Cow("momo")
print()

# invoke eat method
animal.eat()
dog.eat()
dog.bark()
print()


# demonstrate the using of inheritance to calculate the are and perimeter of the circle and rectangle
class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14* self.radius


class Rectangle(Shape):
    def __init__(self, name, length, breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)


circle = Circle("circle", 5)
print(circle.calculate_area())
print( circle.calculate_perimeter())

print()

rectangle = Rectangle("Rectangle", 6, 5)
print( rectangle.calculate_area())
print(rectangle.calculate_perimeter())

print()
 
 #multiple inheritance
print("Multiple inheritance")  
class Flyable:

    def fly(self):
        print(f"{self.name} is flying")


class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Bird(animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def fly(self):
        print(f"{self.name} is flying")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")
my_bird = Bird("duck", "Bird")
my_bird.display_info()
my_bird.eat()
my_bird.fly()
#method overriding and method overloading
class Animal:
    def make_sound(self):
        print(f"Animal makes a sound")
class Pig(Animal):
    def make_sound(self):
        print("pig is grunting")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
def animal_sound(animal):
    animal.make_sound()
# create objects
animal = Animal()
dog = Dog()
pig = Pig()
print()
# calling make animal sound
animal_sound(animal)
animal_sound(dog)
animal_sound(pig)

#polymorphism
print("polymorphism")
class Shape:
    # create methods

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
# sub class rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)
# sub class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
# create objects
rectangle = Rectangle(15, 20)
circle = Circle(10)
# calculate Area
print(f"The area of a rectangle is {rectangle.calculate_area()}")
print(f" The area of a Circle is {circle.calculate_area()}")
print()
# calculate Perimeter
print(f" The perimeter of a rectangle is {rectangle.calculate_perimeter()}")
print(f" The perimeter of a Circle is {circle.calculate_perimeter()}")

#abstrction
print("Abstraction")
from abc import ABC, abstractclassmethod
from pyparsing import abstractmethod
class Vechicle(ABC):
    @abstractclassmethod
    def start(self):
        pass
    @abstractclassmethod
    def stop(self):
        pass
class Car(Vechicle):
    def start(self):
        print("starting car")

    def stop(self):
        print("stoping car")
class Truck(Vechicle):
    def start(self):
        print("starting truck")

    def stop(self):
        print("stoping truck")
# create objects
car = Car()
truck = Truck()
car.start()
truck.start()
print()
# start thr vechicle
car.stop()
truck.stop()
       
#exercise 2
print("exercise2") 
class Figure(ABC):
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
# creating objects
rectangle = Rectangle(12, 10)
circle = Circle(10)
# invoke the methods
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print()
print(f"circle Area: {circle.area()}")
print(f"circle Perimeter: {circle.perimeter()}")        
import tkinter as tk
from tkinter import messagebox

def print_receipt():
    # Get the values from the input fields
    customer_name = name_entry.get()
    item_name = item_entry.get()
    item_price = price_entry.get()
    quantity = quantity_entry.get()
    

    # Validate input fields
    if not customer_name or not item_name or not item_price or not quantity:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        # Calculate total price
        total_price = float(item_price) * int(quantity)

        # Create the receipt text
        receipt_text = f"Customer: {customer_name}\n"
        receipt_text += f"Item: {item_name}\n"
        receipt_text += f"Price per item: Ugx{item_price}\n"
        receipt_text += f"Quantity: {quantity}\n"
        receipt_text += f"Total price: Ugx{total_price:.2f}"
      

        # Display the receipt in a message box
        messagebox.showinfo("Receipt", receipt_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity.")

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program") 
window.geometry("800x600") 
window.configure(background="gray")
font_size = ("Arial", 44)


# Create labels and input fields
name_label = tk.Label(window, text="Customer Name:", foreground="black", background="brown",font=font_size )
name_label.pack()
name_entry = tk.Entry(window, font=font_size)
name_entry.pack()

item_label = tk.Label(window, text="Name of the item:",foreground="black", background="brown",  font=font_size)
item_label.pack()
item_entry = tk.Entry(window, font=font_size)
item_entry.pack()

price_label = tk.Label(window, text=" price of item :",foreground="black", background="brown",  font=font_size)
price_label.pack()
price_entry = tk.Entry(window , font=font_size)
price_entry.pack()

quantity_label = tk.Label(window, text=" Size/Quantity:",foreground="black", background="brown", font=font_size)
quantity_label.pack()
quantity_entry = tk.Entry(window, font=font_size)
quantity_entry.pack()




# Create the print button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Run the main event loop
window.mainloop()      
            
            
            