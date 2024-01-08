


import turtle

class Maze:
    def __init__(self, maze_filename):
        self.mazeblock_color = "#ffe227"
        self.dotsize = 15
        self.mazebg_color = "#f4f4f2"
        self.boxedge = 3
        self.dotcolor_tried = "#bbbfca"

        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_filename,"r")
        
        for line in maze_file:
            row_list = []
            column_index = 0
            for char in line[:-1]:
                row_list.append(char)
                if char == "S":
                    self.start_row = rows_in_maze
                    self.start_column = column_index
                column_index += 1
            rows_in_maze += 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)
        
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = - columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        
        self.t = turtle.Turtle()
        
        turtle.setup(width = 600, height = 600)
        turtle.bgcolor(self.mazebg_color)
        turtle.title("Maze")
        turtle.setworldcoordinates((-(columns_in_maze - 1) / 2 - 0.5),
                            (-(rows_in_maze - 1) / 2 - 0.5),
                            (columns_in_maze - 1) / 2 + 0.5,
                            (rows_in_maze - 1) / 2 + 0.5)
        
        
        
    def draw_maze(self):
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_box(x + self.x_translate,
                                 -y + self.y_translate, self.mazeblock_color)
        self.t.shapesize(3,3,3)
        self.t.fillcolor("red")
    
    def draw_box(self, x, y, color):
        turtle.tracer(0) # 省略绘图过程，加速绘图
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color("black",color)
        self.t.pensize(self.boxedge)
        self.t.setheading(90) # 设置绝对角度，90 代表 x 轴正半轴方向
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90) # 相对角度，90 代表向右转动 90 度
        self.t.end_fill()
        turtle.update()
        turtle.tracer(1)
    
    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,
                                       -y + self.y_translate))
        self.t.goto(x + self.x_translate, 
                   -y + self.y_translate)
    
    def drop_bread_crumb(self, color):
        self.t.dot(self.dotsize, color)
        
    def update_position(self, row, column, value=None):
        if value:
            self.maze_list[row][column] = value # 把 maze 相应点的状态改成 value
        self.move_turtle(column, row)
        
        if value == OBSTACLE:
            color = "red"
        elif value == PART_OF_PATH:
            color = "forest green" # refer to: "TkInter color charts"
        elif value == TRIED:
            color = self.dotcolor_tried
        elif value == DEAD_END:
            color = "red2"
        else:
            color = None
        
        if color:
            self.drop_bread_crumb(color)
        
    def is_exit(self, row, column):
        return (row == 0 or
                row == self.rows_in_maze - 1 or
                column == 0 or
                column == self.columns_in_maze -1)
    
    def __get_item__(self, index):
        return self.maze_list[index]

def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)
    
    # Three base cases of recursion:
    if maze.maze_list[start_row][start_column] == OBSTACLE:
        return False
    elif maze.maze_list[start_row][start_column] == TRIED:
        return False
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    
    maze.update_position(start_row, start_column, TRIED)
    
    found = search_from(maze, start_row - 1, start_column) or \
            search_from(maze, start_row, start_column + 1) or \
            search_from(maze, start_row + 1, start_column) or \
            search_from(maze, start_row, start_column - 1)
    
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
        
    return found

PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"

my_maze = Maze("maze_1.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_column)
search_from(my_maze, my_maze.start_row, my_maze.start_column)
turtle.done()
