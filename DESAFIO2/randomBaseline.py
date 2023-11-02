import numpy as np

dfEdgesToEvaluate = pd.read_csv('edgesToEvaluate.csv')

random_predictions = np.random.choice([0, 1], size=dfEdgesToEvaluate.shape[0])

dfEdgesToEvaluate['link'] = random_predictions

# Please pay attention: Kaggle demands that you add "linkID" and "link" column headers
dfEdgesToEvaluate.to_csv("randomTeste.csv", columns=['linkID','link'],index=False)  
