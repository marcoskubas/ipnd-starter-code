

print "# 23 Quiz: Teste 2"
s = 'Qualquer coisa'
print s.find(s)
print s.find('s')
print 's'.find('s')
print s.find('')
print s.find(s + '!!!')+1

# Add your own code and notes here
print "# 24. Usando find com numbers"
danton = "De l'audace, encore de l'audace, touhours de l'audace"
print danton.find('audace', 10)

# 25. Quiz: Quiz usando find com numbers
s = "Marcos Kubas"
t = "Luiz Ricardo"
i = 4
print s.find(t,i)
print s[i:].find(t)
print s[i:].find(t)+i
print s[i:].find(t[i:])
print ' '

# 26. Quiz: Extracting Links and 27. Quiz: Final Quiz
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]
print url

