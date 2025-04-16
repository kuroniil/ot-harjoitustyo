from tkinter import ttk, Frame, StringVar
from game_logic import GameLogic
from scores import Scores

class Game:
    """Class for the game view of the user interface"""
    def __init__(self, root, grid_size, font, handle_menu_click, restart_game, start_grid=[], score=0):
        self._root = root
        self._grid_size = int(grid_size[0])
        self._font = font
        self._menu_click = handle_menu_click
        self._restart_game = restart_game
        self._score_submitted = False
        self._game = GameLogic(self._grid_size, start_grid, score) if len(start_grid) != 0 else GameLogic(self._grid_size)
        self._grid = self._game.grid.ret_grid()
        self._curr_score = StringVar(value=f"tulos: {score}")
        self._header_text = StringVar(value=f"Peli ({self._grid_size}x{self._grid_size})")
        self._game_over_text = StringVar(value="Tallenna tuloksesi nimimerkillä:")
        self._scores = Scores(self._grid_size)
        self._configure_cell_color()
        self._configure_cell_style()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, bg="#02044d")
        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        [self._frame.grid_columnconfigure(i, weight=2, minsize=100) for i in range(1, 5)]
        self._frame.grid_columnconfigure(5, weight=1, minsize=100)

        [self._frame.grid_rowconfigure(i, weight=1, minsize=100) for i in range(0, 7)]
        self._frame.grid_rowconfigure(7, weight=1, minsize=50)

        if self._grid_size == 5:
            self._frame.grid_columnconfigure(6, weight=1, minsize=100)
            self._frame.grid_rowconfigure(8, weight=1, minsize=50)

        header = ttk.Label(
            master=self._frame,
            textvariable=self._header_text,
            font=(self._font, 40, "bold"),
            background="#02044d",
            foreground="white"
            )
        
        menu_button = ttk.Button(
            master=self._frame,
            text="main menu",
            command=self._handle_menu_click
        )

        score_label = ttk.Label(
            master=self._frame,
            textvariable=self._curr_score,
            font=(self._font, 10, "bold"),
            background="#02044d",
            foreground="white"
        )

        save_game_button = ttk.Button(
            master=self._frame,
            text="tallenna peli",
            command=self._save_game
        )
        
        menu_button.grid(row=2, column=1, columnspan=2)
        save_game_button.grid(row=2, column=3)
        score_label.configure(anchor="center")
        score_label.grid(row=2, column=4 if self._grid_size == 4 else 5, columnspan=1)
        header.grid(row=0, column=1, columnspan=4 if self._grid_size == 4 else 5)
        self._root.bind("<Key>", self._handle_keypress)
        self._initialize_grid()

    def _handle_keypress(self, event):
        if event.keysym == "Up":
            self._game.move_up()
        elif event.keysym == "Right":
            self._game.move_right()
        elif event.keysym == "Left":
            self._game.move_left()
        elif event.keysym == "Down":
            self._game.move_down()
        elif event.keysym == "Escape":
            self._restart_game()
            return
        else: # ignore other keypresses 
            return
        self._update_grid()
        self._update_score()
        self._check_game_over()

    def _handle_menu_click(self):
        self._root.unbind("<Key>")
        self._menu_click()

    def _initialize_grid(self):
        self._grid = self._game.grid.ret_grid()
        for i in range(0, self._grid_size):
            for j in range(0, self._grid_size):
                setattr(self, f"cell_{i}_{j}_text", StringVar(value=self._grid[i, j]))
                setattr(self, f"cell_{i}_{j}", ttk.Label(
                    master=self._frame,
                    textvariable=getattr(self, f"cell_{i}_{j}_text"),
                    style="Game.TLabel"
                    )
                )
                getattr(self, f"cell_{i}_{j}").configure(anchor="center")
                getattr(self, f"cell_{i}_{j}").grid(row=i+3, column=j+1, ipady=25, padx=5, pady=5)
        
        self._update_grid()

    def _save_game(self):
        self._game.save()

    def _update_grid(self):
        self._grid = self._game.grid.ret_grid()
        for i in range(0, len(self._grid)):
            for j in range(0, len(self._grid)):
                font_color = "white"
                curr_cell = self._grid[i, j]
                cell_color = self._cell_colors[curr_cell]
                if curr_cell <  10:
                    cell_value = f"   {curr_cell}   "
                    if curr_cell == 0:
                        font_color = "#a19a89"
                elif curr_cell < 100:
                    cell_value = f"  {curr_cell}  "
                elif curr_cell < 1000:
                    cell_value = f" {curr_cell} "
                else:
                    cell_value = str(curr_cell)
                getattr(self, f"cell_{i}_{j}").configure(background=cell_color, foreground=font_color)
                getattr(self, f"cell_{i}_{j}_text").set(cell_value)

    def _update_score(self):
        self._curr_score.set(f"tulos: {str(self._game.ret_score())}")

    def _check_game_over(self):
        if self._game.ret_game_over():
            self._game_over_label = ttk.Label(
                master=self._frame,
                textvariable=self._game_over_text,
                font=(self._font, 12, "bold"),
                background="#02044d",
                foreground="white"
            )
            self._score_entry = ttk.Entry(
                master=self._frame,
                text="Tulos",
                width=15,
                background="#02044d"
            )
            self._score_submit_button = ttk.Button(
                master=self._frame,
                text="tallenna",
                command=self._handle_entry_submit
            )
            self._header_text.set(f"Peli ({self._grid_size}x{self._grid_size}) Päättyi")
            self._game_over_label.grid(row=1, column=1, columnspan=2)
            self._score_entry.grid(row=1, column=3)
            self._score_submit_button.grid(row=1, column=4)

    def _handle_entry_submit(self):
        name = self._score_entry.get()
        if not self._score_submitted:
            if self._scores.add_new_score(name, self._game._score, self._grid_size):
                self._score_submitted = True
                self._game_over_text.set("Tallennettu! Uusi peli -> Esc")
            else:
                self._game_over_text.set("Virhe tuloksen tallennuksessa")

    def _configure_cell_color(self):
        self._cell_colors = {
            0: "#a19a89",
            2: "#fff261",
            4: "#c3ff7a",
            8: "#83d61e",
            16: "#3c9157",
            32: "#60fce0",
            64: "#0db596",
            128: "#c2390c",
            256: "#961e09",
            512: "#0536a1",
            1024: "#6900cc",
            2048: "#6a038c",
            4096: "#ff0808",
        }

    def _configure_cell_style(self):
        self._style = ttk.Style()
        self._style.configure(
            "Game.TLabel",
            font=(self._font, 40),
            )
