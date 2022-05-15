from adafruit_servokit import ServoKit
from hexapod.descriptors import Angle


class Leg2Axis:
    """
    
    """
    v_angle = Angle(min=20, max=160)
    h_angle = Angle(min=20, max=160)

    def __init__(
        self,
        horizontal_pin:int = None,
        vertical_pin:int = None,
        axes_flipped:bool = False
        ):

        self.h_pin = horizontal_pin
        self.v_pin = vertical_pin

        kit = ServoKit(channels=16)
        self.h_axis = kit.servo[self.h_pin] 
        self.v_axis = kit.servo[self.v_pin] 
        self.axes_flipped = axes_flipped
        

    def forward(self):
        if self.axes_flipped:
            self.h_angle.min()
        else:
            self.h_angle.max()

        self._move()
    
    def backward(self):
        if self.axes_flipped:
            self.h_angle.max()
        else:
            self.h_angle.min()

        self._move()

    def up(self):
        if self.axes_flipped:
            self.v_angle.min() 
        else:
            self.v_angle.max() 

        self._move()

    def down(self):
        if self.axes_flipped:
            self.v_angle.max()
        else:
            self.v_angle.min()

        self._move()

    def horizontal(self, angle:float = None):
        if angle is None:
            raise ValueError("must provide angle to horizontal")
        self.h_angle = angle
        self._move()

    def vertical(self, angle:float = None):
        if angle is None:
            raise ValueError("must provide angle to vertical")
        self.v_angle = angle
        self._move()

    def h_middle(self):
        print(self.h_angle.middle_angle)
        self.h_angle.middle()
        self._move()

    def v_middle(self):
        self.v_angle = 90

    def off(self):
        self.v_axis.angle = None
        self.h_axis.angle = None
        
    def _move(self):
        self.v_axis.angle = self.v_angle
        self.h_axis.angle = self.h_angle

