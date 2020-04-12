import random
import csv
from datetime import datetime

#List of all exercises
MuscleGroups = ['Calves', 'Hamstrings', 'Quads', 'Glutes', 'Abs', 'Biceps', 'Triceps', 'Chest', 'Shoulders', 'Lats']
ExerciseDict = {'Calves':['Standing Calf Raises', 'Incline Walk/Run'],
                'Hamstrings':['Romanian Dead Lifts', 'Single Leg Hip Raise','Squat Jumps'],
                'Quads' : ['Wall Sit','Pistol Squat', 'Lunges', 'Bulgarian Split Squat'],
                'Glutes' : ['Squats', 'Front Squats', 'Step Ups', 'Side Lunges' ],
                'Abs' : ['Mountain Climbers','Planks','Lying Leg Lifts', 'Bicycle Crunches', 'Regular Crunches','Russian Twist','Oblique Crunches','Plate Lowers - Legs off the ground','Reverse Crunches', 'Hanging Knee Lifts','Hanging Knee Twists','Jack Knives'],
                'Biceps' : ['Supinated Rows','EZ-Bar Curls Wide', 'EZ-Bar Curls Close', 'Hammer Curls', 'Close Grip Chin-ups', 'Hammer-Supinated Curls'],
                'Triceps' : ['Tricep Kickback', 'Single Arm Dips', 'Powerbombs', 'Skull-Crushers'],
                'Chest' : ['Pushups', 'Pushups in a circle', '90 degree holds', 'Decline Pushups','Slow Negative Explosive Pushups', 'Dumbbell Chest Press'],
                'Shoulders' : ['Pike Pushups', 'Overhead Press', 'Arnold Press', 'Front Raise','Horizontal Raise'],
                'Back/Lats' : ['Dumbbell Lat Pulls', 'Barbell Rows', 'Pull-ups', 'Renegade Row Reaches', 'Dumbbell Pull-Overs'],
                'Extra' : ['Scalp Pushups', 'Shrugs', 'Upright Row'],
}

finishedWorkout = False

while finishedWorkout == False:  
    exerciseList = ['Standing Calf Raises','Squat Jumps','Single Leg Hip Raise','Wall Sit','Pistol Squat', 'Lunges', 'Bulgarian Split Squat','Squats','Step Ups', 'Side Lunges','Mountain Climbers','Planks','Lying Leg Lifts', 'Bicycle Crunches', 'Regular Crunches','Russian Twist','Oblique Crunches','Reverse Crunches','Jack Knives','Pushups', 'Pushups in a circle', '90 degree holds', 'Decline Pushups','Slow Negative Explosive Pushups','Scalp Pushups','Pike Pushups']
    randomExercise = random.choice(exerciseList)
    randomRange = random.randint(1,21)

    print(f'Your random exercise is {randomExercise} for {randomRange}')
    print('')


    a_file = open("../../sample.csv", "a",newline='')
    writer = csv.writer(a_file)
    writer.writerow([randomExercise, randomRange, datetime.now()])

    a_file.close()

    userDecision = input("Press y for another exercise or Press any key to close.")
    if userDecision == 'y':
        finishedWorkout = False
    else:
        finishedWorkout = True
