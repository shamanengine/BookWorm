import unittest
# import context
from src.main.py.const import Const
from src.main.py.DAO.entities.badge import Badge
from src.main.py.DAO.badgeDAO import BadgeDAO


# print(Badge("A", "AA", 0.25, 0.5, "descr"))
#
# badgeDAO = BadgeDAO(Const.BADGE_JSON_TEST)
# badges = badgeDAO.findAllBadges()
# print("\t==== BADGES ====\n")
# for badge in badges:
#     print(badge, '\n')


class TestBadgeDAO(unittest.TestCase):
    """Tests DAO class to work with badges"""

    def test_findAllBadges(self):
        """Tests that all badges are fetched properly"""

        badgeDAO = BadgeDAO(Const.BADGE_JSON_TEST)
        self.assertEqual(len(badgeDAO.findAllBadges()), Const.BADGES_COUNT)


if __name__ == '__main__':
    unittest.main()
