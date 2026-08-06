import tkinter as tk
from tkinter import messagebox

#defining variables

# maxium booking time
MAX_BOOKING_HOURS = 2

# title
SYSTEM_TITLE = "School Equipment Booking"

# tracks if equipment is available
is_available = True

# list of equipment
equipment_list = ["G1", "G2", "G3","G4", "G5", "G6", "G7", "G8", "G9"]


#functions

def btn_submit_click():
    """
    Function: Validates user input and processes the booking.
    Data Use: Reads text from 'txt_hours_entry' and updates 'is_available'.
    """
    global is_available
    
    # text from box
    str_user_input = txt_hours_entry.get()
    
    # validation
    if str_user_input == "":
        messagebox.showerror("Error", "Input Error: Hours field cannot be left blank!")
        return
    
    # convert into string
    int_hours = int(str_user_input)   

    # booking
    if is_available == True:
        is_available = False  
        lbl_status.config(text="Status: Booked Successfully!", fg="green")
        messagebox.showinfo("Success", f"Gear reserved for {int_hours} hour(s)!")
    else:
        lbl_status.config(text="Status: Gear Unavailable", fg="red")
        messagebox.showwarning("Notice", "This resource is already booked.")


#tkinter
app = tk.Tk()
app.title(SYSTEM_TITLE)
app.geometry("1920x1080")


lbl_heading = tk.Label(app, text="Available Resources")
lbl_heading.pack(pady=10)

# label items
for str_item in equipment_list:
    lbl_item = tk.Label(app, text=f"• {str_item}")
    lbl_item.pack()

# input
lbl_prompt = tk.Label(app, text="\nEnter booking hours (1-2):")
lbl_prompt.pack(pady=5)

# text
txt_hours_entry = tk.Entry(app, width=15)
txt_hours_entry.pack(pady=5)

# button
btn_submit = tk.Button(app, text="Confirm Booking", command=btn_submit_click)
btn_submit.pack(pady=10)

# status
lbl_status = tk.Label(app, text="Status: Ready", fg="blue")
lbl_status.pack(pady=10)

# run program
app.mainloop()