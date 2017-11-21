import random

# print random_num
def grade():
    
    for i in range(1,11):
        random_num = random.randint(60,100)
        if 100 >= random_num >= 90:
            print "Score: {}; Your grade is A".format(random_num)

        elif 89 >= random_num >= 80:
            print "Score: {}; Your grade is B".format(random_num)
        
        elif 79 >= random_num >= 70:
            print "Score: {}; Your grade is C".format(random_num)
        
        else:
            print "Score: {}; Your grade is F".format(random_num)

grade()

# print random_num
# def scores(random_num):
#     from random import *
#     random_num = randint(60,100)
#     if random_num > 89:
#         print "A"
#     else:
#         print "F"
