from openscoring import Openscoring
import os

class FNDOpenScoring:

    def __init__(self):
        self.scoring = Openscoring("http://localhost:8080/openscoring")
        self.arguments = {
            "fakeFactSitesCount": 2.0,
            "reporterScore": 3.0
        }

    def _deploy(self):
        self.scoring.deployFile("FakeNewsDetector", "FakeNewsAIModel.pmml", {"auth": ("admin", "adminadmin")})

    def _setArgs(self, jsonString):
        self.arguments["similarWebAvgScore"] = jsonString['average']
        self.arguments["similarWebStdScore"] = jsonString['variance']
        self.arguments["sourceTaggedAsFakeCount"] = jsonString['blacklisted']

    def __call__(self, jsonString):
        self._deploy()
        self._setArgs(jsonString)
        result = self.scoring.evaluate("FakeNewsDetector", self.arguments)
        return result

if __name__ == "__main__":
    scorer = FNDOpenScoring()
    with open("json.txt", "r") as f:
        print(scorer(f.read()))