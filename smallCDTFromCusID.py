import  csv

path =  'C:/Users/hp/Documents/CDT DATA UPLOAD/September 2019/COMMERCIAL/Unity/'
bank = 'Unity'
cusID = []
# A function that  generates smaller Credit-Information file
# this is generated using specified account number( can be pmrAcc in the previous upload)
def smallerCreditInfo(bigCreditFile, missingCusID):
    f = open(missingCusID, "r")
    lines = f.readlines()
    contents = []
    smallCredInfo = []

    for x in lines:
        x = x.rstrip('\n')
        if len(x) != 0:
            contents.append(x) # customer ids

    f.close()
    #print(contents)

    with open(bigCreditFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        creditInfo = list(readCSV)


        for row in creditInfo:
            if row[0] in contents:
                smallCredInfo.append(row)
                cusID.append(row[0])

    return smallCredInfo





# A function that generates smaller Individual-Borrower file
def smallerIndBorrower(bigIndBorrower, cusIds):
    cusIds = cusID
    #print(len(cusIds))
    with open(bigIndBorrower) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        smallIndBorrower = list(readCSV)
        smallIndB = []


        for row in smallIndBorrower:
            if row[0] in cusIds:
                smallIndB.append(row)

    return smallIndB


# Afunction that generates smaller Corporate-Borrower file
def smallerCorpBorrower(bigCorpBorrower, cusIds):
    cusIds = cusID
    #print(len(cusIds))
    with open(bigCorpBorrower) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        smallCorpBorrower = list(readCSV)
        smallCorpB = []
        #corpID = []

        for row in smallCorpBorrower:
            #corpID.append(row[5])
            if row[5] in cusIds:
                smallCorpB.append(row)

        #print(corpID)

    return smallCorpB




smallCredInfo = smallerCreditInfo(path + '732854732854333808-Credit-Information-2019Sep29.txt',
                  path+'cusIDs.txt')

# write to file
with open(bank+"smallCredInfo.txt", "w", newline='') as f:
    wr = csv.writer(f, delimiter='|')
    wr.writerows(smallCredInfo)

# Write Customer ID
with open(bank+"cusIDs.txt", "w") as f:
    f.write('\n'.join(cusID))

smallIndBorro = smallerIndBorrower(path+'732854732854333808-Individual-Borrower-2019Sep29.txt',cusID)
# write to file
with open(bank+"smallIndBorrower.txt", "w", newline='') as f:
    wr = csv.writer(f, delimiter='|')
    wr.writerows(smallIndBorro)


smallCorpBorro = smallerCorpBorrower(path+'732854732854333808-Corporate-Borrower-2019Sep29.txt',cusID)
# write to file
with open(bank+"smallCorpBorrower.txt", "w", newline='') as f:
    wr = csv.writer(f, delimiter='|')
    wr.writerows(smallCorpBorro)



