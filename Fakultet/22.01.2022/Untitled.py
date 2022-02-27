#!/usr/bin/env python
# coding: utf-8

# In[3]:


def f(n):
    if n > 2:
        return f(n-1) + f(n-2)
    if n <= 2:
        return n + 4
f(6)


# In[4]:


def f(n):
    if n >= 2:
        return f(n-1) * n
    if n == 1:
        return 2
f(5)


# In[5]:


def f(n):
    if n == 0:
        return 0
    if (n > 0) and (n % 3 == 0):
        return f(n/3)
    if n % 3 > 0:
        return (n % 3) + f(n - (n % 3))
for i in range(1000):
    if f(i) == 9:
        print(i, f(i))
        break


# In[6]:


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*(n+1)
f(4)


# In[7]:


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*(n+1)
f(5)


# In[8]:


def f(n):
    if n == 0:
        return 0
    if (n > 0) and (n % 3 == 0):
        return n + f(n-3)
    if n % 3 > 0:
        return n + f(n - (n % 3))
f(22)


# In[9]:


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n-1)*n-2*f(n-2)
f(6)


# In[10]:


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*f(n-1)-f(n-1)*n+2*n
f(4)


# In[11]:


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return f(n-1)*f(n-2)+(n-2)
f(5)


# In[13]:


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2*f(n-1)+1
f(6)

