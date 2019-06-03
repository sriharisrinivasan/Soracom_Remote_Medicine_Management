from soracom_library import *
from GPS_Data import *


def main():
    
    #print("Authenticating.....")
    #soracom_auth()
    for i in range(1,25):
        [nmea_time,nmea_latitude,nmea_longitude] = GPS_Data_Read()
        send_gps_data_to_funnel_s3(nmea_time, nmea_latitude, nmea_longitude)


if __name__ == "__main__":
    main()
    
