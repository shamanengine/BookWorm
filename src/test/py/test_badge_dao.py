import unittest
import context
import main.py.const
from main.py.DAO.badgeDAO import BadgeDAO
from main.py.DAO.entities.badge import Badge

print(Badge("A", "AA", 0.25, 0.5, "descr"))

class TestBadgeDAO(unittest.TestCase):
	'''Tests DAO class to work with badges'''

	def test_findAllBadges(self):
		'''Tests that all badges are fetched propperly'''
		badgeDAO = BadgeDAO(const.BADGE_JSON_FILENAME)


