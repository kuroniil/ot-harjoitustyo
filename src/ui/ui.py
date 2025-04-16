from ui.main_menu_view import MainMenu
from ui.game_view import Game
from ui.leaderboard_view import Leaderboard
from ui.load_game_view import LoadGame

class UI:
    """Class responsible for managing different views
       of the user interface"""
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

    def _show_view(self, view, old_game=False, **kwargs):
        self._close_curr_view()
        match view:
            case "main_menu":
                self._curr_view = MainMenu(
                    self._root, 
                    self._handle_4x4_click,
                    self._handle_5x5_click,
                    self._handle_leaderboard_click,
                    self._handle_load_game_click,
                    self._font
                )
            case "4x4_game":
                args = [self._root,"4x4", self._font, self._handle_menu_click, self._handle_4x4_click]
                if old_game == True:
                    [args.append(val) for val in kwargs.values()]
                self._curr_view = Game(*args)
            case "5x5_game":
                args = [self._root, "5x5", self._font, self._handle_menu_click, self._handle_5x5_click]
                if old_game == True:
                    [args.append(val) for val in kwargs.values()]
                self._curr_view = Game(*args)
                
            case "load_game":
                self._curr_view = LoadGame(
                    self._root,
                    self._handle_menu_click,
                    self._font,
                    self._handle_starting_old_game
                )
            case "leaderboard":
                self._curr_view = Leaderboard(
                    self._root,
                    self._handle_menu_click,
                    self._font
                )
        self._curr_view.pack()
        
    def _handle_menu_click(self):
        self._show_view("main_menu")

    def _handle_4x4_click(self):
        self._show_view("4x4_game")
        
    def _handle_5x5_click(self):
        self._show_view("5x5_game")

    def _handle_load_game_click(self):
        self._show_view("load_game")

    def _handle_leaderboard_click(self):
        self._show_view("leaderboard")

    def _handle_starting_old_game(self, mode, start_grid, score):
        self._show_view(f"{mode}x{mode}_game",
                         True,
                         start_grid=start_grid,
                         score=score, 
                        )

