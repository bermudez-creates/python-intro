import tkinter

root = tkinter.Tk()
root.title("Mad lib")
root.resizable(False, False)

canvas = tkinter.Canvas(root, bg="black", width= 300, height=300, borderwidth= 0, highlightthickness=0 )
canvas.pack()
root.update()

# center window
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x = int((screen_width / 2) - (root_width / 2))
root_y = int((screen_height / 2) - (root_height / 2))
#format: "(w)x(h)+(x)+(y)"
root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")




# Keeps window open
root.mainloop()