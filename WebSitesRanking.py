import requests
import numpy
# import statistics


class FNDWebRanking:

    similarWebUrlPart1 = 'https://api.similarweb.com/v1/website/'
    similarWebUrlPart2 = '/category-rank/category-rank?api_key=09e455f22c5b484eb925891d5122450f'

    def getSimilarWebRank(self, domain):
        rank = -1;
        url = self.similarWebUrlPart1 + domain + self.similarWebUrlPart2
        print('getting ranking for: ' + domain)
        print('using similar web API: ' + url)
        resp = requests.get(url)
        print('similar web API response: ' + resp.text)
        if resp.status_code == 200 and "Error" not in resp.text:
            rank = numpy.log10(resp.json()['rank'])
        return int(rank)

    def getRanking(self, domains, blacklist, ignorelist):
        ranks = []
        blacklisted_domains = 0
        for domain in domains:
            if domain in ignorelist:
                continue
            rank = self.getSimilarWebRank(domain)
            if rank != -1:
                ranks.append(rank)
            if domain in blacklist:
                blacklisted_domains += 1
        ranks.sort()
        avg = sum(ranks)/len(ranks)
        # variance = statistics.pvariance(ranks)
        variance = sum((avg - value) ** 2 for value in ranks) / len(ranks)

        return '{ "average":' + str(avg) + ', "variance":' + str(variance) + ', "blacklisted":' + str(blacklisted_domains) + ' }'

if __name__ == "__main__":
    ranker = FNDWebRanking()
    blacklist = [domain for domain in open("blacklist.txt","r").read().split()]
    ignorelist = [domain for domain in open("ignorelist.txt","r").read().split()]
    domains = [domain for domain in open("domains.txt","r").read().split()]
    print(ranker.getRanking(domains, blacklist, ignorelist))




