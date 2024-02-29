import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for num in range(0, value):
                self.contents.append(key)
    def __repr__(self) -> str:
        return f'{self.contents}'


def experiment(**kwargs):
    # Extract keyword arguments
    hat = kwargs.get('hat')
    expected_balls = kwargs.get('expected_balls')
    num_balls_drawn = kwargs.get('num_balls_drawn')
    num_experiments = kwargs.get('num_experiments')

    # Initialize count for successful experiments
    success_count = 0

    # Perform experiments
    for _ in range(num_experiments):
        # Create a deep copy of the hat contents to avoid modifying the original hat
        hat_copy = copy.deepcopy(hat)
        # Draw balls from the hat
        balls_drawn = [hat_copy.contents.pop(random.randrange(len(hat_copy.contents))) for _ in range(num_balls_drawn)]

            # Check if the drawn balls match the expected balls
        success = True
        for ball_color, expected_count in expected_balls.items():
            if balls_drawn.count(ball_color) < expected_count:
                success = False
                break
        if success:
            success_count += 1

    # Calculate probability
    probability = success_count / num_experiments
    return probability

random.seed(95)
hat = Hat(blue=4, red=2, green=6)

probability = experiment(hat=hat, expected_balls={"blue": 2, "red": 1}, num_balls_drawn=4, num_experiments=3000)
print("Probability:", probability)
