from tkinter import *
from tkinter import ttk, messagebox

import os
from tkinter import *
from tkinter import messagebox
import credentials as cr
import pymysql
from PIL import ImageTk, Image
from PIL import ImageTk

from signup_page import SignUp
import credentials as cr


class login_page:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME TO SIGN LANGUAGE RECOGNITION"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 20, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=100, y=40, width=900, height=30)
        # ============================================================================
        # ==============================DESIGN PART===================================
        # ============================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo)
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=500, y=332)
        self.email_entry = Entry(font=("times new roman", 15, "bold"), fg="black")
        self.email_entry.place(x=750, y=400, width=300)

        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=500, y=414)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

        # ================Buttons===================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          command=self.redirect_window,
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', command=self.login_func,
                            font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                            )
        self.login.place(x=20, y=10)

        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    command=self.forgot_func,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

    def login_func(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s",
                            (self.email_entry.get(), self.password_entry.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.window)
                else:
                    messagebox.showinfo("Success", "Wellcome to the Sign Language Recognition System", parent=self.window)
                    # Clear all the entries
                    self.reset_fields()
                    window.destroy()
                    import run

                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def forgot_func(self):
        if self.email_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Email Id", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()

                    # =========================SECOND WINDOW===============================
                    # ------------Toplevel:create a window top of another window-----------
                    # ------------focus_force:Helps to to focus on the current window------
                    # -----Grab:Helps to grab the current window until user ungrab it------

                    self.root = Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root, text="Change your password", font=("times new roman", 20, "bold"),
                                   bg="white").place(x=10, y=10)

                    title4 = Label(self.root, text="It's quick and easy", font=("times new roman", 12),
                                   bg="white").place(x=10, y=45)

                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"),
                                   bg="white").place(x=10, y=85)

                    self.sec_ques = ttk.Combobox(self.root, font=("times new roman", 13), state='readonly',
                                                 justify=CENTER)
                    self.sec_ques['values'] = (
                    "Select", "What's your pet name?", "Your first teacher name", "Your birthplace",
                    "Your favorite movie")
                    self.sec_ques.place(x=10, y=120, width=270)
                    self.sec_ques.current(0)

                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(
                        x=10, y=160)

                    self.ans = Entry(self.root, font=("arial"))
                    self.ans.place(x=10, y=195, width=270)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"),
                                   bg="white").place(x=10, y=235)

                    self.new_pass = Entry(self.root, font=("arial"))
                    self.new_pass.place(x=10, y=270, width=270)

                    self.create_button = Button(self.root, text="Submit", command=self.change_pass,
                                                font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2",
                                                fg="white").place(x=95, y=340, width=200)
                    # =========================================================================

            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    def change_pass(self):
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and question=%s and answer=%s",
                            (self.email_entry.get(), self.sec_ques.get(), self.ans.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s",
                                    (self.new_pass.get(), self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")

            except Exception as er:
                messagebox.showerror("Error!", f"{er}")

    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        window = Tk()
        obj = SignUp(window)
        window.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


# The main function
if __name__ == "__main__":
    window = Tk()
    obj = login_page(window)
    window.mainloop()
