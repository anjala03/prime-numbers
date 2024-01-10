print (" hello world")
a=9
b=4
if a>b:
    print ("a is greatest")
else:
    print ("b is greatest")
    # this is a comment in python
x=5
y="Ram"
z=4.0
print (x)  
print (y)  
print (z)  
r= float(3)
print (r)
i,j,k= "ram", "hari", "shyam"
print(i,j,k)
d=e=f= "ram"
print(d)
print(e)
print(f)
fruits=["apple", "cherry", "mango"]
m,n,o=fruits
print(m)
print(n)
print(o)
v="mornings"
def greet():
    print("good"+v)
greet()
s="hi"
def greetings():
    s="me"
    print("its"+s)
greetings()
print("ITS"+s)
print(type(a))
k=2+5j
print(type(k))
name="ranjit"
print(name[2])
print(name[-4:-1])
l="All in uppercase"
print(l.upper())
t="hi, its me  "
print(t.strip())
u= "helloo, world"
print(u.split(","))
result=t+u
print(result)
age=22
print("hi, i'm {} years old" .format(age))
print ("we are \"vixings\" of the north")
list1=["ram", 1, 6.0, "hari"]
print (list1)
print (list1[1])
list1[0]="anjala"
print(list1)
list1.insert(3, "bhatta")
print(list1)
list2=["apple", "cat", "banana", "dog"]
list2.sort()
print(list2)
tuples= (1, 2, 3)
print(tuples)
sets= {2,3,4,4,5}
sets.remove(2)
print(sets)
dict1={1:"ram",2:"hari", 3:"shyam" }
dict1[4]="rahendra"
print(dict1)
list2={"Anjala", "Karuna", "Sarita"}
for i in list2:
    print(i)
j=1
while (j<=6):
    print("hiiiiii")
    j+=1
def func(a,b):
    sum=a+b
    print(sum)
func(2,3)
