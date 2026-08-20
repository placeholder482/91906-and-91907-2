from tkinter import *
from tkinter import messagebox
import pywinstyles
import json
import ast
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
    #class that creates chess board and frame 

    def __init__(self,root):
        self.root = root
        self.container = Frame(self.root)
        self.root.geometry("800x800")
        self.main_board_create_function()
        self.passing = chess_board_piece_place(main_chess_board_frame=self.container)
        #self.passing_save_game = file_saving(root=root)
        

    #place holder function to check buttons are pressed
    def placeholder_button_press_function(self,button_var):
        print("button pressed ")
        print(button_var)
        self.passing.placeholder_piece_press_function(piecetype=0,button_location=button_var)
        #passes button location to piece movmenet 

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
                #print('yes')
                final_x_y_grid = [grid_y_value,grid_x_value]
                if loop_run_amount % 2 == 0:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_y_value},Y:{grid_x_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="black")
                    button_dict[grid_button_var] = final_x_y_grid,grid_button_var
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                    #loop to make buttons in chess board pattern
                else:
                    grid_button_var = Button(frame_main_board_function,text=f"X:{grid_y_value},Y:{grid_x_value}",command=lambda button_command_var = final_x_y_grid:self.placeholder_button_press_function(button_var=button_command_var),height=5,width=10,bg="black")
                    button_dict[grid_button_var] = final_x_y_grid,grid_button_var
                    grid_button_var.grid(row=grid_x_value,column=grid_y_value)
                
            
                loop_run_amount += 1
                #print(button_dict)
        
            



        frame_main_board_function.grid()

#creation of class that places and puts the pieces into a team 
class chess_board_piece_place:

    def __init__(self,main_chess_board_frame):
        self.chess_piece_frame = (main_chess_board_frame)   
        self.piece_type_list = ["rook","knight","bishop","king","queen","bishop","knight","rook"]
        self.piece_move_holder = {}
        self.button_loc_holder = []
        self.piece_loc_holder = []
        self.move_check = [0,0]
        self.piece_move_holder_piece_click_first = {}
        self.piece_ready_to_move = 0
        self.button_ready_to_move = 0
        self.button_location = []
        self.main_piece_place_function()
        file_saving(root=root,frame=main_chess_board_frame)

        #function with placeholder is to be removed and replaced with actual function 
        #purpose of function below is to take the positon of the piece that the user clicks and the locaiton of the button that is where the user wants to move the piece to and passes that to component 4

    def placeholder_piece_press_function(self,piecetype,button_location):
        #print(f"piece type is {piecetype}")
        move_check = [False,False]
        move_transfer_var = ["placeholderpiecetype","placeholderbuttoninfo"]
        
        try:
            if button_location == 0:
                #print(f"piece type = {piecetype[0]}")
                transfer_str = str(piecetype[0])
                self.piece_loc_holder.insert(0,piecetype)
                #self.button_location = []
                move_transfer_var[0] = str(piecetype[0])
                self.piece_ready_to_move = 1
                move_check[0] == True
            if piecetype == 0 and button_location == []:
                #print("restart function")
                chess_board_piece_place()
            if piecetype == 0:
                #print(F"piece type = 0 button location {button_location}")
                self.button_location = button_location
                self.button_loc_holder.insert(0,button_location)
                #print(f"button location = {self.button_location}")
                move_transfer_var[1] = button_location
                self.button_location == button_location[0],button_location[1]
                self.button_ready_to_move = 1
            
            if self.move_check[0] or self.move_check[1] == 0:
                chess_board_piece_place()
        except KeyError and TypeError:
            print("A")
        #print(f"move check {self.move_check}")
        #print(self.piece_loc_holder,self.button_loc_holder)
        if (move_transfer_var[0] == "placeholderpiecetype") == True:
            
            print("move change running")
        if (move_transfer_var[1] == "placeholderbuttoninfo") == True:
            self.move_check[0] == 0
            #print("move second change running")
            #print(f"self move check = {self.move_check}")
        if (self.piece_ready_to_move == 1) and (self.button_ready_to_move == 1):
            #print("check running")
            #print(f"self button location = {self.button_location}")
            
            piece_holder = (self.piece_loc_holder[0])
            #print(f"button location test {self.button_location[0],self.button_location[1]}")
            piece_mover_transfer_key = [self.button_location[0],self.button_location[1]]
           
            button_holder = (self.button_loc_holder[0])
            #print(f"button = {[button_holder[0],button_holder[1]]}")
            self.piece_move_holder[button_holder[0],button_holder[1]]= piece_holder
            print(f"piece move2 = {self.piece_move_holder}")
            piece_holder
            #print(f"piece move holder = {piece_holder}")
            #print(f"move transfer var = {move_transfer_var}")
            #print(f"piece click first var test {self.piece_move_holder_piece_click_first}")
            piece_rules(frame=self.chess_piece_frame,piece_move_info=piece_holder,button_to_move = piece_mover_transfer_key)
            self.piece_move_holder.clear()
            self.piece_move_holder = {}
            self.button_loc_holder = []
            self.piece_loc_holder = []
            self.move_check = [0,0]
            self.piece_move_holder_piece_click_first = {}
            self.piece_ready_to_move = 0
            self.button_ready_to_move = 0
            self.button_location = []
            self.button_loc_holder.clear()
            piece_mover_transfer_key.clear()
            piece_holder = ""
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
                #print("white piece placed")
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
                    #print("black piece placed")
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
        
        
        self.frame = frame
        
        
        
        if turn == 0:
            for x in black_pieces_dict.keys():
                black_piece_to_change = self.frame.nametowidget(name=x)
                black_piece_to_change.lift()
                
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
                
            for x in black_pieces_dict.keys():
                black_piece_to_change = self.frame.nametowidget(name=x)
                
                
                for x in button_dict.keys():
                      button_to_change = self.frame.nametowidget(name=x)
                      pywinstyles.set_opacity(button_to_change,value=0.1)
                      
                      black_piece_to_change.lower()
                      
               
        if turn == 0:
                turn += 1
        else: 
                turn -= 1
        
        self.piece_info = piece_move_info
        
        #print(f"turn global value = {turn}")
        
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
            
            self.piece_type_transfer = ""
            self.piece_move_too_transfer = ""

        piece_move_info = ""
        

    def pawn_move_check_function(self,piece_move_loc,move_to):
       
        global turn 
        global move_valid
        global white_pieces_dict
        global black_pieces_dict
        white_pieces_location_grid = []
        black_pieces_location_grid = []
        
        #print(f'black pieces items = {black_pieces_dict.items()}')
        for x in black_pieces_dict.keys():
            poiece = self.frame.nametowidget(x)
            grid = poiece.grid_info()
            rgrid = grid["row"]
            cgrid = grid["column"]
            black_pieces_location_grid.append([rgrid,cgrid])
        for x in white_pieces_dict.keys():
            poiece = self.frame.nametowidget(x)
            grid = poiece.grid_info()
            rgrid = grid["row"]
            cgrid = grid["column"]
            white_pieces_location_grid.append([rgrid,cgrid])
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        
        transfer_grid_loc = piece_moving.grid_info()
        
        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        piece_current_row_test = piece_current_row
        white_pieces_dict_Test = white_pieces_dict
        forward_var = 0
        if turn == 0:
            if move_to != white_pieces_location_grid:
                 forward_var = 0
            else:
                 forward_var = 1
        if turn == 1:
            if move_to != black_pieces_location_grid:
                 forward_var = 0
            else:
                 forward_var = 1
        
        
        location = ([piece_current_column,piece_current_row_test])
        taking_pawn_white_right = [location[1] - 1,location[0] + 1]
        taking_pawn_white_left = [location[1] + 1,location[0] - 1]
        taking_pawn_black_right = [location[1] - 1,location[0] + 1]
        taking_pawn_black_left = [location[1] + 1,location[0] - 1]
        print(f"forward var = {forward_var}")
        print(f"taking = {taking_pawn_white_right,taking_pawn_white_left,taking_pawn_black_right,taking_pawn_black_left}")
        
        if move_to == taking_pawn_white_right:
                    #print("a")
                    move_valid = 1
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
            
        else:
            self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
        if move_to == taking_pawn_white_left:
                    #print("a")
                    move_valid = 1
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                    
        else:
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
        if move_to == taking_pawn_black_right:
                    #print("a")
                    move_valid = 1
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                            
        else:
                            self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
        if move_to == taking_pawn_black_left:
                    #print("a")
                    move_valid = 1
                    self.move_validity_check(move_start=location,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                                    
        else:
                        self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
        # if piece_move_loc[1] == "white":
        #     while piece_current_row_test < (piece_current_row + 2):
        #                 print('B')
        #                 a = ([piece_current_column,piece_current_row_test])
        #                 if a in white_pieces_location_grid or a in black_pieces_location_grid:
        #                         move_valid = 0
        #                         break
        #                 piece_current_row_test += 1

        #     for x in black_pieces_location_grid:
        #             #print(f"pawn x = {x}")
        #             if (x == taking_pawn_white_right):
        #                 move_valid = 1
        #                 if move_to == taking_pawn_white_right:
        #                     print("pawn bishop true1")
        #                     piece_moving.grid_configure(row=x[1],column=x[0])
        #                     taking_piece()
        #                     #self.__init__()
        #                     break
        #     for x in black_pieces_location_grid:
        #             #print(f"pawn x = {x}")
        #             if (x == taking_pawn_white_left):
        #                             move_valid = 1
        #                             if move_to == taking_pawn_white_left:
        #                                 print("pawn bishop true2")
        #                                 #move_valid = 1
        #                                 piece_moving.grid_configure(row=x[1],column=x[0])
        #                                 taking_piece()
        #                                 #self.__init__()
        #                                 break
        #     if piece_current_row == 2:
        #         self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
        #         if (piece_current_row - move_to[1] == -2):
        #             if move_valid == 1:
        #                 if move_to[1] +2 in white_pieces_dict.values():
        #                                                                         move_valid = 0
        #                 else:
        #                     piece_moving.grid_configure(row=piece_current_row + 2)
        #             else:
        #                                  print("a")
        #             #self.__init__()
        #         elif move_valid == 0:
        #             print(move_valid)
        #             print("move invalid1")
        #             messagebox.showerror("error","move invalid")
        #     if (piece_current_row - move_to[1] == -1):
        #         if move_valid == 1:
        #             if move_to[1] +1 in white_pieces_dict.values():
        #                             move_valid = 0
        #             else:
                                    
        #                 piece_moving.grid_configure(row=piece_current_row + 1)
        #         else:
        #                              print("a")
        #         #self.__init__()
        #     elif move_valid == 0:
        #             print(move_valid)
        #             print("move invalid2")
        #             messagebox.showerror("error","move invalid")
        if piece_move_loc[1] == "white":
                    while piece_current_row_test < (piece_current_row + 2):
                    
                        
                            print("a")
                            b = ([piece_current_column,piece_current_row_test])
                            print(b)
                            if b in black_pieces_location_grid:
                                move_valid = 0
        
                                break
                            else:
                                                                
                                piece_current_row_test += 1
                    for x in black_pieces_location_grid:
                                        #print(f"pawn x = {x}")
                                        if (x == taking_pawn_white_left):
                                            
                                            if move_to == taking_pawn_white_left:
                                               
                                                print("pawn bishop true3")
                                                
                                                piece_moving.grid_configure(row=x[1],column=x[0])
                                                taking_piece()
                                                #self.__init__()
                                                break
                    for x in black_pieces_location_grid:
                                        #print(f"pawn x = {x}")
                                        if (x == taking_pawn_white_right):
                                                        move_valid = 1
                                                        if move_to == taking_pawn_white_right:
                                                            #move_valid == 1
                                                            
                                                            print("pawn bishop true4")
                                                        
                                                            piece_moving.grid_configure(row=x[1],column=x[0])
                                                            taking_piece()
                                                            #self.__init__()
                                                            break                
                    if piece_current_row == 2:
                        self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
                        if (piece_current_row - move_to[1] == -2):
                            
                            if move_valid == 1:
                                if [move_to[1] -2,move_to[0]] in white_pieces_dict.values():
                                     move_valid = 0
                                else:
                                    if forward_var == 0:
                                        piece_moving.grid_configure(row=piece_current_row +2)
                                        print("asfdsfasdf1")
                            else:
                                                 print("a")
                            
                            #self.__init__()
                        elif move_valid == 0:
                            print(move_valid)
                            print("move invalid3")
                            messagebox.showerror("error","move invalid")
                   
                    if (piece_current_row - move_to[1] == -1):
                        
                        
                        if move_valid == 1:
                            if [move_to[1] -1,move_to[0]] in white_pieces_dict.values():
                                        move_valid = 0
                            else:
                                    if forward_var == 0 and [move_to[1],move_to[0]] not in black_pieces_location_grid:
                                            print([move_to[1] +1,move_to[0]])
                                            print(black_pieces_location_grid)
                                            piece_moving.grid_configure(row=piece_current_row +1)
                                            print("asfdsfasdf2")
                                    else:
                                         print("a")
                        else:
                             print("a")
                        #self.__init__()
                    elif move_valid == 0:
                            print(move_valid)
                            print("move invalid4")
                            messagebox.showerror("error","move invalid")
        if piece_move_loc[1] == "black":
            while piece_current_row_test < (piece_current_row + 2):
            
                
                    print("a")
                    b = ([piece_current_column,piece_current_row_test])
                    print(b)
                    if b in black_pieces_location_grid:
                        move_valid = 0

                        break
                    else:
                                                        
                        piece_current_row_test += 1
            for x in white_pieces_location_grid:
                                #print(f"pawn x = {x}")
                                if (x == taking_pawn_black_right):
                                    
                                    if move_to == taking_pawn_black_right:
                                       
                                        print("pawn bishop true3")
                                        
                                        piece_moving.grid_configure(row=x[1],column=x[0])
                                        taking_piece()
                                        #self.__init__()
                                        break
            for x in white_pieces_location_grid:
                                #print(f"pawn x = {x}")
                                if (x == taking_pawn_black_left):
                                                move_valid = 1
                                                if move_to == taking_pawn_black_left:
                                                    #move_valid == 1
                                                    
                                                    print("pawn bishop true4")
                                                
                                                    piece_moving.grid_configure(row=x[1],column=x[0])
                                                    taking_piece()
                                                    #self.__init__()
                                                    break                
            if piece_current_row == 7:
                self.move_validity_check(move_start=location,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
                if (piece_current_row - move_to[1] == 2):
                    
                    if move_valid == 1:
                        if [move_to[1] -2,move_to[0]] in black_pieces_dict.values():
                             move_valid = 0
                        if forward_var == 0 and [move_to[1],move_to[0]] not in white_pieces_location_grid:
                            piece_moving.grid_configure(row=piece_current_row -2)
                    else:
                                         print("a")
                    
                    #self.__init__()
                elif move_valid == 0:
                    print(move_valid)
                    print("move invalid3")
                    messagebox.showerror("error","move invalid")
           
            if (piece_current_row - move_to[1] == 1):
                
                
                if move_valid == 1:
                    if [move_to[1] -1,move_to[0]] in black_pieces_dict.values():
                                    move_valid = 0
                    if forward_var == 0 and [move_to[1],move_to[0]] not in white_pieces_location_grid:
                        piece_moving.grid_configure(row=piece_current_row -1)
                else:
                     print("a")
                #self.__init__()
            elif move_valid == 0:
                    print(move_valid)
                    print("move invalid4")
                    messagebox.showerror("error","move invalid")
                

        
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
            

            if bishop_test == move_to:
                print("bishop move match ")
                
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    print("move 1")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    print("move 2")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    print("move 3")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    print("move 4")
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
    def rook_move_check_function(self,piece_move_loc,move_to):
        global move_valid
        piece_moving = self.frame.nametowidget(name=piece_move_loc[2])
        move_valid = 0
        transfer_grid_loc = piece_moving.grid_info()

        piece_current_row = transfer_grid_loc['row']
        piece_current_column = transfer_grid_loc['column']
        rook_loc = [piece_current_column,piece_current_row]
        print(move_to)
        print(piece_current_column)
        print(piece_current_row)
        if piece_current_column == move_to[0]:
            self.move_validity_check(move_start=rook_loc,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
            if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1])
            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
        if piece_current_row == move_to[1]:
            self.move_validity_check(move_start=rook_loc,move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
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
        move_valid = 0
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
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
                self.move_validity_check(move_start=bishop_list_loc_list,move_end=move_to,diagonal=1,piecename=piece_move_loc[2])
                if move_valid == 1:
                    piece_moving.grid_configure(row=move_to[1],column=move_to[0])
                    break
                elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
                taking_piece()
            x += 1
        
        print(move_to)
        print(piece_current_column)
        print(piece_current_row)
        if piece_current_column == move_to[0]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
            if move_valid == 1:
                piece_moving.grid_configure(row=move_to[1])

            elif move_valid == 0:
                    print("move invalid")
                    messagebox.showerror("error","move invalid")
            taking_piece()
        if piece_current_row == move_to[1]:
            self.move_validity_check(move_start=[piece_current_column,piece_current_row],move_end=move_to,diagonal=0,piecename=piece_move_loc[2])
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


    def move_validity_check(self,move_start,move_end,diagonal,piecename):
            global move_valid
            move_valid = 0
            move_start_true = [move_start[1],move_start[0]]
            #move_valid = 1
            piece_locations = []
            row_change = False
            column_change = False
            global white_pieces_dict
            global black_pieces_dict
            print(white_pieces_dict)
            white_pieces_dict_transfer = {}
            black_pieces_dict_transfer = {}
            # print(f"black dict = {black_pieces_dict}")
            # print(f"white dict = {white_pieces_dict}")
            # for x in white_pieces_dict.items():
            #      print(x)
            #      if x[0] == piecename:
            #           pass
            #      else:
            #         white_pieces_dict_transfer[x[0]] = x[1]
            # for x in black_pieces_dict.items():
            #              print(x)
            #              if x[0] == piecename:
            #                   pass
            #              else:
            #                 black_pieces_dict_transfer[x[0]] = x[1]
            
    
            # for x in white_pieces_dict_transfer.keys():
            #     print(x)
            #     piece_moving = self.frame.nametowidget(name=x)
            #     transfer_grid_loc = piece_moving.grid_info()
    
            #     piece_current_row = transfer_grid_loc['row']
            #     piece_current_column = transfer_grid_loc['column']
            #     append_list = [piece_current_row,piece_current_column]
                
            #     piece_locations.append(append_list)
            #     # print(f"piece location = {piece_locations}")
            #     # print(f"x = {x}")
            # for x in black_pieces_dict_transfer.keys():
            #     print(x)
            #     piece_moving = self.frame.nametowidget(name=x)
            #     transfer_grid_loc = piece_moving.grid_info()
                
            #     piece_current_row = transfer_grid_loc['row']
            #     piece_current_column = transfer_grid_loc['column']
            #     append_list = [piece_current_row,piece_current_column]
                
            #     piece_locations.append(append_list)
            # #piece_locations_bishop = piece_locations.remove([move_start[1],move_start[0]])
            # print(f"piece locations = {piece_locations}")
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
            piece_locations.remove(move_start_true)
            row_diffrence = move_end[1] - move_start[1]
            column_diffrence = move_end[0] - move_start[0]
            step_of_rows = (row_diffrence >> 2) | (row_diffrence >> 0) if row_diffrence != 0 else 0
            step_of_column = (column_diffrence >> 2) | (column_diffrence >> 0) if column_diffrence != 0 else 0
            current_row = move_start_true[1] + step_of_rows
            current_column = move_start_true[0] + step_of_column
            print(f"move start = {move_start}")
            print(f"move end = {move_end}")
            print(F"move true = {move_start_true}")
            print(f"row diffrence = {row_diffrence}")
            print(f"row diffrence = {row_diffrence}")
            if (move_start[0] == move_end[0]) == True:
                row_change = True
                #ensure true/false changes
                print("A")
            if (move_start[1] == move_end[1]) == True:
                column_change = True
            print(f"row = {row_change}")
            print(f"column = {piece_locations}")
            #piece_locations_true = piece_locations
            #print(f'move start true = {move_start}')
            #piece_locations_true = piece_locations_true.remove(move_end)
            piece_in_the_way_if_rows_true = abs(move_end[1] - move_start[1])
            filtered_piece_row = []
            filtered_piece_column = []
            all_grids = []
            for x in black_pieces_dict_transfer.values():
                 print(f"move grid x = {x[0]}")
                 all_grids.append(x[0])
            for x in white_pieces_dict_transfer.values():
                 print(f"move grid x = {x[0]}")
                 all_grids.append(x[0])
            print(f"all grids = {all_grids}")
            for x in piece_locations:
                if x[0] == move_start[0]:
                    filtered_piece_row.append(x)
            for x in piece_locations:
                if x[1] == move_start[1]:
                    filtered_piece_column.append(x)
            if diagonal == 0:
                if row_change == True:
                    minus = False
                    loop_ran = False
                    if row_diffrence < 1:
                         minus = True
                         print("row diffrence is negitive")
                    print(f"check = {(move_start[1],move_start[0])}{(move_end[1],move_end[0])}")
                    print(step_of_column,step_of_rows)
                    a = [current_row,current_column]
    
                    #print((current_row,current_column) != (move_end[1],move_end[0]))
                    if minus == False:
                            print([move_start[1],move_start[0]]) != ([move_end[1],move_end[0]])
                            while ([move_start[1],move_start[0]]) != ([move_end[1],move_end[0]]):
                                 print("check")
                                 loop_ran = True
                                 #print(F"piece locations = {piece_locations}")
                                 
                                 list_check = [move_start[1],move_start[0]]
                                 #print(f"list check = {list_check}")
                                 #print(f"piece locations = {piece_locations}")
                                 if list_check in piece_locations:
                                       move_valid = 0    
                                       print("a")
                                       print(list_check)
                                       print(piece_locations)
                                       return False
                                 
                                 
                                 
                                 move_start[1] += 1
                            else:
                                 move_valid = 1
                            if piece_moving.cget("text") == "pawn":
                                 move_valid = 1
                            move_valid = 1
                            if [current_row -1,current_column] in piece_locations:
                                 move_valid = 0
                            else:
                                 move_valid = 1 
                                 #remember to do this for two move piece
                            return True
                            
                    if minus == True:
                         while ([move_start[1],move_start[0]]) != ([move_end[1],move_end[0]]):
                                                      print("adc")
                                                      loop_ran = True
                                                      #print(F"piece locations = {piece_locations}")
                                                      #current_row -= 1
                                                      list_check = [move_start[1],move_start[0]]
                                                      #print(f"list check = {list_check}")
                                                      #print(f"piece locations = {piece_locations}")
                                                      if list_check in piece_locations:
                                                            move_valid = 0    
                                                            print("asfaffd")
                                                            print(list_check)
                                                            print(piece_locations)
                                                            return False
                                                      else:
                                                           move_valid = 1
                                                      move_start[1] -= 1
                                                      
                         move_valid = 1
                         return False
                            #  else:
                # if loop_ran == False:
                #      while (current_row,current_column) == (move_end[1],move_end[0]):
                #           print("ad")
                #           print(F"piece locations = {piece_locations}")
                #           list_check = [current_column,current_row]
                #           print(f"list check = {list_check}")
                #           print(f"piece locations = {piece_locations}")
                #           if list_check in piece_locations:
                #                    move_valid = 0    
                #                    print("asfaffd1")
                #                    return False
                #           else:
                #                   move_valid = 1
                #           current_row += step_of_rows
                #           current_column += step_of_column
                          #print(f"current = {(current_column, current_row)}"
                
                #return True
                
                # print("a",piece_in_the_way_if_rows_true)
                # for x in filtered_piece_row:
                #      print(f"filtered1 = {x}")
                # print(f"x = {x}")
                # test = move_start
                # test_row = test[1]
                # while test_row <= move_end[1]:
                #      test_row += 1
                #      print("a")
                #      print([test_row,test[1]])
                #      print(f"piece locations ={piece_locations}")
                #      if [test[0],test_row] in piece_locations:
                #           print("piece moving througha")
                #           print(piece_locations)
                #           print([test[0],test_row])
                #           break
                # while test_row >= move_end[1]:
                #      test_row -= 1
                #      print([test[0],test_row])
                #      if [test[0],test_row] in piece_locations:
                #           print("piece moving throughb")
                #           print(piece_locations)
                #           print([test[0],test_row])
                #           break
                     
                # range_list = [move_start[0],move_end[1]]
                # range_list.sort()
                # print(f"range = {range(range_list[0],range_list[1])}")
                # print(piece_in_the_way_if_rows_true)
                # if x[1] in range(range_list[0],range_list[1]):
                #     print("piece moving through1")
                #     move_valid = 0
                    
                        
                # else:
                #     move_valid = 1
                    
        
                  
            # if column_change == True:
            #     print("a",piece_in_the_way_if_rows_true)
            #     for x in filtered_piece_column:
            #          print(f"filtered2 = {x}")
            #     range_list2 = [move_start[0],move_end[1]]
            #     range_list2.sort()
            #     print(f"x = {x}")
            #     test = move_start
            #     test_column = test[0]
            #     while test_column < move_end[1]:
            #          test_column += 1
            #          print(test[1],test_column)
            #          print("a")
            #          print(f"piece locations ={piece_locations}")
            #          if [test[0],test_column] in piece_locations:
            #               print("piece moving through2")
            #     while test_column < move_end[1]:
            #          test_column -= 1
            #          print("a")
            #          if [test[0],test_column] in piece_locations:
            #               print("piece moving through435")
                     
            #     print(f"range = {range(int(range_list2[0]),int(range_list2[1]))}")
            #     if x[0] in range(int(range_list2[0]),int(range_list2[1])):
            #         print("piece moving through3")
                    
            #         move_valid = 0
                        
            #     else:
            #         move_valid = 1
            if column_change == True:
                while (current_row,current_column) != (move_end[1],move_end[0]):
                             print("ad")
                             print(F"piece locations = {piece_locations}")
                             list_check = [current_column,current_row]
                             print(f"list check = {list_check}")
                             print(f"piece locations = {piece_locations}")
                             if list_check in piece_locations:
                                   move_valid = 0    
                                   print("asfaffd")
                                   return False
                             else:
                                  move_valid = 1
                             current_row += step_of_rows
                             current_column += step_of_column
                             print(f"current = {(current_column, current_row)}")
                            #  else:
                print("true1")
                move_valid = 1
                return True
                    
            if diagonal == 1:
                
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
                                move_valid = 0
                                break
                            else:
                                move_valid = 1
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
                                move_valid = 0
                                break
                            else:
                                move_valid = 1
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
                                move_valid = 0
                                break
                            else:
                                move_valid = 1
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
                                move_valid = 0
                                break
                            else:
                                move_valid = 1
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
                                move_valid = 0
                                break
                            else:
                                move_valid = 1
                        
                

        
        
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
            
            white_piece_taking_widget = self.frame.nametowidget(x[0])
            transfer_grid_loc = white_piece_taking_widget.grid_info()
        
            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            location_append1 = [piece_current_column,piece_current_row]
            white_pieces_location_list[x[0]] = (location_append1)
            
        for x in black_pieces_dict.items():
            
            black_piece_taking_widget = self.frame.nametowidget(x[0])
            transfer_grid_loc = black_piece_taking_widget.grid_info()
        
            piece_current_row = transfer_grid_loc['row']
            piece_current_column = transfer_grid_loc['column']
            location_append2 = [piece_current_column,piece_current_row]
            black_pieces_location_list[x[0]] = (location_append2)
           
        temp_list1 = []
        temp_list2 = []  
        a = (white_pieces_location_list)
        b = (black_pieces_location_list)
        
        print("overlap")
        
        for blackname,item in b.items():
            
            if item in a.values():
                take = True
                
                break  
        for whitename,item in a.items():
            
            if item in b.values():
                take2 = True
                
                break  
                
        
            
        if take and take2 == True:
            
            if turn == 0:
              print("take")
              piece_remove = self.frame.nametowidget(whitename)
              grid_info = piece_remove.grid_info()
              no_move_zone = [grid_info["row"],grid_info["column"]]
            #   for x in black_pieces_dict.items():
            #          print(f"x == {x}")
            #          if x[0] == no_move_zone:
            #               print(f"piece {x[0]} no move")
              if piece_remove.cget("text") == "king":
                    print("white wins")
              piece_remove.grid_forget()
              white_pieces_dict.pop(whitename)
              piece_remove.destroy()
              
            if turn == 1:
                print('take')
                piece_remove = self.frame.nametowidget(blackname)
                grid_info = piece_remove.grid_info()
                no_move_zone = [grid_info["row"],grid_info["column"]]
                # for x in white_pieces_dict.items():
                #      print(f"x == {x}")
                #      if x[0] == no_move_zone:
                #           print(f"piece {x[0]} no move")
                if piece_remove.cget("text") == "king":
                    print("black wins")
                piece_remove.grid_forget()
                black_pieces_dict.pop(blackname)
                piece_remove.destroy()

class file_saving:
    def __init__(self,root,frame):
          self.root = root
          self.frame = frame
          #self.root2 = Tk()
          #self.new_root = (self.root2)
          #self.frame = frame
          self.file_saving_gui(root)
          
    def game_save(self):
        #blank = ""
        dict_value = {}
        team = ""
        with open("gamedata.txt","w") as f:
                pass
        for x in self.frame.winfo_children():
             #print(x)
             
             #Button.widgetName
             #a = Button.configure
             button_name = frame.nametowidget(x)
             value_to_add_to_json_text = button_name.cget("text")
             value_to_add_to_json_grid = button_name.grid_info()
             row = value_to_add_to_json_grid["row"]
             column = value_to_add_to_json_grid["row"]
             for b in white_pieces_dict.keys():
                if button_name == b:
                    team = "white"
             for b in black_pieces_dict.keys():
                if button_name == b:
                    team = "black"


             dict_value = {}
             button_name_x = str(x)
             print(button_name_x)
             dict_value[button_name_x] = [value_to_add_to_json_text],[row,column],team
             with open("gamedata.txt","a") as f:
                f.write(str(dict_value))
                f.write("\n")
                
                
                

             
             
    def game_load(self):
        game_data_load_dictionary = {}
        #print("a")
        with open("gamedata.txt","r") as r:
               game_data_load = r.read()
               #print(game_data_load)
               #recovered_dict = ast.literal_eval(r.read())
            #    for x in r:
            #     #x.strip()
            #     if ":" in x:
            #         key,value = x.split(":",1)
            #         print(key)
            #         game_data_load_dictionary[key] = value
            #         print("read running")
            #         print(f"key = {key}")
                    
            #         #print(game_data_load_dictionary)
               print(game_data_load)
            #    for x,key in game_data_load_dictionary:
            #             button_object = frame.nametowidget(x)
            #             button_object.configure(key)
            #             print("a")

                
         
            

    def file_saving_gui(self,root):
          
          save_button = Button(root,text=f"X:dfa",command=self.game_save)
          load_button = Button(root,text=f"X:dfa",command=self.game_load)
          load_button.place(x=1000,y=300)
          
          save_button.place(x=1000,y=200)
          save_button.lift()
          
          

app = chess_board_create_class(root)

app.root.mainloop()