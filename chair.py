class DChair:
    type = ""
    color = ""
    height = 0
    number_of_legs = 0

    def __init__(self, chair_type, chair_color, chair_height, chair_number_of_legs):
        self.type = chair_type
        self.color = chair_color
        self.height = chair_height
        self.number_of_legs = chair_number_of_legs

    def __str__(self):
        return self.type+ " | "+ self.color+ " | "+ str(self.height)+ " | "+ str(self.number_of_legs)

dChair1 = DChair("C", "White",40,4)
dChair2 = DChair("D","Black",60,4)

print()
print("DChair 1:", dChair1.type, " | ", dChair1.color, " | ", str(dChair1.height), " | ", str(dChair1.number_of_legs))
print("DChair 2:", dChair2.type, " | ", dChair2.color, " | ", str(dChair2.height), " | ", str(dChair2.number_of_legs))
print()
print(dChair1)
print(dChair2)