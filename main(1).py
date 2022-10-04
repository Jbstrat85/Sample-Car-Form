print("===============================")
#Introduction to Car Custom form

print("Brandon Dorsey Custom Car Form")
print("===============================")

#Multipule choice answers
print()
print("(For Multiple answers, please enter in blank section)")
print("~Mercedes Model~")
print("1.Vehicle Make and Model")
print(" a. GLE")
print(" b. S-Class")
print(" c. GT-63")
print(" d. GLC")
userModel = input("Please enter choice: ")

# Type of Interior
print()
print("~Interior~")
print("2.Leather of Cloth Interior?")
userInterior = input("Please enter choice: ")

# Vehicle Color
print()
print("~Exterior Color~")
print("3.Choose Vehicle Color")
print(" a. Black")
print(" b. White")
print(" c. Red")
print(" d. Blue")
userVehicle = input("Please enter choice: ")

# Tire size
print()
print("4.Rim Size?")
print("20 or 22?")
userTire = input("Please enter choice: ")

# Audio System
print()
print("5.Upgraded Stereo System?")
userAudio = input("Please enter 'Yes' or 'No': ")

# Engine upgrade
print()
print("6.Sports Package?")
userEngine = input("Please enter 'Yes' or 'No': ")

#Print Summary
print()
print("=============================")
print("~Summary~")
print()
print(f'Model option: {userModel}')
print(f'Interior: {userInterior}')
print(f'Color of Vehicle: {userVehicle}')
print(f'Rime Size: {userTire}')
print(f'Upgraded Option: {userAudio}')
print(f'Sports Package: {userEngine}')
