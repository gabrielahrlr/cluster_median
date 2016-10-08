set m:= 1..22;
param k:=2;
param d {i in m, j in m};
var x {i in m, j in m} binary;

#objective function: minimize the distance of all points to their cluster medians
minimize objective_function: sum{i in m}(sum{j in m} d[i,j]*x[i,j]);

#Every point must belong to one cluster
subject to point {i in m}:
sum{j in m} x[i,j]=1;

#Exactly k clusters
subject to cluster:
sum{j in m} x[j,j]=k;

#A point may belong to a cluster only if it exists
subject to one {i in m, j in m}:
x[j,j] >= x[i,j];
