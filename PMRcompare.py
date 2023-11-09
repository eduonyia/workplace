# function reads a file and return a list
def file2list(filename):
    f = open(filename, "r")
    lines = f.readlines()
    contents = []

    for x in lines:
        x = x.split('|')[0]
        x = x.rstrip('\n')
        if len(x) != 0:
            contents.append(x)

    f.close()

    return contents


path = '/Users/Chinedu/Documents/PMR/2023_Q3/Stanbic/'

preval = file2list(path + 'ava.txt')
pmrList = file2list(path + 'NotPresentStanbic.txt')

print('In pre-validation: ', len(preval))
print('All unique accounts in PMR list: ', len(pmrList))

# remove duplicates
pmrList = set(pmrList)
print(f'Generated List of accounts without duplicates {len(pmrList)}')

inBoth = set(pmrList).intersection(set(preval))
print(f'No of accounts in both list {len(inBoth)}')

notPresent = set(pmrList).difference(set(preval))
print(f'In monitored list but not in generated(Preval) list: {len(notPresent)}')

# write to file

with open("NotPresent.txt", "w") as f:
    f.write('\n'.join(notPresent))

with open("inBoth.txt", "w") as f:
    f.write('\n'.join(inBoth))







