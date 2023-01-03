import tkinter as tk
import threading
from queue import Queue

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"

class BleGui(threading.Thread):
    MAX_LEN = 50

    def __init__(self,q_send,q_receive,q_connection):
        self.new_msg_to_send_flag = False
        self.msg = ""
        self.q_send = q_send
        self.q_receive = q_receive
        self.q_connection = q_connection
        threading.Thread.__init__(self)
        self.start()

    def connection_indicator(self):
        if not self.q_connection.empty() and self.q_connection.queue[0]:
            self.connection_canvas.itemconfig(self.connection_led, fill="#55FF33")
        elif not self.q_connection.empty():
            self.connection_canvas.itemconfig(self.connection_led, fill="red")
        else:
            self.connection_canvas.itemconfig(self.connection_led, fill="grey")

        self.window.after(100,self.connection_indicator)
        
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

        self.frame_up = tk.Frame(master=self.window, width=600, height=150, bg="#EFEFEF", borderwidth=3, highlightbackground="#2F2F2F", highlightthickness=2)
        self.frame_left = tk.Frame(master=self.window, width=300, height=300, bg="#EFEFEF", borderwidth=3, highlightbackground="#2F2F2F", highlightthickness=2)
        self.frame_right = tk.Frame(master=self.window, width=300, height=300, bg="#EFEFEF", borderwidth=3, highlightbackground="#2F2F2F", highlightthickness=2)
        
        self.frame_up.pack(fill=tk.BOTH, expand=True)
        self.frame_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.connection_canvas = tk.Canvas(master=self.frame_up, width=25, height=25)  # Create 200x200 Canvas widget
        self.connection_led = self.connection_canvas.create_oval(3, 3, 21, 21)  # Create a circle on the Canvas
        self.connection_canvas.itemconfig(self.connection_led, fill="grey")

        self.title_label = tk.Label(
            master=self.frame_up,
            fg="#2F2F2F",
            bg="#EFEFEF",
            font=("Arial", 15),
            text="Ping/Pong Demonstration App")

        self.connection_label = tk.Label(
            master=self.frame_up,
            fg="#2F2F2F",
            bg="#EFEFEF",
            font=("Arial", 15),
            text="Connection: ")

        self.send_label = tk.Label(
            master=self.frame_left,
            fg="#2F2F2F",
            bg="#EFEFEF",
            font=("Arial", 15),
            text="Message to send")

        self.send_field = tk.Entry(
            master=self.frame_left,
            #bg="#7F7F7F",
            width=20,)

        self.received_label = tk.Label(
            master=self.frame_right,
            fg="#2F2F2F",
            bg="#EFEFEF",
            font=("Arial", 15),
            text="Received message")

        self.received_field = tk.Entry(
            master=self.frame_right,
            #bg="#7F7F7F",
            width=20,)

        self.button = tk.Button(
            master=self.frame_left,
            text="Send",
            width=10,
            height=2,
            bg="#2F2F2F",
            fg="yellow",
        )

        self.button.bind("<Button-1>", self.handle_send_message)

        self.title_label.place(anchor="c", relx=.5, rely=.2)
        self.connection_canvas.place(anchor="c", relx=.57, rely=0.518)
        self.connection_label.place(anchor="c", relx=.45, rely=.5)
        self.send_label.place(anchor="c", relx=.5, rely=.2)
        self.send_field.place(anchor="c", relx=.5, rely=.5)
        self.button.place(anchor="c", relx=.5, rely=.65)
        self.received_label.place(anchor="c", relx=.5, rely=.2)

        self.received_field.place(anchor="c", relx=.5, rely=.5)

        self.window.after(100,self.connection_indicator)
        self.window.mainloop()

    def callback(self):
        self.window.quit()

""" q_connection = Queue()
q_connection.put(True)
q_send = Queue()
q_receive = Queue()
gui = BleGui(q_send,q_receive,q_connection) """
#for i in range(100):
#    print(i)

""" def main():
    gui = BleGui()
    gui.run()
    for i in range(100):
        print(i) """
    
""" if __name__ == "__main__":
    main() """
    