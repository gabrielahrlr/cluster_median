# Cluster Median Problem - An Integer Optimization Problem

========================================================================================================================
                                                         Description
========================================================================================================================
Implementation of the cluster-median classification problem using integer programming (in AMPL). This combinatorial 
optimization problem provides an acceptable solution to the cluster-median problem however it is considered as NP-hard 
on general networks and its solution is only viable when the number of points is not very large. Thus, an heuristic
solution using a Spanning Tree is also provided.

========================================================================================================================
                                                         Requirements
========================================================================================================================
For the integer implementation - AMPL (http://ampl.com/)

For the Heuristic Solution using Spanning Trees: 
  - Python 3
  - Numpy
  - Networkx
  - Matplotlib

========================================================================================================================
                                                         Organization 
========================================================================================================================

This program is divided into three main folders:

AMPL: Contains the .dat and .mod files for the integer implementation for random points and for the well-known Iris data.
Examples: Contain data files to test the programs.
Python: Contains two scripts, one for generate random points and other for the spanning tree.
Documentation: Contains the description and further details about implementation and theory.
