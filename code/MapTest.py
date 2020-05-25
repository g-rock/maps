#!/usr/bin/env python
# coding: utf-8

# In[1]:


import osmnx as ox
import matplotlib.pyplot as plt


# In[2]:


# Graph from address
def graph_from_address_wrapper(address, distance=1000, distance_type='bbox', network_type='drive', fig_height=5, node_size=0, color='#999999'):
    g = ox.graph_from_address(
        address=address, 
        distance=distance, 
        distance_type=distance_type, 
        network_type=network_type)
    
    project_and_plot(g, fig_height, node_size)
    
def graph_from_point_wrapper(point, text, distance=1000, distance_type='bbox', network_type='drive', fig_height=5, node_size=0, color=None, save=False):
    g = ox.graph_from_point(
        point,
        distance=distance, 
        distance_type=distance_type, 
        network_type=network_type)
    
    project_and_plot(g, fig_height, node_size, point=point, text=text, color=color, save=save)

def project_and_plot(g, fig_height, node_size, point=None, text='test', color=None, save=False):
    if point: # Don't show plot until point is added to graph
        fig, ax = ox.plot_graph(g, 
            fig_height=fig_height, 
            node_size=node_size, 
            edge_color=color, 
            node_color=color,
            show=False, 
            close=False
           )
        ax.scatter(x=point[1], y=point[0], c=['#00688B'])
        
        if save:
            ox.save_and_show(
                fig=fig,
                ax=ax,
                save=True,
                show=True,
                close=False,
                filename=text,
                file_format='svg',
                dpi=None,
                axis_off=True
            )
        else:
            plt.show()
    else:
        fig, ax = ox.plot_graph(g, fig_height=fig_height, node_size=node_size, edge_color=color, node_color=color)


# ### Define the places we would like to map

# In[13]:


kennett=(39.8513072,-75.7215973) # 122 Davenport Road, Kennett Square PA
charleston=(32.783620, -79.942120) # 94B Smith Street, Charleston SC
durham=(36.005800, -78.897020) #212 W Trinity Avenue, Durham, NC
germantown=(40.034720,-75.179240) #222 west Rittenhouse st Philadelphia 19144


# In[4]:


## Kennett driving network, 2000m bounding box
# graph_from_point_wrapper(
#     point=kennett, 
#     distance=2000,
#     fig_height=10,
#     network_type='walk'
# )


# In[5]:


# # Kennett walking network, 2000m network
# graph_from_point_wrapper(
#     point=kennett, 
#     distance=4000,
#     fig_height=10,
#     network_type='walk',
#     distance_type='network'
# )


# In[6]:


# Charleston driving network, 1 mile
graph_from_point_wrapper(
    point=charleston,
    text='94BSmith',
    distance=2000,
    fig_height=20,
    network_type='drive',
    distance_type='bbox',
    save=True
)


# In[7]:


# # Charleston walking network, 1 mile
# graph_from_address_wrapper(
#     address=charleston,
#     distance=1600,
#     fig_height=10,
#     network_type='walk',
#     distance_type='bbox'
# )


# In[8]:


# # Durham walking network, 1 mile
# graph_from_address_wrapper(
#     address=durham,
#     distance=1600,
#     fig_height=10,
#     network_type='walk',
#     distance_type='network'
# )


# In[9]:


# Germantown walking network, 1 mile
graph_from_point_wrapper(
    point=germantown,
    text='222WestRittenhouse',
    distance=1000,
    fig_height=10,
    network_type='drive',
    distance_type='bbox',
    save=True
)


# In[10]:


# # Germantown walking network, 1 mile
# graph_from_point_wrapper(
#     point=germantown,
#     distance=1000,
#     fig_height=10,
#     network_type='walk',
#     distance_type='bbox'
# )


# In[14]:


# Germantown walking network, 1 mile
graph_from_point_wrapper(
    point=durham,
    text='212WTrinity',
    distance=1000,
    fig_height=10,
    network_type='drive',
    distance_type='bbox',
    save=True
)

