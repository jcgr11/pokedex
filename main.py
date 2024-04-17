import tkinter as tk
from tkinter import ttk
from pokedex_gui import create_pokemon_tab, create_login_tab, create_register_tab


def main():
    root = tk.Tk()
    root.title("PokeDex")
    tab_control = ttk.Notebook(root)

    login_tab = create_login_tab(tab_control)
    register_tab = create_register_tab(tab_control)
    pokemon_tab = create_pokemon_tab(tab_control)

    tab_control.add(login_tab, text="Login")
    tab_control.add(register_tab, text="Register")
    tab_control.add(pokemon_tab, text="Pokemon")

    tab_control.pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    main()
