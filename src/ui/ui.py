from ui.main_menu_view import MainMenu
from ui.game_view import Game

class UI:
    def __init__(self, root):
        self._root = root
        self._curr_view = None
        self._font = "Arial"

    def start(self):
        self._show_view("main_menu")

    def _close_curr_view(self):
        if self._curr_view:
            self._curr_view.destroy()
        self._curr_view = None

    def _show_view(self, view):
        self._close_curr_view()
        match view:
            case "main_menu":
                self._curr_view = MainMenu(
                    self._root, 
                    self._handle_4x4_click,
                    self._handle_5x5_click,
                    self._handle_leaderboard_click,
                    self._font
                )
            case "4x4_game":
                self._curr_view = Game(
                    self._root,
                    "4x4", 
                    self._font, 
                    self._handle_menu_click,
                    self._handle_4x4_click
                    )
        self._curr_view.pack()
        
    def _handle_menu_click(self):
        self._show_view("main_menu")

    def _handle_4x4_click(self):
        self._show_view("4x4_game")
        
    def _handle_5x5_click(self):
        self._show_view("5x5_game")

    def _handle_leaderboard_click(self):
        self._show_view("leaderboard")
