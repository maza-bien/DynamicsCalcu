from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Entry, Label
from math import sqrt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\Tkinter-Designer-master\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_page(page):
    print("Showing page:", page)
    page.tkraise()

def change_to_page1():
    show_page(page1)

def change_to_page2():
    show_page(page2)

def change_to_page3():
    show_page(page3)

def go_back():
    print("Go back function called")
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

window = Tk()
window.geometry("600x300")
window.configure(bg="#9F9F9F")

# Define pages
main_menu = Frame(window, bg="#9F9F9F")
page1 = Frame(window, bg="#9F9F9F")
page2 = Frame(window, bg="#9F9F9F")
page3 = Frame(window, bg="#9F9F9F")

#all frames in the same loc
for page in (main_menu, page1, page2, page3):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)

# Main menu setup with header
canvas = Canvas(
    main_menu,
    bg="#9F9F9F",
    height=300,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    60.0,
    600.0,
    300.0,
    fill="#9F9F9F",
    outline=""
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(
    300.0,
    32.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    main_menu,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=change_to_page1,
    relief="flat"
)
button_1.place(
    x=78.0,
    y=104.0,
    width=187.0,
    height=61.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    main_menu,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=change_to_page2,
    relief="flat"
)
button_2.place(
    x=206.0,
    y=171.0,
    width=187.0,
    height=61.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    main_menu,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=change_to_page3,
    relief="flat"
)
button_3.place(
    x=333.0,
    y=102.0,
    width=187.0,
    height=61.0
)

# Go back buttons on each page
go_back_button_page1 = Button(
    page1,
    text="Go Back",
    command=go_back
)
go_back_button_page1.pack(pady=10)

go_back_button_page2 = Button(
    page2,
    text="Go Back",
    command=go_back
)
go_back_button_page2.pack(pady=10)

go_back_button_page3 = Button(
    page3,
    text="Go Back",
    command=go_back
)
go_back_button_page3.pack(pady=10)

# Calculator on page1
mass_label = Label(page1, text="Mass (kg):")
mass_label.pack(pady=5)
mass_entry = Entry(page1)
mass_entry.pack(pady=5)

acceleration_label = Label(page1, text="Acceleration (m/s^2):")
acceleration_label.pack(pady=5)
acceleration_entry = Entry(page1)
acceleration_entry.pack(pady=5)

calculate_button = Button(page1, text="Calculate Force", command=calculate_force)
calculate_button.pack(pady=10)

result_label_page1 = Label(page1, text="Force: ")
result_label_page1.pack(pady=5)

# velocity calculator on page2
distance_label_page2 = Label(page2, text="Distance (m):")
distance_label_page2.pack(pady=5)
distance_entry_page2 = Entry(page2)
distance_entry_page2.pack(pady=5)

time_label_page2 = Label(page2, text="Time (s):")
time_label_page2.pack(pady=5)
time_entry_page2 = Entry(page2)
time_entry_page2.pack(pady=5)

calculate_button_page2 = Button(page2, text="Calculate Velocity", command=calculate_velocity)
calculate_button_page2.pack(pady=10)

result_label_page2 = Label(page2, text="Velocity: ")
result_label_page2.pack(pady=5)

# Mass calculator on page3
force_label = Label(page3, text="Force (N):")
force_label.pack(pady=5)
force_entry = Entry(page3)
force_entry.pack(pady=5)

acceleration_label_page3 = Label(page3, text="Acceleration (m/s^2):")
acceleration_label_page3.pack(pady=5)
acceleration_entry_page3 = Entry(page3)
acceleration_entry_page3.pack(pady=5)

calculate_button_page3= Button(page3, text="Calculate Mass", command=calculate_mass)
calculate_button_page3.pack(pady=10)

result_label_page3 = Label(page3, text="Mass: ")
result_label_page3.pack(pady=5)

# Initially show the main menu
show_page(main_menu)
window.resizable(False,False)
window.mainloop()