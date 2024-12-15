from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus

# Define supply points and demand points
suppliers = ['A1', 'A2', 'A3', 'A4']
customers = ['B1', 'B2', 'B3', 'B4', 'B5']

# Supply amounts
supply = {
    'A1': 150,
    'A2': 50,
    'A3': 100,
    'A4': 100
}

# Demand amounts
demand = {
    'B1': 50,
    'B2': 150,
    'B3': 50,
    'B4': 100,
    'B5': 50
}

# Cost matrix
costs = {
    ('A1', 'B1'): 3, ('A1', 'B2'): 3, ('A1', 'B3'): 5, ('A1', 'B4'): 3, ('A1', 'B5'): 3,
    ('A2', 'B1'): 7, ('A2', 'B2'): 3, ('A2', 'B3'): 6, ('A2', 'B4'): 1, ('A2', 'B5'): 3,
    ('A3', 'B1'): 2, ('A3', 'B2'): 8, ('A3', 'B3'): 7, ('A3', 'B4'): 2, ('A3', 'B5'): 9,
    ('A4', 'B1'): 1, ('A4', 'B2'): 3, ('A4', 'B3'): 9, ('A4', 'B4'): 6, ('A4', 'B5'): 4
}

# Create the minimization problem
prob = LpProblem("Transportation_Problem", LpMinimize)

# Decision variables: x[supplier][customer]
x = LpVariable.dicts("Shipments", [(s, c) for s in suppliers for c in customers], lowBound=0, cat='Continuous')

# Objective function: minimize total transportation cost
prob += lpSum([costs[(s, c)] * x[(s, c)] for s in suppliers for c in customers]), "Total_Cost"

# Supply constraints
for s in suppliers:
    prob += lpSum([x[(s, c)] for c in customers]) <= supply[s], f"Supply_{s}"

# Demand constraints
for c in customers:
    prob += lpSum([x[(s, c)] for s in suppliers]) >= demand[c], f"Demand_{c}"

# Solve the problem
prob.solve()

# Check the status of the solution
print("Status:", LpStatus[prob.status])

# Print the optimal shipment amounts and total cost
print("Optimal Shipments:")
for s in suppliers:
    for c in customers:
        if x[(s, c)].varValue > 0:
            print(f"{s} -> {c}: {x[(s, c)].varValue}")

print(f"\nTotal Minimum Cost: {prob.objective.value()}")
