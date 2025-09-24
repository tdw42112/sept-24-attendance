# This script generates random numbers for a PowerBall lottery ticket.

# Import the necessary modules.

import random
import time

# --- Part 1: Greeting and User Input ---

# Greet the user and ask for their name.
print("Welcome to the PowerBall Number Generator!")
varUserName = input("What is your name? ")

# Greet the user by their name.
print(f"\nHello, {varUserName}! Let's generate your lucky numbers.")

# Add a short delay to build suspense.
time.sleep(1)

# --- Part 2: Generate and Display Lottery Numbers ---

# Generate the first five white ball numbers (1-69).
# These numbers should be unique, so we'll use a set to ensure this.
# The `random.sample` function is a great way to get unique numbers from a range.
white_balls = random.sample(range(1, 70), 5)

# Generate the red PowerBall number (1-26).
red_ball = random.randint(1, 26)

# Store the numbers in individual variables as requested.
# We'll use the numbers from the list and the single integer.
ball1 = white_balls[0]
ball2 = white_balls[1]
ball3 = white_balls[2]
ball4 = white_balls[3]
ball5 = white_balls[4]
powerball = red_ball

# Print the numbers with the specified spacing.
# The f-string is used for easy formatting and includes the space characters.
print("Generating numbers...")
time.sleep(2) # A longer delay before showing the final numbers
print("Your winning numbers are:")
print(f"{ball1}  {ball2}  {ball3}  {ball4}  {ball5}    {powerball}")

# --- Part 3: Farewell Message ---

# Print a farewell message to the user.
print("\nGood luck! May the odds be ever in your favor.")
print("Thank you for using the PowerBall Number Generator!")