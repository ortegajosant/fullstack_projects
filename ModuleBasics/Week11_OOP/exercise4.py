LEFT_SIDE = "left"
RIGHT_SIDE = "right"


class Head:
    def __init__(self, eyes, ears, nose, mouth):
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.mouth = mouth


class Torso:
    def __init__(self, heart, lungs, stomach):
        self.heart = heart
        self.lungs = lungs
        self.stomach = stomach


class Arm:
    def __init__(self, side, hand):
        self.side = side
        self.hand = hand


class Hand:
    def __init__(self, fingers):
        self.fingers = fingers


class Leg:
    def __init__(self, side, feet):
        self.side = side
        self.feet = feet


class Feet:
    def __init__(self, toes, side):
        self.toes = toes
        self.side = side


class Human:
    def __init__(self, head, torso, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.torso = torso
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


head = Head(eyes=2, ears=2, nose=1, mouth=1)
torso = Torso(heart=1, lungs=2, stomach=1)
left_hand = Hand(fingers=5)
right_hand = Hand(fingers=5)
left_arm = Arm(side=LEFT_SIDE, hand=left_hand)
right_arm = Arm(side=RIGHT_SIDE, hand=right_hand)
left_feet = Feet(toes=5, side=LEFT_SIDE)
right_feet = Feet(toes=5, side=RIGHT_SIDE)
left_leg = Leg(side=LEFT_SIDE, feet=left_feet)
right_leg = Leg(side=RIGHT_SIDE, feet=right_feet)


person = Human(head, torso, left_arm, right_arm, left_leg, right_leg)


print(
    f"Human has {person.head.eyes} eyes and {person.left_leg.feet.toes} toes on each foot."
)
