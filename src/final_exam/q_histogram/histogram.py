def display_histogram():
    survey_file = open('survey.dat', 'r')
    for line in survey_file:
        line1 = line.split()
        for i in line1:
            asterisk = '*'
            count = 0
            while count < int(i):
                asterisk += '*'
                count+=1
            print(i,asterisk)
        print()

    survey_file.close()

