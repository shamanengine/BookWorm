class Const:
    """Constants to be used in the project"""

    BADGE_JSON_MAIN = "../../resources/badges.json"
    BADGE_JSON_MAIN_ABS = "src/main/resources/badges.json"
    BADGE_JSON_TEST = "../resources/badges.json"
    BADGES_COUNT = 5


if __name__ == '__main__':
    print(Const.BADGE_JSON_MAIN)
    const = Const
    print(const.BADGE_JSON_TEST)
    print(Const.BADGES_COUNT)

# Put in const.py...:
# class _const:
#     class ConstError(TypeError):
#         pass
#
#     def __setattr__(self, name, value):
#         if self.__dict__.has_key(name):
#             raise self.ConstError("Can't rebind const(%s)" % name)
#         self.__dict__[name] = value
#
#     BADGE_JSON_FILENAME = "../resources/badges.json"
#
#
# import sys
# sys.modules[__name__] = _const()


# that's all -- now any client-code can
# import const
# and bind an attribute ONCE:
# const.magic = 23
# but NOT re-bind it:
# const.magic = 88      # raises const.ConstError
# you may also want to add the obvious __delattr__
