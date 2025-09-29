import geo_graph as geog
import calcular_ruta as cr
import grafo as gg

FILE_PATH = "Estaciones_Sistema_Metro_-OD.geojson"

def start_system():
    print("Bienvenido al sistema de rutas del Metro de Medellín")
    print("En unos momentos podras visualizar una representacion grafica del sistema metro.")
    print("Para calcular la ruta mas corta, necesitaras los IDs de las estaciones.\nPara esto necesitaras acceder a este enlace donde encontraras una \nlista con los IDs de las estaciones: https://github.com/josefranco05/Rule-Based-Systems/blob/main/README.md")
    print("Por favor, ingrese las estaciones de origen y destino.")
    
    estacion_origen = input("Estación de origen (ID): ")
    estacion_destino = input("Estación de destino (ID): ")
    
    try:
        estacion_origen = int(estacion_origen)
        estacion_destino = int(estacion_destino)
    except ValueError:
        print("Por favor, ingrese IDs numéricos válidos para las estaciones.")
        return None, None
    
    cr.ruta_mas_corta(geog.create_graph(FILE_PATH), estacion_origen, estacion_destino)
    gg.graficar(geog.create_graph(FILE_PATH), gdf=geog.gpd.read_file(FILE_PATH))
    
    return

if __name__ == "__main__":
    start_system()