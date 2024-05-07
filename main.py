import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pokedex_gui import create_pokemon_tab, create_login_tab, create_register_tab


def setup_background(canvas, path):
    img = Image.open(path)
    img = img.resize((800, 600), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image


def main():
    root = tk.Tk()
    root.title("PokéDex")
    root.geometry("800x600")
    root.resizable(False, False)

    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)
    setup_background(
        canvas,
        "C:path\\to\image",
    )

    style = ttk.Style(root)
    print(style.theme_names())
    style.theme_use("default")

    style.configure(
        "Red.TNotebook.Tab", background="red", foreground="white", padding=[5, 5]
    )
    style.map(
        "Red.TNotebook.Tab", background=[("selected", "red"), ("active", "darkred")]
    )

    frame = tk.Frame(canvas)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tab_control = ttk.Notebook(frame, style="Red.TNotebook")
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
