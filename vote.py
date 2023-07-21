# In the high school student council elections there are two candidates: Adam and Mila.
# A student interested in choosing Mila will vote 1, and a student interested in choosing Adam will vote 2.

# Write a program that will record the name of each of the students who came to vote and the number of the candidate for whom they voted.

# The program will count the number of votes received by each of the candidates, and print for each candidate his name and the number of votes he received.

# The program will end when "exit" is recorded for the student's name.


candidates = {1:{'name':'Mila','vote':0},2:{'name':'Adam','vote':0}}
student_list = []
while True:
    student_name = input('Please Enter Student Name (or "exit" to stop): ')
    if student_name == 'exit':
        break

    student_list.append(student_name)

    vote_num = int(input('Please Enter Vote Number: '))
    v = candidates[vote_num]['vote']+1
    candidates[vote_num]['vote'] = v

print(f'The candidate {candidates[1]["name"]} received {candidates[1]["vote"]} votes')
print(f'The candidate {candidates[2]["name"]} received {candidates[2]["vote"]} votes')
print(student_list)
