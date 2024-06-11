from graphics import Canvas

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BOX_SIZE = 80
square = [0,1,2,3,4,5,6,7,8,9]

def game_status():
    if square[1] == square[2] and square[2] == square[3]:
        return 1
    elif square[4] == square[5] and square[5] == square[6]:
        return 1
    elif square[7] == square[8] and square[8] == square[9]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[3] == square[6] and square[6] == square[9]:
        return 1
    elif square[1] == square[5] and square[5] == square[9]:
        return 1
    elif square[3] == square[5] and square[5] == square[7]:
        return 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        return 0
    else:
        return -1

def findIndex(row,col):
    if row==1:
        return row*col
    elif row==2:
        return row+col+1
    elif row==3:
        return row*2+col
    

def main():
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_text(140,50,text="Tic Tac Toe", font_size=20,color="mediumorchid")
    # Draw the grid of rectangles
    for row in range(1,4):
        for col in range(1,4):
            x1 = col * BOX_SIZE 
            y1 = row * BOX_SIZE 
            x2 = x1 + BOX_SIZE
            y2 = y1 + BOX_SIZE
            canvas.create_rectangle(x1, y1, x2, y2,"lemonchiffon",outline="black")
    
    # Display changeable text below the grid
    turntext=canvas.create_text(140, 350, text="Game Starts", font_size=14)

    player = 1
    status = -1

    while status== -1:
        canvas.delete(turntext)
        if player%2 == 1:
            player = 1
            flag=True
            turntext = canvas.create_text(160, 350, text="Your turn", font_size=14,color="darkslategray")
        else:
            player = 2
            turntext = canvas.create_text(140, 350, text="Computer's turn", font_size=14,color="darkslategray")

        if player == 1:
            while flag:
                click = canvas.get_last_click()
                if click:
                    x, y = click[0], click[1]
                    if 80<x and x<320 and 80<y and y<320:
                        # Calculate the center of the clicked box
                        col = x // BOX_SIZE
                        row = y // BOX_SIZE
                        indcol= int(col)
                        indrow=int(row)
                        
                        index=findIndex(indrow,indcol)
                        
                        # If the square is empty, place an "X" in it
                        if square[index] == index:
                            square[index] = "X"
                            center_x = (col * BOX_SIZE) + (BOX_SIZE // 2) -25
                            center_y = (row * BOX_SIZE) + (BOX_SIZE // 2) -30
                            # Display the "X" at the center of the clicked box
                            canvas.create_text(center_x, center_y, text="X", font_size=60, color="red")
                            flag=False
                            
                        else:
                            # Clear the existing text
                            
                            # Display a new text indicating that the square is already occupied
                            alerttext = canvas.create_text(140, 350, text="This position is already taken!", font_size=14)
                            player -= 1
                            flag=False
                            canvas.delete(alerttext)

        else:
            mark = 'O'
                        
            for i in range(1,10):
                if square[i]==i:
                    choice=i
                    square[i]='X'
                    if(game_status()==1):
                        square[i]=i
                        break
                    square[i]=i
            
            for i in range(1,10):
                if square[i]==i:
                    square[i]='O'
                    if(game_status()==1):
                        square[i]=i
                        choice=i
                        break
                    square[i]=i
            if square[choice]==choice:
                square[choice]=mark
                col = ((choice - 1) % 3) + 1
                row = ((choice - 1) // 3) + 1
                center_x = (col * BOX_SIZE) + (BOX_SIZE // 2) - 25
                center_y = (row * BOX_SIZE) + (BOX_SIZE // 2) - 30
                # Display the "O" at the center of the clicked box
                canvas.create_text(center_x, center_y, text="O", font_size=60, color="blue")
        status = game_status()
        player += 1
    
    if status==1:
        canvas.delete(turntext)
        if player-1==1:
            turntext = canvas.create_text(80, 350, text="Congratulations, You have won the game", font_size=16,color="springgreen")
        else:
            turntext = canvas.create_text(140, 350, text="Computer wins", font_size=16,color="teal")
    else:
        canvas.delete(turntext)
        turntext = canvas.create_text(140, 350, text="Game is Draw", font_size=16,color="gold")
    canvas.create_text(130,370,text="Game ends! Run again to play", font_size=14,color="salmon")
if __name__ == "__main__":
    main()
