import tkinter as tk
import threading

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"

class BleGui(threading.Thread):
    MAX_LEN = 50

    def __init__(self,q_send,q_receive):
        self.new_msg_to_send_flag = False
        self.msg = ""
        self.q_send = q_send
        self.q_receive = q_receive
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
            #self.new_msg_to_send_flag = True
            self.q_send.put(self.msg)
            self.send_field.delete(0, 'end')
    
    def show_received_msg(self):
        msg = self.q_receive.get()
        self.received_field.delete(0, 'end')
        self.received_field.insert(0, msg)

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

        self.button.bind("<Button-1>", self.handle_send_message)

        self.send_field.place(anchor="c", relx=.5, rely=.5)
        self.button.place(anchor="c", relx=.5, rely=.65)
        self.received_field.place(anchor="c", relx=.5, rely=.5)

        self.window.mainloop()

    def callback(self):
        self.window.quit()

#gui = BleGui()
#gui.run()
#for i in range(100):
#    print(i)

""" def main():
    gui = BleGui()
    gui.run()
    for i in range(100):
        print(i) """
    
""" if __name__ == "__main__":
    main() """
    