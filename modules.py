import math
import sys
import random as rdm
from enum import Enum
import exampleModule as exmo
from rps import rockPaperScissors

print(math.pi)

for item in dir(rdm):
    print(item)

print(exmo.animal)
exmo.test_phrase()

print(__name__)
print(exmo.__name__)

rockPaperScissors()