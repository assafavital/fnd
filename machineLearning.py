from openscoring import Openscoring
import os


os = Openscoring("http://localhost:8080/openscoring")
kwargs = {"auth": ("admin", "adminadmin")}

try:
    os.deployFile("FakeNewsDetector", "FakeNewsAIModel.pmml", **kwargs)
except Exception as ex:
    print(ex)

arguments = {
    "similarWebAvgScore": 5.1,
    "similarWebStdScore": 2.27,
    "sourceTaggedAsFakeCount": 5.0,
    "fakeFactSitesCount": 2.0,
    "reporterScore": 3.0
}

result = os.evaluate("FakeNewsDetector", arguments)
print(result)

