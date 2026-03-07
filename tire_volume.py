# program to calculate the tire volume

import datetime

# ask numbers
width = int(input("Enter the tire width in mm: "))
aspect = int(input("Enter the tire aspect ratio: "))
diameter = int(input("Enter the wheel diameter in inches: "))

# convert and calculate volume
volume = (3.14 * (width * aspect) *
          (width * aspect + 2540 * diameter)) / 10000000000

print("The tire volume is :", round(volume, 2))
# corrent date
data_actual = datetime.datetime.now()
file = open("volume.text", "a")
file.write("Data: " + str(data_actual.date()) + "\n")
file.write
(f"Width:{width} , Apperance: {aspect} ,Diameter: {diameter}, Volume: {round(volume, 2)} \n")

# close file
file.close()
