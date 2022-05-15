from hexapod.leg2axis import Leg2Axis

class Robot:
    """
    """
    def __init__(
        self,
        n_legs:int = 6,
        flipped_legs:list = [0, 2, 4],
        left_legs:list = [1, 3, 5],
        right_legs:list = [0, 2, 4]
        ):
        self.n_legs = n_legs
        self.flipped_legs = flipped_legs
        self.legs = []
        self.left_legs = []
        self.right_legs = []

        for leg_number in range(n_legs):
            v_pin = 2*leg_number
            h_pin = (2*leg_number)+1
            axes_flipped = False
            if leg_number in self.flipped_legs:
                axes_flipped = True

            leg = Leg2Axis(
                vertical_pin=v_pin,
                horizontal_pin=h_pin,
                axes_flipped=axes_flipped) 

            self.legs.append(leg)
            if leg_number in left_legs:
                self.left_legs.append(leg)
            elif leg_number in right_legs:
                self.right_legs.append(leg)
            else:
                raise ValueError(f"leg {leg_number} not in either right of left leg list")

    def all_off(self):
        for leg in self.legs:
            leg.off()

    def all_up(self):
        for leg in self.legs:
            leg.up()

    def all_down(self):
        for leg in self.legs:
            leg.down()

    def all_middle(self):
        for leg in self.legs:
           leg.h_middle()
           leg.v_middle() 
