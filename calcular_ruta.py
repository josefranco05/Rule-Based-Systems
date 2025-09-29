import networkx as nx


def ruta_mas_corta(G, origen, destino):
    try:
        if origen not in G.nodes or destino not in G.nodes:
            print("Una o ambas estaciones no existen en el grafo.")
            return None

        ruta = nx.shortest_path(G, source=origen, target=destino, weight="weight")
        distancia = nx.shortest_path_length(G, source=origen, target=destino, weight="weight")

        nombre_origen = G.nodes[origen].get("name", str(origen))
        nombre_destino = G.nodes[destino].get("name", str(destino))
        print(f"\nRuta mas corta entre {nombre_origen} y {nombre_destino}:")

        for paso in ruta:
            datos = G.nodes[paso]
            nombre = datos.get("name", str(paso))
            linea = datos.get("linea", "?")
            print(f"  -> {nombre} (Linea {linea})")

        print(f"\nDistancia aproximada: {distancia:.0f} metros ({distancia/1000:.2f} km)")
        return ruta

    except nx.NetworkXNoPath:
        print("No hay ruta entre esas estaciones.")
        return None
