from pathlib import Path

from src.main.py.DAO.badgeDAO import BadgeDAO
from src.main.py.const import Const
from src.main.py.processor import Processor


class KickStarter:
    """Main class to process user activity"""

    def __init__(self):
        pass


if __name__ == '__main__':
    badge_dao = BadgeDAO(Const.BADGE_JSON_TEST)

    war_and_peace = Path(Const.WAR_TEXT).read_text()
    readme = Path(Const.README).read_text()

    readme_score = Processor.score(war_and_peace, readme)

    print("Your score is:\t" + str(readme_score))
    print("Your Badge is:\t" + badge_dao.findBadgeByIndex(readme_score).title)
    # print(Processor.score(war_and_peace, war_and_peace))
