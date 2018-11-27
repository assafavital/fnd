try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

filename = "c:\\temp\\afnd\\query.txt"
lines = tuple(open(filename, 'r'))
# to search
query = lines[0]
numberOfMatches = 10
for j in search(query, tld="co.in", num=numberOfMatches, stop=1, pause=2):
	domain = j.split("/")[2].replace("www.","")
	print(domain)
