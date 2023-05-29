import tkinter as tk


def on_botton_press(panel):
    panel.pack(side="bottom", fill="both", expand="yes")

def main():
    root = tk.Tk()
    root.title("question :)")
    root.geometry('600x400')
    photo_image = tk.PhotoImage(file=r"unit6/img.png")
    panel = tk.Label(root, image=photo_image)

    tk.Label(root, text="whats my favorite animal?").pack()
    tk.Button(root, text="show the answer", command=lambda: on_botton_press(panel)).pack()
    root.mainloop()



if __name__ == '__main__':
    main()