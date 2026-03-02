import tkinter as tk

root = tk.Tk()
root.configure(background="lightgrey")
root.title("New Employee Entry")
root.geometry("500x600")

#Labels
lbl_first = tk.Label(root, text="First Name", bg="lightgrey")
lbl_last = tk.Label(root, text="Last Name", bg="lightgrey")
lbl_address = tk.Label(root, text="Address", bg="lightgrey")
lbl_city = tk.Label(root, text="City", bg="lightgrey")
lbl_state = tk.Label(root, text="State", bg="lightgrey")
lbl_zip = tk.Label(root, text="Zip", bg="lightgrey")
lbl_phone = tk.Label(root, text="Phone Number", bg="lightgrey")
lbl_rate = tk.Label(root, text="Hourly Rate", bg="lightgrey")
lbl_hours = tk.Label(root, text="Normal Hours", bg="lightgrey")

#Entry Boxes
ent_first = tk.Entry(root)
ent_last = tk.Entry(root)
ent_address = tk.Entry(root)
ent_city = tk.Entry(root)
ent_state = tk.Entry(root)
ent_zip = tk.Entry(root)
ent_phone = tk.Entry(root)
ent_rate = tk.Entry(root)
ent_hours = tk.Entry(root)

#Buttons
btnSave = tk.Button(root, text="Save", fg="blue", width=8)
btnClear = tk.Button(root, text="Clear", fg="blue", width=8)
btnClose = tk.Button(root, text="Close", fg="blue", width=8)

#Layout Constants
LX = 30   # Label X
EX = 180  # Entry X
Y_START = 40
Y_STEP = 35

#Row 1: First Name
lbl_first.place(x=40, y=50)
ent_first.place(x=200, y=50)

#Row 2: Last Name
lbl_last.place(x=40, y=85)
ent_last.place(x=200, y=85)

#Row 3: Address
lbl_address.place(x=40, y=120)
ent_address.place(x=200, y=120)

#Row 4: City
lbl_city.place(x=40, y=155)
ent_city.place(x=200, y=155)

#Row 5: State
lbl_state.place(x=40, y=190)
ent_state.place(x=200, y=190)

#Row 6: Zip
lbl_zip.place(x=40, y=225)
ent_zip.place(x=200, y=225)

#Row 7: Phone Number
lbl_phone.place(x=40, y=260)
ent_phone.place(x=200, y=260)

#Row 8: Hourly Rate
lbl_rate.place(x=40, y=295)
ent_rate.place(x=200, y=295)

#Row 9: Normal Hours
lbl_hours.place(x=40, y=330)
ent_hours.place(x=200, y=330)

#Buttons
btnSave.place(x=100, y=450)
btnClear.place(x=200, y=450)
btnClose.place(x=300, y=450)

root.mainloop()