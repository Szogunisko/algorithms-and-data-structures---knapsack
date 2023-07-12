KNAPSACK PROBLEM

Courier has received n parcels ai of weight s(ai) to be delivered to customers. Because of
permissible load capacity of the car, it can take only b kilograms. Every parcel has it own value w(ai) that is independent of weight.

1.
Write a program that supports the work of a courier by selecting packages for delivery in a way that maximizes profit, based on the strategies:

- Dynamic Programming (DP)
- Brute Force (BF)
- Brute Force with elimination of unacceptable solutions (BF2)
- Heuristic methods:
 1st heuristics - random (GH1)
 2nd heuristics - min weight (GH2)
 3rd heuristics - max value (GH3)
 4th heuristics - max value to weight ratio (GH4)

Parcels weight and value are randomly generated from the following ranges
s(ai)∈[10, 1000], w(ai)∈[100, 10 000].


2.
Examine the dependence of calculation time t on the number of parcels n (minimum of 10 measuring points
adapted to the time requirements of BF) for b = 50%Σs(ai).

3.
Examine the dependence of calculation time t on the number of packets n (minimum of 10 measuring points) for the methods
PD, BF1, BF2 and GH4 for b = 25%Σs(ai) and 75%Σs(ai). Methods can be tested independently.

4.
Determine the solution to the problem using PD, GH1, GH2, GH3 and GH4 methods for a minimum of 10
values of n (selected for the duration of the methods) and b = 25%Σs(ai), 50%Σs(ai) and 75%Σs(ai).
Calculate the average error (((xPD-xGHi)/xPD)*100%) made by individual heuristics for different b and n.



Repository contains code required to solve tasks. 
