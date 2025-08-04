# OPTIMIZATION-MODEL

Task 4 – Business Optimization using Linear Programming

This project solves a product mix problem using Linear Programming and the PuLP library in Python.

Problem Statement:
A business produces two products:
- Product A: Uses 2 units of material and 3 hours of labor
- Product B: Uses 4 units of material and 2 hours of labor

Available resources:
- Max 100 units of material
- Max 90 hours of labor

Objective:
Maximize total profit:
- ₹20 profit per unit of Product A
- ₹30 profit per unit of Product B

Constraints:
1. 2A + 4B ≤ 100 (Material constraint)
2. 3A + 2B ≤ 90 (Labor constraint)

Solution:
Using PuLP, we find the number of units of each product that should be produced to achieve the highest possible profit without exceeding resource limits.

Output:
The Python script will output the optimal units to produce and the total maximum profit.

Technologies Used:
- Python
- PuLP (Linear Programming Solver)
- Matplotlib (for visualization)


