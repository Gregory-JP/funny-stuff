#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# # Three-Dimensional points and lines

# In[6]:


plt.figure(figsize=(5, 5))
ax = plt.axes(projection='3d')
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x, y, z, 'red')

# data for the three-dimensional scattered points

z = 15 * np.random.random(100)
x = np.sin(z) + 0.1 * np.random.randn(100)
y = np.cos(z) + 0.1 * np.random.randn(100)
ax.scatter3D(x, y, z, c=z, cmap='Greens')
plt.show()


# # Three-Dimensional countor plots

# In[7]:


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


# In[17]:


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)
z = f(x, y)

fig = plt.figure(figsize=(5, 5))
ax = plt.axes(projection='3d')
ax.contour3D(x, y, z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


# 
# # Chessboard

# In[18]:


def chess(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))


# In[20]:


plt.figure(figsize=(5, 5))

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)

X, Y = np.meshgrid(x, y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(z1, cmap='binary_r', interpolation='nearest', extent=extent, alpha=1)

z2 = chess(X, Y)
plt.imshow(z2, alpha=0, interpolation='bilinear', extent=extent)
plt.title('Make your move')
plt.show()


# # Multiple Violin Plots

# In[29]:


import seaborn as sns


# In[30]:


data = sns.load_dataset('tips')


# In[31]:


plt.figure(figsize=(6, 4))
sns.violinplot(x='day', y='total_bill', data=data)
plt.show()


# # Fidget Spinner game

# In[21]:


from turtle import *


# In[23]:


state = {'turn': 0}


# In[24]:


def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    
    dot(120, 'blue')
    back(100)
    right(120)
    update()


# In[25]:


def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spinner()
    ontimer(animate, 20)


# In[26]:


def flick():
    state['turn'] += 10


# In[28]:


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()


# In[ ]:




