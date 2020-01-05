# class_average_sentinel.py
"""Class average program with sentinel-controlled iteration."""

# initialization phase
total = 0
grade_counter = 0

# processing phase
grade = int(input('Enter grade, -1 to end: '))  # get one grade

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter a grade, -1 to end: '))

# termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
    average = 123
    # same as above but ">" right aligned, "10." decimal point
    print(f'Class average is {average:>10.2f}')
else:
    print('No grades were entered')
