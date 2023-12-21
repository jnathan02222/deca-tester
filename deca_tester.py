import random

#Variables and files
questions = open("questions.txt", "r")
answers = open("answers.txt", "r")
question_list = []
answer_list = []
correct = 0

#Retrieve questions and answers
line_num = 0
for line in questions:
    line = line.replace("\n", "")
    if line_num % 5 == 0:
        q = line
    elif line_num % 5 == 1:
        a = line
    elif line_num % 5 == 2:
        b = line
    elif line_num % 5 == 3:
        c = line
    elif line_num % 5 == 4:
        d = line
        if("C. " in b):
            question_list.append((q, a, c, b, d))
        else:
            question_list.append((q, a, b, c, d))

    line_num += 1

for line in answers:
    answer_list.append(line.replace("\n", ""))

questions.close()
answers.close()

#Intro
print("Welcome to the DECA Tester program!")
test_num = -1
while True:
    try:
        test_num = int(input("Indicate the quiz you would like to write (1-6): ")) - 1
    except:
        pass
    if(test_num > - 1 and test_num < 6):
        break
    print("Invalid value.")

index_list = []
for i in range(100 * test_num, 100 * test_num + 100):
    index_list.append(i)
    
if input("Shuffle? (Y/n): ").lower() == "y":
    random.shuffle(index_list)
print()

question_num = 1
#Asking each question
for i in index_list:
    print("Question " + str(question_num))
    for part in question_list[i]:
        print(part)
        
    answer = input("Answer: ")
    if answer != "" and answer.lower() in answer_list[i].lower():
        print("Correct!")
        correct += 1
    else:
        print("Wrong! The correct answer is " + str(answer_list[i][len(answer_list[i])-1]))
    print()    

    question_num += 1
#End
print("You have completed the quiz. Your score was " + str(correct) + "/100.")
input("Done?")
