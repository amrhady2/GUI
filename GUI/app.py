import tkinter as tk

#Thinter Window
root_window = tk.Tk()

#Window Settings

root_window.title('Application Title')
root_window.geometry('600x200')
root_window.configure( background = '#353535')

#Text
tk.Label(root_window, text='Hello World', fg='White', bg='#353535').pack()

#Exit Button
tk.Button(root_window, text='Exit', width=20, command=root_window.destroy).pack()

#Main loop
root_window.mainloop()