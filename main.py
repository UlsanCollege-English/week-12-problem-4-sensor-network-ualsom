import heapq

def prim_mst(graph, start):
    """
    Build a Minimum Spanning Tree (MST) using Prim's algorithm.
    Deterministic selection: tie-breaking by node names.
    """

    visited = set([start])
    mst_edges = []
    total_cost = 0
    edge_heap = []

    # Push all edges from start node
    for neighbor, weight in graph[start]:
        heapq.heappush(edge_heap, (weight, start, neighbor))

    while edge_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edge_heap)

        if v in visited:
            continue

        visited.add(v)
        # Order nodes deterministically
        mst_edges.append((u, v, weight))
        total_cost += weight

        for neighbor, w in graph[v]:
            if neighbor not in visited:
                # Ensure deterministic ordering
                heapq.heappush(edge_heap, (w, v, neighbor))

    return mst_edges, total_cost


if __name__ == "__main__":
    sample_graph = {
        "A": [("B", 3), ("C", 1), ("D", 4)],
        "B": [("A", 3), ("C", 2), ("D", 5)],
        "C": [("A", 1), ("B", 2), ("D", 1)],
        "D": [("A", 4), ("B", 5), ("C", 1)],
    }

    edges, cost = prim_mst(sample_graph, "A")
    print("MST edges:", edges)
    print("Total cost:", cost)
