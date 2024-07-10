from sklearn.ensemble import IsolationForest
import pandas as pd

def IsoForest(X):
  iforest_model = IsolationForest(n_estimators=300, contamination=0.1, max_samples=700)
  iforest_ret = iforest_model.fit_predict(X.reshape(-1, 1))
  iforest_df = pd.DataFrame()
  iforest_df['anomaly']  = [1 if i==-1 else 0 for i in iforest_ret]
  return X, iforest_df['anomaly'].values