from tkinter import ttk, Frame, StringVar
from game_logic import GameLogic

class Game:
    def __init__(self, root, grid_size, font, handle_menu_click):
        self._root = root
        self._grid_size = int(grid_size[0])
        self._font = font
        self._handle_menu_click = handle_menu_click
        self._game = GameLogic(self._grid_size)
        self._grid = self._game.ret_grid()
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

        header = ttk.Label(
            master=self._frame,
            text=f"Peli ({self._grid_size}x{self._grid_size})",
            font=(self._font, 30, "bold"),
            background="#02044d",
            foreground="white"
            )
        
        menu_button = ttk.Button(
            master=self._frame,
            text="main menu",
            command=self._handle_menu_click
        )
        
        menu_button.grid(row=2, column=1, columnspan=2)
        header.grid(row=0, column=1, columnspan=4)
        self._root.bind("<Key>", self._handle_keypress) # keycodes: left - 113, up - 111, right - 114, down - 116
        self._initialize_grid()

    def _handle_keypress(self, event):
            if event.keycode == 111:
                self._game.move_up()
    
            self._update_grid()

    def _initialize_grid(self):
        self._grid = self._game.ret_grid()
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

    def _update_grid(self):
        self._grid = self._game.ret_grid()
        for i in range(0, len(self._grid)):
            for j in range(0, len(self._grid)):
                curr_cell = self._grid[i, j]
                cell_color = self._cell_colors[curr_cell]
                if curr_cell <  10:
                    cell_value = f"   {curr_cell}   "
                elif curr_cell < 100:
                    cell_value = f"  {curr_cell}  "
                elif curr_cell < 1000:
                    cell_value = f" {curr_cell} "
                else:
                    cell_value = str(curr_cell)
                getattr(self, f"cell_{i}_{j}").configure(background=cell_color)
                getattr(self, f"cell_{i}_{j}_text").set(cell_value)

    def _configure_cell_color(self):
        self._cell_colors = {
            0: "#a19a89",
            2: "green",
            4: "yellow",
            8: "orange",
            16: "red",
            32: "purple",
            2048: "blue"
        }

    def _configure_cell_style(self):
        self._style = ttk.Style()
        self._style.configure(
            "Game.TLabel",
            font=(self._font, 40),
            foreground="white"
            )