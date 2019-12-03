from tkinter import * # For GUI
import smtplib # Module for sending mails
from tkinter import messagebox # for displaying message box

root = Tk()

# This fucntion will be called when the user will click on send mail button
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Your Username', 'Your Password')
    user_given_to_text = user_to_text.get()
    user_given_message_text = message_text.get(1.0, END)
    server.sendmail('Your Username', user_given_to_text, user_given_message_text)
    server.quit()
    messagebox.showinfo('Congratulation', 'Your Message has been sent successfully.')

# For making our code shorter and more readble i have created this function that will return a text
def reusable_text(user_text, user_row, user_column):
    return Label(root, text=user_text, fg='black', font=('Arial', 16, 'bold'),
                 ).grid(row=user_row, column=user_column)

# ================================= GUI =============================== #
# ================== TO ================ #
reusable_text('TO: ', 0, 0)
user_to_text = StringVar()
to_entry = Entry(root, bg='powder blue', fg='black', font=('Arial', 16, 'bold'),
                 textvariable=user_to_text, width=40, bd=6).grid(row=0, column=1)

# ====== MESSAGE AREA ============= #
reusable_text('MESSAGE: ', 1, 0)
message_text = Text(root, bg='powder blue', fg='black', font=('Arial', 16, 'bold')
                    , bd=6, width=40, height=6)
message_text.grid(row=1, column=1)

# ================ BUTTON =============== #
btn_Send_Mail = Button(root, width=38, text='Send Mail', bg='powder blue',
                       fg='black', font=('Arial', 16, 'bold'), bd=6, command=send_mail).grid(row=2, column=1, pady=5)
root.mainloop()
