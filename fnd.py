from vid2txt import FNDVid2Txt
from bagOfWords import FNDVectorizer
from google_search import FNDGoogleSearcher
from WebSitesRanking import FNDWebRanking
from machineLearning import FNDOpenScoring
import argparse, os

if __name__ == "__main__":
    # Argument parsing
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", type=str)
    args = argparser.parse_args()

    # Fetch text from video
    vid2txt = FNDVid2Txt()
    text = vid2txt(args.file)

    # Generate keywords for Google Search API
    vectorizer = FNDVectorizer()
    query = vectorizer([text], therealdeal=False)

    # Execute Google Search
    searcher = FNDGoogleSearcher()
    domains = searcher(query, therealdeal=False)

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
    print(scorer(jsonString))


