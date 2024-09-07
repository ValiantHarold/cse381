import pulp as p

LB_Prob = p.LpProblem("Problem", p.LpMinimize)

x = p.LpVariable.dicts("x", ["x1", "x2", "x3"], lowBound=0)
y = p.LpVariable.dicts("y", ["y1", "y2", "y3"], lowBound=0)

LB_Prob += 2 * x["x1"] + 3 * y["y1"] >= 12
LB_Prob += -x["x2"] + y["y2"] <= 3
LB_Prob += x["x3"] >= 4
LB_Prob += y["y3"] <= 3

LB_Prob.setObjective(3 * x["x1"] + 5 * y["y1"])

status = LB_Prob.solve()

print(p.LpStatus[status])

print(p.value(x["x1"]))
print(p.value(x["x2"]))
print(p.value(x["x3"]))