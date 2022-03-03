#Kristina Shaw
#CS-175L
#Calculate_Average.py

#function to determine the letter grade
def determine_grade(score):
        if score >=90 and score <= 100:
            return 'A'
        elif score >=80 and score <= 89:
            return 'B'
        elif score >=70 and score <= 79:
            return 'C'
        elif score >=60 and score <= 69:
            return 'D'
        elif score <= 59:
            return 'F'
        else:
            return 'invalid'
#function to calculate the average score
def calc_average(s1,s2,s3,s4,s5):
    return(s1+s2+s3+s4+s5) / 5.0

#main function to accept input and display results
def main():
    score1 = float(input('Enter score 1: '))
    score2 = float(input('Enter score 2: '))
    score3 = float(input('Enter score 3: '))
    score4 = float(input('Enter score 4: '))
    score5 = float(input('Enter score 5: '))
    
    print('Score'  ' Numeric Grade' ' Letter Grade')
    print('-------------------------------')
    print('Score 1: ', score1,    determine_grade(score1))
    print('Score 2: ', score2,    determine_grade(score2))
    print('Score 3: ', score3,    determine_grade(score3))
    print('Score 4: ', score4,    determine_grade(score4))
    print('Score 5: ', score5,    determine_grade(score5))

    average = calc_average(score1, score2, score3, score4, score5)
    print('Average score: ' + str(average), determine_grade(average))

#function to ask user if they would like to run the program again
def repeat():
    loop= input('Enter "yes" if you would like to make another calculation: ')
    #if the user answers 'yes', then the program will repeat
    if loop.lower() == 'yes':
        loop == True
        main()
        repeat()
    #if the user answers 'no', then the program will end
    elif loop.lower() == 'no':
        loop == False

#callback to the main function  
loop = True
if loop == True:
    main()
    repeat()
