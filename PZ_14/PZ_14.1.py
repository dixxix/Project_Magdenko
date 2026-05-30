import tkinter as tk
from tkinter import ttk


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.put_placeholder()
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


def create_sign_up_form():
    root = tk.Tk()
    root.title("Sign Up Form - Variant 8")
    root.geometry("500x600")
    root.resizable(False, False)

    header_footer_bg = "#e67e22"
    body_bg = "#2b2b3d"
    label_color = "#f1c40f"
    entry_bg = "#ffffff"

    header_frame = tk.Frame(root, bg=header_footer_bg, height=40)
    header_frame.pack(side='top', fill='x')

    header_label = tk.Label(header_frame, text="Sign Up", font=("Arial", 14),
                            bg=header_footer_bg, fg="white", padx=10, anchor='w')
    header_label.pack(side='left', fill='x', expand=True)

    main_frame = tk.Frame(root, bg=body_bg)
    main_frame.pack(side='top', fill='both', expand=True, padx=20, pady=10)

    main_frame.columnconfigure(0, weight=1, minsize=120)
    main_frame.columnconfigure(1, weight=3)

    def add_entry_row(label_text, row_idx, placeholder=""):
        lbl = tk.Label(main_frame, text=label_text, font=("Arial", 10, "bold"),
                       bg=body_bg, fg=label_color, anchor='e')
        lbl.grid(row=row_idx, column=0, sticky='e', padx=5, pady=5)

        ent = PlaceholderEntry(main_frame, placeholder=placeholder,
                               bg=entry_bg, width=40, bd=1, relief='solid')
        ent.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)

    add_entry_row("First Name", 0, "Enter First Name...")
    add_entry_row("Last Name", 1, "Enter Last Name...")
    add_entry_row("Screen Name", 2, "Enter Screen Name...")

    lbl_dob = tk.Label(main_frame, text="Date of Birth", font=("Arial", 10, "bold"),
                       bg=body_bg, fg=label_color, anchor='e')
    lbl_dob.grid(row=3, column=0, sticky='e', padx=5, pady=5)

    dob_frame = tk.Frame(main_frame, bg=body_bg)
    dob_frame.grid(row=3, column=1, sticky='w', padx=5, pady=5)

    cb_month = ttk.Combobox(dob_frame, values=["May", "June", "July", "August"], width=10)
    cb_month.current(0)
    cb_month.pack(side='left', padx=2)

    cb_day = ttk.Combobox(dob_frame, values=[str(i) for i in range(1, 32)], width=5)
    cb_day.current(4)
    cb_day.pack(side='left', padx=2)

    cb_year = ttk.Combobox(dob_frame, values=[str(i) for i in range(1950, 2030)], width=8)
    cb_year.current(35)
    cb_year.pack(side='left', padx=2)

    lbl_gender = tk.Label(main_frame, text="Gender", font=("Arial", 10, "bold"),
                          bg=body_bg, fg=label_color, anchor='e')
    lbl_gender.grid(row=4, column=0, sticky='e', padx=5, pady=5)

    gender_frame = tk.Frame(main_frame, bg=body_bg)
    gender_frame.grid(row=4, column=1, sticky='w', padx=5, pady=5)

    var_gender = tk.StringVar(value="Male")
    rb_male = tk.Radiobutton(gender_frame, text="Male", variable=var_gender,
                             value="Male", bg=body_bg, fg=label_color,
                             selectcolor=body_bg, activebackground=body_bg)
    rb_male.pack(side='left', padx=5)
    rb_female = tk.Radiobutton(gender_frame, text="Female", variable=var_gender,
                               value="Female", bg=body_bg, fg=label_color,
                               selectcolor=body_bg, activebackground=body_bg)
    rb_female.pack(side='left')
    lbl_country = tk.Label(main_frame, text="Country", font=("Arial", 10, "bold"),
                           bg=body_bg, fg=label_color, anchor='e')
    lbl_country.grid(row=5, column=0, sticky='e', padx=5, pady=5)

    cb_country = ttk.Combobox(main_frame, values=["USA", "Russia", "China", "Germany"], width=38)
    cb_country.current(0)
    cb_country.grid(row=5, column=1, sticky='ew', padx=5, pady=5)

    add_entry_row("E-mail", 6, "Enter E-mail......")
    add_entry_row("Phone", 7, "Enter Phone......")

    lbl_pass = tk.Label(main_frame, text="Password", font=("Arial", 10, "bold"),
                        bg=body_bg, fg=label_color, anchor='e')
    lbl_pass.grid(row=8, column=0, sticky='e', padx=5, pady=5)
    ent_pass = PlaceholderEntry(main_frame, placeholder="Enter Password",
                                bg=entry_bg, width=40, show="*", bd=1, relief='solid')
    ent_pass.grid(row=8, column=1, sticky='ew', padx=5, pady=5)

    lbl_conf_pass = tk.Label(main_frame, text="Confirm Password", font=("Arial", 10, "bold"),
                             bg=body_bg, fg=label_color, anchor='e')
    lbl_conf_pass.grid(row=9, column=0, sticky='e', padx=5, pady=5)
    ent_conf_pass = PlaceholderEntry(main_frame, placeholder="Confirm Password",
                                     bg=entry_bg, width=40, show="*", bd=1, relief='solid')
    ent_conf_pass.grid(row=9, column=1, sticky='ew', padx=5, pady=5)

    check_frame = tk.Frame(main_frame, bg=body_bg)
    check_frame.grid(row=10, column=0, columnspan=2, sticky='w', padx=130, pady=15)

    var_agree = tk.IntVar()
    chk_agree = tk.Checkbutton(check_frame, text="I agree to the Terms of Use",
                               variable=var_agree, bg=body_bg, fg=label_color,
                               selectcolor=body_bg, activebackground=body_bg)
    chk_agree.pack(side='left')

    footer_frame = tk.Frame(root, bg=header_footer_bg, height=50)
    footer_frame.pack(side='bottom', fill='x')

    btn_frame = tk.Frame(footer_frame, bg=header_footer_bg)
    btn_frame.pack(side='right', padx=15, pady=10)

    btn_submit = tk.Button(btn_frame, text="submit", bg="#27ae60", fg="white",
                           font=("Arial", 10, "bold"), relief='flat',
                           padx=15, pady=5, cursor="hand2")
    btn_submit.pack(side='left', padx=5)

    btn_cancel = tk.Button(btn_frame, text="Cancel", bg="#c0392b", fg="white",
                           font=("Arial", 10, "bold"), relief='flat',
                           padx=15, pady=5, cursor="hand2")
    btn_cancel.pack(side='left', padx=5)

    root.mainloop()
create_sign_up_form()
