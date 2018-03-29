from time import sleep
import os
from random import randint
from zodiac import get_zodiac


if __name__ == '__main__':
    while True:
        try:
            message = ["You are the best couple of the century!", "Your love has been proposed by god :-)", "Your love is like Heer and Ranjha",
                       "Your love is one of its kind", "Have a coffee together this weekend !", "Yours' love is divine"]

            print "\n\nEnter the details for the boy : \n"
            boy = raw_input("Enter the boy's name : ")
            boy_date_of_birth, boy_age, boy_zodiac_sign = get_zodiac()

            print "\n\nEnter the details for the girl :\n"
            girl = raw_input("Enter the girl's name : ")
            girl_date_of_birth, girl_age, girl_zodiac_sign = get_zodiac()

            print "\n\nObtaining Zodiac details..."
            sleep(1)
            print "Done!"
            print "Making calculations..."
            sleep(1)
            print "Done!"

            os.system("clear")
            print "\n\n\nLove Guru presents the details of : " + boy + " and " + girl
            print "\n" + boy + "'s Zodiac sign is : " + boy_zodiac_sign
            print boy + "'s age is : " + str(boy_age)

            print "\n" + girl + "'s Zodiac sign is : " + girl_zodiac_sign
            print girl + "'s age is : " + str(girl_age)

            print ""
            print message[randint(0, 5)]

            print "\nLove is : " + str(randint(78,100)) + " %"

            with open("love_letter_python", 'a') as love_letter:
                love_letter.write(boy)
                love_letter.write("\n")
                love_letter.write(boy_date_of_birth)
                love_letter.write("\n")
                love_letter.write(girl)
                love_letter.write("\n")
                love_letter.write(girl_date_of_birth)
                love_letter.write("\n\n")


        except Exception as e:
            print "\n\nSome error occurred :-( \nPlease try again"
            print e
            print "\n\n\n\n\n\n"

