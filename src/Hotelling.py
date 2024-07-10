import pandas as pd
import scipy.stats as stats

def Hotelling(X):
  hotelling_df = pd.DataFrame()
  mean = X.mean()
  std = X.std()
  hotelling_df['anomaly_score'] = [((x - mean)/std) ** 2 for x in X]
  hotelling_df['anomaly_threshold'] = stats.chi2.ppf(q=0.95, df=1)
  hotelling_df['anomaly']  = hotelling_df.apply(lambda x : 1 if x['anomaly_score'] > x['anomaly_threshold'] else 0, axis=1)
  return X, hotelling_df['anomaly'].values