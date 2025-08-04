# OPTIMIZATION-MODEL

company: CODTECH IT SOLUTIONS

NAME: OM KUMAR

INTERN ID: CT04DH1971

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: Muzammil

DESCRIPTION OF TASK

Optimizing Product Mix with Linear Programming – A Practical Business Application
As part of my internship with CODTECH, Task 4 challenged me to solve a real-world business problem using optimization techniques. I selected a classic product mix optimization scenario that companies often face in manufacturing environments. This project uses Linear Programming (LP) and the PuLP library in Python to determine the best way to allocate limited resources to maximize profit.

Project Objective
The central aim of this project is to help a company determine how many units of two products—Product A and Product B—should be produced in order to maximize overall profit, without exceeding constraints related to available resources like labor and raw material.

Business Scenario
The company manufactures two products:

Product A: Requires 2 units of raw material and 3 hours of labor

Product B: Requires 4 units of raw material and 2 hours of labor

The company has access to:

A maximum of 100 units of raw material

A maximum of 90 hours of labor

Each unit of Product A yields a profit of ₹20, while each unit of Product B yields a profit of ₹30.

Approach and Methodology
To solve this optimization problem, I used Linear Programming—a mathematical method used for decision-making when resources are limited. The LP model includes:

Decision variables: Number of units of Product A and Product B to produce

Objective function: Maximize total profit (20 × A + 30 × B)

Constraints:

2A + 4B ≤ 100 (Material constraint)

3A + 2B ≤ 90 (Labor constraint)

Using the PuLP library, I defined the problem, declared the decision variables, set up the constraints and the objective function, and finally solved the model. PuLP handled all the optimization logic and returned the values for A and B that result in the maximum possible profit under the given constraints.

Results and Output
The program outputs the optimal number of units of each product to manufacture and the maximum profit achievable. I also created a graphical representation of the solution using Matplotlib, which shows the feasible region defined by the constraints and where the optimal solution lies. This visual helps understand how different constraints affect the decision-making process.

Technologies Used
Python: Core programming

PuLP: Linear Programming solver

Matplotlib: For plotting constraint lines and feasible region

NumPy: For numerical operations

What I Learned
This task taught me how linear programming can be used to tackle real business problems efficiently. I learned how to model problems with constraints and objectives, apply mathematical reasoning, and interpret solutions programmatically. It also helped me gain experience with Python libraries used in operations research and analytics.

Future Improvements
Add a Flask-based UI for non-technical users

Extend to multi-product, multi-resource scenarios

Deploy on cloud platforms for business use

#output#

<img width="1600" height="1200" alt="Image" src="https://github.com/user-attachments/assets/f9ace6a8-34fb-4e92-8b80-0234a39e4101" />

