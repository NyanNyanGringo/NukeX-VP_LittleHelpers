# import nuke
# import os
#
# from little_helpers.vp_little_helpers import osHelpers, cmdHelper


# def open_nuke_in_new_terminal(script_path=None):
#     """
#     Opens NukeX or NukeStudio in new terminal
#     :param script_path: string, path to script for open
#     :return: None
#     """
#     nuke_path = nuke.rawArgs[0]
#     start_mode = nuke.rawArgs[1]
#
#     command = ""
#
#     # change disk if Windows
#     if script_path and nuke.env["WIN32"]:
#         command += script_path.replace("\\", "/").split("/")[0] + " & "
#
#     # change dir to script dir
#     if script_path:
#         command += "cd " + osHelpers.correct_path_to_console_path(os.path.dirname(script_path)) + " & "
#
#     # run nuke in sertain mode
#     command += osHelpers.correct_path_to_console_path(nuke_path) + " " + start_mode
#
#     # open script
#     if script_path:
#         command += " " + os.path.basename(script_path)
#
#     cmdHelper.run_terminal_command(command)
#
#
# def restart_any_nuke():
#     """
#     Restart NukeX or NukeStudio (support script reopening)
#     :return: None
#     """
#     if nuke.env["LINUX"]:
#         nuke.message("My Lord, I'm sorry...\n\nRestart Nuke for your OS not supported yet :(")
#         return
#
#     script_path = nuke.Root().name()
#
#     if script_path == "Root" and nuke.ask("My Lord, script isn't saved!\n\nRestart anyway?"):
#         open_nuke_in_new_terminal()
#         nuke.scriptExit()
#
#     elif not script_path == "Root" and nuke.ask("My Lord,\n\nRestarn Nuke?"):
#         open_nuke_in_new_terminal(script_path=script_path)
#         nuke.scriptSave(nuke.Root().name())
#         nuke.scriptExit()
