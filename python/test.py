# Run tkinter code in another thread

import tkinter as tk
import threading

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def handle_send_message(self, event):
        self.msg = self.send_field.get()
        if len(self.msg) == 0:
            print("Cannot send empty message.")
        elif len(self.msg) >= self.MAX_LEN:
            print("Message is too long (message length is {}, maximum length is {})."
                .format(len(self.msg),self.MAX_LEN))
        else:
            print("Sent message \'{}\'.".format(self.msg))
            self.send_field.delete(0, 'end')

    def run(self):
        self.window = tk.Tk()

        self.frame_left = tk.Frame(master=self.window, width=300, height=300, bg="red", borderwidth=3)
        self.frame_right = tk.Frame(master=self.window, width=300, height=300, bg="yellow", borderwidth=3)

        self.frame_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.send_label = tk.Label(
            master=self.frame_left,
            text="Message to send")

        self.send_field = tk.Entry(
            master=self.frame_left,
            width=20,)

        self.received_label = tk.Label(
            master=self.frame_right,
            text="Received message")

        self.received_field = tk.Entry(
            master=self.frame_right,
            width=20,)

        self.button = tk.Button(
            master=self.frame_left,
            text="Send",
            width=10,
            height=2,
            bg="blue",
            fg="yellow",
        )

        self.send_field.place(anchor="c", relx=.5, rely=.5)
        self.button.place(anchor="c", relx=.5, rely=.65)
        self.received_field.place(anchor="c", relx=.5, rely=.5)

        self.button.bind("<Button-1>", self.handle_send_message)

        self.window.mainloop()


app = App()
print('Now we can continue running code while mainloop runs!')

for i in range(100):
    print(i)