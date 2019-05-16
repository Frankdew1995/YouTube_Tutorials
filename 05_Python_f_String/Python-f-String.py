
# coding: utf-8

# # Python-f-String Tutorial  and why you should start using it

# ### 1. Old school %s String Formatting
# ### 2. A better string method String: str.format()
# ### 3. f "string" method - why it's the best for String formatting in Python compared to .format() and %s

# In[1]:


name = "Frank"
age = 24
profession = "Python Dev"
language = "Python"


# ## 1. old-school % string  formatting

# In[2]:



"My name is %s and I'm a %s. I'm currently being %s and my favourite language is %s" % (
 name, profession, age, language )

