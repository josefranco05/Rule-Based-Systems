import geopandas as gpd
import networkx as nx
import graficar_grafo as gg

def create_graph(file_path):
    
    gdf = gpd.read_file(file_path).sort_values(by=["linea", "estacion"])
    
    # Proyectamos las coordenadas a un sistema métrico estandar en Colombia
    gdf = gdf.to_crs(epsg=3116)   # ahora las coords estarán en metros

    # Creamos un grafo vacio
    G = nx.Graph()
    
    # Agregamos los nodos (estaciones) al grafo
    for row in gdf.itertuples(index=False):
        id_Estacion = row.objectid
        nombre_Estacion = row.label
        coords = (row.geometry.x, row.geometry.y)
        G.add_node(id_Estacion, name=nombre_Estacion, linea=row.linea, pos=coords)
    
    # Contectamos las estaciones consecutivas en el grafo
    for linea, grupo in gdf.groupby("linea"):
        grupo_ordenado = grupo.sort_values("estacion")
        prev_id, prev_coords = None, None
        
        for idx, row in grupo_ordenado.iterrows():
            id_Estacion = row.objectid
            coords = (row.geometry.x, row.geometry.y)
            
            if prev_id is not None:
                dist = ((coords[0] - prev_coords[0])**2 + (coords[1] - prev_coords[1])**2) ** 0.5
                G.add_edge(prev_id, id_Estacion, weight=dist)
            
            prev_id, prev_coords = id_Estacion, coords
    
    print(f"Grafo construido con {G.number_of_nodes()} estaciones y {G.number_of_edges()} conexiones.")
#    gg.graficar(G, gdf)
    
    return G
