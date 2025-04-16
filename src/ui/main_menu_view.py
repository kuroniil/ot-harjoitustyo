from tkinter import ttk, Frame

class MainMenu:
    """Class for the main menu view of the game UI"""
    def __init__(self, root, handle_4x4_click, handle_5x5_click, handle_leaderboard_click, handle_load_game_click, font):
        self._root = root
        self._font = font
        self._frame = None
        self._handle_4x4_click = handle_4x4_click
        self._handle_5x5_click = handle_5x5_click
        self._handle_load_game_click = handle_load_game_click
        self._handle_leaderboard_click = handle_leaderboard_click
        self._configure_button_style()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root, bg="#02044d")
        self._frame.grid_columnconfigure(0, weight=1, minsize=121)
        [self._frame.grid_columnconfigure(i, weight=2, minsize=121) for i in range(1, 5)]
        self._frame.grid_columnconfigure(5, weight=1, minsize=121)

        [self._frame.grid_rowconfigure(i, weight=1, minsize=100) for i in range(0, 8)]
        self._frame.grid_rowconfigure(8, weight=1, minsize=50)
        
        header = ttk.Label(
            master=self._frame,
            text="Päävalikko",
            font=(self._font, 30, "bold"),
            background="#02044d",
            foreground="white"
            )
        
        game_4x4_button = ttk.Button(
            master=self._frame,
            text="4x4",
            style="Menu.TButton",
            command=self._handle_4x4_click
            )
        
        game_5x5_button = ttk.Button(
            master=self._frame,
            text="5x5",
            style="Menu.TButton",
            command=self._handle_5x5_click
            )
        
        load_game_button = ttk.Button(
            master=self._frame,
            text="Lataa peli",
            style="Menu.TButton",
            command=self._handle_load_game_click
            )

        leaderboards_button = ttk.Button(
            master=self._frame, 
            text="Tulokset", 
            style="Menu.TButton",
            command=self._handle_leaderboard_click
            )
        
        self._header_label = header.grid(column=2, columnspan=2, pady=20)
        self._4x4_button = game_4x4_button.grid(row=1, column=2, columnspan=2, sticky="ew", ipady=20)
        self._5x5_button = game_5x5_button.grid(row=3, column=2, columnspan=2, sticky="ew", ipady=20)
        self._load_game_button = load_game_button.grid(row=5, column=2, columnspan=2, sticky="ew", ipady=20)
        self._leaderboards_button = leaderboards_button.grid(row=7, column=2, columnspan=2, sticky="ew", ipady=20)

    def _configure_button_style(self):
        self._style = ttk.Style()
        self._style.configure(
            "Menu.TButton",
            font=(self._font, 15, "bold"),
            background="#0362fc",
            foreground="white"
            )

