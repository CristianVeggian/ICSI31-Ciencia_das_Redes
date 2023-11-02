import numpy as np
import pandas as pd
import networkx as nx

dfEdgesToEvaluate = pd.read_csv('edgesToEvaluate.csv')

# IMPLEMENTE AQUI A SUA LÓGICA
# Abrir o grapho
# achar quem são os vizinhos dos edges para avaliar
# para todos os edges no grapho, encontrar o common_vizinhos

G = nx.read_gml("GraphMissingEdges.gml")

predictions = []

for index, row in dfEdgesToEvaluate.iterrows():
    common_vizinhos = nx.common_neighbors(G, row['venue1'], row['venue2'])
    if len(sorted(common_vizinhos)) > 0:
        predictions.append(1) 
    else:
        predictions.append(0)

dfEdgesToEvaluate['link'] = predictions

# Please pay attention: Kaggle demands that you add "linkID" and "link" column headers
dfEdgesToEvaluate.to_csv("vizinhosComuns.csv", columns=['linkID','link'],index=False)  
