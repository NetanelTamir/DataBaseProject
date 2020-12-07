import tkinter as tk

def handle_click():
    ##todo- goto the model and get user name and password
    print("The button was clicked: " + str(loginButton.winfo_pointerx()) + str(loginButton.winfo_pointery()) + "----" + entry2.get())
    #database_intercation
def handle_sign_up():
    print("sign up button was clicked")

root = tk.Tk()
root.title("login")
label = tk.Label(
    text="enter your user name\nand password",
    fg="white",
    bg="black",
    width=50,
    height=10
)
entry = tk.Entry(width=20,text="user name",master=root)
entry2 = tk.Entry(width=20,text="password",master=root)
loginButton = tk.Button(
    root,
    text="login!",
    width=8,
    height=1,
    bg="black",
    fg="white",
    command=handle_click
)
signUpButton = tk.Button(
    root,
    text="sign up!",
    width=8,
    height=1,
    bg="black",
    fg="white",
    command=handle_sign_up
)
signUpButton.place(relx=0,
    rely=1.0,
    anchor='sw')
label.pack()
entry.pack()
entry2.pack()
loginButton.pack()
signUpButton.pack()
root.mainloop()
