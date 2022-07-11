import requests
class speed_limit:
    def __init__(self,api_key):
        self.key = api_key
        self.avail = []
        self.data  = None
        
    #Input to this function must be list/1d-array having single latitude and longitude   
    #eg: coord  = [latitude,longitude]
    def get_data(self,coord = []):
        if list(self.avail) != list(coord):
            self.avail = coord
            api_url = "https://routematching.hereapi.com/v8/match/routelinks?apikey={key}&waypoint0={lat},{long}&mode=fastest;car&routeMatch=1&\
                       attributes=SPEED_LIMITS_FCn(FROM_REF_SPEED_LIMIT,TO_REF_SPEED_LIMIT)".format(key = self.key ,lat=coord[0],long = coord[1])
            r = requests.get(url = api_url ) 
            self.data = r.json()
            return self.data
        else:
            return self.data
        
    #Input to this function must be list/1d-array having single latitude and longitude    
    #eg: coord  = [latitude,longitude]   
    def get_limit(self,coord = []):
        data = self.get_data(coord)
        try:
            to_loc = data['response']['route'][0]['leg'][0]['link'][0]['attributes']['SPEED_LIMITS_FCN'][0]['TO_REF_SPEED_LIMIT']
            from_loc = data['response']['route'][0]['leg'][0]['link'][0]['attributes']['SPEED_LIMITS_FCN'][0]['FROM_REF_SPEED_LIMIT']
            return max(int(to_loc),int(from_loc))
        except:
            return 0
