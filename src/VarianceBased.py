import pandas as pd

def VarianceBased(X):
  sigma_df = pd.DataFrame()
  sigma_df['value'] = X
  std = sigma_df['value'].std()
  mean = X.mean()
  sigma_df['anomaly_threshold_3r'] = mean + 1.5*std
  sigma_df['anomaly_threshold_3l'] = mean - 1.5*std
  sigma_df['anomaly']  = sigma_df.apply(lambda x : 1 if (x['value'] > x['anomaly_threshold_3r']) or (x['value'] < x['anomaly_threshold_3l']) else 0, axis=1)
  return X, sigma_df['anomaly'].values