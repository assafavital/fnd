import requests
# import statistics


class WebRanking:

    similarWebUrlPart1 = 'https://api.similarweb.com/v1/website/'
    similarWebUrlPart2 = '/category-rank/category-rank?api_key=09e455f22c5b484eb925891d5122450f'

    def getSimilarWebRank(self, domain):
        rank = -1;
        url = self.similarWebUrlPart1 + domain + self.similarWebUrlPart2
        print('getting ranking for: ' + domain)
        print('using similar web API: ' + url)
        resp = requests.get(url)
        print('similar web API response: ' + resp.text)
        if resp.status_code == 200:
            rank = resp.json()['rank']
        return int(rank)

    def getRanking(self, domains):
        ranks = []
        for domain in domains:
            ranks.append(self.getSimilarWebRank(domain))
        ranks.sort()
        avg = sum(ranks)/len(ranks)
        # variance = statistics.pvariance(ranks)
        variance = sum((avg - value) ** 2 for value in ranks) / len(ranks)
        return '{ "average":' + str(avg) + ', "variance":' + str(variance) + ' }'


ranker = WebRanking()
print(ranker.getRanking(["globes.co.il", "ynet.co.il", "cnn.com"]))




