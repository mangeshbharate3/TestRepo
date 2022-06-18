import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="Stream_Mangesh", # Replace with your username

    version="1.0.0",

    author="MangeshBharate",

    author_email="mangesh.bharate@gmail.co,",

    description="Sample Package - Mangesh Decription here",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/authorname/templatepackage",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
#!/usr/bin/env python
# coding: utf-8

# In[1]:


#---------------------------------------------------------------------------------------------------


# # Simple Linear Regression - Part 3 - Prediction on Unseen Data
# 

# In[ ]:


#---------------------------------------------------------------------------------------------------


# ### Load Simple_Linear_Regression_Model

# In[4]:


from pickle import load
filename = 'Simple_Linear_Regression_Model.sav'
 
# load the model from disk
classifier = load(open(filename, 'rb'))


# In[5]:


#---------------------------------------------------------------------------------------------------


# #### Prediction on Unseen data

# In[10]:


#import numpy as np

#Unseen_Data = np.array([40,50,60]).reshape(-1, 1)
#Unseen_Data


# In[11]:

def Predict_Mangesh(Unseen_Data):
    y_pred = classifier.predict(Unseen_Data)
    #print("Predicted values:")
    #print(y_pred)
    return y_pred


# In[ ]:


#---------------------------------------------------------------------------------------------------

