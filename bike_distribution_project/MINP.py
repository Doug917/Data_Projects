import pulp as p # type: ignore
import pandas as pd # type: ignore

Distribution = p.LpProblem('Distribution', p.LpMinimize)

#Create problem variables.

possibleTrips = [tuple(c) for c in p.permutation(range(1,196), 2)]

X = p.LpVariable.dicts(
    "X", possibleTrips, lowBound=0, upBound = None, cat=p.LpInteger
)

#Objective function
Distribution += p.lpSum([X[Trip] for Trip in possibleTrips])

df = pd.read_csv('station_net_flux.csv')
initialData = df['net_flux'].to_list()

#Constraints

#Flux

for i in range(1,196):
    Distribution += initialData[i-1] + p.lpSum(X[T] for T in possibleTrips if T[1]==i and T[0] != i) \
                    - p.lpSum(X[T] for T in possibleTrips if T[0] == i and T[1] != i) >= -10
    Distribution += initialData[i-1] + p.lpSum(X[T] for T in possibleTrips if T[1]==i and T[0] != i) \
                    - p.lpSum(X[T] for T in possibleTrips if T[0] == i and T[1] != i) <= 10


Distribution.solve()
Distribution.writeLP("DistributionModel.lp")

for v in Distribution.variables():
    if v.varValue != 0:
        print(v.name, "=", v.varValue)

#Show final result after trips completed.



