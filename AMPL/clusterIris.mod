set m:= 1..20;
param K:=3;
param N:=20; 
param d {i in m, j in m};
var x {i in m, j in m}binary;

minimize objective_function:  sum{i in m}(sum{j in m} d[i,j]*x[i,j]);

subject to point {i in m}:
sum{j in m} x[i,j]=1;

subject to cluster:
sum{j in m} x[j,j]=K;

subject to one {i in m, j in m}:
x[j,j] >= x[i,j];