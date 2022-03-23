#AverageFromInput_WithExceptionHandling.py
#Kristina Shaw
#CS-175L

#establishing main function to open file and perform calcuations
def main():
    #command to check if the file exists
    try:
        #opening the file
        number_file = open('numbers.txt')
        #setting variables
        total = 0
        count = 0
        average = 0
        #command for each line in the file
        for line in number_file:
            #command to check for invalid values in the file
            try:
               total = total + float(line)
               count = count +1
               #displaying results
               print('I read', count, 'number(s) Current number is:', float(line), \
                        'total is', total)
               #calculation and output for average
               average = total / count
               print('Average:', average)
            #exception for when there is an invalid value
            except ValueError as err:
                print(err)
        #closing the file
        number_file.close()
    #exception for when the file does not exist
    except FileNotFoundError:
        print('Error: The file does not exist.')
       
#callback to main function
if __name__ == '__main__':
        main()
