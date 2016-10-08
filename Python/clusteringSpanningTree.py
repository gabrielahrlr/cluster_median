"""
Created by Gabriela and Maira on December 2014

Input:
Number of desired clusters

Output:
- Spanning Tree
- Clusters

Pre-conditions:
Numpy, networkx and matplotlib packages have to be installed
File "InputMatrix.txt" should be in the same directory that this program.

"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Number of clusters maximum m, if m is the total of points



#Spanning Tree function
#Input: A matrix of euclidean distances between points
#Output: Spanning tree, edges of the spanning trees, clusters.
def spanning_tree(X,c):
    #Number of vertices
    vertices = X.shape[0]
    #Initlizes the Spanning Tree Graph
    st = nx.Graph()
    #Initilizes theSpanning Tree Edges with its weights
    spanning_edges = []
    #Visited vertices starting with vertex 1
    visited_vertices = [0]
    #First vertex is taking into account
    number_visited = 1
    #Changes the zero of the diagonal for infinite
    diagonal_indices = np.arange(vertices)
    y = X.copy()
    X[diagonal_indices, diagonal_indices] = np.inf

    while number_visited != vertices:
        #Step 1: Obtains the indices for the minimum distance along the visited vertices
        edge = np.argmin(X[visited_vertices], axis=None)
        edge = divmod(edge,vertices)
        edge = [visited_vertices[edge[0]], edge[1]]
        u = edge[0]
        v = edge[1]
        #Step 2: Updates the spanning tree and the visited_vertices set
        edge_st = [u + 1, v + 1, X[u][v]]
        spanning_edges.append(edge_st)
        st.add_edge(u + 1, v + 1, weight=X[u][v])
        visited_vertices.append(v)
        #Step 3: Makes infinite all the distances between the visited vertices
        X[visited_vertices, v] = np.inf
        X[v, visited_vertices] = np.inf
        #Step 4: Increments the accumulator
        number_visited += 1
    
    #Convert the spanning edges to a matrix
    se = np.asmatrix(spanning_edges)
    #Sort the edges according tho their weights (incremental)
    sep = np.sort(se,axis=0)
    #Obtains only the weights
    weights = sep[:, 2]
    n = 0
    #Cluster -1, to remove only c-1 branches if c clusters are desired
    c = c-1
    #Matrix where the branches to be removed will be stored
    t = np.zeros(c)

    while n != c:
        a = max(weights)
        t[n] = a
        weights[weights == a] = 0
        n += 1
    if 0 < c:
        gd = min(t)
        H = st.copy()
        H.remove_edges_from( (u,v) for u,v,d in st.edges_iter(data=True) if d['weight'] >= gd)
    else:
        H = st.copy()

    #get the position of the points
    positions = readPositions()
    #Plot Clusters
    clusters_sum_means = get_min_means(visited_vertices,H,y)
    print('sum median: ',clusters_sum_means)
    plt.figure(1)
    nx.draw_networkx(H,positions)
    plt.show()
    #PlotOriginalSpanningTree :)
    plt.figure(2)
    nx.draw_networkx(st,positions)
    plt.show()

def readPositions():
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    f = open(path+'/DataPoints.txt', 'r')
    content = f.readlines()
    dataPos = {}
    for i in range(len(content)):
        line_content = content[i].replace('\n', '').split(' ')
        line_content[0] = float(line_content[0])
        line_content[1] = float(line_content[1])
        dataPos[i+1] = line_content
    return dataPos

def get_min_means(vertices, g, distances):
    visited_vertices = []
    clustersMeans = {}
    for v in vertices:
        if not (v+1) in visited_vertices:
            cluster = nx.node_connected_component(g,v+1)
            visited_vertices.extend(cluster)
            mean = {}
            dd = {}
            added = False
            for c in cluster:
                d = 0
                for c1 in cluster:
                    d += distances[c-1,c1-1]
                dd[c] = d
            mean = min(dd.values())
            for d in dd:
                if dd[d] == mean and not added:
                    clustersMeans[d] = mean
                    added = True
    total = 0
    for c in clustersMeans:
        total += clustersMeans[c]
    get_min_distance_between_clusters(clustersMeans.keys(),distances)
    return total


def get_min_distance_between_clusters(clusters, distances):
    distance = np.inf
    calculated_distances_nodes = []
    for c in clusters:
        for c1 in clusters:
            if not [c,c1] in calculated_distances_nodes and c != c1:
                distance = min(distances[c-1,c1-1], distance)
                calculated_distances_nodes.append([c,c1])
    print('Min of distance between clusters', distance)

if __name__ == "__main__":
    input3 = input("number of clusters: k = ")
    c = int(input3)

    readPositions()

    #Getting The distances of the points from the Matrix
    X = np.genfromtxt("InputMatrix.txt", delimiter='     ')

    #Check if the number of cluster satisfies the condition
    if c > X.shape[0]:
        print("The number of clusters should be smaller or equal to the number of points."
          " Try Again :) ")
        exit()

    spanning_tree(X,c)