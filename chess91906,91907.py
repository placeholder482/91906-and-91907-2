from tkinter import *

root = Tk()

frame = Frame(root)
#defining frame and importing tkiter 
#variables that contain the piece type and grid location of the piece with the key being the tkinter name of the widget that is assorated with the piece
#dictionary that contains the location of each button as defined by grid location id [1,8] with the key of the dictionary being the widget name of the button 
white_pieces_dict = {}
black_pieces_dict = {}
button_dict = {}
#variable below is of the turn that the board is in with 0 in this case meaning white and 1 meaning black
turn = 0

#creation of class that contains frame and loop which places the buttons that act as the squares of the chess board that being 64 in total 
class chess_board_create_class:
    

    def __init__(self,root):
        self.root = root
        self.container = Frame(self.root)
        self.root.geometry("800x800")
        self.main_board_create_function()
    #place holder function to check buttons are pressed
    def placeholder_button_press_function(self,button_var):
        print("button pressed ")
        print(button_var)


    #function that places buttons into grid format
    def main_board_create_function(self):
        #variables that determine what grid location in which the buttons are placed at and defining of frame that the function will ultlise 
       
        grid_x_value = 0
        grid_y_value = 0
        frame_main_board_function = (self.container)
        frame_main_board_function.rowconfigure((0,1,2,3,4,5,6,7),minsize=100,weight=1)
        frame_main_board_function.columnconfigure((0,1,2,3,4,5,6,7),minsize=100,weight=1)
        loop_run_amount = 0
        grid_squares = [8,8]
        while grid_y_value < grid_squares[1]:
            grid_y_value += 1
            grid_x_value = 0
            loop_run_amount += 1
            while grid_x_value < grid_squares[0]:
                grid_x_value += 1
                print('yes')
                final_x_y_grid = [grid_x_value,grid_y_value]
                if loop_run_amount % 2 == 0:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_x_value},Y:{grid_y_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="black")
                    button_dict[grid_button_var] = final_x_y_grid
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                    
                else:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_x_value},Y:{grid_y_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="white")
                    button_dict[grid_button_var] = final_x_y_grid
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                
            
                loop_run_amount += 1
                print(button_dict)
        
            



        frame_main_board_function.grid()







app = chess_board_create_class(root)

app.root.mainloop()