from tkinter import *
from tkinter import messagebox
import pywinstyles
root = Tk()
from collections import Counter
frame = Frame(root)
#defining frame and importing tkiter 
#variables that contain the piece type and grid location of the piece with the key being the tkinter name of the widget that is assorated with the piece
#dictionary that contains the location of each button as defined by grid location id [1,8] with the key of the dictionary being the widget name of the button 
white_pieces_dict = {}
black_pieces_dict = {}
button_dict = {}
#variable below is of the turn that the board is in with 0 in this case meaning white and 1 meaning black
turn = 0
move_valid = 0
first_run = True
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
                    button_dict[grid_button_var] = final_x_y_grid,grid_button_var
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                    
                else:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_y_value},Y:{grid_x_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="black")
                    button_dict[grid_button_var] = final_x_y_grid,grid_button_var
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
            piece_rules(frame=self.chess_piece_frame,piece_move_info=piecetype,button_to_move = self.button_loc_holder[0])
            self.piece_move_holder.clear()
            self.button_loc_holder.clear()
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
                piece_place_var.config(command=lambda piece_press_var = (piece_type,"white",piece_place_var):self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0))
                piece_place_var.grid(row=white_piece_y_position,column=piece_place_loop_count + 1)
                piece_place_loop_count += 1
                white_pieces_dict[piece_place_var] = (piece_grid_loaction,piece_type)
            while pawn_loop_count < 8:
                    piece_grid_loaction = [pawn_loop_count + 1,white_piece_y_position +1 ]
                    piece_place_var_pawn = Button(frame,text="pawn",height=5,width=10)
                    piece_place_var_pawn.config(command=lambda piece_press_var = ["pawn","white",piece_place_var_pawn]:self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0))
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
                    piece_place_var.config(command=lambda piece_press_var = (piece_type,"black",piece_place_var):self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0),)
                    piece_place_var.grid(row=black_piece_y_position,column=piece_place_loop_count + 1)
                    piece_place_loop_count += 1
                    black_pieces_dict[piece_place_var] = (piece_grid_loaction,piece_type) 
                while pawn_loop_count < 8:
                    piece_grid_loaction = [pawn_loop_count + 1,black_piece_y_position -1]
                    piece_place_var_pawn = Button(frame,text="pawn",height=5,width=10)
                    piece_place_var_pawn.config(command=lambda piece_press_var =["pawn","black",piece_place_var_pawn]:self.placeholder_piece_press_function(piecetype=piece_press_var,button_location=0),)
                    piece_place_var_pawn.grid(row=black_piece_y_position -1,column=pawn_loop_count + 1)
                    pawn_loop_count += 1
                    black_pieces_dict[piece_place_var_pawn] = (piece_grid_loaction,"pawn")


class piece_rules:

    def __init__(self,frame,piece_move_info,button_to_move):
        global turn
        global first_run
        
        #turn = int(turn)
        self.frame = frame
        
        
        
        if turn == 0:
            for x in black_pieces_dict.keys():
                black_piece_to_change = self.frame.nametowidget(name=x)
                black_piece_to_change.lift()
                #pywinstyles.set_opacity(piece_to_change,value=0.01)
            for x in white_pieces_dict.keys():
                white_piece_to_change = self.frame.nametowidget(name=x)
                
                
                for x in button_dict.keys():
                    button_to_change = self.frame.nametowidget(name=x)
                    pywinstyles.set_opacity(button_to_change,value=0.1)
                    
                    white_piece_to_change.lower()
                    
            
        if turn == 1:
            for x in white_pieces_dict.keys():
                white_piece_to_change = self.frame.nametowidget(name=x)
                white_piece_to_change.lift()
                #pywinstyles.set_opacity(piece_to_change,value=0.01)
            for x in black_pieces_dict.keys():
                black_piece_to_change = self.frame.nametowidget(name=x)
                
                
                for x in button_dict.keys():
                      button_to_change = self.frame.nametowidget(name=x)
                      pywinstyles.set_opacity(button_to_change,value=0.1)
                      
                      black_piece_to_change.lower()
                      
                #     break
                    #button_to_change.lift()
        if turn == 0:
                turn += 1
        else: 
                turn -= 1
        #turn_class()
        self.piece_info = piece_move_info
        # print(f"piece move info = {self.piece_info}")
        # self.piece_move_too_transfer = list(self.piece_info.keys())
        # self.piece_type_transfer = list(self.piece_info.values())
        # #print(self.piece_type_transfer)
        # self.piece_type_transfer = self.piece_type_transfer[0]
        # self.piece_move_transfer = self.piece_info.keys()
        # #print(self.piece_type_transfer)
        # print(f"piece type = {list(self.piece_move_transfer)}")
        # print(f"piece move too = {self.piece_move_too_transfer[0]}")
        # self.move_function_transfer = (self.piece_move_too_transfer[0])
        # self.piece_function_transfer = list(self.piece_type_transfer)
        # print(f"move info {self.move_function_transfer}")
        # print(f"piece function {self.piece_function_transfer[4]}")
        # self.piece_function_transfer.append(self.move_function_transfer)
        # print(self.piece_function_transfer)
        # print(f"piece info {self.piece_info}")
        #print(f"button to move = {piece_move_info[self.piece_move_transfer]}")
        #print(piece_move_info)
        print(f"turn global value = {turn}")
        #print(f"piece dict = {black_pieces_dict}")
        

        #print(f"button dict = {button_dict}")
        try:
            if str(piece_move_info[0]) == "pawn":
                self.pawn_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move)   
                taking_piece()
            if str(piece_move_info[0]) == "bishop":
                self.bishop_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move)
                taking_piece()
            if str(piece_move_info[0]) == "rook":
                self.rook_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move)
                taking_piece()
            if str(piece_move_info[0]) == "knight":
                self.knight_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move) 
                taking_piece()   
            if str(piece_move_info[0]) == "queen":
                self.queen_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move)
                taking_piece()
            if str(piece_move_info[0]) == "king":
                self.king_move_check_function(piece_move_loc=self.piece_info,move_to=button_to_move)
                taking_piece()
                
            
        except TypeError:
            #print("ok")
            self.piece_type_transfer = ""
            self.piece_move_too_transfer = ""

        piece_move_info = ""
        

    def pawn_move_check_function(self,piece_move_loc,move_to):
        # piece_current_location = []
        global turn 
        global move_valid
        global white_pieces_dict
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        # piece_current_location.append(piece_move_loc[0])
        transfer_grid_loc = piece_moving.grid_info()
        # piece_current_location.append(piece_move_loc[1])
        # piece_grid_move_to = piece_move_loc[5]
        # piece_row_move_to = piece_grid_move_to[1]
        # piece_column_move_to = piece_grid_move_to[0]
        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        piece_current_row_test = piece_current_row
        white_pieces_dict_Test = white_pieces_dict
        # white_pieces_dict_Test.pop(piece_move_loc[2])
        check_values = white_pieces_dict_Test.values()
        pieces = ['rook','knight','bishop','king','queen','pawn']
        check_values_removed = [x for x in check_values if x !=pieces]
        #print(f"white pieces dict = {white_pieces_dict_Test}")
        b = (white_pieces_dict_Test)
        location = ([piece_current_column,piece_current_row_test])
        # a = (b,'pawn')
        #print(f"a = {check_values_removed}")
        #print(f"piece move loc = {check_values_removed}")
        if piece_move_loc[1] == "white":
            # print("white piece")
            # print(f"b = {b}")
            # print(f"current row = {piece_current_row}")
            # print(f"piece current column = {piece_current_column}")
            while piece_current_row_test < (piece_current_row + 2):
                        # print("test")
                        # print(f"test dict ={white_pieces_dict_Test}")
                        # print(piece_current_row_test)
                        a = ([piece_current_column,piece_current_row_test])
                        #print(f"a = {a}")
                        if (a) in white_pieces_dict_Test.values():
                            # print(white_pieces_dict_Test)
                            # print("piece in piece")
                            print('')
                            
                        piece_current_row_test += 1
            x = 0
            while x < 2:
                bishop_test = [location[0]+x ,location[1] +x]
                print(f"pawn bishop loc = {bishop_test}")
                print(f"move to = {move_to}")
                print(x)
                x += 1
                if bishop_test == move_to:
                    print("bishop move match ")
                
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)
                    if (black_pieces_dict.items() in bishop_test) and (move_valid == 1):
                        print("pawn bishop true")
                        piece_moving.grid_configure(row=bishop_test[0],column=bishop_test[1])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x = 0
            while x < 2:
                bishop_test = [location[0]-x ,location[1] +x]
                print(f"pawn bishop loc = {bishop_test}")
                print(f"move to = {move_to}")
                print(x)
                x += 1
                if bishop_test == move_to:
                    print("bishop move match ")
                
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)
                    if (black_pieces_dict.items() in bishop_test) and (move_valid == 1):
                        print("pawn bishop true")
                        piece_moving.grid_configure(row=bishop_test[0],column=bishop_test[1])
                    elif move_valid == 0:
                        print("move invalid")
                        messagebox.showerror("error","move invalid")
                taking_piece()
            if piece_current_row == 2:
                self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)
                if (piece_current_row - move_to[1] == -2) and (move_valid == 1):
                    
                    piece_moving.grid_configure(row=piece_current_row + 2)
                    taking_piece()
                    self.__init__()
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                    
            self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)      
            if (piece_current_row - move_to[1] == -1) and(move_valid == 1):
                
                
                piece_moving.grid_configure(row=piece_current_row + 1)
                taking_piece()
                self.__init__()
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
        if piece_move_loc[1] == "black":
            # print("white piece")
            # print(move_to)
            # print(f"current row = {piece_current_row}")
            # print(f"piece current column = {piece_current_column}")
            if piece_current_row == 7:
                self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)
                if (piece_current_row - move_to[1] == 2) and (move_valid == 1):
                    
                    
                    piece_moving.grid_configure(row=piece_current_row -2)
                    taking_piece()
                    self.__init__()
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            self.move_validity_check(move_start=location,move_end=move_to,diagonal=0)
            if (piece_current_row - move_to[1]) and (move_valid == 1) == 1:
                
                
                piece_moving.grid_configure(row=piece_current_row -1)
                taking_piece()
                self.__init__()
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            
           
                
        # one_space_move = move_to[1] -1 
        # print(f"piece current location ")
        # print(f"one space move = {one_space_move}")
        # print((one_space_move == piece_current_row) == True)
        # if piece_color == "white":
        #     print(f"piece value = {(piece_current_row)}")
        #     if piece_current_row == 2:
        #           piece_grid_move_to = piece_move_loc[5]
        #           piece_row_move_to = piece_grid_move_to[1]
        #           piece_column_move_to = piece_grid_move_to[0]
        #           print(f"column move to = {piece_column_move_to}")
        #           #print(F"tuple[0] = {piece_row_move_to[0]}")
        #           two_space_move = move_to[1] - 2
        #           print(two_space_move)
        #           print(f"move to = {move_to}")
        
        #           if (piece_current_column == two_space_move):
        #               print('move accepted')
        #               piece_moving.grid_configure(row=piece_current_row + 2,column=piece_current_column)
        #               pass
        #     if (one_space_move == piece_current_row) == True:
                
               
        #         #print(two_space_move)
        #         print(f"move to = {move_to}")
        #         if (piece_current_column == one_space_move):
        #               print('move accepted')
        #               #piece_moving = self.frame.nametowidget(name=piece_to_move)
        #               piece_moving.grid_configure(row=piece_current_row + 1,column=piece_current_column)
        #               pass
        # piece_type = ""
        # piece_current_location = ""
        # piece_to_move = ""
        # move_to = ""
        # piece_row_move_to=""
        # piece_column_move_to=""



        
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

        
    def bishop_move_check_function(self,piece_move_loc,move_to):
        global move_valid
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
       
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        bishop_list_loc_list = [piece_current_column,piece_current_row]
        x = 0
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]+x ,bishop_list_loc_list[1] +x]
            # print(f"bishop loc = {bishop_test}")
            # print(f"move to = {move_to}")
            # print(x)

            if bishop_test == move_to:
                print("bishop move match ")
                
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    print("move 1")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        x = 0
    
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]+x ,bishop_list_loc_list[1] -x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if bishop_test == move_to:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    print("move 2")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        x = 0
        
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]-x ,bishop_list_loc_list[1] +x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if (bishop_test == move_to) == True:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    print("move 3")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        x = 0
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]-x ,bishop_list_loc_list[1] -x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if (bishop_test == move_to) == True:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    print("move 4")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
    def rook_move_check_function(self,piece_move_loc,move_to):
        global move_valid
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        
        print(move_to)
        print(piece_current_column)
        print(piece_current_row)
        if piece_current_column == move_to[0]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0)
            if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1])
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
        if piece_current_row == move_to[1]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0)
            if move_valid == 1:
                piece_moving.grid_configure(column=move_to[0])
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
    def knight_move_check_function(self,piece_move_loc,move_to):
        
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        
       
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        
        print(move_to)
        print(piece_current_column)
        print(piece_current_row)
        if move_to == [piece_current_column -2,piece_current_row - 1]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()
    
        if move_to == [piece_current_column +2,piece_current_row - 1]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()

        if move_to == [piece_current_column -1,piece_current_row - 2]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])  
            taking_piece()      

        if move_to == [piece_current_column +1,piece_current_row +2]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()
        
        if move_to == [piece_current_column -1,piece_current_row +2]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()
        if move_to == [piece_current_column -2,piece_current_row +1]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()
        if move_to == [piece_current_column +2,piece_current_row +1]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()
        if move_to == [piece_current_column +1,piece_current_row +2]:
            piece_moving.grid_configure(row=move_to[1],column=move_to[0])
            taking_piece()




        
    def queen_move_check_function(self,piece_move_loc,move_to):
        global move_valid
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        bishop_list_loc_list = [piece_current_column,piece_current_row]
        x = 0
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]+x ,bishop_list_loc_list[1] +x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if bishop_test == move_to:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            
                taking_piece()
            x += 1
        x = 0
    
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]+x ,bishop_list_loc_list[1] -x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if bishop_test == move_to:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        x = 0
        
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]-x ,bishop_list_loc_list[1] +x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if (bishop_test == move_to) == True:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        x= 0
        while x < 10:
            bishop_test = [bishop_list_loc_list[0]-x ,bishop_list_loc_list[1] -x]
            print(f"bishop loc = {bishop_test}")
            print(f"move to = {move_to}")
            print(x)

            if (bishop_test == move_to) == True:
                print("bishop move match ")
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1)
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        
        print(move_to)
        print(piece_current_column)
        print(piece_current_row)
        if piece_current_column == move_to[0]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0)
            if move_valid == 1:
                piece_moving.grid_configure(row=move_to[1])

            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
        if piece_current_row == move_to[1]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0)
            if move_valid == 1:
                piece_moving.grid_configure(column=move_to[0])
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
    def king_move_check_function(self,piece_move_loc,move_to):
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        if (piece_current_column + 1) == move_to[0]:
            piece_moving.grid_configure(column=move_to[0])
            taking_piece()
        if (piece_current_column -1) == move_to[0]:
            piece_moving.grid_configure(column=move_to[0])
            taking_piece()

        if (piece_current_row + 1) == move_to[1]:
            piece_moving.grid_configure(row=move_to[1])
            taking_piece()
        if (piece_current_row - 1) == move_to[1]:
            piece_moving.grid_configure(row=move_to[1])
            taking_piece()


    def move_validity_check(self,move_start,move_end,diagonal):
        global move_valid
        move_valid == 0
        piece_locations = []
        row_change = False
        column_change = False
        print(white_pieces_dict)
        for x in white_pieces_dict.keys():
            print(x)
            piece_moving = self.frame.nametowidget(name=x)
            transfer_grid_loc = piece_moving.grid_info()

            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            append_list = [piece_current_column,piece_current_row]
            piece_locations.append(append_list)
            print(f"piece location = {piece_locations}")
            print(f"x = {x}")
        for x in black_pieces_dict.keys():
            print(x)
            piece_moving = self.frame.nametowidget(name=x)
            transfer_grid_loc = piece_moving.grid_info()

            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            append_list = [piece_current_column,piece_current_row]
            piece_locations.append(append_list)
            print(f"piece location = {piece_locations}")
            print(f"x = {x}")
        piece_locations.remove(move_start)
        print(f"move start = {move_start}")
        print(f"move end = {move_end}")
        if (move_start[0] == move_end[0]) == True:
            row_change = True
            #ensure true/false changes
            print("A")
        if (move_start[1] == move_end[1]) == True:
            column_change = True
        print(f"row = {row_change}")
        print(f"column = {column_change}")
        
        piece_in_the_way_if_rows_true = abs(move_end[1] - move_start[1])
        filtered_piece_row = []
        filtered_piece_column = []
        print(f"piece locations 2 {piece_locations}")
        for x in piece_locations:
            if x[0] == move_start[0]:
                filtered_piece_row.append(x)
        for x in piece_locations:
            if x[1] == move_start[1]:
                filtered_piece_column.append(x)
        if row_change == True:
            print("a",piece_in_the_way_if_rows_true)
            for x in filtered_piece_row:
                print(f"filtered = {x}")
                range_list = [move_start[1],move_end[1]]
                range_list.sort()
                if x[1] in range(range_list[0],range_list[1]):
                      print("piece moving through")
                      move_valid == 0

        
                  
        if column_change == True:
            print("a",piece_in_the_way_if_rows_true)
            for x in filtered_piece_column:
                print(f"filtered = {x}")
                range_list2 = [move_start[0],move_end[0]]
                range_list2.sort()
                if x[0] in range(int(range_list2[0]),int(range_list2[1])):
                    print("piece moving through")
                    
                    move_valid == 0
        if diagonal == 1:
                if column_change == True:
                    print("a",piece_in_the_way_if_rows_true)
                loop_amount = 0
                print("bishop")
                while loop_amount < 10:
                    print("bishop2")
                    check_list = [move_start[0] - loop_amount,move_start[1]- loop_amount]
                    loop_amount += 1
                    if check_list == move_end:
                        print("move match")
                        loop_anoumt_move_through = 0
                        while loop_anoumt_move_through < 10:
                            move_through_check = [move_start[0]-loop_anoumt_move_through,move_start[1]-loop_anoumt_move_through]
                            loop_anoumt_move_through += 1
                            if move_through_check in piece_locations:
                                print("bishop moving through")
                                move_valid == 0
                loop_amount = 0
                while loop_amount < 10:
                    check_list = [move_start[0] + loop_amount,move_start[1]- loop_amount]
                    loop_amount += 1
                    if check_list == move_end:
                        loop_anoumt_move_through = 0
                        while loop_anoumt_move_through < 10:
                            move_through_check = [move_start[0]+loop_anoumt_move_through,move_start[1]-loop_anoumt_move_through]
                            loop_anoumt_move_through += 1
                            if move_through_check in piece_locations:
                                print("bishop moving through")
                                move_valid == 0
                loop_amount = 0
                while loop_amount < 10:
                    check_list = [move_start[0] - loop_amount,move_start[1]+ loop_amount]
                    loop_amount += 1
                    if check_list == move_end:
                        loop_anoumt_move_through = 0
                        while loop_anoumt_move_through < 10:
                            move_through_check = [move_start[0]-loop_anoumt_move_through,move_start[1]+loop_anoumt_move_through]
                            loop_anoumt_move_through += 1
                            if move_through_check in piece_locations:
                                print("bishop moving through")
                                move_valid == 0
                loop_amount = 0
                while loop_amount < 10:
                    check_list = [move_start[0] + loop_amount,move_start[1]+ loop_amount]
                    loop_amount += 1
                    if check_list == move_end:
                        loop_anoumt_move_through = 0
                        while loop_anoumt_move_through < 10:
                            move_through_check = [move_start[0]+loop_anoumt_move_through,move_start[1]+loop_anoumt_move_through]
                            loop_anoumt_move_through += 1
                            if move_through_check in piece_locations:
                                print("bishop moving through")
                                move_valid == 0
                loop_amount = 0
                while loop_amount < 10:
                    check_list = [move_start[0] + loop_amount,move_start[1]- loop_amount]
                    loop_amount += 1
                    if check_list == move_end:
                        loop_anoumt_move_through = 0
                        while loop_anoumt_move_through < 10:
                            move_through_check = [move_start[0]+loop_anoumt_move_through,move_start[1]+loop_anoumt_move_through]
                            loop_anoumt_move_through += 1
                            if move_through_check in piece_locations:
                                print("bishop moving through")
                                move_valid == 0
                for x in filtered_piece_column:
                    print(f"filtered = {x}")
                    range_list2 = [move_start[0],move_end[0]]
                    range_list2.sort()
                    if x[0] in range(int(range_list2[0]),int(range_list2[1])):
                        print("piece moving through")
                    
                        move_valid = 0
                # if move_start[0] in range piece_in_the_way_if_rows_true:
                #     print("B")

            #print(f"piece location rows {piece_locations_rows}")
            
            # loop_num = 0 
            # move_test = []
            # move_test[0] == loop_num
            # move_test[1] == move_start[1]

            # while loop_num > abs(move_start[0] - move_end[0]):
            #     move_test[0] == loop_num
            #     if move_test in piece_locations:
            #         print("piece move through")
            #     loop_num += 1

        return
        
class taking_piece:
    def __init__(self):
        self.frame = frame
        global black_pieces_dict
        global white_pieces_dict
        global turn 
        self.take()
    #0 in turn = white move 1 in turn = black move
    def take(self):
        take = False
        take2 = False
        white_pieces_location_list = {}
        black_pieces_location_list = {}
        for x in white_pieces_dict.items():
            #print(f"white = {x}")
            white_piece_taking_widget = self.frame.nametowidget(x[0])
            transfer_grid_loc = white_piece_taking_widget.grid_info()
        
            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            location_append1 = [piece_current_column,piece_current_row]
            white_pieces_location_list[x[0]] = (location_append1)
            #print(f"white pieces list = {white_pieces_location_list}")
        for x in black_pieces_dict.items():
            #print(f"white = {x}")
            black_piece_taking_widget = self.frame.nametowidget(x[0])
            transfer_grid_loc = black_piece_taking_widget.grid_info()
        
            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            location_append2 = [piece_current_column,piece_current_row]
            black_pieces_location_list[x[0]] = (location_append2)
            #print(f"black pieces list = {black_pieces_location_list}")
        #check_white = [whitegrid for whitegrid in white_pieces_location_list.items()]
        #check_black = [blackgrid for blackgrid in black_pieces_location_list.items()]
        temp_list1 = []
        temp_list2 = []  
        a = (white_pieces_location_list)
        b = (black_pieces_location_list)
        #print(a)
        #print(set(a))
        print("overlap")
        
        for blackname,item in b.items():
            
            if item in a.values():
                take = True
                
                break  
        for whitename,item in a.items():
            
            if item in b.values():
                take2 = True
                # print(item)
                # print(take)
                # print(whitename)
                break  
                
        
            
        if take and take2 == True:
            
            if turn == 0:
              print("take")
              piece_remove = self.frame.nametowidget(whitename)
              if piece_remove.cget("text") == "king":
                    print("white wins")
              piece_remove.grid_forget()
              white_pieces_dict.pop(whitename)
              piece_remove.destroy()
              
            if turn == 1:
                print('take')
                piece_remove = self.frame.nametowidget(blackname)
                if piece_remove.cget("text") == "king":
                    print("black wins")
                piece_remove.grid_forget()
                black_pieces_dict.pop(blackname)
                piece_remove.destroy()

app = chess_board_create_class(root)

app.root.mainloop()