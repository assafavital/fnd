from googlesearch import search

class FNDGoogleSearcher:

	def __init__(self):
		self.numOfMatches = 10
		self.stopPage = 1
		self.pausePage = 2

	def __call__(self, query, therealdeal=False):
            if therealdeal is False:
                with open("query.txt", "r") as f:
                    query = f.read()

		    return [result.split("/")[2].replace("www.", "") for result in search(query, tld="co.in",
																			  num=self.numOfMatches,
																			  stop=self.stopPage,
																			  pause=self.pausePage)]

if __name__ == "__main__":
	searcher = FNDGoogleSearcher()
	query = open("query.txt", "r").read()
	with open("domains.txt", "w") as f:
		txt = ""
		for result in searcher(query):
			txt += " {}".format(result)
		f.write(txt)

