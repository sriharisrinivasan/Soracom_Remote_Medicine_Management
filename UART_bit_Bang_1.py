#!/usr/bin/python

import sys
import time
import difflib
import pigpio

RX=26
gpgga_info = b'$GPGGA,'
received_data = bytearray()
GPGGA_data_available = bytearray()
NMEA_Buff = bytearray()
pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.bb_serial_read_open(RX, 9600, 8)

try:
        iter_count = 0
        print("DATA - SOFTWARE SERIAL:")
        while(iter_count < 20):
                (count, data) = pi.bb_serial_read(RX)
                if count > 0:
                        received_data+= data
                        #print('Total Received data: ', received_data)
                        GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string
                        #print('GPGGA_data_available: ',GPGGA_data_available)
                        if (GPGGA_data_available>0):
                                received_data = received_data.split(gpgga_info,1)[1]  #store data coming after "$GPGGA," string
                                (count, data) = pi.bb_serial_read(RX)
                                #print('Count: ', count)
                                if count > 0:
                                        received_data+= data
                                        print('Total Received data: ', received_data)
                                        GPGGA_data_available = received_data.find(b'\r\n')   #check for NMEA GPGGA string
                                        #print('GPGGA_data_available: ',GPGGA_data_available)
                                        while (GPGGA_data_available < 0):
                                                (count, data) = pi.bb_serial_read(RX)
                                                if count > 0:
                                                        received_data+= data
                                                        GPGGA_data_available = received_data.find(b'\r\n')   #check for NMEA GPGGA string
                                                        #print('GPGGA_data_available: ',GPGGA_data_available)
                                        received_data = received_data.split(b'\r\n',1)[0]  #store data coming before new line
                                        print('Received data after GPGGA string: ', received_data)
                                        NMEA_Buff = received_data.split(b',')   #store data coming before new line
                                        #print('\nNMEA_Buff: ',NMEA_Buff)
                                        nmea_time = NMEA_Buff[0]                    #extract time from GPGGA string
                                        nmea_latitude = NMEA_Buff[1]                #extract latitude from GPGGA string
                                        nmea_longitude = NMEA_Buff[3]               #extract longitude from GPGGA string

                                        
                                        print('\n**********************************************************')
                                        print('Iteration: ', iter_count)
                                        print("NMEA Time: ", nmea_time.decode('utf-8'))
                                        print ("NMEA Latitude:", nmea_latitude.decode('utf-8'))
                                        print("NMEA Longitude:", nmea_longitude.decode('utf-8'))                                        #get time, latitude, longitude
                                        print('**********************************************************')
                                        
                                        iter_count+= 1
                        else:
                                continue
        pi.bb_serial_read_close(RX)
        pi.stop()                             
                    
except:
        print('Something wrong \n Program exited')
        pi.bb_serial_read_close(RX)
        pi.stop()
