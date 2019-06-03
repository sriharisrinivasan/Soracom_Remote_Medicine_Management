import requests

def soracom_auth():
    headers = {'content-type': 'application/json'}

    data = '{"email": "poc+SrihariS@soracom.jp", "password": "CixmwAkzZRUbRbywvUJMHY9T"}'
    url = 'https://g.api.soracom.io/v1/auth'

    r = requests.post(url, headers=headers, data=data)
    a = r.content.decode('utf-8')[1:len(r.content)-1].split(',')
    apikey = a[0].split(':')[1].strip('"')
    operator_id = a[1].split(':')[1].strip('"')
    token = a[2].split(':')[1].strip('"')
    print("ApiKey: ", apikey)
    print("Operator ID: ", operator_id)
    print("Token: ", token)

def send_gps_data_to_funnel_s3(NMEA_Time, NMEA_Latitude, NMEA_Longitude):
    
    headers = {'content-type': 'application/json'}
    NMEA_Time_str = "NMEA Time - " + str(NMEA_Time)
    NMEA_Latitude_str = ", NMEA Latitude - "+ str(NMEA_Latitude)
    NMEA_Longitude_str = ", NMEA Longitude - " + str(NMEA_Longitude)
    message_str = NMEA_Time_str + NMEA_Latitude_str + NMEA_Longitude_str
    data = '{"message": "' + message_str + '"}'
    #data = '{"message": "Hello Soracom Funnel to HTTP!"}'
    print(data)
    url = 'http://funnel.soracom.io'

    r = requests.post(url, headers=headers, data=data)
    print(r)
