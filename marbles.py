import random

def marble_game(num_plays):
    results = []
    marbles = ['blue', 'blue', 'blue', 'red', 'red', 'black']
    earnings = 0
    
    for _ in range(num_plays):
        drawn_marbles = random.sample(marbles, 2)
        if drawn_marbles[0] == drawn_marbles[1]:
            earnings += 1  # Winning $2 means you get $1 back plus $1 extra
        else:
            earnings -= 1  # Losing means you lose $1
        results.append(earnings)
    
    return results

# Test the function with the provided example
print(marble_game(5))  # Output might vary, e.g., [-1, -2, -1, -2, -3]
