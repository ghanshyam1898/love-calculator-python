import os
from datetime import date


def get_zodiac():
    zodiac_sign = ''
    Year = input("\nyear of birth : " )
    Month = input("month of birth : " )
    Day = input("day of birth : " )
    date_of_birth = (str(Day) + "/" + str(Month) + "/" + str(Year))
    d = date.today()
    y = d.year
    age = y - int(Year)

    if ((int(Month)==12 and int(Day) >= 22)or(int(Month)==1 and int(Day)<= 19)):
        zodiac_sign = ("Capricorn")
    elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 17)):
            zodiac_sign = ("aquarium")
    elif ((int(Month)==2 and int(Day) >= 18)or(int(Month)==3 and int(Day)<= 19)):
            zodiac_sign = ("Pices")
    elif ((int(Month)==3 and int(Day) >= 20)or(int(Month)==4 and int(Day)<= 19)):
            zodiac_sign = ("Aries")
    elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
            zodiac_sign = ("Taurus")
    elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
            zodiac_sign = ("Gemini")
    elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
            zodiac_sign = ("Cancer")
    elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)): 
            zodiac_sign = ("Leo")
    elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)): 
            Signo_Zodiacal = ("Virgo")
    elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
            zodiac_sign = ("Libra")
    elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 21)): 
            zodiac_sign = ("Scorpio")
    elif ((int(Month)==11 and int(Day) >= 22)or(int(Month)==12 and int(Day)<= 21)):
            zodiac_sign = ("Sagittarius")

    return date_of_birth, age, zodiac_sign


if __name__ == '__main__':
    while True:
        get_zodiac()
