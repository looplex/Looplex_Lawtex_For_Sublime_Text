from Looplex_Lawtex_For_Sublime_Text.lib.Config import Config
import os
import sublime

class Open_folder() :

    def __init__(self, view) :
        self.view = view

    def openLogsFolder(self) :

        if sublime.platform() == "windows":

            os.startfile(Config.retrieve_logs_folder_windows())

        else :

            # Both Linus and OSX
            os.system('xdg-open "%s"' % Config.retrieve_logs_folder_linux())

    def openDatabaseFolder(self) :

        if sublime.platform() == "windows":

            os.startfile(Config.retrieve_database_folder_windows())

        else :

            # Both Linus and OSX
            os.system('xdg-open "%s"' % Config.retrieve_database_folder_linux())