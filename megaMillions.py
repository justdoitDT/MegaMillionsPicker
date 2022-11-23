def megaMillions(n=1):

    import random

    tickets = []
    count = 0
    while count < n:
        count += 1
        nums = list(range(1, 71))
        ticket = []
        for _ in range(5):
            remainingNums = len(nums) - 1
            ticket.append(nums.pop(random.randint(0, remainingNums)))
        ticket.sort()
        ticket.append(set([random.randint(1, 25)]))
        tickets.append(ticket)

    digits = len(str(len(tickets)))
    for index, ticket in enumerate(tickets):
        print(f'ticket #{index + 1}:', ' '*(digits - len(str(index + 1))), ticket)







# Program to test megaMillions function. It works.
'''
def megaMillionsDiagnostic(n):

    regResults = {}
    for i in range(1, 71):
        regResults[i] = 0

    megaResults = {}
    for i in range(1, 26):
        megaResults[i] = 0

    iteration = 0
    for ticket in megaMillions(n):
        for i in ticket[:5]:
            regResults[i] += 1
        megaResults[list(ticket[5])[0]] += 1
        iteration += 1
        print('Progress: ', round(iteration/n, 4))

    for i in regResults:
        regResults[i] /= (n * (1 - (69*68*67*66*65/(70*69*68*67*66))))

    for i in megaResults:
        megaResults[i] *= (25 / n)

    print(regResults)
    print(megaResults)
'''