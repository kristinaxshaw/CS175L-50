#AverageFromInput.py
#Kristina Shaw
#CS-175L

#establishing main function to open file and perform calcuations
def main():
    #opening the file
    number_file = open('numbers.txt')
    #setting variables
    total = 0
    count = 0
    average = 0
    #command for each line in the file
    for line in number_file:
        total = total + float(line)
        count = count +1
        #displaying results
        print('I read', count, 'number(s) Current number is:', float(line), \
              'total is', total)
        #calculation and output for average
        average = total / count
        print('Average:', average)
    #closing the file
    number_file.close()

#callback to main function
if __name__ == '__main__':
    main()
