from igraph import Graph
from igraph import summary
from igraph import plot, mean
from igraph import *
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import igraph

karate = Graph.Read_GML("karate.gml")
igraph.plot(karate)
#read edge list from a data file
el = Graph.Read_Ncol('karate.txt', directed=True)

#convert the edgelist to an igraph graph object
g = igraph.Graph.Read_Ncol('karate.txt')
#summary(karate)

#no of vertices
print("No of vertices",karate.vcount())
#no of edges
print("No of edges",karate.ecount())

#plot the graph
igraph.plot(g)

print("Degree of vertices",karate.degree())
print("Mean: " , mean(karate.degree()))
#print("Betweeness: ", karate.edge_betweenness())

#plotly.tools.set_credentials_file(username='pradipti.mcs16.du', api_key='yeBweYgKVZKMkFUfS3G2')
#sorted_list = sorted(karate.degree())


#find cliques
clique=karate.cliques()
#print clique
#largest clique
cliques=karate.maximal_cliques()
#print cliques

#find k-cliques
karate.cliques(min=4, max=4)



#community detection based on edge_betweenness
dendrogram = g.community_edge_betweenness()
clusters = dendrogram.as_clustering()
igraph.plot(clusters)
membership = clusters.membership
print("Modularity based on edge_betweeness",g.modularity(membership,weights=None))

#community detection based on greedy optimization of modularity
g1=g.as_undirected()
dendrogram2 = g1.community_fastgreedy()
clusters2 = dendrogram2.as_clustering()
igraph.plot(clusters2)
membership2 = clusters2.membership
print("Modularity based on greedy optimization",g.modularity(membership2,weights=None))

#community detection based on random walks
dendrogram3=g.community_walktrap()
clusters3 = dendrogram3.as_clustering()
igraph.plot(clusters3)
membership3 = clusters3.membership
print("Modularity based on random walks",g.modularity(membership3,weights=None))

#community detection based on propagating labels
dendrogram4=g.community_label_propagation()
#clusters4 = dendrogram4.as_clustering()
igraph.plot(dendrogram4)
membership4 = dendrogram4.membership
print("Modularity based on propagating labels",g.modularity(membership4,weights=None))