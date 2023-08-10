#exercise no1 lists
#no1

hady=['nalukwago','hadijah','flower','kimuli','lady']
x =hady[1]
#no2
hady[0]="Harriet"
print(hady)
#no3
hady.append("kcee")
print(hady)
#no4
hady[2]="Kaguta"
print(hady)
#no5
hady.pop(3)
print(hady)
#no6
print(hady[-1])
#no7
daily=["orange","mango","apple","banana","cucumber", "pumpkin","pineapple"]
#no8
print(daily[3:5])
#no9
Countries=["US", "Uganda","kenya","algeria","mozambique","Tanzania","Sudan"]
#no10
Countries2=Countries.copy()
print(Countries2)
for x in Countries:
    print(x)
    #no11
    Animals=["Dog","Cat","Bird","Fox"]
    Animals.sort()
    print(Animals)
Animals.sort(reverse=True)
print(Animals)
    
for x in Animals:
 if "a" in x:
        print(x)

myname=["hadijah"]
myname2=["kitti"]
#joining the two lists
myname.extend(myname2)
print(myname)
 #tuples
x=("sumsang","iphone","tecno","redmi")
print(x[3])

#no 2
print(x[-2])
 #no 3
z = list(x)
z[1]="nitel"
x =tuple(z)
print(x)
#no4
s = list(x)
s.append("huwaei")
x=tuple(s)
print(x)
#no.5
for l in x:
    print(l)
#no6
#no7 
mycities=tuple(["Kampala","Jinja","Masaka","Gulu"])
print(mycities)
#no8
print(mycities[0],mycities[1],mycities[2],mycities[3])
#no9
print(mycities[1:3])
#no10
firstname=("hady")
lastname=("dijah")
fullname=firstname+lastname
print(fullname)
#no11
colors=("red","blue","green","yellow")
    #multiplying the tuple by three
colors=colors*3
print(colors)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    #return the number of times 8 appears in this tuple
print(thistuple.count(8))
 #SETS
jati= set(("mukwano","tea","bags"))
print(jati)
#no2
j =jati.add("adam")
print(j)
 #no.3
mySet={"oven","kettle","microwave","refrigerator"}
if" microwave"in mySet:
 print("it exists in mySet")
else:
    print("it doesnot exist") 
 #no.4
x =mySet.discard(("kettle"))
print(x) 
#no.5
for g in mySet:
    print(x)
#no.6
dija= set((1,2,3,4))
list=[5,6]
dija.update(list)
print(dija)
 #no.7
age={14,15,1,16}
names={"hady","dija","jati"}
s =age.union(names)
#STRINGS
#no1
a =1
z=str(a)
b ="hady"+str(a)
print(b)
#no2
txt="  hello, Uganda! "
print(txt.strip())
#no3
print(txt.upper())
 #no4
print(txt.replace("U","V"))
#no5
y="i am proudly Ugandan"

#no6
x = "“ All, “Data Scientists” are cool!” "
#dictionary
#no1
Shoes ={
    "brand": "nick",
    "color": "black",
    "size": 40
}
Shoes["size"]=50
#no2
Shoes["brand"]="adidas"
#no3
Shoes.update({"type": "sneakers"})
print(Shoes)
#no4
v =Shoes.keys
print(v)
#no5
s= Shoes.values()
print(s)
#no6
x="size" in Shoes
print(x)
#no7
for n in Shoes:
 print(n)
    #no8
Shoes.pop("color")
print(Shoes)
#no9
Shoes.clear()
print(Shoes)
#no10
hady= Shoes.copy()
print(hady)
#no11
jail = {
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
  }}
print(jail)    

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 