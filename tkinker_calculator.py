import tkinter as tk

# GUI Tkinter menampilkan UInya, warna gelap biru, tulisan diatas di line 5
window = tk.Tk()
window.title("Calculator V2023.03")
window.configure(bg="#202124")

# Tabel kotak untuk melihat angka yang diinput & output,
result_label = tk.Label(window, text="", width=30, height=2, bg="#282a2e", fg="white", anchor="e", font=("Arial", 15))
result_label.grid(row=0, column=0, columnspan=5, padx=4, pady=4)

# Function for backspace
def backspace():
    current_text = result_label.cget("text")
    if len(current_text) > 0:
        result_label.config(text=current_text[:-1])

# Urutan button dari kiri atas ke kanan bawah (5 vert kolumn, 4 horz row)
button_list = [
    "7", "8", "9", "DEL", "Bck",
    "4", "5", "6", "*", "-",
    "1", "2", "3", "(", ")",
    "=", "0", ".", "/", "+"
]
# mendefinisikan button
bt_colors = {
    "num_op": "#2c3c52",
    "fungsi": "#3b3e42",
    "equals": "#FF9800",
    "erase": "#423b3b"
}
button_row = 1
button_col = 0
for button_text in button_list:
    # Perilaku button
    def button_click_handler(button_text=button_text):
        if button_text == "DEL":
            result_label.config(text="")
        elif button_text == "Bck":
            backspace()
        elif button_text == "=":
            try:
                result = eval(result_label.cget("text"))
                result_label.config(text=str(result))
            except:
                result_label.config(text="Error")
        else:
            result_label.config(text=result_label.cget("text") + button_text)

    # warna button
    bt_type = ""
    if button_text in ["+", "-", "*", "/", "(", ")"]:
        bt_type = "num_op"
    elif button_text in ["DEL","Bck"]:
        bt_type = "erase"
    elif button_text in ["="]:
        bt_type = "equals"
    else:
        bt_type = "fungsi"
    bt_color = bt_colors[bt_type]

    button = tk.Button(window, text=button_text, width=5, height=2, bg=bt_color, fg="white", command=button_click_handler, font=("Arial", 16))
    button.grid(row=button_row, column=button_col, padx=5, pady=5)
    button_col += 1
    if button_col > 4:
        button_col = 0
        button_row += 1

window.mainloop()
