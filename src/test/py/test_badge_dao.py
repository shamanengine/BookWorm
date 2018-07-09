import unittest
from src.main.py.const import Const
from src.main.py.DAO.badgeDAO import BadgeDAO


class TestBadgeDAO(unittest.TestCase):
    """Tests DAO class to work with badges"""

    def setUp(self):
        self.badge_dao = BadgeDAO(Const.BADGE_JSON_TEST)

        self.test_badges = {
            "Pithecanthropus": {0, 0.1, 0.2},
            "Younger sister": {0.3, 0.4},
            "Pragmatic writer": {0.6, 0.7},
            "Neat essayist": {0.8, 0.9},
            "Beyond Good and Evil": {1, 1.2, 10, 998, 999998}
        }

    def test_findAllBadges(self):
        """Tests fetching of all badges"""

        self.assertEqual(len(self.badge_dao.findAllBadges()), Const.BADGES_COUNT)

    def test_findBadgeByIndex(self):
        """Tests search of the badge by index"""

        for title, indices in self.test_badges.items():
            with self.subTest(indices=indices, title=title):
                for index in indices:
                    self.assertEqual(title, self.badge_dao.findBadgeByIndex(index).title)

    # def tearDown(self):
    #     self.badge_dao.dispose()


if __name__ == '__main__':
    unittest.main()
