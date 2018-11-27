from sklearn.feature_extraction.text import CountVectorizer

class FNDVectorizer:

    def __init__(self):
        self.vector = CountVectorizer()
        self._define_vector()

    def _define_vector(self):
        self.vector.lowercase = True
        self.vector.stop_words = 'english'
        self.vector.max_features = 16

    def __call__(self, spoken_text, therealdeal=True):
        if not therealdeal:
            spoken_text = open("elevator.txt", "r").read().split()
        self.vector.fit(spoken_text)
        query = ""
        for feature in self.vector.get_feature_names():
            query += " {}".format(feature)
        print("Writing query to file query.txt")
        with open("query.txt" , "w") as f:
            f.write(query)
        return query

if __name__ == "__main__":
    with open("elevator.txt", "r") as f:
        article = f.read().split()
        bagger = FNDVectorizer()
        bagger(article)
