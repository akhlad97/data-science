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

# %%
nums

# %%


# %%


# %%


# %%


# %%



