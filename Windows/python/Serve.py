import tkinter as tk
from tkinter import filedialog
from tkinter import ttk # TODO: Make things look nice with ttk.
from functools import partial
import os

class Serve:
    __BASE_CONFIG = {
        "bg" : "gray14"
    }

    # __TTK_BASE_CONFIG = ttk.Style().configure('Base', **__BASE_CONFIG)

    def __init__(self, width: int= 600, height: int= 440):
        menus = [
                ("☰", [("Open", self.__file_select), ("New", None)]),
                ("⚙", [("Temp", None)])
                ]

        self.__root = tk.Tk()
        self.__root.title("")
        self.__root.geometry(f"{width}x{height}")

        content = tk.Frame(self.__root)
        self.__add_theme(content)
        content.pack(fill=tk.BOTH, expand=True)

        self.__upper = tk.Frame(content)
        self.__add_theme(self.__upper, {'bg' : 'white'})
        self.__upper.pack(side=tk.TOP, fill=tk.Y, padx=6, pady=6)


        self.__main_menu = tk.Menu(self.__root)
        
        for menu in menus:
            self.__add_theme(self.__add_menu(*menu), {'font': ('Georgia')})

        self.__root.config(menu = self.__main_menu)


    def __add_theme(self, elem: any, options: dict = {}) -> None:
        theme: dict = self.__BASE_CONFIG

        for key in options: theme[key] = options[key]

        elem.config(**theme)


    def __add_menu(self, label: any, items: list) -> tk.Menu:
        men = tk.Menu(self.__main_menu, tearoff=0)
        self.__main_menu.add_cascade(label=label, menu = men, font=("Arial", 16))

        for item in items:
            men.add_command(label= item[0], command=item[1])

        return men


    def __list_files(self) -> list:
        images: list = []
        
        for file in os.listdir(self.__SAVE_DIR):
            if file.endswith('.png') or file.endswith('.jpg'):
                images.append(file)
        return images


    def __open_file(self, wind, event) -> None:        
        pass


    def __preview_file(self, wind, event) -> None :
        pass


    def __file_select(self) -> None:
        path = filedialog.askopenfilename(
            initialdir="/",
            title='Select a File'
        )
        print(path)
        # TODO: Make work !
        # wind = tk.Toplevel(self.__root)
        # wind.title("Select file")
        # wind.geometry("700x400")

        # content = tk.Frame(wind)
        # content.pack(fill=tk.BOTH, expand=True)

        # left = tk.Frame(content)
        # left.pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)

        # right = tk.Frame(content)
        # right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=6, pady=6)

        # wind.preview_frame = right

        # selection = tk.Listbox(master=left)
        # selection.pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)

        # selection.bind('<<ListboxSelect>>', partial(self.__preview_file, wind))
        # selection.bind('<Double-1>', partial(self.__open_file, wind))

        # for file in self.__list_files():
        #     selection.insert(tk.END, file)


    def run(self) -> None:
        self.__root.mainloop()


if __name__ == "__main__":
    sv = Serve()
    sv.run()
