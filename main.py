import math
import random
import numpy as np

print("***** Homework CN 2020 *******")
"""
    Să se găsească cel mai mic număr pozitiv u > 0, de forma u = 10^(-m) 
    care satisface proprietatea: 1 +c u ≠ 1
    unde prin +c am notat operația de adunare efectuată de calculator. Numărul u se
    numește precizia mașină.
"""
# n =  global number
n = 16
m = int(math.log2(n))
p = int(n / m) + 1
nPeM = n / m


def createArrForComparison(n):
    res = []
    for i in range(n):
        tempRes = bin(i)
        tempRes = tempRes.split("b")
        res1 = str(tempRes[1])
        length1 = len(res1)
        if (length1 < 4):
            for i in range(4 - length1):
                res1 = "0" + res1
        res.append(list(map(int, str(res1))))
    return res


def randomNumber(min, max):
    return random.randint(min, max)


def getArrOfSmallMatrix(matrix, invers=True):
    global n
    res = []
    a = 0
    b = 4
    if invers:
        while (b <= n):
            tempAsnwer = matrix[:, a:b]
            res.append(tempAsnwer)
            a += 4
            b += 4
    else:
        while (b <= n):
            tempAsnwer = matrix[a:b, :]
            res.append(tempAsnwer)
            a += 4
            b += 4
    return res


def getRandomMatrix(n):
    arr = np.random.randint(2, size=(n, n))

    # for i in range(2):
    #     arr.ravel()[i::arr.shape[1] + 2] = 1
    # print(arr)
    return arr


def getNCombinationsOfSummLines():
    matrixB = getRandomMatrix(n)

    arrOfSubmatrixB = getArrOfSmallMatrix(matrixB, False)
    listOfBinariesCombinations = createArrForComparison(n)

    subListOfNxNinB = []
    for submatrixBi in arrOfSubmatrixB:
        resultForBi = []
        for i in listOfBinariesCombinations:
            tempRes = []
            temp3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for j in range(len(i)):
                if (i[j] == 1):
                    # j is the pos ex: 0 0 1 0 => j = 1
                    tempRes.append(np.array(submatrixBi[j]))
            if tempRes is not []:
                for el in tempRes:
                    temp3 = np.logical_or(np.array(temp3), np.array(el))

            resultForBi.append(temp3)
        # print(resultForBi)
        subListOfNxNinB.append(resultForBi)
    return subListOfNxNinB


def getTheIndexFromBinaryArray(arr):
    res = 0
    sz = len(arr)
    for i in range(len(arr)):
        if (arr[i] == 1):
            res = res + 2 ** (sz - i - 1)
    return res


def getNCombinationsForCxCMatrixFinal():
    matrixA = getRandomMatrix(n)
    arrOfSubmatrixA = getArrOfSmallMatrix(matrixA)
    dataProcessedFromB = np.array(getNCombinationsOfSummLines())

    matrixWithAllCi = []
    for subMatrix in range(len(arrOfSubmatrixA)):
        result1 = []
        for line in arrOfSubmatrixA[subMatrix]:
            tempIndex = getTheIndexFromBinaryArray(line)
            result1.append(dataProcessedFromB[subMatrix][tempIndex])
            # tempResForEveryCmatrix = []
            # print(np.array(elFromA))
        matrixWithAllCi.append(result1)
    return matrixWithAllCi


def getFinalFinalMatrix(matrix):
    # print(matrix)
    resultFinal = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    res3 = []
    for i in range(len(matrix)):
        # print(matrix[i])
        res12 = []
        for j in range(len(matrix[i])):
            res12.append(np.logical_or(np.array(resultFinal[j]), np.array(matrix[i][j])))
        res3.append(res12)
    print(len(res3))
    #
    # return np.array(resultFinal)


def problema1():
    ok = True
    i = 0
    while ok:
        i += 1
        if 10 ** (-i) + 1 == 1:
            ok = False
            return 10 ** (-i)


def getRoundNumbers():
    result = []
    for i in range(2, 10000):
        res = i / math.log2(i)
        if (int(res) - res == 0):
            result.append(i)
    return result

getFinalFinalMatrix(getNCombinationsForCxCMatrixFinal())
# print(getFinalFinalMatrix(getNCombinationsForCxCMatrixFinal()))
