import tkinter as tk
import model

class Textbox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, text="n ").grid(row=0, sticky="E")
        tk.Label(self, text="l ").grid(row=1, sticky="E")
        tk.Label(self, text="m ").grid(row=2, sticky="E")
        tk.Label(self, text="Z ").grid(row=3, pady=(20, 0), sticky="E")
        tk.Label(self, text="a0 (# of px) ").grid(row=4, sticky="E")

        self.n = tk.Entry(self)
        self.n.grid(row=0, column=1)

        self.l = tk.Entry(self)
        self.l.grid(row=1, column=1)

        self.m = tk.Entry(self)
        self.m.grid(row=2, column=1)

        self.Z = tk.Entry(self)
        self.Z.grid(row=3, column=1, pady=(20, 0))

        self.a0 = tk.Entry(self)
        self.a0.grid(row=4, column=1)

        tk.Label(self, text="Resolution ").grid(row=5, pady=(20, 0), sticky="E")
        tk.Label(self, text="(default 1000, change only if grainy) ").grid(row=6, sticky="E")

        self.res = tk.Entry(self)
        self.res.grid(row=5, column=1, pady=(20, 0))

        self.graph = tk.Button(self, text='Graph', command=self.load_graph, padx=10, pady=10)
        self.graph.grid(row=7, column=1, pady=(20, 0))
        self.graph.bind('<Return>', self.load_graph)

    def load_graph(self):

        n = int(self.n.get())
        l = int(self.l.get())
        m = int(self.m.get())
        Z = int(self.Z.get())
        a0 = int(self.a0.get())

        model.Z = Z
        model.a0 = Z*a0

        if len(self.res.get()) > 0:
            res = int(self.res.get())

        model.validate_quantum_numbers(n, l, m)

        model.graph(n, l, m, resolution=res)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.textbox = Textbox(self, relief='raised', borderwidth=2, padx=20, pady=20)
        self.textbox.pack(fill='both', expand=True)

        self.pack()


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Orbitals")

    # center in middle of screen
    x = int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2)
    y = int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2)
    root.geometry('+{x}+{y}'.format(x=x, y=y))

    app = MainApplication(root)

    tk.mainloop()