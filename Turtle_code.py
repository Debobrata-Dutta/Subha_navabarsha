import turtle

# Function to draw alpona pattern
def draw_alpona():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    for i in range(36):
        for j in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(10)

# Function to print "শুভ নববর্ষ"
def print_shubho_noboborsho():
    print("শুভ নববর্ষ")

# Main function
def main():
    # Set up the Turtle screen
    turtle.setup(800, 600)
    turtle.bgcolor("light yellow")
    turtle.title("আল্পনা ও নতুন বছর")

    # Draw alpona
    draw_alpona()

    # Print "শুভ নববর্ষ"
    print_shubho_noboborsho()

    # Hide the Turtle
    turtle.hideturtle()

    # Keep the window open until closed by the user
    turtle.mainloop()

if __name__ == "__main__":
    main()
