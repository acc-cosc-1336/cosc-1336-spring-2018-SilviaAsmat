def display_histogram():
    survey_file = open('survey.dat', 'r')
    for line in survey_file:
        line1 = line.split()
        for i in line1:
            asterisk = '*'
            count = 0
            while count <line1[i]:
                asterisk += '*'
                count+=1
            print(line1[i],asterisk)

    survey_file.close()
