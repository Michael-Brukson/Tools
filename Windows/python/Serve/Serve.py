import customtkinter as Ctk
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename
from functools import partial
import subprocess
import threading
import sys
import os

class Serve:
    class TextField:
        def __init__(self, root, writeable: bool = True):
            self.__tf = tk.Text(root, font=("Courier", 12), wrap="word")
            if not writeable: self.__tf.bind("<Key>", lambda x: "break")


        def write(self, msg: str):
            self.__tf.insert(Ctk.END, msg)
            self.__tf.see(Ctk.END)

        def print_divider(self):
            self.write("=========================================================================\n")

        def flush(self):
            pass
            
        @property
        def field(self):
            return self.__tf

    IPV4: str = subprocess.run(['ipv4'], capture_output=True, text=True, shell=True).stdout.split()[0]

    __BASE_CONFIG = {
        "bg" : "gray14"
    }

    def __init__(self, width: int= 600, height: int= 440) -> None:
        self.__processes: list = []

        self.__set_paths()

        self.__root = Ctk.CTk()
        self.__root.title("Serve")
        self.__root.geometry(f"{width}x{height}")
        self.__root.iconbitmap(self.__ico_path)
        self.__root.protocol("WM_DELETE_WINDOW", self.kill)


        content = Ctk.CTkFrame(self.__root)
        content.pack(fill=Ctk.BOTH, expand=True)

        self.__add_console(content)

        self.__main_menu = tk.Menu(self.__root)
        
        for menu in self.__menus:
            self.__add_menu(*menu)

        self.__root.config(menu = self.__main_menu)


    def __add_theme(self, elem: any, options: dict = {}) -> None:
        """
        Wrapper function to configure() a passed element wtih css-like cascading themes. Returns None.
        
        :param elem: CTkinter-like element.
        :param options: Dictionary-like. Refer to CTkinter configure() for available options.
        """
        theme: dict = self.__BASE_CONFIG.copy()

        for key in options: theme[key] = options[key]

        if elem: elem.configure(**theme)


    @property
    def __menus(self) -> list:
        """
        Property function that initializes menu at topbar of window. Made to be dynamic, currenly supports basic dropdowns and checked boxes.
        Menus is initialized as a list of tuples. First value of tuple is the toplevel name for the submenu, second value of tuple is a list of labels and functions to call when label is activated.
        Checkmark subitem requires that a boolean variable be initialized first, then passed to the third value of tuple.
        
        :return: List of tuples representing menu items.
        :rtype: list
        """
        self.__verbose = tk.BooleanVar(value=True)

        menus: list = [
                ("Open", [("File", partial(self.__file_select, True)), ("Directory", partial(self.__file_select, False))]),
                ("⚙", [("Verbose", None, {"check": True, "variable": self.__verbose})])
                ]
        
        return menus


    # TODO: Finish documentation 
    def __add_menu(self, label: str, items: list) -> None:
        """
        Function to add menus to the main menu dynamically. 
        Iterates through list of items and checks their 
        
        :param label: Description
        :type label: string
        :param items: Description
        :type items: list
        """

        men = tk.Menu(self.__main_menu, tearoff=0)
        self.__main_menu.add_cascade(label=label, menu = men)

        for item in items:
            if len(item) >= 3 and isinstance(item[2], dict) and item[2].get("check"):
                var = item[2].get("variable", tk.BooleanVar())
                cmd = item[1]
                men.add_checkbutton(label=item[0], variable=var, command=cmd, font=('Arial', 12))
            else:
                men.add_command(label=item[0], command=item[1], font=('Arial', 12))


    def __add_console(self, root) -> None:
        self.__console = self.TextField(root, writeable=False)
        self.__add_theme(self.__console.field, {'bg' : 'black', 'fg':'white'})
        self.__console.field.pack(side=Ctk.LEFT, fill=Ctk.Y, padx=6, pady=6)
        self.__console.write("Welcome to Serve! Select a file or directory, and a QR code will be printed. Scan that QR code on your phone, and you'll be able to download the file from there! \n")
        self.__console.print_divider()

    
    def __set_paths(self) -> None:
        self.__base: str = ''
        self.__serve_path: str = ''
        if getattr(sys, 'frozen', False):
            # when packaged
            self.__base = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
            self.__serve_path = os.path.join(self.__base, "serve.cmd")
            self.__ico_path = os.path.join(self.__base, "favicon.ico")
        else:
            # when running locally
            self.__base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            self.__serve_path = os.path.join(self.__base, "cmd", "serve", "serve.cmd")
            self.__ico_path = os.path.join(self.__base, "python", "Serve", "favicon.ico")


    # TODO: Set up previewing files 
    def __preview_file(self, root) -> None :
        pass


    def __run_serve(self, path: str, file: str) -> tuple:
        def output(process):
            for line in process.stdout: 
                self.__console.write(line.decode('utf-8'))
            # TODO: Figure out why the hosting statement does not print
            # MARK: This line does not print, because stdout is a constant stream. 
            self.__console.print_divider() 

        if os.path.exists(self.__serve_path):
            cmd_base = self.__serve_path
            cmd = ["cmd", "/c", cmd_base, "-d", path, "-f", file] + (["-v"] if self.__verbose.get() else [])
        else:
            cmd = ["serve", "-d", path, "-f", file] + (["-v"] if self.__verbose.get() else [])

        kwargs: list = {
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": False,
            "shell": True,
            "creationflags": subprocess.CREATE_NEW_PROCESS_GROUP
        }
        
        process = subprocess.Popen(cmd, **kwargs)
        
        self.__processes.append(process)
        
        threading.Thread(target=output, args=(process,), daemon=True).start()
        

    def __file_select(self, file: bool) -> None:
        path: str = ''
        filename: str = ''
        title_base: str = 'Select a '

        if file:
            path = askopenfilename(title=title_base.join('File'))
            filename = path[path.rfind('/') + 1:]
            path = path[:path.rfind('/')]
        else:
            path = askdirectory(title=title_base.join('Directory'))

        if path: 
            self.__run_serve(path, filename)
        
    # TODO: This is slow on the actual build. Make it faster.
    def kill(self) -> None:
        for process in reversed(self.__processes):
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(process.pid)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            self.__processes.pop()

        self.__root.destroy()


    def run(self) -> None:
        self.__root.mainloop()


if __name__ == "__main__":
    sv = Serve()
    print(sv.IPV4)
    # sv.run()
