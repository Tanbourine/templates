""" Template for GUIs"""
try:
    # python 3.x
    import tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk


class MainApplication(tk.Frame):

    """ master app """
    # pylint: disable = too-many-ancestors, too-many-instance-attributes

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("Your Title Here")
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)

    def create_menus(self):
        """ creating dropdown menus """
        main_menu = tk.Menu(self.master)

        # options menu
        file_menu = tk.Menu(main_menu, tearoff=0)

        main_menu.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=main_menu)

    def create_widgets(self):
        """ initalizes widgets """
        # create quit app button
        tk.Button(
            self, text='Quit', command=self.quit_app).grid(
                row=100, column=0)

    def quit_app(self):
        """ closes screen """
        self.master.destroy()


def main():
    """ main function """
    # pylint: disable =
    root = tk.Tk()
    app = MainApplication(root)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(200, 800)

    app.pack(fill='both')

    app.mainloop()


if __name__ == "__main__":
    main()
