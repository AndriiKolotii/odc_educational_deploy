#!/usr/bin/env python
# coding: utf-8

# In[16]:


import datacube
dc = datacube.Datacube(app='Sentinel_2')


# In[18]:


lat, lon = 49, 30
buffer = 0.25

query = {
 'time': ('2021-06', '2021-07'),
    'x': (lon - buffer, lon + buffer),
    'y': (lat + buffer, lat - buffer),
    'output_crs': 'epsg:6933',
    'resolution':(-20,20),
}


# In[19]:


ds = dc.load(product='s2_l2a', dask_chunks={},**query)
print(ds)


# In[20]:


bands = ['green', 'blue', 'red']
ds = dc.load(product='s2_l2a', measurements=bands, dask_chunks={},**query)
print(ds)


# In[21]:


print(ds.green.time)


# In[22]:


first_timestep = ds.green.sel(time='2021-06-24')
print(first_timestep)


# In[23]:


first_timestep.plot(figsize = (16,11), robust=True)


# In[24]:


ds.green.plot(col="time", robust=True)


# In[ ]:




