from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Entry, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sol\Desktop\DynamicsCalcu\build\assets\frame0")
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lenovo\OneDrive\Desktop\Mercado_WS\DynamicsCalcu\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_page(page):
    page.tkraise()

def change_to_page1():
    show_page(page1)

def change_to_page2():
    show_page(page2)

def change_to_page3():
    show_page(page3)

def go_back():
    show_page(main_menu)

def calculate_force():
    try:
        mass = float(mass_entry.get())
        acceleration = float(acceleration_entry.get())
        force = mass * acceleration
        result_label_page1.config(text=f"Force: {force} N")
    except ValueError:
        result_label_page1.config(text="Please enter valid numbers")

def calculate_velocity():
    try:
        distance = float(distance_entry_page2.get())
        time = float(time_entry_page2.get())
        velocity = distance / time
        result_label_page2.config(text=f"Velocity: {velocity} m/s")
    except ValueError:
        result_label_page2.config(text="Please enter valid numbers")

def calculate_mass():
    try:
        force = float(force_entry.get())
        acceleration = float(acceleration_entry_page3.get())
        mass = force / acceleration
        result_label_page3.config(text=f"Mass: {mass} kg")
    except ValueError:
        result_label_page3.config(text="Please enter valid numbers")

def calculate_elastic_collision():
    try:
        m1 = float(m1_entry.get())
        v1 = float(v1_entry.get())
        m2 = float(m2_entry.get())
        v2 = float(v2_entry.get())
        
        v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        
        result_label_page2.config(text=f"Final velocities:\nv1' = {v1_final} m/s\nv2' = {v2_final} m/s")
    except ValueError:
        result_label_page2.config(text="Please enter valid numbers")

def calculate_inelastic_collision():
    try:
        m1 = float(m1_entry_page3.get())
        v1 = float(v1_entry_page3.get())
        m2 = float(m2_entry_page3.get())
        v2 = float(v2_entry_page3.get())
        
        vf = (m1 * v1 + m2 * v2) / (m1 + m2)
        
        result_label_page3.config(text=f"Final velocity: v_f = {vf} m/s")
    except ValueError:
        result_label_page3.config(text="Please enter valid numbers")

window = Tk()
window.geometry("600x500")
window.configure(bg="#C4C4C4")

# Define pages
main_menu = Frame(window, bg="#C4C4C4")
page1 = Frame(window, bg="#9F9F9F")
page2 = Frame(window, bg="#9F9F9F")
page3 = Frame(window, bg="#9F9F9F")

# All frames in the same location
for page in (main_menu, page1, page2, page3):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)

# Main menu setup
canvas = Canvas(
    main_menu,
    bg="#9F9F9F",
    height=500,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

header = Label(main_menu, text="Dynamics Calculator", font=("Arial", 24, "bold"), bg="#9F9F9F")
header.pack(pady=20)

instruction = Label(main_menu, text="Please choose one of the following options:", font=("Arial", 14), bg="#9F9F9F", pady=25)
instruction.pack(pady=10)

# Styling for buttons to match the design
button_style = {
    "height": 2,
    "width": 25,
    "font": ("Arial", 12, "bold"),
    "bg": "#FFFFFF",
    "fg": "#000000",
    "borderwidth": 0,
    "highlightthickness": 0
}

button_1 = Button(
    main_menu,
    text="Newton's Second Law",
    command=change_to_page1,
    **button_style
)
button_1.pack(pady=10)

button_2 = Button(
    main_menu,
    text="Elastic Collision",
    command=change_to_page2,
    **button_style
)
button_2.pack(pady=10)

button_3 = Button(
    main_menu,
    text="Inelastic Collision",
    command=change_to_page3,
    **button_style
)
button_3.pack(pady=10)

# Page 1: Newton's Second Law
go_back_button_page1 = Button(
    page1,
    text="Go Back",
    command=go_back,
    **button_style
)
go_back_button_page1.pack(pady=(50, 30))

mass_label = Label(page1, text="Mass (kg):", bg="#9F9F9F", font=("Arial", 12))
mass_label.pack(pady=5)
mass_entry = Entry(page1)
mass_entry.pack(pady=(5, 20))

acceleration_label = Label(page1, text="Acceleration (m/s^2):", bg="#9F9F9F", font=("Arial", 12))
acceleration_label.pack(pady=5)
acceleration_entry = Entry(page1)
acceleration_entry.pack(pady=(5, 30))

calculate_button = Button(page1, text="Calculate Force", command=calculate_force, **button_style)
calculate_button.pack(pady=10)

result_label_page1 = Label(page1, text="Force: ", bg="#9F9F9F", font=("Arial", 12))
result_label_page1.pack(pady=5)

# Page 2: Elastic Collision Calculation
go_back_button_page2 = Button(
    page2,
    text="Go Back",
    command=go_back,
    **button_style
)
go_back_button_page2.pack(pady=(20, 10))

m1_label = Label(page2, text="Mass of object 1 (kg):", bg="#9F9F9F", font=("Arial", 12))
m1_label.pack(pady=(10, 5))
m1_entry = Entry(page2)
m1_entry.pack(pady=(10, 5))

v1_label = Label(page2, text="Initial velocity of object 1 (m/s):", bg="#9F9F9F", font=("Arial", 12))
v1_label.pack(pady=5)
v1_entry = Entry(page2)
v1_entry.pack(pady=5)

m2_label = Label(page2, text="Mass of object 2 (kg):", bg="#9F9F9F", font=("Arial", 12))
m2_label.pack(pady=5)
m2_entry = Entry(page2)
m2_entry.pack(pady=5)

v2_label = Label(page2, text="Initial velocity of object 2 (m/s):", bg="#9F9F9F", font=("Arial", 12))
v2_label.pack(pady=(5, 10))
v2_entry = Entry(page2)
v2_entry.pack(pady=(5, 10))

calculate_button_page2 = Button(page2, text="Calculate Final Velocities", command=calculate_elastic_collision, **button_style)
calculate_button_page2.pack(pady=10)

result_label_page2 = Label(page2, text="Final velocities: ", bg="#9F9F9F", font=("Arial", 12))
result_label_page2.pack(pady=5)

# Page 3: Inelastic Collision Calculation
go_back_button_page3 = Button(
    page3,
    text="Go Back",
    command=go_back,
    **button_style
)
go_back_button_page3.pack(pady=(20, 10))

m1_label_page3 = Label(page3, text="Mass of object 1 (kg):", bg="#9F9F9F", font=("Arial", 12))
m1_label_page3.pack(pady=(10, 5))
m1_entry_page3 = Entry(page3)
m1_entry_page3.pack(pady=(10, 5))

v1_label_page3 = Label(page3, text="Initial velocity of object 1 (m/s):", bg="#9F9F9F", font=("Arial", 12))
v1_label_page3.pack(pady=5)
v1_entry_page3 = Entry(page3)
v1_entry_page3.pack(pady=5)

m2_label_page3 = Label(page3, text="Mass of object 2 (kg):", bg="#9F9F9F", font=("Arial", 12))
m2_label_page3.pack(pady=5)
m2_entry_page3 = Entry(page3)
m2_entry_page3.pack(pady=5)

v2_label_page3 = Label(page3, text="Initial velocity of object 2 (m/s):", bg="#9F9F9F", font=("Arial", 12))
v2_label_page3.pack(pady=(5, 10))
v2_entry_page3 = Entry(page3)
v2_entry_page3.pack(pady=(5, 10))

calculate_button_page3 = Button(page3, text="Calculate Final Velocity", command=calculate_inelastic_collision, **button_style)
calculate_button_page3.pack(pady=10)

result_label_page3 = Label(page3, text="Final velocity: ", bg="#9F9F9F", font=("Arial", 12))
result_label_page3.pack(pady=5)

# Initially show the main menu
show_page(main_menu)
window.resizable(False, False)
window.mainloop()
