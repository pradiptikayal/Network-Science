import pandas as pd
import numpy as np
from math import sqrt
from pandas import DataFrame
from igraph import Graph, plot
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

distances = np.zeros(shape=(150,150))
reduced_dist = []
quartile = 0
df = pd.read_csv("iris.csv")
sepal_length = np.array(df['Sepal Length'])
sepal_width = np.array(df['Sepal Width'])
petal_length = np.array(df['Petal Length'])
petal_width = np.array(df['Petal Width'])

def distance():
    
    for i in range( 98 ):
        for k in range( i+1, 99 ):
            dist = sqrt(pow(sepal_length[i] - sepal_length[k], 2) + pow(sepal_width[i] - sepal_width[k], 2) + \
                                pow(petal_length[i] - petal_length[k], 2) + pow(petal_width[i] - petal_width[k], 2))
            distances[i][k] =  dist
    
    print('Euclidean distance matrix')        
    print DataFrame(distances.tolist())
    
    return distances

def findquartile():
    euc_dist = distance()
    temp_dist = euc_dist.flatten()
    j=0
    for i in temp_dist:
            if(i!=0):
                reduced_dist.insert(j, i)
                j +=1
            
            
    quartile = np.percentile(reduced_dist,25)
    print('First Quartile of the iris data set is')
    print(quartile)
    return quartile
    
def cuttOffEdge(edge_weight, threshold):
    
    if(edge_weight >= threshold):
        return True

def createGraph():
    threshold = findquartile()
    
    g = Graph()
    g.add_vertices(99)
    for src, i in enumerate(distances.tolist()):
        for dest, j in enumerate(i):
            if(cuttOffEdge(j, threshold)):
                g.add_edge(src, dest)
    
    #print g
    print('Radius of the generated graph is ')
    print(g.radius(mode="ALL"))
    print('Diameter of the generated graph is')
    print(g.diameter(directed=False, unconn=False, weights=None))
    plot(g.degree_distribution(1))

def createBoxPlot():
    plotly.tools.set_credentials_file(username='pradipti.mcs16.du', api_key='yeBweYgKVZKMkFUfS3G2')

    x = []
    for _ in range(33):
        x.append('setosa')
    for _ in range(33,68):
        x.append('versicolor')
    for _ in range(68,99):
        x.append('virginica')    
    
    
    trace0 = go.Box(
        y=sepal_length,
        x=x,
        name='Sepal length',
        marker=dict(
            color='#F430DF'
        )
    )
    trace1 = go.Box(
        y=sepal_width,
        x=x,
        name='Sepal width',
        marker=dict(
            color='#85C1E9'
        )
    )
    trace2 = go.Box(
        y=petal_length,
        x=x,
        name='Petal length',
        marker=dict(
            color='#E74C3C'
        )
    )
    trace3 = go.Box(
        y=petal_width,
        x=x,
        name='Petal width',
        marker=dict(
            color='#45B39D'
        )
    )
    data = [trace0, trace1, trace2, trace3]
    layout = go.Layout(
        yaxis=dict(
            title='Class wise boxplot',
            zeroline=False
        ),
        boxmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)
    print('Box plot successfully created. Go check plot.ly!')
    
    
createGraph()
createBoxPlot()