# Rule-Based-Systems
Actividad 2 curso Inteligencia Artificial - Corporación Universitaria Iberoamericana

# Modelo de Optimización de Rutas del Metro de Medellín.

El objetivo de este modelo es brindar al usuario una herramienta que le permita seleccionar una estacion de origen y una de destino, y el modelo retornara la ruta mas eficiente para llegar. El modelo esta construido a partir de los datos abiertos del Metro de Medellin, que pueden ser encontrados en el siguiente enlace: https://datosabiertos-metrodemedellin.opendata.arcgis.com/datasets/92c600b0049e43749ef50e4fc0b0064f_1/explore?location=6.231537%2C-75.605779%2C15.59

# Video Demostracion del Modelo

El video de demostracion del modelo se puede encontrar en este enlace: https://youtu.be/CncPC0V_cLQ

# Instrucciones para Utilizar el modelo

Para ejecutar el modelo se deben tener instaladas todas las dependencias, a continuacion se detallan las librerias y los comandos pip para instalarlas:

- NetworkX (pip install networkx)
- geopandas (pip install geopandas)
- matplotlib (pip install matplotlib)
- contextily (pip install contextily)

Una vez tengamos las dependencias instaladas, procedemos a descargar el repositorio en ZIP para ejecutarlo localmente, o se puede clonar este repo de Github ya que es público. El usuario decide cómo ejecutarlo.

Una vez tengamos el repo, solo debemos ejecutar el archivo main.py para ejecutar el modelo.

El modelo le pedira al usuario el ID de las estaciones de origen y destino, a continuacion se detallan los IDs de todas las estaciones del sistema Metro de Medellín:
## Línea 1

| ID | Estación |
|----|----------|
| 99 | Estación Industriales (Línea 1) |
| 54 | Estación Universidad de Medellín (Línea 1) |
| 137 | Estación Universidad de Medellín (Línea 1) |
| 55 | Parada Los Alpes (Línea 1) |
| 105 | Parada Los Alpes (Línea 1) |
| 56 | Parada La Palma (Línea 1) |
| 104 | Parada La Palma (Línea 1) |
| 60 | Parada Parque Belén (Línea 1) |
| 103 | Parada Parque Belén (Línea 1) |
| 61 | Parada Rosales (Línea 1) |
| 102 | Parada Rosales (Línea 1) |
| 62 | Parada Fátima (Línea 1) |
| 101 | Parada Fátima (Línea 1) |
| 63 | Parada Nutibara (Línea 1) |
| 100 | Parada Nutibara (Línea 1) |
| 64 | Parada Plaza Mayor (Línea 1) |
| 98 | Parada Plaza Mayor (Línea 1) |
| 65 | Parada Cisneros (Línea 1) |
| 97 | Parada Cisneros (Línea 1) |
| 66 | Parada Minorista (Línea 1) |
| 96 | Parada Minorista (Línea 1) |
| 67 | Parada Chagualo (Línea 1) |
| 95 | Parada Chagualo (Línea 1) |
| 68 | Parada Ruta N (Línea 1) |
| 94 | Parada Ruta N (Línea 1) |
| 69 | Parada San Pedro (Línea 1) |
| 91 | Parada San Pedro (Línea 1) |
| 70 | Parada Palos Verdes (Línea 1) |
| 90 | Parada Palos Verdes (Línea 1) |
| 71 | Parada Gardel (Línea 1) |
| 89 | Parada Gardel (Línea 1) |
| 72 | Parada Manrique (Línea 1) |
| 88 | Parada Manrique (Línea 1) |
| 73 | Parada Las Esmeraldas (Línea 1) |
| 87 | Parada Las Esmeraldas (Línea 1) |
| 74 | Parada Berlin (Línea 1) |
| 86 | Parada Berlin (Línea 1) |
| 75 | Parada Parque Aranjuez (Línea 1) |
| 135 | Parada Parque Aranjuez (Línea 1) |
| 92 | Estación Hospital (Línea 1) |
| 93 | Estación Hospital (Línea 1) |

## Línea 2

| ID | Estación |
|----|----------|
| 76 | Paradero Barrio Colombia (Línea 2) |
| 77 | Paradero Barrio Colombia (Línea 2) |
| 78 | Parada Perpetuo Socorro (Línea 2) |
| 106 | Parada Perpetuo Socorro (Línea 2) |
| 79 | Parada Barrio Colón (Línea 2) |
| 107 | Parada Barrio Colón (Línea 2) |
| 80 | Parada San José (Línea 2) |
| 108 | Parada San José (Línea 2) |
| 81 | Parada La Playa (Línea 2) |
| 109 | Parada La Playa (Línea 2) |
| 82 | Parada Catedral Metropolitana (Línea 2) |
| 110 | Parada Catedral Metropolitana (Línea 2) |
| 83 | Paradero Prado (Línea 2) |
| 84 | Paradero Prado (Línea 2) |
| 133 | Estación Universidad de Medellín (Línea 2) |
| 138 | Estación Universidad de Medellín (Línea 2) |
| 131 | Parada Los Alpes (Línea 2) |
| 132 | Parada Los Alpes (Línea 2) |
| 129 | Parada La Palma (Línea 2) |
| 130 | Parada La Palma (Línea 2) |
| 127 | Parada Parque Belén (Línea 2) |
| 128 | Parada Parque Belén (Línea 2) |
| 125 | Parada Rosales (Línea 2) |
| 126 | Parada Rosales (Línea 2) |
| 123 | Parada Fátima (Línea 2) |
| 124 | Parada Fátima (Línea 2) |
| 121 | Parada Nutibara (Línea 2) |
| 122 | Parada Nutibara (Línea 2) |
| 85 | Paradero Palos Verdes (Línea 2) |
| 134 | Parada Palos Verdes (Línea 2) |
| 118 | Parada Gardel (Línea 2) |
| 119 | Parada Gardel (Línea 2) |
| 116 | Parada Manrique (Línea 2) |
| 117 | Parada Manrique (Línea 2) |
| 114 | Parada Las Esmeraldas (Línea 2) |
| 115 | Parada Las Esmeraldas (Línea 2) |
| 112 | Parada Berlin (Línea 2) |
| 113 | Parada Berlin (Línea 2) |
| 111 | Parada Parque Aranjuez (Línea 2) |
| 136 | Parada Parque Aranjuez (Línea 2) |
| 120 | Parada Industriales (Línea 2) |

## Línea A

| ID | Estación |
|----|----------|
| 22 | Estación Niquía (Línea A) |
| 7 | Estación Parque Berrío (Línea A) |
| 8 | Estación San Antonio (Línea A) |
| 10 | Estación Alpujarra (Línea A) |
| 11 | Estación Exposiciones (Línea A) |
| 12 | Estación Industriales (Línea A) |
| 13 | Estación Poblado (Línea A) |
| 14 | Estación Aguacatala (Línea A) |
| 23 | Estación Ayurá (Línea A) |
| 24 | Estación Envigado (Línea A) |
| 25 | Estación Itaguí (Línea A) |
| 21 | Estación Bello (Línea A) |
| 26 | Estación Sabaneta (Línea A) |
| 27 | Estación La Estrella (Línea A) |
| 20 | Estación Madera (Línea A) |
| 1 | Estación Acevedo (Línea A) |
| 2 | Estación Tricentenario (Línea A) |
| 3 | Estación Caribe (Línea A) |
| 4 | Estación Universidad (Línea A) |
| 5 | Estación Hospital (Línea A) |
| 6 | Estación Prado (Línea A) |

## Línea B

| ID | Estación |
|----|----------|
| 28 | Estación San Antonio (Línea B) |
| 9 | Estación Cisneros (Línea B) |
| 15 | Estación Suramericana (Línea B) |
| 16 | Estación Estadio (Línea B) |
| 17 | Estación Floresta (Línea B) |
| 18 | Estación Santa Lucia (Línea B) |
| 19 | Estación San Javier (Línea B) |

## Línea H

| ID | Estación |
|----|----------|
| 43 | Estación Oriente (Línea H) |
| 39 | Estación Las Torres (Línea H) |
| 37 | Estación Villa Sierra (Línea H) |

## Línea J

| ID | Estación |
|----|----------|
| 44 | Estación San Javier (Línea J) |
| 33 | Estación Juan XXIII (Línea J) |
| 34 | Estación Vallejuelos (Línea J) |
| 35 | Estación La Aurora (Línea J) |

## Línea K

| ID | Estación |
|----|----------|
| 32 | Estación Andalucía (Línea K) |
| 31 | Estación Popular (Línea K) |
| 30 | Estación Santo Domingo (Línea K) |
| 41 | Estación Acevedo (Línea K) |

## Línea L

| ID | Estación |
|----|----------|
| 40 | Estación Santo Domingo (Línea L) |
| 29 | Estación Arví (Línea L) |

## Línea M

| ID | Estación |
|----|----------|
| 42 | Estación Miraflores (Línea M) |
| 38 | Estación El Pinal (Línea M) |
| 36 | Estación 13 de Noviembre (Línea M) |

## Línea Sin_linea

| ID | Estación |
|----|----------|
| 139 | Parada Caribe Buses CR 64 |
| 154 | Parada Caribe Buses CR 64 |
| 140 | Parada Cementerio Universal |
| 166 | Parada Cementerio Universal CR 65 |
| 141 | Parada Barrio Cordoba Tranversal 78 |
| 142 | Parada Barrio Pilarica CL 73 x CR 72A |
| 143 | Parada Ciudadela Universitaria |
| 144 | Parada Facultad de Minas |
| 145 | Parada Barrio los Colores AV 80 x CL 54 |
| 146 | Parada Barrio Calazans |
| 147 | Parada Integracion Estación Floresta |
| 148 | Parada Barrio Los Pinos |
| 149 | Parada Barrio Laureles |
| 150 | Parada  Santa Gema |
| 151 | Parada Nueva Villa de Aburrá |
| 152 | Parada Integracion La Palma |
| 153 | Parada Integracion La Palma |
| 155 | Parada  Nueva Villa de Aburrá |
| 156 | Parada Barrio Santa Gema |
| 157 | Parada Barrio Laureles |
| 158 | Parada Barrio Los Pinos |
| 159 | Parada Integracion Barrio Floresta |
| 160 | Parada Barrio Calazans |
| 161 | Parada Barrio los colores AV 80 x CL 54 |
| 162 | Parada Facultad de Minas |
| 163 | Parada Ciudadela Universitaria |
| 164 | Parada Barrio Pilarica CL 73 x CR 72A |
| 165 | Parada Barrio Cordoba CR 67 x CL 78A |

## Línea P

| ID | Estación |
|----|----------|
| 59 | Estación Acevedo (Línea P) |
| 167 | Estación Sena-Pedregal (Línea P) |
| 57 | Estación Doce de Octubre (Línea P) |
| 58 | Estación El Progreso (Línea P) |

## Línea T

| ID | Estación |
|----|----------|
| 53 | Estación San Antonio (Línea T) |
| 50 | Estación San José (Línea T) |
| 49 | Estación Pabellón del Agua (Línea T) |
| 46 | Estación Bicentenario (Línea T) |
| 51 | Estación Buenos Aires (Línea T) |
| 52 | Estación Miraflores (Línea T) |
| 47 | Estación Loyola (Línea T) |
| 45 | Estación Alejandro Echavarría (Línea T) |
| 48 | Estación Oriente (Línea T) |
