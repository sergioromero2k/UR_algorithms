from collections import deque

def visitar_nodo(grafo, estado, resultado, nodo_actual):
    estado[nodo_actual] = "VISITED"

    for nodo_vecino in grafo[nodo_actual]:
        if estado[nodo_vecino] == "NOT_VISITED":
            visitar_nodo(grafo, estado, resultado, nodo_vecino)

    estado[nodo_actual] = "FINISHED"
    resultado.appendleft(nodo_actual)

def ordenacion_topologica(grafo):
    estado = dict()
    resultado = deque()

    for nodo in grafo.keys():
        estado[nodo] = "NOT_VISITED"

    for nodo in grafo.keys():
        if estado[nodo] == "NOT_VISITED":
            visitar_nodo(grafo, estado, resultado, nodo)

    print(resultado)

def main() -> None:
    grafo_ropa = {
        "calcetines": ["zapatos"],
        "pantalon": ["zapatos", "cinturon"],
        "camisa": ["cinturon", "jersey"],
        "zapatos": [],
        "cinturon": [],
        "jersey": []
    }

    ordenacion_topologica(grafo_ropa)

if __name__ == "__main__":
    main()
