from src.main.py.DAO.badgeDAO import BadgeDAO
from src.main.py.DAO.entities.badge import Badge
from src.main.py.const import Const

badgeDAO = BadgeDAO(Const.BADGE_JSON_TEST)

badge1 = badgeDAO.findBadgeByIndex(0.2)
print(badge1.title)

# print(badgeDAO)
