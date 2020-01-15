from typing import List
import numpy as np
RANDOM_KEYVALUES = { np.random.choice(list("abcdefghilnop")) * str(i):
np.random.random() for i in np.random.choice(list(range(100)))}
def some_function(

an_argument : int, another_argument: List, an_array: np.ndarray,

repeat: int = 10
) -> np.ndarray:
  result = 0
  for j in range(repeat): result += (an_argument * an_array).sum() * np.cos(another_argument) * j
  return result
