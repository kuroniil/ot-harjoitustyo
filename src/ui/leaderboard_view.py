from tkinter import ttk, Frame, StringVar
from scores import Scores

class Leaderboard:
    def __init__(self, root, handle_menu_click, font):
        self._mode = 4
        self._scores = Scores(self._mode)
        self._root = root
        self._page = 0
        self._handle_menu_click = handle_menu_click
        self._font = font
        self._style = ttk.Style()
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._configure_style()
        self._frame = Frame(master=self._root, bg="#02044d")
        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        [self._frame.grid_columnconfigure(i, weight=2, minsize=100) for i in range(1, 5)]
        self._frame.grid_columnconfigure(5, weight=1, minsize=100)

        self._frame.grid_rowconfigure(0, weight=1, minsize=100)
        self._frame.grid_rowconfigure(1, weight=1, minsize=100, pad=0)
        self._frame.grid_rowconfigure(2, weight=1, minsize=50, pad=0)
        [self._frame.grid_rowconfigure(i, weight=1, minsize=100) for i in range(3, 7)]
        self._frame.grid_rowconfigure(7, weight=1, minsize=100)
        self._frame.grid_rowconfigure(8, weight=1, minsize=50)

        self._header_text = StringVar(value="Tulokset {self._mode}x{self._mode}")
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

        mode_4x4_button = ttk.Button(
            master=self._frame,
            text="4x4",
            command=self._handle_4x4_click
        )
        
        mode_5x5_button = ttk.Button(
            master=self._frame,
            text="5x5",
            command=self._handle_5x5_click
        )

        next_page_button = ttk.Button(
            master=self._frame,
            text="seuraava sivu",
            command=self._handle_next_page_click
        )
        
        table_header = ttk.Label(
            master=self._frame,
            text=f"{' '*9}sija{' '*20}nimimerkki{' '*32}tulos",
            font=(self._font, 15, "bold"),
            background="#02044d",
            foreground="white"
            )
        
        header.grid(row=0, column=1, columnspan=4)
        mode_4x4_button.grid(row=1, column=1, columnspan=1)
        mode_5x5_button.grid(row=1, column=2, columnspan=1)
        next_page_button.grid(row=1, column=3)
        menu_button.grid(row=1, column=4)
        table_header.grid(row=2, column=0, columnspan=5)
        self._initialize_table()
        self._table()

    def _initialize_table(self):
        for i in range(5):
            setattr(self, f"score_{i}_text", StringVar())
            setattr(self, f"score_{i}", 
                    ttk.Label(
                        master=self._frame,
                        textvariable=getattr(self, f"score_{i}_text"),
                        style="Leaderboard.TLabel",
                        width=43
                        )
                    )
            getattr(self, f"score_{i}").configure(background="#02044d")
            getattr(self, f"score_{i}").grid(row=i+3, column=1, ipady=25, padx=5, pady=5, columnspan=4, ipadx=20)

    def _table(self):
        self._get_scores()
        for i in range(5):
            if self._page*5 + i < len(self._scores):
                setattr(self, f"score_{i}_text", StringVar(
                    value=f"  {self._page*5 + (i + 1)}.{' ' if (self._page*5 + (i + 1)) < 10 else ''}{self._scores[self._page*5 + i].display()}")
                    )
                setattr(self, f"score_{i}", 
                        ttk.Label(
                            master=self._frame,
                            textvariable=getattr(self, f"score_{i}_text"),
                            style="Leaderboard.TLabel",
                            width=45
                            )
                        )
                getattr(self, f"score_{i}").configure(background="#0db596")
                getattr(self, f"score_{i}").grid(row=i+3, column=1, ipady=25, padx=5, pady=5, columnspan=4, ipadx=20)
            else:
                getattr(self, f"score_{i}").configure(background="#02044d", foreground="#02044d")

    def _get_scores(self):
        scores = Scores(self._mode)
        self._scores = scores.get_all_scores()

    def _handle_4x4_click(self):
        self._page = 0
        self._mode = 4
        self._header_text.set(f"Tulokset {self._mode}x{self._mode}")
        self._table()

    def _handle_5x5_click(self):    
        self._page = 0
        self._mode = 5
        self._header_text.set(f"Tulokset {self._mode}x{self._mode}")
        self._table()

    def _handle_next_page_click(self):
        if self._page * 5 < len(self._scores) - 5:
            self._page += 1
            self._table()

    def _configure_style(self):
        self._style.configure(
            "Leaderboard.TLabel",
            font=("DejaVu Sans Mono", 15),
            background="#02044d",
            foreground="white"
            )
