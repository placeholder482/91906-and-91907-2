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
        self.passing = chess_board_piece_place(main_chess_board_frame=self.container)
    #place holder function to check buttons are pressed
    def placeholder_button_press_function(self,button_var):
        print("button pressed ")
        print(button_var)
        self.passing.placeholder_piece_press_function(piecetype=0,button_location=button_var)

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
                final_x_y_grid = [grid_y_value,grid_x_value]
                if loop_run_amount % 2 == 0:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_y_value},Y:{grid_x_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="black")
                    button_dict[grid_button_var] = final_x_y_grid
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                    
                else:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_y_value},Y:{grid_x_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="white")
                    button_dict[grid_button_var] = final_x_y_grid
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                
            
                loop_run_amount += 1
                print(button_dict)
        
            



        frame_main_board_function.grid()

#creation of class that places and puts the pieces into a team 
class chess_board_piece_place:

    def __init__(self,main_chess_board_frame):
        self.chess_piece_frame = (main_chess_board_frame)   
        self.piece_type_list = ["rook","knight","bishop","king","queen","bishop","knight","rook"]
        self.piece_move_holder = {}
        self.button_loc_holder = []
        self.piece_loc_holder = []
        self.move_check = [False,False]
        self.main_piece_place_function()

        #function with placeholder is to be removed and replaced with actual function 
        #purpose of function below is to take the positon of the piece that the user clicks and the locaiton of the button that is where the user wants to move the piece to and passes that to component 4

    def placeholder_piece_press_function(self,piecetype,button_location):
        print(f"piece type is {piecetype}")
        
        # print(f"white pieces are {white_pieces_dict}")
        # print(f"black pieces are {black_pieces_dict}")
        try:
            if button_location == 0:
                print(f"piece type = {piecetype[0]}")
                transfer_str = str(piecetype[0])
                self.piece_loc_holder.insert(0,piecetype)
                self.move_check[0] = True
            if piecetype == 0:
                self.button_loc_holder.insert(0,button_location)
                print(f"button location = {button_location}")
                self.move_check[1] = True
        except KeyError and TypeError:
            print("A")
        print(self.piece_loc_holder,self.button_loc_holder)
        if self.move_check == [True,True]:
            #self.piece_move_holder[str(self.button_loc_holder)].append(str(self.piece_loc_holder))
            piece_holder = (self.piece_loc_holder[0])
            button_holder = (self.button_loc_holder[0])
            print(f"button = {[button_holder[0],button_holder[1]]}")
            self.piece_move_holder[button_holder[0],button_holder[1]]= piece_holder
            print(f"piece move2 = {self.piece_move_holder}")
            piece_rules(frame=self.chess_piece_frame,piece_move_info=self.piece_move_holder,button_to_move = self.button_loc_holder[0])
            self.piece_move_holder.clear()
            self.move_check = [False,False]
    def main_piece_place_function(self):
        global black_pieces_dict
        global white_pieces_dict
        frame = self.chess_piece_frame
        piece_place_loop_count = 0
        placing_white_or_black = 0
        #0 = white 1 = black order does not matter
        white_piece_y_position = 1
        black_piece_y_position = 8
        pawn_loop_count = 0 
        if placing_white_or_black == 0:
            
            while piece_place_loop_count < len(self.piece_type_list):
                
                piece_grid_loaction = [piece_place_loop_count + 1,white_piece_y_position]
                print("white piece placed")
                piece_type = self.piece_type_list[piece_place_loop_count]
                piece_place_var = Button(frame,text=self.piece_type_list[piece_place_loop_count],height=5,width=10)
                piece_place_var.config(command=lambda piece_press_var = (piece_grid_loaction[0],piece_grid_loaction[1],piece_type,"white",piece_place_var):self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0))
                piece_place_var.grid(row=white_piece_y_position,column=piece_place_loop_count + 1)
                piece_place_loop_count += 1
                white_pieces_dict[piece_place_var] = (piece_grid_loaction,piece_type)
            while pawn_loop_count < 8:
                    piece_grid_loaction = [pawn_loop_count + 1,white_piece_y_position +1 ]
                    piece_place_var_pawn = Button(frame,text="pawn",height=5,width=10)
                    piece_place_var_pawn.config(command=lambda piece_press_var = [piece_grid_loaction[0],piece_grid_loaction[1],"pawn","white",piece_place_var_pawn]:self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0))
                    piece_place_var_pawn.grid(row=white_piece_y_position + 1,column=pawn_loop_count + 1)
                    pawn_loop_count += 1
                    white_pieces_dict[piece_place_var_pawn] = (piece_grid_loaction,"pawn")
            if piece_place_loop_count == len(self.piece_type_list):
                piece_place_loop_count = 0
                pawn_loop_count = 0
                while piece_place_loop_count < len(self.piece_type_list):
                    piece_grid_loaction = [piece_place_loop_count + 1,black_piece_y_position]
                    print("black piece placed")
                    piece_type = self.piece_type_list[piece_place_loop_count]
                    piece_place_var = Button(frame,text=self.piece_type_list[piece_place_loop_count],height=5,width=10)
                    piece_place_var.config(command=lambda piece_press_var = (piece_grid_loaction[0],piece_grid_loaction[1],piece_type,"black",piece_place_var):self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0),)
                    piece_place_var.grid(row=black_piece_y_position,column=piece_place_loop_count + 1)
                    piece_place_loop_count += 1
                    black_pieces_dict[piece_place_var] = (piece_grid_loaction,piece_type) 
                while pawn_loop_count < 8:
                    piece_grid_loaction = [pawn_loop_count + 1,black_piece_y_position -1]
                    piece_place_var_pawn = Button(frame,text="pawn",height=5,width=10)
                    piece_place_var_pawn.config(command=lambda piece_press_var =[piece_grid_loaction[0],piece_grid_loaction[1],"pawn","black",piece_place_var_pawn]:self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0),)
                    piece_place_var_pawn.grid(row=black_piece_y_position -1,column=pawn_loop_count + 1)
                    pawn_loop_count += 1
                    black_pieces_dict[piece_place_var_pawn] = (piece_grid_loaction,"pawn")


class piece_rules:

    def __init__(self,frame,piece_move_info,button_to_move):
        self.frame = frame
        self.piece_info = piece_move_info
        print(f"piece move info = {self.piece_info}")
        self.piece_move_too_transfer = list(self.piece_info.keys())
        self.piece_type_transfer = list(self.piece_info.values())
        #print(self.piece_type_transfer)
        self.piece_type_transfer = self.piece_type_transfer[0]
        self.piece_move_transfer = self.piece_info.keys()
        #print(self.piece_type_transfer)
        print(f"piece type = {list(self.piece_move_transfer)}")
        print(f"piece move too = {self.piece_move_too_transfer[0]}")
        self.move_function_transfer = (self.piece_move_too_transfer[0])
        self.piece_function_transfer = list(self.piece_type_transfer)
        print(f"move info {self.move_function_transfer}")
        print(f"piece function {self.piece_function_transfer[4]}")
        self.piece_function_transfer.append(self.move_function_transfer)
        print(self.piece_function_transfer)
        print(f"piece info {self.piece_info}")
        #print(f"button to move = {piece_move_info[self.piece_move_transfer]}")
        if str(self.piece_type_transfer[2]) == "pawn":
            self.pawn_move_check_function(piece_type=self.piece_type_transfer[2],piece_move_loc=self.piece_function_transfer,piece_color=self.piece_type_transfer[3],move_to=button_to_move,piece_to_move=self.piece_function_transfer[4])    
        if str(self.piece_type_transfer[2]) == "bishop":
            print('a')
        if str(self.piece_type_transfer[2]) == "rook":
            print('a')
        if str(self.piece_type_transfer[2]) == "knight":
            print('a')
        if str(self.piece_type_transfer[2]) == "queen":
            print('a')
        if str(self.piece_type_transfer[2]) == "king":
            print('a')
        self.piece_type_transfer = ""
        self.piece_move_too_transfer = ""

    def pawn_move_check_function(self,piece_type,piece_move_loc,piece_color,move_to,piece_to_move):
        piece_current_location = []
        piece_moving = self.frame.nametowidget(name=piece_to_move)
        piece_current_location.append(piece_move_loc[0])
        transfer_grid_loc = piece_moving.grid_info()
        piece_current_location.append(piece_move_loc[1])
        piece_grid_move_to = piece_move_loc[5]
        piece_row_move_to = piece_grid_move_to[1]
        piece_column_move_to = piece_grid_move_to[0]
        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        one_space_move = move_to[1] -1 
        print(f"piece current location ")
        print(f"one space move = {one_space_move}")
        print((one_space_move == piece_current_row) == True)
        if piece_color == "white":
            print(f"piece value = {(piece_current_row)}")
            if piece_current_row == 2:
                  piece_grid_move_to = piece_move_loc[5]
                  piece_row_move_to = piece_grid_move_to[1]
                  piece_column_move_to = piece_grid_move_to[0]
                  print(f"column move to = {piece_column_move_to}")
                  #print(F"tuple[0] = {piece_row_move_to[0]}")
                  two_space_move = move_to[1] - 2
                  print(two_space_move)
                  print(f"move to = {move_to}")
        
                  if (piece_current_column == two_space_move):
                      print('move accepted')
                      piece_moving.grid_configure(row=piece_current_row + 2,column=piece_current_column)
                      pass
            if (one_space_move == piece_current_row) == True:
                
               
                #print(two_space_move)
                print(f"move to = {move_to}")
                if (piece_current_column == one_space_move):
                      print('move accepted')
                      #piece_moving = self.frame.nametowidget(name=piece_to_move)
                      piece_moving.grid_configure(row=piece_current_row + 1,column=piece_current_column)
                      pass
        piece_type = ""
        piece_current_location = ""
        piece_to_move = ""
        move_to = ""
        piece_row_move_to=""
        piece_column_move_to=""



        
        # piece_point_to_move_too = []
        # piece_point_to_move_too.append(piece_move_loc[4])
        # if piece_color == "white":
        #     if piece_current_location[1] == 2:
        #         two_space_move = move_to[1] + 1
        #         print(two_space_move)
        #         if (piece_current_location[1] == two_space_move):
        #             print('move accepted')
        # match_var = piece_current_location,piece_type
        # print(match_var)
        # print(piece_color)
        # if piece_color == "white":
        #     for x,b in white_pieces_dict.items():

        #         print(x)
        #         print(f"b = {b}")
        #         if x == match_var:
        #             print("yes")
        #             #print(white_pieces_dict[x])



    def rook_move_check_function(self,piece_type,piece_move_loc):
        pass
    def knight_move_check_function(self,piece_type,piece_move_loc):
        pass
    def bishop_move_check_function(self,piece_type,piece_move_loc):
        pass
    def queen_move_check_function(self,piece_type,piece_move_loc):
        pass
    def king_move_check_function(self,piece_type,piece_move_loc):
        pass


app = chess_board_create_class(root)

app.root.mainloop()