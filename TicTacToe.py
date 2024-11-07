grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def create_grid():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
def display_grid(grid):
    for row in grid:
        print("|".join(row))  # Displays each row with | separators
        print("-" * 5)  # Separates the rows with dashes
# Create the grid
grid = create_grid()

# Display the grid
display_grid(grid)