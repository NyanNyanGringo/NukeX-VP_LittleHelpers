import nuke

# from PySide2.QtWidgets import *
# from PySide2.QtGui import *
# from PySide2.QtCore import *

from little_helpers.vp_little_helpers import configHelper, userconfigHelper


# class CustomQMenu(QMenu):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def mouseReleaseEvent(self, event):
#         action = self.activeAction()
#         if action and action.isEnabled():
#             if not action.menu():
#                 action.trigger()
#             else:
#                 action.menu().exec_(self.mapToGlobal(event.pos()))
#         else:
#             super().mouseReleaseEvent(event)


def check_action_is_checked(config_key):
    """
    Check action is checked by using config key
    :param config_key: string
    :return: bool
    """
    if configHelper.check_key(config_key):
        return configHelper.read_config_key(config_key)
    return False


def create_and_get_helper_menu():
    """
    Create and Get menu for VP_MyLittleHelpers. If exists - return existed
    menu. Get menu name using ini_config
    :return: Nuke Menu
    """
    userconfig = userconfigHelper.parse_userconfig()
    menu_name = userconfig["UI SETTINGS"]["menu_name"].replace("\\", "/")

    menu = nuke.menu("Nuke")
    for m in menu_name.split("/"):
        menu = menu.addMenu(m)

    return menu
