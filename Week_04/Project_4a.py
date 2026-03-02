#Project 4a
#Zachary Boelter

import tkinter as tk

root = tk.Tk()
root.configure(background="darkgrey")
root.title("New Employee Entry")
root.geometry("500x600")

#Labels
lbl_first = tk.Label(root, text="First Name", bg="darkgrey", fg="white")
lbl_last = tk.Label(root, text="Last Name", bg="darkgrey", fg="white")
lbl_address = tk.Label(root, text="Address", bg="darkgrey", fg="white")
lbl_city = tk.Label(root, text="City", bg="darkgrey", fg="white")
lbl_state = tk.Label(root, text="State", bg="darkgrey", fg="white")
lbl_zip = tk.Label(root, text="Zip", bg="darkgrey", fg="white")
lbl_phone = tk.Label(root, text="Phone Number", bg="darkgrey", fg="white")
lbl_rate = tk.Label(root, text="Hourly Rate", bg="darkgrey", fg="white")
lbl_hours = tk.Label(root, text="Normal Hours", bg="darkgrey", fg="white")

#Entry Boxes
ent_first = tk.Entry(root, bg="white")
ent_last = tk.Entry(root, bg="white")
ent_address = tk.Entry(root, bg="white")
ent_city = tk.Entry(root, bg="white")
ent_state = tk.Entry(root, bg="white")
ent_zip = tk.Entry(root, bg="white")
ent_phone = tk.Entry(root, bg="white")
ent_rate = tk.Entry(root, bg="white")
ent_hours = tk.Entry(root, bg="white")

#Buttons
btnSave = tk.Button(root, text="Save", fg="blue", width=6)
btnClear = tk.Button(root, text="Clear", fg="blue", width=6)
btnClose = tk.Button(root, text="Close", fg="blue", width=6)

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
btnSave.place(x=70, y=450)
btnClear.place(x=200, y=450)
btnClose.place(x=330, y=450)

root.mainloop()