

# 1. Quiz: Lista Mutate

def proc1(p):
	p[0] = p[1]

def proc2(p):
	p = p + [1]

def proc3(p):
	q = p
	p.append(3)
	q.pop()

def proc4(p):
	q = []
	while p:
		q.append(p.pop())
	while q:
		p.append(q.pop())

p = ['Marcos', 'Roberto', 'Carlos']
proc4(p)
#print p

# 2. Quiz: Max of Pages
# file print_all_links

# 3. Quiz: Lists o print abaixo deve se result [1,2,3]
p = [-1,2,1]
p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]
print p

# 4. Quiz: List of Lists
# number total de alunos inscritos em todas as universidades da lista
# e as taxas de matricula totais (que is a soma do numero de alunos matriculados vezes a Taxas de matricula para cada universidade)
udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(lista):
    total_alunos = 0
    total_taxas  = 0
    for p in lista:
        total_alunos += p[1]
        total_taxas += p[1] * p[2]
        
    return total_alunos, total_taxas

print total_enrollment(usa_univs)
#>>> (77285,3058581079)

# 5. Quiz: Max Deep 
# file print_all_links

# 6. Quiz: Max Element
def greatest(list_of_numbers):	
	max = 0
    for e in list_of_numbers:
        if e > max:
            max = e
    return max
