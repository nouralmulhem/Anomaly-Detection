import joblib
import numpy as np 
from scipy.stats import norm
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import load_model


def is_anomaly(error, mean, std, threshold):
    return int(abs(error - mean) > threshold * std)

def anomaly_score(error, dist):
    delta = np.abs(error - dist.mean())
    return dist.cdf(dist.mean() + delta)

def RNN(data):
  model = load_model('src/model/autoencoder_model.h5')
    
  X = data.values.reshape((len(data), 1))
  y = data.values.reshape((len(data), 1))

  X = X[:-1, :]
  y = y[1:, :]

  y_train_pred = model.predict(X)
  y_train_pred.shape

  errors = [mean_absolute_error(y[i, :], y_train_pred[i, :]) for i in range(y_train_pred.shape[0])]

  params = norm.fit(errors)
  dist = norm(loc=params[0], scale=params[1])


  threshold = 2
  anomalies = [is_anomaly(error, dist.mean(), dist.std(), threshold) for error in errors]
  # sum(anomalies)
  
  return X[:, 0, 0].reshape(-1), anomalies
  