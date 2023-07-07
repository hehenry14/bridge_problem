import networkx as nx
import random

"""
Bridge look like this
  2-3
 /| |\
1-4-5-6
 \| |/
  7-8

"""

SIMULATIONS = 10000000

def simulate():
    # Define the graph
    G = nx.Graph()
    G.add_edges_from(
        [
            (1, 2),
            (1, 4),
            (1, 7),
            (2, 3),
            (2, 4),
            (3, 5),
            (3, 6),
            (4, 5),
            (4, 7),
            (5, 6),
            (5, 8),
            (6, 8),
            (7, 8),
        ]
    )

    # Initialize a counter for the number of times a path remains
    count = 0

    # Run the simulations
    for _ in range(SIMULATIONS):
        # Create a copy of the graph
        H = G.copy()

        # Each bridge has a 50% chance of being destroyed in the storm
        for edge in G.edges():
            if random.random() < 0.5:
                H.remove_edge(*edge)

        # Check if there is still a path from cross the bridge, i.e. from node 1 to node 6
        if nx.has_path(H, 1, 6):
            count += 1

    # Estimate the probability
    return count / SIMULATIONS

if __name__ == "__main__":
    result = simulate()
    print(f"The estimated probability to cross the bridge is {result}")
