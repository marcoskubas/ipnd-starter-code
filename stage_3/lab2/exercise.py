
# 1. Quiz: Quadrado Simetrico
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(lista):
    # Your code here
    i = 0
    while i < len(lista):
        column = []
        for p in lista:
            column.append(p[i])
        if column != lista[i]:
            return False
        i = i + 1
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])    

# 2. Quiz: Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2

# 3. Quiz: Media de uma Lista

def list_mean(lista):
    soma = 0
    for p in lista:
        soma = soma + p+0.0
    media = soma / len(lista)
    return media


print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
#print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0




