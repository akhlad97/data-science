# %% [markdown]
# ## PYTHON INTERPRETTER
# ## IDE (INTEGRATED DEVELOPMENT ENVIRONMENT)

# %% [markdown]
# PYTHON INTERPRETER -->
# What is Python interpreter?
# A python interpreter is a computer program that converts each high-level program statement into machine code. An interpreter translates the command that you write out into code that the computer can understand
# 
# PYTHON INTERPRETER EXAMPLE --> 
# You write your Python code in a text file with a name like hello.py . How does that code Run? There is program installed on your computer named "python3" or "python", and its job is looking at and running your Python code. This type of program is called an "interpreter".

# %% [markdown]
# IDE (INTEGRATED DEVELOPMENT ENVIRONMENT) =>
# - using IDE - one can write code, run the code, debug the code
# - IDE takes care of interpreting the Python code, running python scripts, building executables, and debugging the applications.
# - An IDE enables programmers to combine the different aspects of writing a computer program. 
# - if you wanted to be python developer only then you need to install (IDE -- PYCHARM),vs code
# 

# %% [markdown]
# #### Python Compilers 
# Python is a high-level programming language. The code we write in Python is easily understandable to us but not to computers. Since computers can’t understand, computer can’t execute the code. Hence we need to translate our code in Python to something a computer can understand and execute, machine language. So we created a program that can translate our source code to an executable code and the program is called a Compiler
# 

# %% [markdown]
# #### Working of Compilers in Python
# - A lot of processes happen between pressing the run button on our IDEs and getting the output, and half of that
#   process involves the working of compilers.
# - When we run a Python file (.py), the compiler starts reading the file
# - The compiler reads the file and checks for errors.
# - If an error is found, the compiler stops and displays an error message.
# - If no errors are found, then complier translates the Python code to Byte code.
# - The byte code is stored in a file with .pyc or .pyo or .pyd format.
# - The Python Virtual Machine (PVM) receives the Byte code file.
# - PVM is an interpreter. It reads and checks the file for errors.
# - If any  error is found, the interpreter stops and displays an error message.
# - If no errors are found, then interpreter translates the Byte code to Binary code.
# - Binary code which is also called Machine language that is an executable language.
# - Finally, the computer reads the binary code and executes the program
# 

# %% [markdown]
# #### What is a .py File?
# - .py file is a plain text file that contains Python source code. This is the file you write your code in when you    are  developing a Python program. Here are some key points about .py files
# 
# #### What is a .pyc File?
# - .pyc file is a compiled Python file. When you run a Python program, the interpreter compiles the source code into bytecode, which is a low-level set of instructions that can be executed by the Python virtual machine (PVM). This bytecode is then saved as a .pyc file
# 

# %% [markdown]
# #### ANACONDA 
# - Anaconda is a distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment.
# - Anaconda simplifies package management and deployment by providing a large collection of libraries and tools that are essential for data analysis and scientific computing. It's widely used because it streamlines the setup process for data scientists and developers

# %%
1+1 ### addition

# %%
2-1 ### subtraction

# %%
2*2 ### multiplication

# %%
6/2 ### division

# %%
8/5 ## float division

# %%
2+3+5-6

# %%
8+8- ## syntax error 

# %%
(5 + 5) * 5 # BODMAS (Bracket || Oders || Divide || Multiply || Add || Substact)

# %%
2*2*2*2*2

# %%
2**5 ## explonantial

# %%
15/3 ## return float value 

# %%
9//2 ## return integre value ,without floating point

# %%
11%2 ## modulus,return reminder

# %%
15%%2 ## systeax error

# %%
# multiple assignment (or parallel assignment)
a,b,c,d,f=12,13,2+9j,'nit',3.2
print (a)
print(b)
print(c)
print(d)
print(f)

# %%
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(f))

# %% [markdown]
# ### string
# - lets work with string

# %%
'abc'

# %% [markdown]
# - python inbuild function - print & you need to pass the parameter in print()
# 
# - A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# %%
print('abcd')

# %%
s1='welocome to python course from begginer to advanced'
s1

# %%
a=2
b=3
a+b

# %%
a=2
b=3
c=a+b
c

# %%
a=2
b='technology'
print(type(b))

# %%
print('python\'s "programming"') ## \ has specail meaning to ignore error

# %%
'abc '+' abc'

# %%
'abc' ' abc'

# %%
'abc' , ' abc'

# %%
print(type(('abc' , ' abc')))

# %%
print('c:\nnit') ##\n new line

# %%
print(r'E:\python') # raw string

# %%
## variable || identifier || object



# %%
x=2 ## x is variable /identifier /object 2 is value 
x

# %%
x+3

# %%
y=3
x+y

# %%
_ +y ## _ understand previous result here previous result is 5

# %%
_ +y

# %% [markdown]
# #### String in python
# - A String is a data structure in Python Programming that represents a sequence of characters. It is an immutable data type string does not support item assignment , meaning that once you have created a string, you cannot change it. Python String are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text

# %%
# string varible 
name='abc'

# %%
name=name+' technology'
name

# %%
len(name)

# %%
name[0] ## python index begin with zero

# %%
name[13]

# %%
name[14]

# %%
name[-1] ## indexing from revrse side ,right left side 

# %%
name[-5]

# %%
name[-14]

# %% [markdown]
# ### slicing
# 

# %%
name='nit'
name

# %%
name[0:1]## print 2 chracater --> 0 index character 

# %%
name[0:2] # last index is 2-1=1 ,print the character from 0 index to 1 index

# %%
name[1:4]

# %%
name[1:3]

# %%
name

# %%
name[0:] ## from 0 to till last index

# %%
name[3:9]

# %%
name[0:1]='x' ## i want to change the firt character of name 

# %%
name[0]='d' # string  is immutable in python

# %%
name1='fine'

# %%
# i want to change string from fine to dine
'd'+name1[1:]


# %%
print(len(name1))

# %% [markdown]
# ### List 

# %%
nums=[10,20,30]
nums

# %%
nums[0]

# %%
nums[-1] # print the number in revers order from list

# %%
nums[1:] # print list element from 1 index to till last

# %%
nums[:1] # print the list from starting(from zero index ) to till 1 index 1 is exclude

# %%
nums1=['hi','hello']
nums1

# %%
nums2=[12,'hi',4.2,2+2j] ### we can assign multitype of value in list
nums2

# %%
nums3=[nums,nums2,nums2]
nums3

# %%
nums4=[nums,nums1,nums2,nums3]
nums4

# %%
nums

# %%
nums.append(45)

# %%
nums.append(30)

# %%
nums.remove(30)

# %%
nums

# %%
nums.pop(1) ## it delete the element index wise 

# %%
nums.pop() ### if you are not mnetioned the index it will the element from last index

# %%
nums1.insert(2,'nit') ### it will insert the element the index wise ,nit will insert where index is present the element which already prsent in in list that will shift on right side

# %%
nums1

# %%
nums1.insert(2,'abc')


# %%
nums1

# %%
nums2

# %%
# delete multiple walue from the list
del nums2[0:2] ## it will delete the element from index 0 to 2 (2 is exclude )

# %%
nums2

# %%
# add mulitple values to list 
nums2.extend([12,23,45,60])

# %%
nums2

# %%
nums3

# %%
nums3.extend([12,23,45,70])
nums3

# %%
# inbuild function
min(nums)

# %%
max(nums) # inbuilt function

# %%
sum(nums) # inbuilt  function ,addition of  all present in list

# %%
nums.sort() ## sort the elements in asceding order



# %% [markdown]
# ### TUPLE
# - Tuple : Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main
# difference between both is Python tuple is immutable, unlike the Python list which is mutable.
# Create Tuples using Round Brackets ()
# 

# %%
t=(12,13,14,15)
t

# %%
type(t)

# %%
t[0]=10

# %%
t.index(12)

# %%
t.count(10)

# %%
icici = (123456789, 'cizp4456u', 200000, '12th dec 2000')

# %%
icici[:2]

# %%
icici[3]

# %%
icici[3]

# %%
print(icici[3][5]) #nested indexing 

# %%
t1=(10, 20, 30, 5.6, 'nit', (1+2j), True, False, 10)

# %%
t1[1:6:2] # step=2 till index= 6, starting index =1

# %%
for i in enumerate(t1): #it will print the element along with index number 
    print(i)

# %%
sorted(t)

# %%


# %% [markdown]
# #### Set :
# - A Set in Python programming is an unordered collection data type that is iterable and has no duplicate elements. While sets are mutable, meaning you can add or remove elements after their creation, the individual elements within the set must be immutable and cannot be changed directly.
#  The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on  data structure known as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.
# 

# %%
set1={}
# set={} dict In Python, when you write set = {}, it creates an empty dictionary, not a set. This is because {} by default is used to represent a dictionary, not a set.


# %%
type (set1)

# %%
empty_set = set()
print(type(empty_set))

# %%
empty_set

# %%
# createting set by list 
set_by_list=set([12,34,35,23,12,67])
set_by_tuple=set((12,12,34,56,50,50,61))

print(set_by_list)
print(set_by_tuple)

# %%
s1={12,13,45,12,45,23,70}
print(s1)

# %%
s1.add('hello')
print(s1)

# %%

s2=s1.copy()
print(s2)

# %%
s2.clear()
print(s2)

# %%
s1.pop()

# %%
print(s1)

# %%
s1.remove(12)# it remove the element from the set it take exactly one parameter that is set element if element is not present in set then it give an errorKeyError

# %%
s1.discard('hello')
print(s1)

# %%
s1[0] #TypeError set' object is not subscriptable 

# %%
s1.update([70,12,4,8])
print(s1)

# %%
s1.update('welcome')

# %%
print(s1)
# s1.update('welcome')
# s1 {10, 3, 3.3, 5, 50, 'c', 'e', 'l', 'm', 'nit', 'o', 'w'} The update() method takes an iterable (in this case, a string) and adds its elements to the set. Since sets only contain unique items, it will add each character of the string 'welcome' as individual elements to s1


# %%
A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {9,10}


# %%
A.union(B)
# The A.union(B) operation combines the elements of sets A and B into a new set, removing any duplicate values.
# Duplicates (like 4 and 5) are included only once in the result.A | B  is similar to union method 



# %%
A.union(B,C)

# %%
A.intersection(B)
# {4, 5} opposite union The A.intersection(B) operation returns a new set containing only the elements 
# that are common to both sets A and B.

# %%
A.difference(B)
# A={1, 2, 3, 4, 5} B={4,5,6,7,8}output={1,2,3}method in Python returns a new set containing all the elements 
# that are in set A but not in set B. It is equivalent to the A - B operation.

# %%
B.issubset(A)
# True The B1.issubset(A1) method checks if all elements of set B1 are also present in set A1. It returns True if B1 is a subset of A1, and False otherwise.

# %%
C.isdisjoint(A) # All element of A id diffrent fro set c

# %%
A.isdisjoint(B) # all element of b is not different from A set

# %% [markdown]
# ### Dictionary: 
# - Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates, declared as {},

# %%
d={} # this is an empty dictionary
print(type(d))

# %%
d1=dict()# created an empty dictionary using dict constrcutor 

# %%
d1={'one':1,'tow':2,'three':3}


# %%
print(d1.keys())

# %%
print(d1['one'])

# %%
print(d1.values())

# %%
d1.pop('one')

# %%
for i in d1:
    print(i)

# %%
for i in enumerate(d):
    print(i)

# %%
# Create a dictionary that contain three dictionaries:
my_family={
    'child1':{
        "name":'akhlad',
        "email":'akhlad.contact@gmail.com'
    },
    'child2':{
        "name":'asjad',
        "email":"asjad.contact@gmail.com"
    },
     "child3":{
         "name":'ashhad',
         "email":'ashhad.contact@gmail.com'
     }
}

# %%
print(my_family['child1'])

# %%
print(my_family['child1']['name'])

# %%
# update the dictionary with specific key value pair
my_family['child1']={"name":"khalid","email":"khalid.contact@gmail.com"}

# %%
print(my_family['child1'])

# %%
# help(list)

# %% [markdown]
# #### What are the different types of control statements in Python? 
# - In Python, control statements are used to alter the flow of execution based on specific conditions or looping requirements. The main types of control statements are: 
# - Conditional statements: if, else, elif 
# - Looping statements: for, while
# - Control flow statements: break, continue, pass, return
# 
# #### What are the two types of control statements? 
# - The two primary types of control statements in Python are:
# - Conditional statements: Used to execute code based on certain conditions (if, else, elif). 
# - Looping statements: Used to execute code repeatedly until a condition is met (for, while)
# 
# #### Are control statements and conditional statements the same?
# - No, control statements and conditional statements are not exactly the same.
# - Conditional statements (if, else, elif) specifically deal with checking conditions and executing code based on whether those conditions are True or False. 
# - Control statements encompass a broader category that includes both conditional statements (if, else, elif) and looping statements (for, while), as well as other statements 
# (break, continue, pass, return) that control the flow of execution in a program
# 

# %% [markdown]
# ### Python conditional Statement Explanation:
# 
# ##### Python If Statement :
# - The if statement is the most simple decision-making statement. It is used to whether certain statement or block of statement will be executed or not 

# %%
##  illustrate pytho if statement
i=9
if i>=10:
    print('i am inside if statement ')

print('i am out side if statement')

# %% [markdown]
# #### Python If Else Statement :
# The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with the if statement Python to execute a block of code when the Python if condition is false

# %%
##  illustrate pytho if elif statement
i=9
if i>=10:
    print('i am inside if statement ')
else:
    print('i am inside else statement')

# %% [markdown]
# #### Python Nested If Statement
# - A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement. Yes, 
# Python allows us to nest if statements within if statements. i.e., we can place an if statement inside another if statement.
# 

# %%
i=10
if i>=10:
    print('i am in parent if statement')
    if i>=9:
        print('i am in child statement ')
print('i am out side ')

# %% [markdown]
# #### Python Elif: 
# - Here, a user can decide among multiple options. The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, 
# the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final “else” statement will be executed
# 

# %%
# if any condtion is Trueprogram will terminate 

a=10
if a>=11:
    print('i am if statement ')
elif a>=12:
    print('i am first elif statement')
elif a>=4:
    print('i am second elif statement')

# %% [markdown]
# #### Ternary Statement | Short Hand:  
# If Else Statement Whenever there is only a single statement to be executed inside the if block then shorthand  can be used. The statement can be put on the same line as the if statement
# #### Example of Python If shorthand:
#  In the given example, we have a condition that if the number is less than 15, then further code will be executed.
# 

# %%
i=10
if i<15 : print('i am less than 15')

# %% [markdown]
# #### How many else statements can a single if condition have in Python?
# - A single if condition can have at most one else statement. However, you can have multiple elif (else if) statements to check additional conditions if needed:

# %% [markdown]
# #### LOOPS :
# - in programing world some time we keep on repeating ,may be you want to repeat 5 statement so one way is copy & paste multiple times  or other way is.
# if you want to print the datascience 10 times then what you will do you cant copy for 10 times , if you want to print 1000 times then you cant do manualy .
# - type of loops --  While loop & For loop
# 

# %%
print('data science')
print('data science')
print('data science')
print('data science')
print('data science')

# %%
i=0
while i<=5:
    print('data science')
    i+=1

    


# %%
for i in range(5):
    print('data science')
    i+=1

# %%
i=1
while i<=5:
    print('data science',':',i)
    i+=1

# %%
# nested while Loop 
i=1

while i<=5:
    print('data sceince',':',i)
    i+=1
    j=1
    while j<=5:
        print('technology',':',j)
        j+=1
        

# %%
# nested while Loop 
i=1

while i<=5:
    print('data sceince',':',i,end=' ')
    i+=1
    j=1
    while j<=5:
        print('technology',end=',')
        j+=1
    print()
   
        

# %%
for i in range(11):
    print(i)

# %% [markdown]
# #### For|Else in python
# - in other language for else not supportable but in python it is supportable eg- lets print the number from 1- 20 & we dont want print number which is not divisible by 
# - it is alongated with for loop indentation

# %%
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break
else:
    print("No even numbers found")

# %%
for i in range(5):
    if i == 3:
        print("Found 3!")
        
else:
    print("3 not found")


# %%
# The else will execute because break was used.
for i in range(5):
    if i == 3:
        print("Found 3!")
        break
else:
    print("3 not found")
    
    
# %% [markdown]
# ## operator's in python
# 
# 
# - ARITHMETIC OPERATOR ( + , -, *, /, %, %%, **, ^
# - ASSIGNMEN OPERATOR (=)
# - RELATIONAL OPERATOR
# - LOGICAL OPERATOR
# - UNARY OPERATOR

# %% [markdown]
# 

# %% [markdown]
# ##### Arithmetic Operator

# %%
x1,y1=10,5
print(x1+y1)
print(x1-y1)
print(x1*y1)
print(x1/y1)
print(x1%y1)
print(x1//y1) ### it will return value with  floating point or with out decimal value 
print(x1**y1)


# %% [markdown]
# #### Assignment operators

# %%
x=2
x=x+2
x+=2
print(x)
y=2
y=y-2
y-=2
print(y)
z=2
z=z*2
z*=2
print(z)
p=12
p=p/2
p/=2
print(p)

q=12
q=q//2
q//=2
print(q)

r=6
r=r**2
r**=2
print(r)





# %% [markdown]
# ## unary operator 
# 
# Here we are applying unary minus operator(-) on the operand n; the value of m becomes -7, which indicates it as a negative value.

# %%
n=7
m=-(n)
print(m)

# %%
-n

# %% [markdown]
# # Relational operator 
# - we are using this operator for comparing

# %%
a=5
b=7
print(a==b)
print(a>=b)
print(a<=7)
print(a>b)
print(a<b)
print(a!=b)


# %% [markdown]
# #### Logical Operators
# - AND OR NOT

# %%
a=5
b=7
c=False
print(a>b and a>=b)
print(b>a and b>=a)
print(a>b or a>=b)
print(a>b or b>=a)
print(a<b or b>=a)
print(a>b or a<b)
print(not c ) ## reversed the boolean value 


# %% [markdown]
# ## Number system coverstion (bit-binary digit)
# binary : base (0-1) --> please divide 15/2 & count in reverse order 
# octal : base (0-7)
# hexadecimal : base (0-9 & then a-f)
# when you check ipaddress you will these format --> cmd - ipconfig

# %%
## conversion from decimal to binary ,decimal octal , decimal to hexadecimal
a=25
print(bin(a))
print(hex(a))
print(oct(a))

# %%
# conversion hexa to decimal ,decimal to binary ,binary to hexa
print(int(0b11001))
print(int(0x19))
print(int(0o31))
print(hex(0b11001))
print(oct(0x19))

# %% [markdown]
# ## BITWISE OPERATOR 
# - WE HAVE 6 OPERATORS 
# COMPLEMENT ( ~ ) || AND ( & )  || OR ( | ) || XOR ( ^ ) || LEFT SHIFT ( << ) || RIGHT SHIFT ( >> )

# %%
# COMPLEMENT (~) (TILDE  OR TILD)
~12 # why we get -13 . first we understand what is complment means (reversr of binary format)

# %%
print(~-6)
print(~-1)
print(12&13)
print(1&1)
print(1|0)
print(1&0)
print(35&40)
print(35|40)
print(12 ^ 13) # in XOR if the both number are different then we will get 1 or else we will get 0
print(1|0)
print(1^1)
print(0^1)
print(0^0)


# %%
# BIT WISE LEFT OPERATOR
#bit wise left operator bydefault you will take 2 zeros ( )
#10 binary operator is 1010 | also i can say 1010
print(10<<2)
print(10>>2)# right shift 

# %%
### import math module 
import math as mt 
print(mt.sqrt(24))
print(mt.floor(2.8))
print(mt.ceil(2.4))
print(mt.pi)
print(mt.pow(3,2))
print(mt.e)w


# %% [markdown]
# ### user input function in python || command line input

# %%
x=input()
y=input()
z=x+y
print(z)

# %% [markdown]
# - lets take input from the user in char format, but we dont have char format in python

# %%
x2 = int(input('Enter the 1st number'))
y2 = int(input('Enter the 2nd number'))
z2 = x2 + y2
z2

# %%
ch=input('enter characters')
print(ch[0])
print(ch[1])
print(ch[2])
print(ch[-1])
print(ch[-2])
print(ch[-0])

# %%
ch=input('enter character')[0]
print(ch)

# %%
ch=input('enter character')[0:4]
print(ch)

# %%
ch=input('enter expression')[:]
print(ch)

# %%
ch=eval(input('enter expression'))
print(ch)



# %% [markdown]
# ### print function 

# %%
a=20
b=10
a
b # it will print last statment 

# %%
# in order to print both a and b use print function 
a=20
b=10
print (a)
print(b)

# %%
# print more than one varibale 
print(a,b, 'akhlad')

# %%
# pritn with message
a=10
b=20
add=a+b
print('value of a is ',a,'value b is ',b,'simple string is ','akhlad') 
print('addition of {} and {} is  {}'.format(a,b,add))


# %% [markdown]
# ### More short format meythod(f string method)
# variable should be in curly braces
# and write everything inside quots ''
# at starting simpaly add f

# %%
num1=20
num2=30
num3=40
avg=(num1+num2+num3)/3
print(f'the avrgae of {num1} and {num2} and {num3} is {avg}')


# %%
# end 
print('hello',end=' ')
print('good morning',end=',')
print ('how are sir ',end=',')
print('is every thing fine')

# %% [markdown]
# # seprator
# 1. here one print statement only we use
# 2. insisde one print statement we have multipal values
# 3. we want to seperate these multipal values with anything

# %%
print('hello','good','morning','this is python','programming', sep='---->')



