import osmnx as ox
import matplotlib.pyplot as plt

# Take various graph_from_point arguments, create a graph from a lat/lon point, then plot
def graph_from_point_wrapper(point, text="test", distance=1000, distance_type='bbox', network_type='drive', fig_height=5, node_size=0, color=None, save=False):
  g = ox.graph_from_point(
    point,
    distance=distance, 
    distance_type=distance_type, 
    network_type=network_type)
  
  plot(g, fig_height, node_size, point=point, text=text, color=color, save=save)

# Plot the graph
def plot(g, fig_height, node_size, point, text, color, save):
  # Don't show plot until point is added to graph
  if point:
    fig, ax = ox.plot_graph(g, 
      fig_height=fig_height, 
      node_size=node_size, 
      edge_color=color, 
      node_color=color,
      show=False, 
      close=False
      )
    ax.scatter(x=point[1], y=point[0], c=[color])
    
    if save:
      ox.save_and_show(
        fig=fig,
        ax=ax,
        save=True,
        show=False,
        close=False,
        filename=text,
        file_format='jpg',
        dpi=None,
        axis_off=True)
    else:
      return plt
  else:
    fig, ax = ox.plot_graph(g, fig_height=fig_height, node_size=node_size, edge_color=color, node_color=color)
