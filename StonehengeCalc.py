import numpy as np
import ephem
from datetime import datetime
import math

LAT = '51.178870'
LONG = '-1.826199'

class Stonehenge:

    def __init__(self):
        self.latitude = LAT
        self.longitude = LONG


    def calculate_visibility(self, celestial_body, date_time):
        observer = ephem.Observer()
        observer.lat = self.latitude
        observer.lon = self.longitude
        observer.date = date_time
        observer.elevation = 50

        body = None
        if celestial_body == "Sun":
            body = ephem.Sun()
        elif celestial_body == "Moon":
            body = ephem.Moon()

        if body is None:
            return "Неподдерживаемое небесное тело"

        body.compute(observer)

        azimuth_deg = math.degrees(float(body.az))
        return azimuth_deg

def holeNumber(ug):
    a = list(np.arange(47, 57)) + list(np.arange(1, 47))
    shag = 360 / 56

    b = np.arange(shag / 2, shag / 2 + shag * 55, shag)
    b = np.around(b, 2)

    if b[55] <= ug <= 360:
        return 56 + round((ug - b[55]) / shag, 2)
    elif 0 <= ug <= b[0]:
        print(ug)
        return 0 + round((shag / 2 + ug) / shag, 2)
    else:
        for i in range(1, 56):
            if b[i] >= ug:
                return a[i + 1] + round((ug - b[i - 1]) / shag, 2)

def times(y, m, d, func: object):
    o = ephem.Observer()
    o.lat, o.long, o.date = LAT, LONG, f'{y}-{m}-{d} 00:00:00'
    obj = func(o)
    return {'rise': str(o.next_rising(obj)).replace('/', '-'),
            'set': str(o.next_setting(obj)).replace('/', '-')}

def calc(choice, year, month, day, hour=0, minute=0): # choices: 1-Sun, 2-Moon, 3-Sunrise, 4-Sunset, 5-Moonrise, 6-Moonset
    stonehenge = Stonehenge()

    try:
        year = int(year)
        month = int(month)
        day = int(day)

        if choice in ["1", "2"]:
            hour = int(hour)
            minute = int(minute)
            date_time = datetime(year, month, day, hour, minute)
            celestial_body = "Sun" if choice == "1" else "Moon"
        else:
            if choice in ["3", "4"]:
                data = times(year, month, day, ephem.Sun)
                celestial_body = 'Sun'
            elif choice in ["5", "6"]:
                data = times(year, month, day, ephem.Moon)
                celestial_body = 'Moon'
            date_time = data['rise'] if choice in ["3", "5"] else data['set']


        result = stonehenge.calculate_visibility(
            celestial_body, date_time
        )
        return {'azimuth': result, 'hole': holeNumber(result)}

    except ValueError:
        return ValueError
    except Exception as e:
        return e

def run():
    a = calc('6', '2018', '12', '22')
    print(a['azimuth'], a['hole'])
