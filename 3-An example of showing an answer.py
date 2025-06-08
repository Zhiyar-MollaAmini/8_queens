from matplotlib import pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()
plt.title("8-Queens Solution", fontsize=16)

for row in range(8):
    for col in range(8):
        color = "#f0d9b5" if (row + col) %2 == 0 else "#b58863" 
        ax.add_patch(plt.Rectangle((col, row),1 , 1 , color=color))


ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
plt.axis("off")
plt.gca().invert_yaxis()
fig.patch.set_facecolor("linen")

for col in range(8):
    ax.text(col + 0.5, 8.5 , chr(65 + col), ha="center", va="center")

for row in range(8):
    ax.text(-0.5, row + 0.5, str(8 - row), ha="center", va="center")


board = [7, 3, 0, 2, 5, 1, 6, 4]
queen_index = [0]
placed_queens = []


def place_next_queen(event):
    i = queen_index[0]
    if i < len(board):
        row = i
        col = board[i]
        q1 = ax.text(col + 0.5, row + 0.5 ,"♛" , fontsize=28 , ha="center", va="center", color="purple", fontname="DejaVu Sans")
        q2 = ax.text(col + 0.53, row + 0.47, "♛", fontsize=28,ha="center", va="center", color="purple", alpha=0.2)
        placed_queens.extend([q1, q2])
        queen_index[0] += 1
        plt.draw()

def reset_board(event):
    for queen in placed_queens:
        queen.remove()
    placed_queens.clear()
    queen_index[0] = 0
    plt.draw()        
    


button_ax = plt.axes([0.81, 0.54, 0.17, 0.075])
button = Button(button_ax, "next queen")
button.on_clicked(place_next_queen)

button_ax_reset = plt.axes([0.84, 0.46, 0.11, 0.075])
button_reset = Button(button_ax_reset, "reset")
button_reset.on_clicked(reset_board)

plt.show()
