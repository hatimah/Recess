#day3
#basic poertors and expressions (Input and output operat)
"""
arithmetic operators
+addition
-subtraction
*multiplication
/division
 divide
%modulous
**exponention

 -Comparison operators
== Equal to
!= not equal to !=
> -greater than
< -less than
>= - Greater than or equal to
<= less than or equal to

 -LOGICAL OPERATORS
Logical And 'and'
logical OR 'or'
logical not 'not'

ASSIGNMENT OPERATORS
assign value: '='
add value: '+' concatenating
add and assign a value: '+='
subtract and assign a value: '-='
multiplication and assign
division and assign  '/='
modulous and assign :'%='
exponention and assign ='**=+addition

MEMBERSHIP OPERATORS
In -checks if the value exists in a sequence
Not In - checks if the value does not exist in a sequence

Identity operators
Is operator -checks if two values are the same
Is not - checks if two values are not the same
"""
#addition
b = 35+75
print(b)
# subtraction
a = 35-75
print(a)
#division
m= 35/75
print(m)
# multiplication
p = 35*75
print(p)
#exponention
t = 35**3
print(t)
# modulous
s =100%2
print(s)

#comparison operator examples
q=5
p=10 
if q>p:
     print(q>p)
elif p==q:
    print (p==q)
elif p!=q:
    print(p!=q)
else :      
    print(q<p)
    #example2
q=45
p=10
if q>=p:
     print(q>=p)
     print('this is p greater than q')
elif p<=q:
    print ("p is equal to q")
elif p<q:
    print("p is not equal to q")
else :      
    print(q<=p)
    #logical operators
s= True
t =False
#logical and
print(s and t)
#logical or
print(s or t)
#logical not
print(not p)
print(not t)
#compound assignment operators
#assign and an operation
a=10
a+=5
print(a)
b=50
b-=3
print(b)
c=20
c/=5
print(c)
d=45
d%=3
print(d)
e =4
e**=3
print(e)
#membership assignment operators
cars=['bugatti','rollsroyce','mercedese benz','V8']
if 'mercedese'in cars:
 print('rollsroyce' in cars)
print("bugatti"in cars)
print("V8"in cars)
#identity operators
g=5
h=6
print(g is h)
print(g is not h)
print(g==h)
print(g != h)

w =[1,3,4,6,7,5,2,9]
x=[2,1,5,7,8,5,3]
print(w is x)
print(w is not x)
#BITWISE OPERATORS
# ARE USED TO PERFORM opertions on the individual bits of binary numbers
#bitwise AND('&):  performs an AND operation between the coresponding bits of two integers
#bitwise AND('|):  performs a bitwise OR operation between the coresponding bits of two integers
#bitwise AND('XOR):  performs an XOR operation
#bitwise NOT('&):  performs an AND operation between the coresponding bits of two integers
a = 10
b=20
result_and = a & b
print(result_and)
result_xor = a & b
print(result_xor)
result_not = a | b
print(result_not)
#exercise for the calculator
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Nalukwago_ Hadijah's_Calculator")

# Create an entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
button_1 = tk.Button(window, text="1", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=40,fg ="black", bg ="yellow", command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=40,fg ="black", bg ="yellow", command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=40,fg ="black", bg ="yellow", command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=40,fg ="black", bg ="yellow", command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=40,fg ="black", bg ="yellow",  command=lambda: button_click(0))

button_add = tk.Button(window, text="+", padx=40, pady=40, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=40, pady=40, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=40, pady=40, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=40, pady=40, command=lambda: button_click("/"))
button_clear = tk.Button(window, text="C", padx=40, pady=40, command=button_clear)
button_equal = tk.Button(window, text="=", padx=40, pady=40, command=button_equal)

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

# Start the main event loop
window.mainloop()
