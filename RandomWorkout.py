import random
import csv
from datetime import datetime
# import exercises
#List of all exercises
MuscleGroups = ['Calves', 'Hamstrings', 'Quads', 'Glutes', 'Abs', 'Biceps', 'Triceps', 'Chest', 'Shoulders', 'Lats']
                #Exercise, Equipment needed, Movement Type
ExerciseDict = {'Calves':[('Standing Calf Raises','Bodyweight','Compound'), ('Treadmill/Outside Run','Equipment','Timed')],
                'Hamstrings':[('Romanian Dead Lifts','Equipment','Compound'), ('Single Leg Hip Raise','Bodyweight','Single'),('Squat Jumps','Bodyweight','Compound')],
                'Quads' : [('Wall Sit','Bodyweight','Compound'),('Pistol Squat','Bodyweight','Single'), ('Lunges','Bodyweight','Single'), ('Bulgarian Split Squat','Bodyweight','Single')],
                'Glutes' : [('Squats','Bodyweight','Compound'), ('Front Squats','Equipment','Compound'), ('Step Ups','Bodyweight','Single'), ('Side Lunges','Bodyweight','Single'),('Glute Bridge','Bodyweight','Compound') ],
                'Abs' : [('Jog in Place','Bodyweight','Timed'),('High Knees','Bodyweight','Timed'),('Mountain Climbers','Bodyweight','Timed'),('Planks','Bodyweight','Timed'),('Lying Leg Lifts','Bodyweight','Compound'), ('Bicycle Crunches','Bodyweight','Timed'), ('Regular Crunches','Bodyweight','Compound'),('Russian Twist','Bodyweight','Single'),('Oblique Crunches','Bodyweight','Single'),('Crunch and Lower','Equipment','Compound'),('Reverse Crunches','Bodyweight','Compound'), ('Hanging Knee Lifts','Equipment','Compound'),('Hanging Knee Twists','Bodyweight','Single'),('Jack Knives','Bodyweight','Compound')],
                'Biceps' : [('Supinated Rows','Equipment','Compound'),('EZ-Bar Curls Wide','Equipment','Compound'), ('EZ-Bar Curls Close','Equipment','Compound'), ('Hammer Curls','Equipment','Single'), ('Close Grip Chin-ups','Equipment','Compound'), ('Hammer-Supinated Curls','Equipment','Single')],
                'Triceps' : [('Tricep Kickback','Equipment','Single'), ('Single Arm Dips','Bodyweight','Single'), ('Powerbombs','Equipment','Compound'), ('Skull-Crushers','Equipment','Compound'), ('Counter Dips','Bodyweight','Compound'),('Bench Dips','Bodyweight','Compound')],
                'Chest' : [('Pushups','Bodyweight','Compound'), ('Pushups in a circle','Bodyweight','Compound'), ('90 degree holds','Bodyweight','Timed'), ('Decline Pushups','Bodyweight','Compound'),('Slow Negative Explosive Pushups','Bodyweight','Compound'), ('Dumbbell Chest Press','Equipment','Compound')],
                'Shoulders' : [('Pike Pushups','Bodyweight','Compound'), ('Overhead Press','Equipment','Compound'), ('Arnold Press','Equipment','Compound'), ('Front Raise','Equipment','Compound'),('Horizontal Raise','Equipment','Single'),('Lat-Restricted Horizontal Raise','Bodyweight','Single')],
                'Back/Lats' : [('Dumbbell Lat Pulls','Equipment','Single'), ('Barbell Rows','Equipment','Compound'), ('Pull-ups','Equipment','Compound'), ('Renegade Row Reaches','Equipment','Single'), ('Dumbbell Pull-Overs','Equipment','Compound')],
                'Extra' : [('Scalp Pushups','Bodyweight','Compound'), ('Shrugs','Equipment','Compound'), ('Upright Row','Equipment','Compound')],
}

#Adds all exercises that are bodyweight along with their Movement Type
exerciseList = []
for k,vlist in ExerciseDict.items():
    for exercise in vlist:
        if exercise[1] == 'Bodyweight':
            exerciseList.append((exercise[0],exercise[1],exercise[2]))




finishedWorkout = False
typeText = ' repetitions.'

while finishedWorkout == False:  
    #this section of code determines the amount of reps or seconds to perform each exercise
    randomExercise = random.choice(exerciseList)
    if randomExercise[1] == 'Timed':
        randomRange = random.randint(20,60)
        typeText= ' seconds.'
    elif randomExercise[1] == 'Single':
        randomRange = random.randint(5,12)
        typeText= ' repetitions.'
    else:
        randomRange = random.randint(5,21)
        typeText= ' repetitions.'

    print(f'Your random exercise is {randomExercise[0]} for {randomRange}{typeText}')
    print('')


    a_file = open("../../ExerciseHistory.csv", "a",newline='')
    # a_file = open("Testing.csv", "a",newline='')
    writer = csv.writer(a_file)
    writer.writerow([randomExercise[0],randomExercise[1],randomExercise[2], randomRange, datetime.now()])

    a_file.close()

    userDecision = input("Press y for another exercise or Press any key to close.")
    if userDecision == 'y':
        finishedWorkout = False
    else:
        finishedWorkout = True
