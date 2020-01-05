import random

answer = ['It is certain', 'It is decidedly so', 'Yes', 'Reply hazy try again',
          'Ask again later', 'Concentrate and ask again', 'My reply is no',
          'Outlook not so good', 'Very doubtful']

fortune = random.randint(0, 8)

print(answer[fortune])
