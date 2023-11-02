import networkx as nx
import pandas as pd

#Network to evaluate links
GMissingEdges = nx.read_gml("GraphMissingEdges.gml")

#Links to be evaluated
dfEdgesToEvaluate = pd.read_csv('edgesToEvaluate.csv')

listInference = []

for idx, row in dfEdgesToEvaluate.iterrows( ):
    venue1 = row['venue1']
    venue2 = row['venue2']
    cate1 = GMissingEdges.nodes[venue1]['categories']

    cate2 = GMissingEdges.nodes[venue2]['categories']

    setCate1 = set(cate1.split(','))
    setCate2 = set(cate2.split(','))

    value = len(setCate1.intersection(setCate2))

    if value >=2:
        listInference.append(1)
    else:
        listInference.append(0)

dfEdgesToEvaluate['link'] = listInference

dfEdgesToEvaluate.to_csv("baselineCategories.csv", columns=['linkID','link'],index=False)
