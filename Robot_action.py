class Robot:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.held_object = None

    def move(self, destination):
        print(f"{self.name} is moving to {destination}.")

    def pick_up(self, object):
        if self.held_object is None:
            self.held_object = object
            print(f"{self.name} picked up {object}.")
        else:
            print(f"{self.name} already holds an object and cannot pick up {object}.")

    def put_down(self, object, destination):
        if self.held_object == object:
            self.held_object = None
            print(f"{self.name} put down {object} at {destination}.")
        else:
            print(f"{self.name} cannot put down {object} as it is not held.")

    def stack(self, object1, object2):
        if self.held_object == object1:
            print(f"{self.name} is stacking {object1} over {object2}.")
        else:
            print(f"{self.name} cannot stack {object1} over {object2} as it is not held.")

def main():
    # Create a Robot instance named "RoboBot" and place it in the "Living Room."
    robot = Robot("RoboBot", "Living Room")
    object1 = "Saucer"
    object2 = "Cup"
    # Demonstrate a series of actions the robot can perform.
    robot.move("Kitchen")  # Move to the Kitchen
    robot.pick_up(object1)  # Pick up the Saucer
    robot.move("Dining Room")  # Move to the Dining Room
    robot.put_down(object1, "Dining Table")  # Put down the Saucer on the Dining Table
    robot.move("Kitchen")  # Move back to the Kitchen
    robot.pick_up(object2)  # Pick up the Cup
    robot.move("Dining Room")  # Move to the Dining Room again
    robot.stack(object2, object1)  # Stack the Cup over the Saucer

# Check if the script is being run directly and then execute the main function.
if __name__ == "__main__":
    main()
