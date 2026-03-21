## Algoritmos de Grafos

### 1. Dijkstra

**Objetivo:** Encontrar el camino más corto desde un único nodo origen hacia todos los demás nodos del grafo.

**Qué optimiza:** La distancia o coste acumulado en una ruta específica entre dos puntos.

**Cuándo usarlo:**
- Cuando necesitas ir del punto **A** al punto **B** por la vía más rápida o económica.
- Casos reales: navegadores GPS, enrutamiento en redes, planificación de rutas de transporte.

**Resultado:** La ruta exacta y su coste mínimo total.

> **Limitación:** No funciona correctamente con aristas de peso negativo.

---

### 2. Kruskal

**Objetivo:** Construir un **Árbol de Recubrimiento Mínimo (MST)** que conecte todos los nodos del grafo.

**Qué optimiza:** El coste total de las conexiones necesarias para mantener todo el sistema comunicado, sin importar la ruta entre dos nodos concretos.

**Cuándo usarlo:**
- Diseño de infraestructuras donde lo prioritario es conectar todo al menor coste posible.
- Casos reales: redes eléctricas, tendido de fibra óptica, sistemas de tuberías.

**Resultado:** El conjunto de aristas más baratas que mantiene el grafo completamente conectado sin formar ciclos.

> **Enfoque:** Ordena todas las aristas por peso y las va añadiendo de menor a mayor, descartando las que formarían un ciclo.

---

### 3. Prim

**Objetivo:** Al igual que Kruskal, construir un **Árbol de Recubrimiento Mínimo (MST)**.

**Qué optimiza:** El coste total de conexión del sistema completo.

**Cuándo usarlo:**
- Mismo objetivo que Kruskal, pero **más eficiente en grafos densos** (donde casi todos los nodos están interconectados).
- Casos reales: diseño de redes de telecomunicaciones, distribución de energía en zonas muy interconectadas.

**Resultado:** Una red construida desde un nodo inicial, expandiéndose siempre hacia el vecino disponible de menor coste hasta cubrir todos los nodos.

> **Enfoque:** Crece de forma local desde un punto de partida, a diferencia de Kruskal que trabaja con el grafo completo desde el inicio.

---

## Comparativa rápida

| Característica | Dijkstra | Kruskal | Prim |
|---|---|---|---|
| **Objetivo** | Camino mínimo | MST | MST |
| **Parte desde** | Un nodo origen | Todas las aristas | Un nodo inicial |
| **Mejor para** | Grafos dispersos | Grafos dispersos | Grafos densos |
| **Pesos negativos** | No soporta | Soporta | Soporta |
| **Caso de uso** | GPS / Rutas | Infraestructuras | Redes densas |