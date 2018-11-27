from vid2txt import FNDVid2Txt
from bagOfWords import FNDVectorizer
from google_search import FNDGoogleSearcher
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
    query = vectorizer(text)

    # Execute Google Search
    searcher = FNDGoogleSearcher()
    domains = searcher(query)