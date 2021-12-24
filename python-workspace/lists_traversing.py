#example of a list and traversing the list
#illustrates a list of names and creating a new list 
#that reverses the first list
#uses for loop, range, enumerate and appends to a list
applicants = ['Bob', 'John', 'Steve', 'Dave']
print(f'the number of applicants to register is: {len(applicants)}')
for a in applicants:
    print(f'the applicant {a} is registered')

def reverse_list(applicants):
    reversed_list = [] 
    n_applicants = len(applicants)
    print(f'the number of applicants {n_applicants}')
    #loop runs from 0 to 4
    for a in range(0,n_applicants+1):
        reversed_list.append(applicants[(n_applicants-1)-a])
    return reversed_list
#get the reversed list    
reversed_list = reverse_list(applicants)

for i,r in enumerate(reversed_list):
    print(f'reversed list item {i} - {r}')