## Graph Algorithms

### 1. Dijkstra

**Objective:** Find the shortest path from a single source node to all other nodes in the graph.

**What it optimizes:** The distance or accumulated cost along a specific route between two points.

**When to use it:**
- When you need to get from point **A** to point **B** via the fastest or cheapest route.
- Real cases: GPS navigation, network routing, transport route planning.

**Result:** The exact path and its minimum total cost.

> **Limitation:** Does not work correctly with negative weight edges.

---

### 2. Kruskal

**Objective:** Build a **Minimum Spanning Tree (MST)** that connects all nodes in the graph.

**What it optimizes:** The total cost of the connections needed to keep the entire system communicating, regardless of the route between two specific nodes.

**When to use it:**
- Infrastructure design where the priority is connecting everything at the lowest possible cost.
- Real cases: electrical grids, fiber optic cabling, pipeline systems.

**Result:** The cheapest set of edges that keeps the graph fully connected without forming cycles.

> **Approach:** Sorts all edges by weight and adds them from lowest to highest, discarding any that would form a cycle.

---

### 3. Prim

**Objective:** Like Kruskal, build a **Minimum Spanning Tree (MST)**.

**What it optimizes:** The total connection cost of the entire system.

**When to use it:**
- Same goal as Kruskal, but **more efficient on dense graphs** (where almost all nodes are interconnected).
- Real cases: telecommunication network design, power distribution in highly interconnected areas.

**Result:** A network built from an initial node, always expanding toward the available neighbor with the lowest cost until all nodes are covered.

> **Approach:** Grows locally from a starting point, unlike Kruskal which works with the entire graph from the beginning.

---

## Quick Comparison

| Feature | Dijkstra | Kruskal | Prim |
|---|---|---|---|
| **Objective** | Shortest path | MST | MST |
| **Starts from** | A source node | All edges | An initial node |
| **Best for** | Sparse graphs | Sparse graphs | Dense graphs |
| **Negative weights** | Not supported | Supported | Supported |
| **Use case** | GPS / Routing | Infrastructure | Dense networks |