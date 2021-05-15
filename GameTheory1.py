def solve(N, P1, P2, X, Move,
          QuitP1, QuitP2):
    if (N == 0 or (QuitP1 and QuitP2)):
        # Box is empty, Game Over! or
        # Both have quit, Game Over!
        print("Number of pens remaining in the box: ", N)
        print("Number of pens collected by P1: ", P1)
        print("Number of pens collected by P2: ", P2)
        return
    if (Move == 0 and QuitP1 == False):

        # P1 moves
        req_P1 = int(pow(2, X))

        if (req_P1 <= N):
            P1 += req_P1
            N -= req_P1
        else:
            QuitP1 = True
    elif (Move == 1 and QuitP2 == False):

        # P2 moves
        req_P2 = int(pow(3, X))
        if (req_P2 <= N):
            P2 += req_P2
            N -= req_P2
        else:
            QuitP2 = True

    # Increment X
    X += 1

    # Switch moves between P1 and P2
    if (Move == 1):
        Move = 0
    else:
        Move = 1
    solve(N, P1, P2, X, Move, QuitP1, QuitP2)


# Function to find the number of
# pens remaining in the box and
# calculate score for each player
def PenGame(N):
    # Score of P1
    P1 = 0

    # Score of P2
    P2 = 0

    # Initialized to zero
    X = 0

    # Move = 0, P1's turn
    # Move = 1, P2's turn
    Move = False

    # Has P1 quit
    QuitP1 = False

    # Has P2 quit
    QuitP2 = False

    # Recursively continue the game
    solve(N, P1, P2, X, Move,
          QuitP1, QuitP2)


# Driver Code
N = 50
PenGame(N)