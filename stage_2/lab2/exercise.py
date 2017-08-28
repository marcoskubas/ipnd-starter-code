# 1. Quiz: Encontre o ultimo
def find_last(texto, texto_find):
    last_pos = -1
    while True:
        pos = texto.find(texto_find, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('aaaa', 'a')
print 'teste'

# 4. Quiz: Udacify
def udacify(a):
	return 'U' + a

print udacify('dacians')

# 5. Quiz: Medians
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
	big = biggest(a,b,c)
	if big == a:
		return bigger(b,c)
	if big == b:
		return bigger(a,c)
	else:
		return bigger(a,b)


print median(9,3,6)	


