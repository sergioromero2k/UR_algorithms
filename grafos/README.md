## Introduction to Graphs

A graph is a mathematical structure that allows complex relationships between objects to be represented.
It is formally defined as $G = (V, E)$, where:

- **$V$ (Vertices/Nodes):** Represent the elements of the system (cities, computers, concepts, people).
- **$E$ (Edges):** Represent the connections or relationships between those nodes.

It is defined this way because it allows any interconnected system to be modeled abstractly, separating the data from its relational structure.

---

## Objective and Purpose

The main objective is to model connectivity. Graphs are used to solve problems related to routing, dependencies, network flow and critical infrastructure analysis.

- **What is being optimized?** Generally the distance (shortest path), the connection cost or the execution time.
- **What is being maximized?** The flow of information or the robustness of a network against failures.

---

## Representation: Adjacency List

The Adjacency List is a way of storing the graph where each node holds a list of its direct neighbors.

- **When to use it?** It is ideal for sparse graphs (where there are few connections relative to the number of nodes), as it saves a lot of memory compared to a matrix.
- **Efficiency:** It allows fast iteration over a node's neighbors, which optimizes exploration algorithms like DFS and BFS.

---

## Implemented Algorithms

In this repository you will find solutions to specific problems based on:

1. **Exploration:** Depth-First Search (DFS) and Breadth-First Search (BFS).
2. **Ordering:** Topological Sort (Kahn and DFS) for dependency management.
3. **Robustness Analysis:** Articulation Points to identify critical failures in networks.

---

## Application Examples

To better understand when to implement each algorithm, here are practical cases based on the files in this repository:

### 1. Route Search and Mazes (`bfs.py` / `dfs.py`)

- **Shortest path (BFS):** When you need to escape a maze in the fewest steps possible, as in the Henry Pitter or Mon Toya problems.
- **Full exploration (DFS):** When the goal is to visit every room in a dungeon, going as deep as possible before backtracking, as in Exploring Dungeons.

### 2. Dependency and Schedule Management (`topsort.py` / `lexical_tosport.py`)

- **Task ordering:** Determining which concepts to study before others in order to pass a subject (Dora Suspendedora).
- **Alphabetical priority:** If you have several comics you could read at the same time but always want to pick the first one alphabetically, Lexical TopSort is the key.
- **Contract constraints:** Organizing an event schedule where some events are prerequisites of others, as in Organize my Agenda.

### 3. Infrastructure and Network Analysis (`art_points.py`)

- **Critical failure points:** In a computer network, identifying which servers (nodes) are vital. If one of these nodes goes down and leaves the company disconnected, it is considered an Articulation Point (Hackerman Case).

### 4. Grouping and Community Detection (`dfs.py` / `bfs.py`)

- **Cinema rooms:** Splitting a group of people into independent rooms based on their affinities and preferences (Marvel vs DC). Here we look for connected components within the graph.

---

## Selection Summary

| If you need to... | Use the algorithm... |
|---|---|
| Find the shortest path (by hops) | `bfs.py` |
| Know if a node is vital for connectivity | `art_points.py` |
| Get a logical order of tasks with dependencies | `topsort.py` |
| Order tasks while prioritizing by name (A-Z) | `lexical_tosport.py` |
| Explore all possibilities to the deepest level | `dfs.py` |