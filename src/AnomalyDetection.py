import argparse

from utils import *
from Hotelling import Hotelling
from OneClassSVM import OCSVM
from VarianceBased import VarianceBased
from IsolationForest import IsoForest
from RNN import RNN

df = create_time_series(start_date='1/1/2020', end_date='05/01/2021', num_periods=1000)
# df.plot()

def run(X, algo = 'hotelling', plot = False):
  X = np.array(X) 

  if algo == 'hotelling':
    X, y = Hotelling(X)
    
  elif algo == 'ocsvm':
    X, y = OCSVM(X)
    
  elif algo == 'variance':
    X, y = VarianceBased(X)
    
  elif algo == 'isolated_forest':
    X, y = IsoForest(X)

  else:
    raise ValueError(f"Unknown algorithm: {algo}")

  if plot:
    plot_series(X, y)
    
  return y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run anomaly detection algorithms.")
    parser.add_argument(
        '--algo',
        type=str,
        choices=['hotelling', 'ocsvm', 'variance', 'isolated_forest'],
        default='hotelling',
        help="Choose the algorithm to run."
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help="Set this flag to plot the results."
    )
    
    args = parser.parse_args()
    X = df['values'].tolist()
    
    run(X, algo=args.algo, plot=args.plot)