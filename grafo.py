import contextily as ctx
import matplotlib.pyplot as plt
import networkx as nx

def graficar(G, gdf):
    gdf_web = gdf.to_crs(epsg=3857)
    pos = {
        row.objectid: (geom.x, geom.y)
        for row, geom in zip(gdf_web.itertuples(), gdf_web.geometry)
    }

    fig, ax = plt.subplots(figsize=(20, 20))
    gdf_web.plot(ax=ax, alpha=0)  # sólo para fijar extents
    
    nx.draw(
        G,
        pos=pos,
        ax=ax,
        with_labels=False,
        node_color="lightblue",
        edge_color="gray",
        node_size=40,
    )

    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
    ax.set_axis_off()
    plt.show()
