#!/usr/bin/env python3

import argparse
from datetime import datetime
from weather_reporter.WeatherApp import WeatherApp


def main():
    # create argument parser object 
    parser = argparse.ArgumentParser(description = "Weather Reporter") 

    parser.add_argument("-q", "--query", type = str, nargs = 1, metavar = "location", help = "Location") 
    parser.add_argument("-d", "--date", type = datetime , nargs = 1, metavar = "date", default = datetime.now(), help = "Enter date to find weather")

    parser.add_argument("-t", "--type", type=str, nargs=1, metavar="type", default="daily", help="type available [5day, tenday,  monthly, today")
    # parse the arguments from standard input 
    args = parser.parse_args()  
    weather_data = WeatherApp.get_weather_info(args.query[0], args.date, args.type[0])
    print(weather_data)


if __name__ == "__main__":
    main()
