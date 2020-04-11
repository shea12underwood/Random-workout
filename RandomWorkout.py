import random

#List of all exercises
MuscleGroups = ['Calves', 'Hamstrings', 'Quads', 'Glutes', 'Abs', 'Biceps', 'Triceps', 'Chest', 'Shoulders', 'Lats']
ExerciseDict = {'Calves':['Standing Calf Raises', 'Incline Walk/Run'],
                'Hamstrings':['Romanian Dead Lifts', 'Single Leg Hip Raise','Squat Jumps'],
                'Quads' : ['Wall Sit','Pistol Squat', 'Lunges', 'Bulgarian Split Squat'],
                'Glutes' : ['Squats', 'Front Squats', 'Step Ups', 'Side Lunges' ],
                'Abs' : ['Mountain Climbers','Planks','Lying Leg Lifts', 'Bicycle Crunches', 'Regular Crunches','Russian Twist','Oblique Crunches','Plate Lowers - Legs off the ground','Reverse Crunches', 'Hanging Knee Lifts','Hanging Knee Twists','Jack Knives'],
                'Biceps' : ['Supinated Rows','EZ-Bar Curls Wide', 'EZ-Bar Curls Close', 'Hammer Curls', 'Close Grip Chin-ups', 'Hammer-Supinated Curls'],
                'Triceps' : ['Tricep Kickback', 'Single Arm Dips', 'Powerbombs', 'Skull-Crushers'],
                'Chest' : ['Pushups', 'Pushups in a circle', '90 degree holds', 'Decline Pushups','Slow Negative Explosive Pusups', 'Dumbbell Chest Press'],
                'Shoulders' : ['Pike Pushups', 'Overhead Press', 'Arnold Press', 'Front Raise','Horizontal Raise'],
                'Lats' : ['Dumbbell Lat Pulls', 'Barbell Rows', 'Pull-ups'],
                'Extra' : ['Scalp Pushups', 'Shrugs', 'Upright Row'],
}



# LegList = ['Squats','Front Squats','Lunges','Calf Raises','Bulgarian Split Squats','Romanian Dead Lifts','Squat Jumps','Glute Bridge','Single Leg Hip-Raises','Dumbbell Step-Ups', 'Wall-Sits']
# UpperList = ['Dumbbell Lat Pulls','Reverse/Neutral Grip Barbell Rows','Pushups','Dumbbell Chest Press','Overhead Press','Shrugs','Chin-ups/Pullups']
# IsoList = ['Arnold Press','Horizontal Lat Raise','Front Raises', 'Supinated Curls','Hammer Curls', 'Single Arm Dips','Powerbombs','Tricep Kickbacks','Scalp Pushups']
# AbList = ['Mountain Climbers','Planks','Lying Leg Raises', 'Bicycle Crunches','Regular Crunches','Russian Twist','Oblique Crunches','Plate Lowers - Legs off the ground','Reverse Crunches', 'Hanging Knee Lifts']


# TotalList = LegList + UpperList + IsoList + AbList

# LegNum = 1
# UpperNum = 1
# IsoNum = 1
# AbNum = 2

# #Checks to see if a user wants to change the default workout
# LegsChosen = False
# UpperChosen = False
# IsoChosen = False
# AbChosen = False
# ChangeChosen = False
# print(f"The current workout will have {LegNum} Leg exercise, {UpperNum} Upper body exercise, {IsoNum} Isometric exercise, and {AbNum} Ab exercises.")
# print("")
# ChangeWorkout = input("Would you like to change this? Please type 'Y' or 'N':  ")
# while ChangeChosen == False:
#     if ChangeWorkout == 'Y' or ChangeWorkout == 'N':
#         ChangeChosen = True
#         pass
#     else:
#         ChangeWorkout = input("Please Type a capital Y, or a capital N.")

# #Path if the user wants to change the workout
# if ChangeWorkout =='Y':
#     while LegsChosen == False:
#         try:
#             LegNum = int(input("How many Leg exercises do you want to do? Please type a number 0 through 10:  "))
#             if -1 < 0 + LegNum <11:
#                 LegsChosen = True
#             else:
#                 print("That was not a number 0 through 10!")
#                 LegsChosen = False
#         except:
#             print("That is not a valid option!")
#     while UpperChosen == False:
#         try:
#             UpperNum = int(input("How many Upper exercises do you want to do? Please type a number 0 through 10:  "))
#             if -1 < 0 + UpperNum <11:
#                 UpperChosen = True
#             else:
#                 print("That was not a number 0 through 10!")
#                 UpperChosen = False
#         except:
#             print("That is not a valid option!")
#     while IsoChosen == False:
#         try:
#             IsoNum = int(input("How many Isometric exercises do you want to do? Please type a number 0 through 10:  "))
#             if -1 < 0 + IsoNum <11:
#                 IsoChosen = True
#             else:
#                 print("That was not a number 0 through 10!")
#                 IsoChosen = False
#         except:
#             print("That is not a valid option!")
#     while AbChosen == False:
#         try:
#             AbNum = int(input("How many Ab exercises do you want to do? Please type a number 0 through 10:  "))
#             if -1 < 0 + AbNum <11:
#                 AbChosen = True
#             else:
#                 print("That was not a number 0 through 10!")
#                 AbChosen = False
#         except:
#             print("That is not a valid option!")



# #Path if the user wants to keep the default workout

# print("TODAY'S RANDOMIZED WORKOUT")
# print("===========================")
# print("")
# print("Your Leg exercises are:")
# LegChoices = random.sample(LegList, LegNum)
# for i in LegChoices:
#     print(i)
# print("")
# print("")
# print("Your Upper exercises are:")
# UpperChoices = random.sample(UpperList, UpperNum)
# for i in UpperChoices:
#     print(i)
# print("")
# print("")
# print("Your Isometric exercises are:")
# IsoChoices = random.sample(IsoList, IsoNum)
# for i in IsoChoices:
#     print(i)
# print("")
# print("")
# print("Your Ab exercises are:")
# AbChoices = random.sample(AbList, AbNum)
# for i in AbChoices:
#     print(i)
# print("")
# print("")
# print("Your extra exercise is:")
# print(random.choice(TotalList))
# print("")
# print("")
# input("Press enter to continue...")