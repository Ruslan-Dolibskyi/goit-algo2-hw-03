import networkx as nx
from prettytable import PrettyTable

# Створення графа
graph = nx.DiGraph()

# Додавання ребер із пропускною здатністю
edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

graph.add_weighted_edges_from(edges, weight="capacity")

# Оновлений пошук потоку між усіма терміналами та магазинами
sources = ["Термінал 1", "Термінал 2"]
targets = [f"Магазин {i}" for i in range(1, 15)]

total_flow = 0
results = []

for source in sources:
    for target in targets:
        flow_value, flow_dict = nx.maximum_flow(graph, source, target)
        if flow_value > 0:
            results.append((source, target, flow_value))
            total_flow += flow_value

# Виведення загального максимального потоку
print("Загальний максимальний потік:", total_flow)

# Таблиця з результатами
table = PrettyTable()
table.field_names = ["Термінал", "Магазин", "Потік (одиниць)"]
for source, target, flow in results:
    table.add_row([source, target, flow])

print("\nТаблиця потоків:")
print(table)

# Аналіз потоку
print("\nАналіз потоку:")
for source, target, flow in results:
    print(f"{source} до {target} постачає {flow} одиниць товару.")
