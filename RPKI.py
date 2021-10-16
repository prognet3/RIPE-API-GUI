from RipeRouteAnnounced import RouteAnnounced
import requests


class ResultForGUI:
    def __init__(self):
        self.ripe = RouteAnnounced()
        self.sp1 = self.ripe.ripe_route_announced()

    def announced(self):
        finalprefixannouned = []
        for routes in range(len(self.sp1)):
            finalprefixannouned.append("Announced Prefix: {} ".format(self.sp1[routes]))
        return finalprefixannouned

    def rpki(self):
        finalrpki = []
        for JustPrefixes in range(len(self.sp1)):
            result = self.sp1[JustPrefixes]
            url = "https://stat.ripe.net/data/rpki-validation/data.json?resource=49666&prefix={}".format(result)
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            checkrpki = response.json()
            prefix_validation = checkrpki["data"]["validating_roas"]
            # print(prefix_validation)
            for checkvalidation in range(len(prefix_validation)):
                prefix_ex = prefix_validation[checkvalidation]["prefix"]
                validity = prefix_validation[checkvalidation]["validity"]
                if validity == "valid":
                    finalrpki.append("prefix is {} and validity : {}".format(prefix_ex, validity))
                else:
                    finalrpki.append("prefix {} Should be checked ---> {}".format(prefix_ex, validity))
        return finalrpki


