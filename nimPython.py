
#!/usr/bin/env python3

row1 = ["*", "*", "*"]
row2 = ["*", "*", "*", "*"]
row3 = ["*", "*", "*", "*", "*"]
gameboard = [row1, row2, row3]


player1_count = 0  #number of moves of the player
player2_count = 0

def printing_gameboard():
    for i in range(3):
        print(gameboard[i])

printing_gameboard()

def player1():
    print("Player1's turn")  
    
    while True:
        player1_row_option = int(input("select the row: "))-1
        if str(player1_row_option) not in "012":
            print("INVALID OPTION! ENTER VALUES 1, 2, OR 3!")
            continue
        player1_number_of_columns = int(input("select number of columns: "))
        
        if player1_number_of_columns > gameboard[player1_row_option].count('*'):
            print(f"NUMBER OF COLUMNS GIVEN IS LARGER THAN AVAILABLE!!! CHOOSE A NUMBER SMALLER THAN {gameboard[player1_row_option].count('*')}")
            continue
        
        for i in range(player1_number_of_columns):
            gameboard[player1_row_option].pop()
            gameboard[player1_row_option].insert(0, " ")
            
            

        break
        
    printing_gameboard()
   

def player2():
    print("Player2's turn")  
    
    while True:
        player2_row_option = int(input("select the row: "))-1
        if str(player2_row_option) not in "012":
            print("INVALID OPTION! ENTER VALUES 1, 2, OR 3!")
            continue
        player2_number_of_columns = int(input("select number of columns: "))
        
        if player2_number_of_columns > gameboard[player2_row_option].count('*'):
            print(f"NUMBER OF COLUMNS GIVEN IS LARGER THAN AVAILABLE!!! CHOOSE A NUMBER SMALLER THAN {gameboard[player2_row_option].count('*')}")
            continue
        
        for i in range(player2_number_of_columns):
            gameboard[player2_row_option].pop()
            gameboard[player2_row_option].insert(0, " ")
            
            

        break
        
    printing_gameboard()
    
def count_asteriks():
    count=0
    for i in range(3):
        count+=(gameboard[i]).count("*")
    return count



while True:         
     
    player1()
    player1_count+=1

    if count_asteriks()==1:
        break

    player2()
    player2_count+=1

  

    
if player1_count>player2_count:
     print("Player 1 wins!!!!")
else:
     print("Player 2 wins!!!!")   


