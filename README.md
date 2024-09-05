# VRPTW Solver

Este proyecto resuelve el problema de enrutamiento de vehículos con ventanas de tiempo (VRPTW) utilizando varios enfoques. El VRPTW es un problema de optimización donde se deben minimizar el número de vehículos necesarios y la distancia total recorrida, asegurando que cada nodo (cliente) sea visitado exactamente una vez dentro de su ventana de tiempo.

### Archivos Principales

- **aleatorizado.py**: Implementa un algoritmo aleatorizado para resolver el VRPTW.
- **constructivo.py**: Implementa un método constructivo para obtener soluciones iniciales para el VRPTW.
- **cotas_inferiores.py**: Calcula cotas inferiores para el número mínimo de vehículos requeridos.
- **grasp_cardinalidad.py**: Implementa el algoritmo GRASP (Greedy Randomized Adaptive Search Procedure) para optimizar la solución basada en cardinalidad.
- **VRPTW_Miguel_Hoyos_*.xlsx**: Resultados obtenidos de las ejecuciones de los diferentes métodos.
- **VRPTW*.txt**: Archivos de datos que contienen instancias del problema.

## Descripción del Problema

En el problema VRPTW, un conjunto de vehículos homogéneos debe visitar una serie de nodos geográficamente dispersos, respetando las restricciones de capacidad y ventanas de tiempo. Los vehículos deben comenzar y terminar su ruta en un nodo depósito, minimizando la distancia total recorrida.

### Definición del Problema

Dado un conjunto de 𝐾 vehículos de capacidad 𝑄, el VRPTW se define en un grafo 𝐺 = (𝑉; 𝐸), donde 𝑉 es el conjunto de nodos y 𝐸 es el conjunto de arcos. El nodo 0 es el depósito, y cada nodo cliente tiene una demanda 𝑞𝑖, un tiempo de servicio 𝑠𝑖, y una ventana de tiempo [𝑒𝑖; 𝑙𝑖]. Las soluciones deben cumplir con las siguientes restricciones:

1. Cada cliente es visitado exactamente una vez.
2. Los vehículos comienzan y terminan su ruta en el depósito.
3. La demanda total en cada ruta no debe exceder la capacidad 𝑄.
4. El servicio en cada cliente debe comenzar dentro de su ventana de tiempo.

## Instrucciones de Uso

Para ejecutar cada uno de los métodos implementados, simplemente navega hasta la raíz del proyecto y ejecuta el archivo Python correspondiente

## Resultados
Los resultados de las ejecuciones se encuentran en los archivos .xlsx, donde se puede ver el desempeño de cada método para las diferentes instancias del problema.
