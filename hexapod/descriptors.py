
class Angle:
    """Sets an angle range for validation.

    Allows setting a min and max range for an angular value.
    This can then be checked to make sure that some input angle
    is in between these values. 

    Args:
        min(float): The minimum angle allowed.
        max(float): The maximum angle allowed.
    """
    def __init__(self, min:float = 0.0, max:float = 360.0):
        self.min_angle = float(min)
        self.max_angle = float(max)
        self.middle = (self.max_angle - self.min_angle) / 2.0
        self.current = self.middle

    def __get__(self) -> tuple:
        """Get the set min and max angles

        Returns:
            Float with the current angle
        """
        return self.current
    
    def min(self):
        self.current = self.min_angle
        return self.current

    def max(self):
        self.current = self.max_angle
        return self.current

    def middle(self):
        self.current = self.middle
        return self.current

    def __set__(self, input:float = None):
        """Return an angle in the allowed range that is closest to input.

        Tests if input angle is within the range, and if not sets it 
        to the closest edge in the allowed range. Sets the current angle
        to this value.

        Args:
            input(float): The input angle to constrain.
        """
        if input is None:
            raise ValueError("must provide input angle")
        if input > self.max_angle:
            self.current = self.max_angle
        elif input < self.min_angle:
            self.current = self.min_angle
        else:
            self.current = input
    
    def check(self, input:float = None) -> bool:
        """Checks to see if the angle is within the allowed range.
        """
        if input is None:
            raise ValueError("must provide input angle to check")
        if input <= self.max_angle and input >= self.min_angle:
            return True
        else:
            return False
            