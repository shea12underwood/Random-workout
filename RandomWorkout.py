import random

LegList = ['Squats','Front Squats','Lunges','Calf Raises','Single Leg Squats','Romanian Dead Lifts','Squat Jumps','Glute Bridge']
UpperList = ['Dumbbell Lat Pulls','Bar Rows','Pushups','Dumbbell Chest Press','Overhead Press','Shrugs']
IsoList = ['Horizontal Lat Raise','Vertical Lat Raises', 'Supinated Curls','Hammer Curls', 'Single Arm Dips','Powerbombs','Tricep Kickbacks','Scalp Pushups']
AbList = ['Leg Raise', 'Bicycle','Regular Crunches','Russian Twist','Oblique Crunches','Plate Lowers - Legs off','Reverse Crunches']


print(f"Aces are {random.choice(LegList)}, Spades are {random.choice(UpperList)}, Diamonds are {random.choice(IsoList)}, Clubs are {random.choice(AbList)}.")
