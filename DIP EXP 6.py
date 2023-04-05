#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
image1=cv2.imread('icity.jpg')
plt.imshow(image1)


# In[3]:


import cv2
image2 = cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
plt.imshow(image2)


# In[8]:


kernel = np.ones((11,11),np.float32)/121
image3 = cv2.filter2D(image2,-1,kernel)
plt.imshow(image3)


# In[9]:


plt.figure(figsize = (16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image3)
plt.title("BOX FILTER")
plt.axis('off')


# In[10]:


kernel1 = np.array([[8,17,7],[10,64,10],[3,5,4]])/64
image3 = cv2.filter2D(image2,-1,kernel1)
plt.imshow(image3)


# In[26]:


plt.figure(figsize = (16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image3)
plt.title("WEIGHTED AVERAGE FILTER")
plt.axis('off')


# In[11]:


gauss_blur = cv2.GaussianBlur(src=image2, ksize=(11,11),sigmaX=0, sigmaY=0)
plt.imshow(gauss_blur)


# In[30]:


plt.figure(figsize=(16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(gauss_blur)
plt.title("GAUSSIAN BLURRING")
plt.axis('off')


# In[34]:


median = cv2.medianBlur(src=image3,ksize=11)
plt.imshow(median)


# In[37]:


plt.figure(figsize=(16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(median)
plt.title("MEDIAN BLUR")
plt.axis('off')


# In[13]:


kernel2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
laplacian_kernel = cv2.filter2D(image2,-1,kernel2)
plt.imshow(laplacian_kernel)


# In[14]:


plt.figure(figsize=(16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(laplacian_kernel)
plt.title("LAPLACIAN KERNEL")
plt.axis('off')


# In[15]:


laplacian_operator = cv2.Laplacian(image2,cv2.CV_64F)
plt.imshow(laplacian_operator)


# In[16]:


plt.figure(figsize=(16,16))
plt.subplot(1,2,1)
plt.imshow(image2)
plt.title("ORIGINAL IMAGE")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(laplacian_operator)
plt.title("LAPLACIAN OPERATOR")
plt.axis('off')


# In[ ]:




