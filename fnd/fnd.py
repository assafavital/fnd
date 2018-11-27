from fnd.vid2txt import FNDVid2Txt
from fnd.bagOfWords import FNDVectorizer
from fnd.google_search import FNDGoogleSearcher
from fnd.WebSitesRanking import FNDWebRanking
from fnd.machineLearning import FNDOpenScoring
from fnd.logger import log
import argparse, os

def mainFlow(filename, therealdeal=False):
    with open("fnd\log.txt", "w") as f:
        f.write("")

    # Fetch text from video
    vid2txt = FNDVid2Txt()
    text = vid2txt(filename, therealdeal)

    # Generate keywords for Google Search API
    vectorizer = FNDVectorizer()
    query = vectorizer([text], therealdeal)

    # Execute Google Search
    searcher = FNDGoogleSearcher()
    domains = searcher(query, therealdeal)
    log("\nGot the following domains:")
    for domain in domains:
        log("\t{}".format(domain))

    # Calculate domains ranking
    webRanker = FNDWebRanking()
    blacklist = ["snopes.com", "urbanlegends.about.com", "breakthechain.org",
                 "truthorfiction.com", "sophos.com", "hoax-slayer.com",
                 "vmyths.com", "hoaxbusters.org", "virusbusters.itcs.umich.edu"]
    ignorelist = ["facebook.com", "youtube.com", "google.com",
                  "instagram.com", "snapchat.com", "twitter.com"]
    jsonString = webRanker.getRanking(domains, blacklist, ignorelist)

    # Evaluate result of machine learning (PFS)
    scorer = FNDOpenScoring()
    res = scorer(jsonString)
    credibilityScore = 100 - round(100 * res['probabilityOfFakeNews'], 2)
    log("\n Credibility Score: {}%".format(credibilityScore))
    # print("Credibility Score: {}%".format(credibilityScore))


