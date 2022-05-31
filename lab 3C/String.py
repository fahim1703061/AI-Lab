#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = "GATTACA"


# In[4]:


s[0]


# In[5]:


s[6]


# In[10]:


#s[7]  indexerror:out of range

s[-1]


# In[7]:


s[-7]


# In[8]:


s[1:3]


# In[9]:


s[:3]


# In[2]:


s[1:]


# In[3]:


s[:]


# In[4]:


s[::2] #inc 2


# In[7]:


s[::3]


# In[8]:


s[-2:2:-1]


# In[38]:


s = "GATTACA"
s[-1:2:-2]   #-2 inc. slicing start from last -1and end at 2 pos from first


# In[14]:


s[-1:-6]


# In[27]:


s[-7:-1]  #not accessed last element


# In[39]:


#escape

s = "escape double qoute\" here"


# In[40]:


s


# In[41]:


print(s)


# In[42]:


s = "escape backlash\\ here"


# In[46]:


s           #backslah not removed


# In[47]:


print(s)            #backslah removed


# In[50]:


s = "GATTACA"
len(s)


# In[53]:


print("GAT","TACA")


# In[54]:


print("GAT" + "TACA")   #concatenation


# In[56]:


s = "A"*10
s


# In[57]:


'G' in "GATTACA"


# In[58]:


"GAT" in "GATTACA"


# In[59]:


"AGT" in "GATTACA"


# In[60]:


"GATTACA".find("TTA")  #subtring loaction


# In[62]:


"GATTACA".count('T')


# In[1]:


#Converting from/to strings


#"45" + 5  it will get typeError

int("45") + 5


# In[2]:


"45" + str(5)


# In[3]:


int("45"), str(5)


# In[5]:


type((int("45"), str(5)))


# # tuple
# 
# Tuples are used to store multiple items in a single variable.
# 
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# 
# A tuple is a collection which is ordered and unchangeable.
# 
# Tuples are written with round brackets.

# In[7]:


#valueError  int("2.345")

float("2.345")


# In[8]:


#Strings cannot be modified
# They are immutable
# Instead, create a new one


s = "GATTACA"
# it will get type error
# s[3] = "c"

# use this

s = s[:3] + "C" + s[4:]
print(s)


# ## Some methods

# In[9]:


"GATTACA".lower()


# In[10]:


'gattaca'.upper()


# In[11]:


'GATTACA'.replace("T", "U")


# In[12]:


'GATTACA'.replace("AT","**")


# In[14]:


'GATTACA'.startswith("G")


# In[16]:


'GATTACA'.startswith("g")


# In[19]:


#  sequence: ATGTATTGCATATCGT
seq = input("Enter a DNA sequence: ")


# In[20]:


seq.count("A")


# In[21]:


"there are" + str(seq.count("A")) + "thymines"


# In[22]:


print("there are" , (seq.count("A")) , "thymines")


# In[23]:


"ATA" in seq


# In[24]:


# Enter a subsequence to find: GCA
subsq = input("Enter a subsequence to find: ")


# In[25]:


subsq in seq


# In[1]:


#assignment 4
# sq = ATTU*gtc

sq = input("Enter a Sequence: ")

bases = len(sq)
print("It is", len(sq), "long")


# In[4]:


adenine = sq.count("A") + sq.count("a")
thymine = sq.count("T") + sq.count("t")
cytosine = sq.count("C") + sq.count("c")
guanine = sq.count("G") + sq.count("g")
unknown = bases - (adenine + thymine + cytosine + guanine)
print("adenine: ",adenine)
print("thymine: ",thymine)
print("cytosine: ",cytosine)
print("guanine: ",guanine)
print("unknown: ",unknown)


# In[ ]:





# In[ ]:




