# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:38:07 2023

@author: santi
"""

import pyomo.environ as pyo

#SETS
C = ['Small','Large']
R = ['Plastic','Machine','Painting']
T = [1,2,3,4]

#T2 is for inventory
T2 = [0,1,2,3,4]

#PARAMETERS
#di,t = demand of cans of type i in month t for i ∈ C, t ∈ T
d = {('Small',1):2500,('Large',1):3000,('Small',2):4000,('Large',2):4500,('Small',3):4000,('Large',3):3000,
     ('Small',4):4000,('Large',4):4000}

#ci = cost of can i for i ∈ C
c = {'Small':10,'Large':15}

#si = storage cost of can i for i ∈ C
s = {'Small':1,'Large':2}

#ai = inventory space of can i for i ∈ C
a = {'Small':3,'Large':6}

#rk,i = amount of resource k needed for can i for i ∈ C, k ∈ R
r = {('Plastic','Small'):3,('Plastic','Large'):5,('Machine','Small'):.08,('Machine','Large'):.1,
      ('Painting','Small'):.04,('Painting','Large'):.05}

#bk = amount of resource k available for k ∈ R
b = {'Plastic':30000,'Machine':650,'Painting':350}

#A = total inventory space available
A = 10000

#ADD THE MODEL CODE, TO CREATE MODEL
model = pyo.ConcreteModel()

#This gives Non-Negativity and CREATES THE VARIABLES
model.x = pyo.Var(C,T, domain = pyo.NonNegativeReals)
model.y = pyo.Var(C,T2, domain = pyo.NonNegativeReals)

#OBJECTIVE 
#Sum two stuff 
#min 
def obj_rule(model):
    return sum(c[i] * model.x[i,t] + s[i] * model.y[i,t] for i in C for t in T)
model.obj = pyo.Objective(rule=obj_rule,sense=pyo.minimize)

#CONSTRAINTS
#s.t. Ii,t−1 + xi,t − di,t = Ii,t for i ∈ C, t ∈ T (Inventory Balance)
def InvBal_rule(model,i,t):
    return model.y[i,t] == model.y[i,t-1] + model.x[i,t] - d[i,t]
model.InvBal = pyo.Constraint (C,T,rule = InvBal_rule)

#aiIi,t ≤ A for t ∈ T
def InvSpace_rule (model,t):
    return sum(a[i]*model.y[i,t] for i in C) <= A
model.InvSpace = pyo.Constraint(T, rule = InvSpace_rule)

#rk,ixi,t ≤ bk for t ∈ T, k ∈ R (Resource Constraints)
def ResCons_rule (model,t,k):
    return sum(r[k,i]*model.x[i,t] for i in C) <= b[k]
model.ResCons = pyo.Constraint(T,R, rule = ResCons_rule)

#Il,0 = 75 (Initial inventory)
def InInvL_rule(model):
    return model.y['Large',0] == 75
model.InInvL = pyo.Constraint(rule = InInvL_rule)

#Is,0 = 50 (Initial inventory)
def InInvS_rule(model):
    return model.y['Small',0] == 50
model.InInvS = pyo.Constraint(rule = InInvS_rule)

#Now SOLUTION
#Solve for model
result = pyo.SolverFactory("glpk").solve(model)

#If result part
if result.solver.termination_condition == pyo.TerminationCondition.optimal:
    print(f"Optimal value: {pyo.value(model.obj)}")
    print("Optimal Solution: ")
    for i in C:
        for t in T:
            print(f"x[{i,t}] = {pyo.value(model.x[i,t])}")
    
    for i in C:
        for t in T2:
            print(f"I[{i,t}] = {pyo.value(model.y[i,t])}")