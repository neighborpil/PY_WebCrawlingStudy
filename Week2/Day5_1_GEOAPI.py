"""
# Google Geo API
 - http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
 - Google Maps API 설정 페이지 : https://console.cloud.google.com/google/maps-apis/api-list?consoleUI=CLOUD&project=webcrawling-1543313268147
"""

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?key=내키&'


while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break;

    url = serviceurl + urllib.parse.urlencode({'address': address}) # 만약 address에 빈칸이 있으면 +, 콤마는 %2이런식으로 바꿔준다

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None # None : null
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4)) # raw string을 보여준다

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)


    """
    # Result

    Enter location: Busan Namgu Bunporo 111
Retrieving https://maps.googleapis.com/maps/api/geocode/json?key=내키&address=Busan+Namgu+Bunporo+111
Retrieved 2156 characters
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "111",
                    "short_name": "111",
                    "types": [
                        "premise"
                    ]
                },
                {
                    "long_name": "Bunpo-ro",
                    "short_name": "Bunpo-ro",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_4"
                    ]
                },
                {
                    "long_name": "Yongho 1(il)-dong",
                    "short_name": "Yongho 1(il)-dong",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_2"
                    ]
                },
                {
                    "long_name": "Nam-gu",
                    "short_name": "Nam-gu",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_1"
                    ]
                },
                {
                    "long_name": "Busan",
                    "short_name": "Busan",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "South Korea",
                    "short_name": "KR",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "608-090",
                    "short_name": "608-090",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "111 Bunpo-ro, Yongho 1(il)-dong, Nam-gu, Busan, South Korea",
            "geometry": {
                "location": {
                    "lat": 35.1292113,
                    "lng": 129.1110962
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 35.1305602802915,
                        "lng": 129.1124451802915
                    },
                    "southwest": {
                        "lat": 35.1278623197085,
                        "lng": 129.1097472197085
                    }
                }
            },
            "place_id": "ChIJfQMpQv7saDURZZur9ZyKrWs",
            "plus_code": {
                "compound_code": "44H6+MC Busan, South Korea",
                "global_code": "8Q7F44H6+MC"
            },
            "types": [
                "street_address"
            ]
        }
    ],
    "status": "OK"
}
lat 35.1292113 lng 129.1110962
111 Bunpo-ro, Yongho 1(il)-dong, Nam-gu, Busan, South Korea
Enter location:
    """
