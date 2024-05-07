import tkinter as tk
from tkinter import ttk, messagebox
from db_operations import load_pokemon, add_pokemon, register_user, check_user
import threading


def create_pokemon_tab(tab_control):
    pokemon_tab = ttk.Frame(tab_control)

    tree_frame = ttk.Frame(pokemon_tab)
    tree_frame.pack(side="bottom", fill="both", expand=True)

    pokemon_tree = ttk.Treeview(
        tree_frame,
        columns=("ID", "Name", "Height", "Weight", "Description"),
        show="headings",
        height="5",
    )

    pokemon_tree.column("ID", anchor="center", width=100, stretch=False)
    pokemon_tree.column("Name", anchor="center", width=150, stretch=False)
    pokemon_tree.column("Height", anchor="center", width=100, stretch=False)
    pokemon_tree.column("Weight", anchor="center", width=100, stretch=False)
    pokemon_tree.column(
        "Description", anchor="w", width=250, stretch=True
    )

    pokemon_tree.heading("ID", text="ID")
    pokemon_tree.heading("Name", text="Name")
    pokemon_tree.heading("Height", text="Height")
    pokemon_tree.heading("Weight", text="Weight")
    pokemon_tree.heading("Description", text="Description")

    vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=pokemon_tree.yview)
    vsb.pack(side="right", fill="y")
    pokemon_tree.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=pokemon_tree.xview)
    hsb.pack(side="bottom", fill="x")
    pokemon_tree.configure(xscrollcommand=hsb.set)

    pokemon_tree.pack(side="left", fill="both", expand=True)

    load_btn = ttk.Button(
        pokemon_tab,
        text="Load Pokemon",
        command=lambda: refresh_pokemon_data(pokemon_tree),
    )
    load_btn.pack(pady=10)

    entries = create_entries(pokemon_tab)
    add_btn = ttk.Button(
        pokemon_tab,
        text="Add Pokemon",
        command=lambda: add_pokemon_entry(*entries, pokemon_tree),
    )
    add_btn.pack(pady=10)

    return pokemon_tab


def refresh_pokemon_data(tree):
    def db_task():
        try:
            tree.delete(*tree.get_children())
            pokemon_data = load_pokemon()
            for pokemon in pokemon_data:
                tree.insert(
                    "",
                    tk.END,
                    values=(
                        pokemon["PokemonID"],
                        pokemon["Name"],
                        pokemon["Height"],
                        pokemon["Weight"],
                        pokemon["Description"],
                    ),
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=db_task).start()


def create_entries(pokemon_tab):
    ttk.Label(pokemon_tab, text="Name:").pack()
    name_entry = ttk.Entry(pokemon_tab)
    name_entry.pack()
    ttk.Label(pokemon_tab, text="Height:").pack()
    height_entry = ttk.Entry(pokemon_tab)
    height_entry.pack()
    ttk.Label(pokemon_tab, text="Weight:").pack()
    weight_entry = ttk.Entry(pokemon_tab)
    weight_entry.pack()
    ttk.Label(pokemon_tab, text="Description:").pack()
    desc_entry = ttk.Entry(pokemon_tab)
    desc_entry.pack()
    return name_entry, height_entry, weight_entry, desc_entry


def add_pokemon_entry(name_entry, height_entry, weight_entry, desc_entry, tree):
    try:
        add_pokemon(
            name_entry.get(), height_entry.get(), weight_entry.get(), desc_entry.get()
        )
        refresh_pokemon_data(tree)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def create_login_tab(tab_control):
    login_tab = ttk.Frame(tab_control)
    ttk.Label(login_tab, text="Username:").pack()
    username_entry = ttk.Entry(login_tab)
    username_entry.pack()
    ttk.Label(login_tab, text="Password:").pack()
    password_entry = ttk.Entry(login_tab, show="*")
    password_entry.pack()

    login_button = ttk.Button(
        login_tab,
        text="Login",
        command=lambda: login_user(username_entry.get(), password_entry.get()),
    )
    login_button.pack(pady=10)
    return login_tab


def create_register_tab(tab_control):
    register_tab = ttk.Frame(tab_control)

    ttk.Label(register_tab, text="Create your Username:").pack()
    username_entry = ttk.Entry(register_tab)
    username_entry.pack()

    ttk.Label(register_tab, text="Create your Password:").pack()
    password_entry = ttk.Entry(register_tab, show="*")
    password_entry.pack()

    register_button = ttk.Button(
        register_tab,
        text="Register",
        command=lambda: register_user(username_entry.get(), password_entry.get()),
    )
    register_button.pack(pady=10)

    return register_tab


def login_user(username, password):
    try:
        user = check_user(username, password)
        if user:
            messagebox.showinfo("Login Info", "Login Successful")
        else:
            messagebox.showinfo("Login Info", "Invalid Credentials")
    except Exception as e:
        messagebox.showerror("Error", str(e))
