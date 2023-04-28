import numpy as np


def calculate(list):

  if len(list) < 9 or len(list) > 9:
    raise ValueError("List must contain nine numbers.")
  else:
    matrix = np.array(list).reshape(3, 3)

  mean = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()),
          (matrix.flatten().mean())]

  variance = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),
              (matrix.flatten().var())]

  std = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()),
         (matrix.flatten().std())]

  max = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()),
         (matrix.flatten().max())]

  min = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()),
         (matrix.flatten().min())]

  sum = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()),
         (matrix.flatten().sum())]

  calculations = {
    "Mean": mean,
    "Variance": variance,
    "Standard Deviation": std,
    "Maximum": max,
    "Minimum": min,
    "Sum": sum,
  }

  return calculations
