from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="product_mix", sense=LpMaximize)

x = LpVariable(name="Product_A", lowBound=0, cat="Integer")
y = LpVariable(name="Product_B", lowBound=0, cat="Integer")

model += 20 * x + 30 * y, "Total_Profit"

model += 2 * x + 4 * y <= 100, "Material_Constraint"
model += 3 * x + 2 * y <= 90, "Labor_Constraint"

model.solve()

print(f"Optimal units of Product A to produce: {x.value()}")
print(f"Optimal units of Product B to produce: {y.value()}")
print(f"Maximum Profit: ₹{model.objective.value()}")
