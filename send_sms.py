import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import dotenv_values

class SMSSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Darkey - SMS SPOOFER")

        # Load API key from api.env file
        config = dotenv_values('api.env')
        self.api_key = config.get('SMS_API_KEY')

        if self.api_key is None:
            messagebox.showerror("Error", "API key not found in api.env file")
            root.destroy()
            return

        # GUI components
        self.label_sender = tk.Label(root, text="Sender ID:")
        self.entry_sender = tk.Entry(root)
        
        self.label_receiver = tk.Label(root, text="Receiver ID:")
        self.entry_receiver = tk.Entry(root, width=30, font=('Arial', 12))  # Increase the font size
        self.label_message = tk.Label(root, text="Message:")
        self.entry_message = tk.Text(root, width=30, height=5, font=('Arial', 12), wrap=tk.WORD, bd=5)  # Use Text for multiline input
        self.send_button = tk.Button(root, text="Send SMS", command=self.send_sms)

        # Grid layout
        self.label_sender.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_sender.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.label_receiver.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_receiver.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.label_message.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_message.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.send_button.grid(row=3, columnspan=2, pady=20)

    def send_sms(self):
        sender_id = self.entry_sender.get()
        receiver_id = self.entry_receiver.get()
        message = self.entry_message.get("1.0", tk.END).strip() 
        data = {
            'api_key': self.api_key,
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'message': message
        }

        try:
            response = requests.post('https://sms.jagrithacker.com/main.php', data=data)
            response.raise_for_status()  # Raises an error for bad response codes
            messagebox.showinfo("API Response", response.text)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SMSSenderApp(root)
    root.mainloop()
