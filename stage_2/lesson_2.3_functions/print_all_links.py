def get_next_target(page):
	start_link  = page.find('<a href=')
	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):	
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)



# Add your own code and notes here
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com"></div>')

seed = 'http://www.udacity.com/cs101x/index.html';
tocrawl = []
crawled = []