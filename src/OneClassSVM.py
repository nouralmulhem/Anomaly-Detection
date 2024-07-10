from sklearn.svm import OneClassSVM
import pandas as pd
import sklearn

def OCSVM(X):
  ocsvm_model = OneClassSVM(nu=0.2, gamma=0.001, kernel='rbf')
  ocsvm_ret = ocsvm_model.fit_predict(X.reshape(-1, 1))
  ocsvm_df = pd.DataFrame()
  ocsvm_df['anomaly']  = [1 if i==-1 else 0 for i in ocsvm_ret]
  return X, ocsvm_df['anomaly'].values