#!/usr/bin/python
import sys
import time
import difflib
import os
import time
try:
        my_command = "sudo killall pigpiod"
        os.system(my_command)
except:
        print("Process already running")
try:
        my_command = "sudo pigpiod"
        os.system(my_command)
except:
        print("Cannot start pigpiod process")
import pigpio
RX=26
gpgga_info = b'$GPGGA,'
received_data = bytearray()
GPGGA_data_available = bytearray()
NMEA_Buff = bytearray()
pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.bb_serial_read_open(RX, 9600, 8)

def GPS_Data_Read():        
        try:
                nmea_time = 0
                nmea_latitude = 13.012
                nmea_longitude = 77.3349
                print("DATA - SOFTWARE SERIAL:")
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
                                        print('Iteration: ', i)
                                        print("NMEA Time: ", nmea_time)
                                        print ("NMEA Latitude:", nmea_latitude)
                                        print("NMEA Longitude:", nmea_longitude)                                        #get time, latitude, longitude
                                        print('**********************************************************')
         
                pi.bb_serial_read_close(RX)
                print('\nNo data - default is printed')
                print('**********************************************************')
                print('Iteration: ', i)
                print("NMEA Time: ", nmea_time)
                print ("NMEA Latitude:", nmea_latitude)
                print("NMEA Longitude:", nmea_longitude)                                        #get time, latitude, longitude
                print('**********************************************************')
         

                pi.bb_serial_read_close(RX)    
                            
        except:
                print('Process Error')
                return nmea_time,nmea_latitude,nmea_longitude
        return [nmea_time,nmea_latitude,nmea_longitude]  
        pi.bb_serial_read_close(RX)
        my_command = "sudo killall pigpiod"
        os.system(my_command)
        pi.stop()        
