import cv2
import cvzone

cap = cv2.VideoCapture(0)  # Initialize the webcam
cap.set(3, 640)  # Set the width of the frame
cap.set(4, 480)

while True:
    imgBG = cv2.imread("Resources/BG.png")  # Load the background image for the game
    success, img = cap.read()  # Read a frame from the webcam
    imgScaled = cv2.resize(img,(0,0),None,0.475,0.568)  # Resize the background image to match the webcam frame

    imgScaled = imgScaled[:,50:290]  # Ensure the scaled image matches the webcam frame size
    # Resize imgScaled to match the target region in imgBG
    imgScaled = cv2.resize(imgScaled, (300, 200))  # Adjust dimensions to increase vertical size (width=400, height=100)
    imgBG[150:350, 795:1095] = imgScaled  # Update the region to match the new size of the human box
    cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    if imgScaled.size > 0:  # Ensure imgScaled is valid before displaying
        cv2.imshow("Scaled", imgScaled)  # Show the scaled image
    else:
        print("Warning: imgScaled is empty or invalid.")
    cv2.waitKey(1)  # Wait for a short time to display the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break


def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Checks if there's a winner."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        # Validate the move
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()