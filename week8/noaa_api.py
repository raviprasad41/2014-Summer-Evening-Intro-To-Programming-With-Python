from urllib import urlopen, urlencode
from datetime import datetime, timedelta
from os.path import isfile, exists
from os import makedirs
from time import sleep

base_url = "http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php"
query_delimiter = "?"
prefix = "noaa_"
suffix = ".xml"
folder = "temp"
folder_deliminator = "/"
sleep_seconds = 1
minutes_round_to = 5

while True:
    begin_time = datetime.now()
    end_time = begin_time + timedelta(hours=12) - timedelta(minutes=minutes_round_to)
    begin_iso = begin_time.isoformat()
    end_iso = end_time.isoformat()

    #round to the nearest fives
    delta = timedelta(minutes=begin_time.minute % minutes_round_to,
                      seconds=begin_time.second,
                      microseconds=begin_time.microsecond)
    file_time = str((begin_time - delta).isoformat())

    #TODO Move constants outside loop and just update dynamic values e.g. begin and end times
    raw_params = {
        "whichClient": "NDFDgen",
        "product": "time-series",
        "begin": begin_iso,
        "end": end_iso,
        "Unit": "e",
        "temp": "temp",
        "sky": "sky",
        "lat": "44.92",
        "lon": "-123",
        "Submit": "Submit",
    }

    file_name = prefix + file_time + suffix

    #do we already have this one?
    if not isfile(file_name):
        encoded_params = urlencode(raw_params)
        final_url = base_url + query_delimiter + encoded_params
        input_file = urlopen(final_url)
        xml_string = input_file.read()
        try:
            path = folder + folder_deliminator + file_name
            if not exists(folder):
                makedirs(folder)
            outfile = open(path, "w")
            outfile.write(xml_string)
            outfile.close()
        except IOError:
            print 'Error writing XML response to file: ' + file_name
    sleep(sleep_seconds)