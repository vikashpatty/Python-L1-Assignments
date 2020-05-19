#!/usr/bin/env python
# coding: utf-8

# In[2]:


mylist = range(4)
seclist = mylist
print(seclist)
mylist.append(4)
print(seclist)
seclist = mylist[:]
print(seclist)
mylist.append(5)
print(seclist)


# In[3]:


def f(n):
  for x in range(n):
    yield x**3

for x in f(6):
  print(x)


# <h3>3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters. 
#    If yes return True else False.
# </h3>

# In[4]:


count=0
string=input()
for i in range(len(string)-1):
  if(string[i]=="e"):
    count=count+1
if(count==2):
  print("True")
else:
  print("False")


# In[5]:


counter = 1
def dolots(count):
  global counter
  for i in (1, 2, 3):
    counter = count + i

print(dolots(4))
print(counter)


# <h3>5.	Write a code to read  the data from  input file called input.txt and count the number of characters per line, number of words per line and write these into output file called as output.txt 
#     </h3>

# In[8]:


words_count=0
char_count=0

file1=open("input.txt","r")
file2=open("output.txt","w")
for line in file1:
    l=1
    words=line.split()
    words_count=len(words)
    char_count=len(line)
    file2.write("line num:%d Number of words:%d Number of words %d \n" %(l,words_count,char_count))
    l=l+1


# In[9]:


List1=[1,2,3,4,5,0]
List2=[7,4,3,2,6,5,2,1]
List3=[9,5,3,0,1]
#a) Create Maxlist by taking 2 maximum elements from each list.
List1.sort()
List2.sort()
List3.sort()
print (List1)
List5=List1[len(List1)-1],List1[len(List1)-2],List2[len(List2)-1],List2[len(List2)-2],List3[len(List3)-1],List3[len(List3)-2]
print (List5)


# In[10]:


#b) Find average value from all the elements of Maxlist.
sum=0
for i in range(len(List5)):
  sum=sum+List5[i]
avg=sum/len(List5)
print (avg)


# In[11]:


#c) Create Minlist by taking 2 minimum elements from each list.
List6=List1[0],List1[1],List2[0],List2[1],List3[0],List3[1]
print (List6)


# In[12]:


#d) Find average value from all the elements of Maxlist.
sum=0
for i in range(len(List6)):
  sum=sum+List6[i]
avg_min=sum/len(List6)
print (avg_min)


# <h3>7.	Write program to convert prefix/net mask to IP
# eg: input:16  output: 255.255.0.0
# </h3>

# In[13]:


from socket import inet_ntoa
from struct import pack


def DottedNetmask(mask):
    bits =  0xffffffff ^ (1 << 32 - mask)-1
    return inet_ntoa(pack('>I', bits))

mask=int(input("enter a mask"))
ip=DottedNetmask(mask)
print(ip)


# <h3>8.	Create a suitable data construct to read the data from an xml document as shown below:
# <bookstore shelf="New Arrivals">
#   <book category="COOKING">
#     <title lang="en">Everyday Italian</title>
#     <author>Giada De Laurentiis</author>
#     <year>2005</year>
#     <price>30.00</price>
#   </book>
#   <book category="CHILDREN">
#     <title lang="en">Harry Potter</title>
#     <author>J K. Rowling</author>
#     <year>2005</year>
#     <price>29.99</price>
#   </book>
#   <book category="WEB">
#     <title lang="en">Learning XML</title>
#     <author>Erik T. Ray</author>
#     <year>2003</year>
#     <price>39.95</price>
#   </book>
# </bookstore>
# </h3>

# In[14]:


import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()
for child in root:
    print(child.tag,child.attrib)
    for item in child:
        print(item.tag,":",item.text)


# <h3>9.	Create a suitable object type and  check for file size of 0 bytes of the directory contents as shown below
# <br>02/15/2016              10:49 PM               962                     switchfinal.py
# <br>02/15/2016             10:49 PM               943                       switchfinal.py.bak
# <br>01/27/2016             11:46 AM                15                        t.py
# <br>03/31/2016            12:39 PM               840                        t1.py
# <br>01/25/2016            10:34 AM             2,407                      tc1.py
# <br>02/14/2017           09:13 AM                 0                           teat.py
# <br>03/15/2016          05:52 PM                 5                             tes.py
# </h3>

# In[16]:


import os
my_dir = r'C:\Users\imvik\Wipro Assignment'

for f in os.listdir(my_dir):   
    path = os.path.join(my_dir, f)
    if os.path.isfile(path):  
        if(os.path.getsize(path)==0):
            print(f)


# <h3>10.Create a suitable object type to eliminate the duplicate elements</h3>

# In[17]:


list=[2,7,3,6,1,2,7]
rem_dup=set() 
for i in list:
    rem_dup.add(i)
print(rem_dup)

