#!/usr/bin/env python
# coding: utf-8

# ## 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.    * ,       'hello'     , -87.8    , -  ,   /  ,      .      , 6
#     

# ### Answer  
#  values: 'hello' , -87.8, 6      
# expression: * , -, / , . 
# 

# ## 2. What is the difference between string and variable?
# 

# ### Answer:
# 1. String is a immutable data type. that is value of string can not be changed.
# 2. variable stores value for different data type.Value of variable can be changed or not depend on variable type.

# ## 3. Describe three different data types.
# 

# ### Answer:
# 1. String e.g. "Nikita",'Life'
# 2. Float  e.g. 12.5 , 34.6
# 3. Integer  e.g. 128,4567
# 4. complex e.g.2+4j, 1-5j

# ## 4. What is an expression made up of? What do all expressions do?
# 

# ## Answer:
# 1. Expression is a combination of values, variables , operators and calls to functions.
# 2.Expressions evaluate to something. also it can print result.Interpreter evaluates expression and displays the result.Evaluation of an expression produces a value.thats why expression can appear on right hand side of assignment statement.
# example of expression:
# print('hello')
# print(len('hello'))

# ## 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 

# ### Answer:
# Statement is instructions given to python interpretor like if statement , for loop statement, def statement which is used to define function, etc. statement dont evaluate to something and also cannot print the result.                     
# Expressions evaluate to something. also it can print result. Function calls are expressions.
# spam=10 this is assignment statement (assignment statement do not return a value. they are simply executed.) 
# print(spam) - this is expression

# ## 6. After running the following code, what does the variable bacon contain?
# bacon = 22         
# bacon + 1
# 

# In[1]:


bacon = 22 
bacon + 1  #bacon=bacon+1


# In[6]:


# as shown above bacon will contain 23


# ## 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'         
# 'spam' * 3
# 

# In[7]:


'spam' + 'spamspam'  #Concanate string


# In[9]:


'spam' * 3 #it will concanate string 3 times


# ## 8. Why is eggs a valid variable name while 100 is invalid?
# 

# ## Answer:
# if variable name starts with any alphabet then that is valid. thus eggs is a valid variable name.
# if variable name starts with numeric value then it is not valid. thus 100 is not a valid variable name.

# ## 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# 

# ### Answer:
# 1. int() is used to get integer version of value
# 2. float() is used to get float version of value
# 3. str() is used to get string version of value

# ## 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'

# In[10]:


'I have eaten ' + 99 + ' burritos.'


# ### Answer
# as 99 is int and we cannot concanate integer number to string hence it is giving error. to remove this error we will need to convert integer number into string by using str(99) instead of 99 

# In[11]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




