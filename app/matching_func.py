from UserProfile import UserProfile
import random

users = [] # users data 
n = int(input("input number of users > ")) 

for i in range(n): # make random user profile
    users.append(UserProfile())
    users[i].gender = random.choice(['male', 'female']) # gender
    users[i].menu = random.choice(['c','j','k','w']) # chinese, japanese, korean, western
    users[i].talking = random.choice(['little','lot']) # talking 
    users[i].age = random.choice(list(range(19,25))) # age
    users[i].tag = "user " + str(i+1) # identifier (temporary)

user = UserProfile()

# for x in users:
#     print(x.gender + ' ', x.menu + ' ', x.talking + ' ', x.age)

user.gender = input("male or female > ")
user.menu = input("input menu > ") # select one of [c, j, k, w]
user.talking = input("input talking > ") # selet one of [little, lot]
user.age = int(input("input age > ")) # input age

result = [] 

# recommending algorithm 
for x in users:
    score = 0
    if x.gender != user.gender: # same gender
        score += 1
    if x.menu == user.menu: # same menu
        score += 1
    if x.talking == user.talking: # same talking
        score += 1
    if max([user.age,x.age]) - min(user.age,x.age) <= 3: # years apart < 4
        score += 1
    
    res = score * 25 # temporary, * 25 can be changed when algorithm come to clear
    result.append([x.tag, str(res) + '%'])

for t in result:
    print(t)