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
    preds = nx.jaccard_coefficient(G, [(row['venue1'], row['venue2'])])
    for u,v,p in preds:
        if p > 0.05:
            predictions.append(1) 
        else:
            predictions.append(0)

dfEdgesToEvaluate['link'] = predictions

# Please pay attention: Kaggle demands that you add "linkID" and "link" column headers
dfEdgesToEvaluate.to_csv("jaccardPrediction.csv", columns=['linkID','link'],index=False)  
