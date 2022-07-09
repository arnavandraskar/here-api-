import requests
class speed_limit:
    def __init__(self,api_key):
        self.key = api_key
        
    def get_speed_limit(self,lat = None ,long = None):
        api_url = "https://routematching.hereapi.com/v8/match/routelinks?apikey={key}&waypoint0={lat},{long}&mode=fastest;car&routeMatch=1&attributes=SPEED_LIMITS_FCn(*)".format(key = self.key ,lat=lat,long = long)
        r = requests.get(url = api_url ) 
        data = r.json()
        try:
            to_loc = data['response']['route'][0]['leg'][0]['link'][0]['attributes']['SPEED_LIMITS_FCN'][0]['TO_REF_SPEED_LIMIT']
            from_loc = data['response']['route'][0]['leg'][0]['link'][0]['attributes']['SPEED_LIMITS_FCN'][0]['FROM_REF_SPEED_LIMIT']
            return max(int(to_loc),int(from_loc))
        except:
            return 0