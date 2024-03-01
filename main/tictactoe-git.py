print("Make sure to read instructions before playing. \nAsegurate de leer las instrucciones antes de jugar. \n")

player_turn = True

def start():

    x = input("Set table dimensions with a number: ")

    if x in ("0", "1", "2"):
        print("That's too low")
        start() 

    try:
        x = int(x)
    
    except:
        print("That is not a number")
        start()

    global table

    table = [[" " for _ in range(x)]for _ in range(x)]
    
    check_table()

def diagonal_win():

    for i in range(len(table[0])):
        upper_l = table[0][0]
        upper_r = table[0][-1]
        diagonal1 = table[-i][-i]
        diagonal2 = table[i][-i - 1]

        if diagonal1 == upper_l and diagonal1 != " ":
            diagonal_win = True
            
        elif diagonal2 == upper_r and diagonal2 != " ":
            diagonal_win = True
            
        else: 
            diagonal_win = False
            break

    return diagonal_win

def row_win():

    for row in table:
        row_win = (row.count("X") == len(table) and row.count(" ") != True) \
        or (row.count("O") == len(table) and row.count(" ") != True)

        if row_win:
            return row_win

    return row_win

def column_win():
    
    column_win = False

    for i in range(len(table[0])):
        
        column_initial = table[0][i]
            
        for row in table:
            
            if row[i] == column_initial and column_initial != " ":
                row_win = True
                
            else:
                row_win = False
                break
                
        if row_win:
            return True
    
    return False

def no_spaces():
    
    draw = False
    
    for row in table:
        if " " not in row:
           draw = True
    
        else:
            draw = False
        
    if draw:
        return True

    else:
        return False

def table_change():

    global player_turn

    try:

        move_row = int(input("Set row of move: "))
        move_replace = int(input("Set element number to replace: "))

        if player_turn:
            
            symbol = "X"
            player_turn = False
        
        else:

            symbol = "O"
            player_turn = True

        table[move_row][move_replace] = symbol

    except:
        print("Invalid coordinate.")

        if not player_turn:
            player_turn = True
    
        else:
            player_turn = False

        
        table_change()

    check_table()

def check_table():

    global table

    for line in table:
        new_line = ""
        for element in line:
            new_line += "|" + element
        new_line += "|"
        print(new_line)
        print("-" * len(new_line))

    if diagonal_win() or row_win() or column_win():
        print("That's a win!")

        end = input("Press Enter to exit or write 'restart' to do that")

        if end == "restart":
            start()

        else:
            print("You had you chance.")
            input("Press Enter to exit")

    elif no_spaces():
        print("That's a draw!")

        end = input("Press Enter to exit or write 'restart' to do that\n- ")
    
        if end == "restart":
            start()
    
        else:
            print("You had you chance.")
            input("Press Enter to exit ")

    else:
        table_change()

start()