## Introduccion a los Grafos

Un grafo es una estructura matematica que permite representar relaciones complejas entre objetos.
Se define formalmente como $G = (V, E)$, donde:

- **$V$ (Vertices/Nodos):** Representan los elementos del sistema (ciudades, ordenadores, conceptos, personas).
- **$E$ (Aristas/Edges):** Representan las conexiones o relaciones entre esos nodos.

Se define asi porque permite modelar cualquier sistema interconectado de forma abstracta, separando los datos de su estructura de relacion.

---

## Objetivo y Fin de Uso

El objetivo principal es modelar la conectividad. Se utilizan para resolver problemas de rutas, dependencias, flujo de redes y analisis de infraestructuras criticas.

- **Que se busca optimizar?** Generalmente la distancia (camino mas corto), el coste de conexion o el tiempo de ejecucion.
- **Que se busca maximizar?** El flujo de informacion o la robustez de una red ante fallos.

---

## Representacion: Lista de Adyacencia

La Lista de Adyacencia es una forma de almacenar el grafo donde cada nodo tiene una lista de sus vecinos directos.

- **Cuando usarla?** Es ideal para grafos dispersos (donde hay pocas conexiones en comparacion con el numero de nodos), ya que ahorra mucha memoria frente a una matriz.
- **Eficiencia:** Permite iterar rapidamente sobre los vecinos de un nodo, lo que optimiza algoritmos de exploracion como DFS y BFS.

---

## Algoritmos Implementados

En este repositorio encontraras soluciones a problemas especificos basados en:

1. **Exploracion:** Busqueda en profundidad (DFS) y anchura (BFS).
2. **Ordenamiento:** Orden Topologico (Kahn y DFS) para gestion de dependencias.
3. **Analisis de Robustez:** Puntos de Articulacion para identificar fallos criticos en redes.

---

## Ejemplos de Aplicacion

Para entender mejor cuando implementar cada algoritmo, aqui tienes casos practicos basados en los archivos de este repositorio:

### 1. Busqueda de Rutas y Laberintos (`bfs.py` / `dfs.py`)

- **Camino mas corto (BFS):** Si necesitas escapar de un laberinto en el menor numero de pasos posibles, como en el problema de Henry Pitter o Mon Toya.
- **Exploracion completa (DFS):** Si el objetivo es recorrer todas las habitaciones de una mazmorra profundizando hasta el final antes de retroceder, como en Explorando Mazmorras.

### 2. Gestion de Dependencias y Agendas (`topsort.py` / `lexical_tosport.py`)

- **Orden de tareas:** Determinar que conceptos estudiar antes que otros para aprobar una asignatura (Dora Suspendedora).
- **Prioridad Alfabetica:** Si tienes varios comics que puedes leer al mismo tiempo pero quieres elegir siempre el primero en orden alfabetico, el TopSort Lexico es la clave.
- **Restricciones de contrato:** Organizar una agenda de eventos donde algunos son requisitos previos de otros, como en Organiza mi agenda.

### 3. Analisis de Infraestructura y Redes (`art_points.py`)

- **Puntos de fallo criticos:** En una red informatica, identificar que servidores (nodos) son vitales. Si uno de estos nodos cae y deja a la empresa desconectada, se considera un Punto de Articulacion (Caso Hackerman).

### 4. Agrupacion y Comunidad (`dfs.py` / `bfs.py`)

- **Salas de cine:** Dividir a un grupo de personas en salas independientes basandose en sus afinidades y gustos (Marvel vs DC). Aqui buscamos componentes conexas dentro del grafo.

---

## Resumen de Seleccion

| Si buscas... | Usa el algoritmo... |
|---|---|
| El camino mas corto (en saltos) | `bfs.py` |
| Saber si un nodo es vital para la conexion | `art_points.py` |
| Un orden logico de tareas con dependencias | `topsort.py` |
| Ordenar tareas pero priorizando el nombre (A-Z) | `lexical_tosport.py` |
| Explorar todas las posibilidades hasta el fondo | `dfs.py` |