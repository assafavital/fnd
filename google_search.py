from googlesearch import search

class FNDGoogleSearcher:

	def __init__(self):
		self.numOfMatches = 10
		self.stopPage = 1
		self.pausePage = 2

	def __call__(self, query):
		return [result.split("/")[2].replace("www.", "") for result in search(query, tld="co.in",
																			  num=self.numOfMatches,
																			  stop=self.stopPage,
																			  pause=self.pausePage)]

