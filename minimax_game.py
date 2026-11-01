# Minimax function
def minimax(coins):

    # No coins left
    if len(coins) == 0:
        return 0

    # Only one coin left
    if len(coins) == 1:
        return coins[0]

    # AI takes left coin
    left = coins[0] + min(
        minimax(coins[2:]),
        minimax(coins[1:-1])
    )

    # AI takes right coin
    right = coins[-1] + min(
        minimax(coins[:-2]),
        minimax(coins[1:-1])
    )

    # AI chooses maximum score
    return max(left, right)


# AI move function
def ai_move(coins):

    if len(coins) == 0:
        return None

    if len(coins) == 1:
        return 0

    # AI takes left coin
    left_coins = coins[1:]

    left_score = coins[0] + min(
        minimax(left_coins[1:]),
        minimax(left_coins[:-1])
    )

    # AI takes right coin
    right_coins = coins[:-1]

    right_score = coins[-1] + min(
        minimax(right_coins[1:]),
        minimax(right_coins[:-1])
    )

    # AI chooses better move
    if left_score >= right_score:
        return 0
    else:
        return len(coins) - 1


# --------------------------------
# Main Program
# --------------------------------

coins = [0, 9, 4, 5, 7, 2, 6, 1, 3, 8]

human_score = 0
ai_score = 0

print("===== COIN GAME =====")
print("You can take only the LEFT or RIGHT coin.")
print("You are HUMAN.")
print("AI uses MINIMAX.\n")

while len(coins) > 0:

    print("\nCoins:", coins)

    # HUMAN TURN
    choice = input("Your choice (L/R): ").upper()

    while choice not in ["L", "R"]:
        choice = input("Enter L for Left or R for Right: ").upper()

    if choice == "L":
        coin = coins.pop(0)
    else:
        coin = coins.pop()

    human_score += coin

    print("You took:", coin)
    print("Your score:", human_score)

    # Check if game is over
    if len(coins) == 0:
        break

    # AI TURN
    position = ai_move(coins)

    if position == 0:
        coin = coins.pop(0)
        print("AI chooses LEFT")
    else:
        coin = coins.pop()
        print("AI chooses RIGHT")

    ai_score += coin

    print("AI took:", coin)
    print("AI score:", ai_score)


# --------------------------------
# FINAL RESULT
# --------------------------------

print("\n====================")
print("GAME OVER")
print("====================")

print("Human Score:", human_score)
print("AI Score:", ai_score)

if human_score > ai_score:
    print("You WIN!")

elif ai_score > human_score:
    print("AI WINS!")

else:
    print("DRAW!")