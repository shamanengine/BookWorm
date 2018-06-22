import os
import sys
# print(sys.path)
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


# print(sys.path)


'''
The way python treats imports is a weird shit. 
Mainly because it considers root directory the one where script was invoked.
Snake doesn't anything up above
Relative imports doesn't work in Python 3.
Writing full path like "C:/..." might be not the best idea for the obvious reasons.

Below is mine workaround:

1) Just create context.py with below in the same folder that you need access:
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

where '../..' - needed amount to get to src folder
2) Than put in your script: 
import context 

3) Than use any of A, B, C approaches below (C is preferred as more clean)

# this works A
import main.py.DAO.entities.badge
print(main.py.DAO.entities.badge.Badge("A", "AA", 0.25, 0.5, "descr"))

# this works B
from main.py.DAO.entities import badge
print(badge.Badge("A", "AA", 0.25, 0.5, "descr2"))

# this works C
from main.py.DAO.entities.badge import Badge
print(Badge("A", "AA", 0.25, 0.5, "descr3"))

# This doesn't work 
import main
from main import pym
from pym import DAO
from DAO import entities
from entities import badge

# print(badge.Badge("A", "AA", 0.25, 0.5, "descr2"))
'''