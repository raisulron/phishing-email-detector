import tkinter as tk
from tkinter import messagebox

# List of suspicious keywords and phrases
phishing_keywords = [
    "verify your account", "click here", "urgent", "update your payment", 
    "login to your account", "suspended", "act now", "limited time"
]

def check_phishing():
    content = email_input.get("1.0", tk.END).lower()
    score = 0
    found_keywords = []

    for keyword in phishing_keywords:
        if keyword in content:
            score += 1
            found_keywords.append(keyword)

    if score == 0:
        result = "✅ Email appears safe."
    elif score <= 2:
        result = "⚠️ Email may be suspicious. Keywords found: " + ", ".join(found_keywords)
    else:
        result = "🚨 Likely phishing attempt! Keywords found: " + ", ".join(found_keywords)

    messagebox.showinfo("Scan Result", result)

# GUI Window
window = tk.Tk()
window.title("Phishing Email Detector")
window.geometry("500x400")

tk.Label(window, text="Paste the email content below:").pack(pady=10)

email_input = tk.Text(window, height=15, width=60)
email_input.pack()

scan_button = tk.Button(window, text="Scan Email", command=check_phishing, bg="blue", fg="white")
scan_button.pack(pady=10)

window.mainloop()
