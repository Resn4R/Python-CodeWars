'''
Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

def rps(p1, p2):
    match p1:
        case "scissors":
            match p2:
                case "scissors":
                    return "Draw!"
                case "paper":
                    return "Player 1 won!"
                case "rock":
                    return "Player 2 won!"
                case _: return
        case "paper":
            match p2:
                case "paper":
                    return "Draw!"
                case "rock":
                    return "Player 1 won!"
                case "scissors":
                    return "Player 2 won!"
                case _: return
        case "rock":
            match p2:
                case "rock":
                    return "Draw!"
                case "scissors":
                    return "Player 1 won!"
                case "paper":
                    return "Player 2 won!"
                case _: return
        case _: return

    #please refactor, wtf is this