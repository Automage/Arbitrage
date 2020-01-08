from graph import Graph
import requests


# Currencies to check
currencies = ['USD', 'CAD', 'AUD', 'EUR']

# Create graph
graph = Graph(len(currencies))

# Perform request to api.exchangeratesapi.io
for base in currencies:
    res = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}")
    rates = res.json()['rates']

    for target in currencies:
        if target == base:
            continue

        graph.add_edge(base, target, rates[target])
        print(f"Added {base}_{target} {rates[target]}")

graph.show()
