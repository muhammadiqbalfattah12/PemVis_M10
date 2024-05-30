from tkinter import *
import tkinter.font

class PaintApp:
    drawing_tool = "pencil"
    left_button = "up"
    x_position, y_position = None, None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None
    canvas = None

    @staticmethod
    def quit_app(event=None):
        root.quit()
    def __init__ (self, root):
        self.root = root
        self.canvas = Canvas(root)
        self.canvas.pack()
        self.canvas.bind("<Motion>", self.motion)
        self.canvas.bind("<ButtonPress-1>", self.left_button_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_button_up)

        the_menu = Menu(root)
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Line", command=self.set_line_drawing_tool)
        file_menu.add_command(label="Pencil", command=self.set_pencil_drawing_tool)
        file_menu.add_command(label="Dot", command=self.set_dot_drawing_tool)

        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)
        the_menu.add_cascade(label="Options", menu=file_menu)
        root.config(menu=the_menu)
    def set_line_drawing_tool (self):
        self.drawing_tool = "line"
    def set_pencil_drawing_tool(self):
        self.drawing_tool = "pencil"
    def set_dot_drawing_tool (self):
        self.drawing_tool = "dot"
    
    def left_button_down(self, event=None):
        self.left_button = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
    def left_button_up(self, event=None):
        self.left_button = "up"
        self.x_position = None
        self.y_position = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool =="line":
            self.line_draw(event)
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)
        if self.drawing_tool == "dot":
            self.dot_draw(event)

    def motion (self, event=None):
        if self.drawing_tool =="pencil":
            self.pencil_draw(event)
        self.x_position = event.x
        self.y_position = event.y

    def pencil_draw (self, event = None):
        if self.left_button =="down":
            if self.x_position is not None and self.y_position is not None:
                self.canvas.create_line(self.x_position, self.y_position, event.x, event.y, smooth=True)
    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            self.canvas.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=True, fill="red")
    def dot_draw(self, event=None):
        self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill="black")

root = Tk()
root.title("Atun, Khansa, Fattah")
paint_app = PaintApp(root)
root.mainloop()