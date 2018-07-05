import json
# import context
# from main.py.DAO.entities.badge import Badge
# from entities.badge import Badge
from src.main.py.DAO.entities.badge import Badge


class BadgeDAO:
    """DAO class to work with Badges"""

    # def __init__(self, source_filename="../../resources/badges.json"):
    def __init__(self, source_filename="../../resources/badges.json"):
        self.source_filename = source_filename

    def findAllBadges(self):
        """Retrives info about all badges"""
        badges = []
        try:
            with open(self.source_filename) as source_file:
                json_badges = json.load(source_file)
                for json_badge in json_badges:
                    badges.append(Badge(
                        json_badge['title'],
                        json_badge['prompt'],
                        json_badge['index_low'],
                        json_badge['index_high'],
                        json_badge['description']
                    ))

        except FileNotFoundError:
            print("File '%s' was not found" % self.source_filename)
        # except BaseException:
        # 	print("Something wrong at showBadges() method")

        return badges

    def findBadgeByIndex(self, index):
        """Retrieves info about badge by given index"""
        for badge in self.findAllBadges():
            if badge.index_low <= index < badge.index_high:
                return badge

    def __repr__(self):
        return "BadgeDAO, source_filename = %s" % self.source_filename


if __name__ == '__main__':
    """Testing routines"""

    badgeDAO = BadgeDAO()
    badges = badgeDAO.findAllBadges()
    print("\t==== BADGES ====\n")
    for badge in badges:
        print(badge, '\n')

    badge1 = badgeDAO.findBadgeByIndex(0.2)
    print(badge1)

    badge2 = badgeDAO.findBadgeByIndex(0.4)
    print(badge2)

    badge3 = badgeDAO.findBadgeByIndex(0.6)
    print(badge3)

    badge4 = badgeDAO.findBadgeByIndex(0.8)
    print(badge4)

    badge5 = badgeDAO.findBadgeByIndex(1)
    print(badge5)

    badge6 = badgeDAO.findBadgeByIndex(-11)
    print(badge6)

    if badge6:
        print("OK")
    else:
        print("empty")

    badge7 = badgeDAO.findBadgeByIndex(1111)
    print(badge7)

# badge8 = badgeDAO.findBadgeByIndex("A")
# print(badge8)

# badge9 = badgeDAO.findBadgeByIndex(null)
# print(badge9)
