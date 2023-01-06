from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def aimtrainer():
    incognito = webdriver.ChromeOptions()
    incognito.add_argument('-incognito')
    google = webdriver.Chrome('/Users/neil/Downloads/chromedriver', options=incognito)
    google.get('https://humanbenchmark.com/tests/aim')
    actionchains = ActionChains(google)
    time.sleep(1)
    start = actionchains.context_click(google.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/div/div[5]')).perform()
    index = 0
    while index < 30:
        try:
            target = google.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/div/div[6]').click()
            index += 1
            print(index)
        except:
            print('miss')
            continue
    print('done')
    google.get_screenshot_as_file('humanbenchmark-aimtrainer.png')
    time.sleep(10)
    google.quit()

def typing():
    google = webdriver.Chrome('/Users/neil/Downloads/chromedriver')
    google.get('https://humanbenchmark.com/tests/typing')
    time.sleep(1)
    textbox = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[2]/div')
    script = textbox.text
    textbox.send_keys(script)
    google.get_screenshot_as_file('humanbenchmark-typing.png')
    time.sleep(10)
    google.quit()

def chimptest():
    def firstchimp():

        oneone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[1]')
        onetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[2]')
        onethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[3]')
        onefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[4]')
        onefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[5]')
        onesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[6]')
        oneseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[7]')
        oneeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[8]')

        twoone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[1]')
        twotwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[2]')
        twothree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[3]')
        twofour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[4]')
        twofive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[5]')
        twosix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[6]')
        twoseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[7]')
        twoeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[8]')

        threeone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[1]')
        threetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[2]')
        threethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[3]')
        threefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[4]')
        threefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[5]')
        threesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[6]')
        threeseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[7]')
        threeeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[8]')

        fourone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[1]')
        fourtwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[2]')
        fourthree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[3]')
        fourfour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[4]')
        fourfive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[5]')
        foursix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[6]')
        fourseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[7]')
        foureight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[8]')

        fiveone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[1]')
        fivetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[2]')
        fivethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[3]')
        fivefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[4]')
        fivefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[5]')
        fivesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[6]')
        fiveseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[7]')
        fiveeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[8]')

        gridlist = [
            oneone, onetwo, onethree, onefour, onefive, onesix, oneseven, oneeight,
            twoone, twotwo, twothree, twofour, twofive, twosix, twoseven, twoeight,
            threeone, threetwo, threethree, threefour, threefive, threesix, threeseven, threeeight,
            fourone, fourtwo, fourthree, fourfour, fourfive, foursix, fourseven, foureight,
            fiveone, fivetwo, fivethree, fivefour, fivefive, fivesix, fiveseven, fiveeight]

        masternum = 4
        masterindex = 1
        try:
            while masterindex <= masternum:
                index = 0
                for item in gridlist:
                    boxtext = gridlist[index].text
                    if boxtext == '':
                        print('none')
                    else:
                        boxtext = str(boxtext)
                        boxtext = int(boxtext)
                        if boxtext == masterindex:
                            gridlist[index].click()
                            break
                        else:
                            print('secondary none')
                    index += 1
                masterindex += 1
        except:
            print('ignoring error')
    def allchimps(masternum):

        target_1 = 1
        target_2 = 2
        target_3 = 3
        target_4 = 4
        target_5 = 5
        target_6 = 6
        target_7 = 7
        target_8 = 8
        target_9 = 9
        target_10 = 10
        target_11 = 11
        target_12 = 12
        target_13 = 13
        target_14 = 14
        target_15 = 15
        target_16 = 16
        target_17 = 17
        target_18 = 18
        target_19 = 19
        target_20 = 20
        target_21 = 21
        target_22 = 22
        target_23 = 23
        target_24 = 24
        target_25 = 25
        target_26 = 26
        target_27 = 27
        target_28 = 28
        target_29 = 29
        target_30 = 30
        target_31 = 31
        target_32 = 32
        target_33 = 33
        target_34 = 34
        target_35 = 35
        target_36 = 36
        target_37 = 37
        target_38 = 38
        target_39 = 39
        target_40 = 40

        oneone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[1]')
        onetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[2]')
        onethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[3]')
        onefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[4]')
        onefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[5]')
        onesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[6]')
        oneseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[7]')
        oneeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[1]/div[8]')

        twoone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[1]')
        twotwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[2]')
        twothree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[3]')
        twofour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[4]')
        twofive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[5]')
        twosix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[6]')
        twoseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[7]')
        twoeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[2]/div[8]')

        threeone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[1]')
        threetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[2]')
        threethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[3]')
        threefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[4]')
        threefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[5]')
        threesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[6]')
        threeseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[7]')
        threeeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[3]/div[8]')

        fourone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[1]')
        fourtwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[2]')
        fourthree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[3]')
        fourfour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[4]')
        fourfive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[5]')
        foursix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[6]')
        fourseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[7]')
        foureight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[4]/div[8]')

        fiveone = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[1]')
        fivetwo = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[2]')
        fivethree = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[3]')
        fivefour = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[4]')
        fivefive = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[5]')
        fivesix = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[6]')
        fiveseven = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[7]')
        fiveeight = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div[5]/div[8]')

        gridlist = [
            oneone, onetwo, onethree, onefour, onefive, onesix, oneseven, oneeight,
            twoone, twotwo, twothree, twofour, twofive, twosix, twoseven, twoeight,
            threeone, threetwo, threethree, threefour, threefive, threesix, threeseven, threeeight,
            fourone, fourtwo, fourthree, fourfour, fourfive, foursix, fourseven, foureight,
            fiveone, fivetwo, fivethree, fivefour, fivefive, fivesix, fiveseven, fiveeight]

        time.sleep(.5)
        masterindex = 1
        while masterindex <= masternum:
            index = 0
            for item in gridlist:
                boxtext = gridlist[index].text
                if boxtext == '':
                    print('none')
                elif boxtext == '.':
                    print('blank')
                else:
                    boxtext = str(boxtext)
                    boxtext = int(boxtext)
                    if boxtext == target_1:
                        target_1 = gridlist[index]
                    elif boxtext == target_2:
                        target_2 = gridlist[index]
                    elif boxtext == target_3:
                        target_3 = gridlist[index]
                    elif boxtext == target_4:
                        target_4 = gridlist[index]
                    elif boxtext == target_5:
                        target_5 = gridlist[index]
                    elif boxtext == target_6:
                        target_6 = gridlist[index]
                    elif boxtext == target_7:
                        target_7 = gridlist[index]
                    elif boxtext == target_8:
                        target_8 = gridlist[index]
                    elif boxtext == target_9:
                        target_9 = gridlist[index]
                    elif boxtext == target_10:
                        target_10 = gridlist[index]
                    elif boxtext == target_11:
                        target_11 = gridlist[index]
                    elif boxtext == target_12:
                        target_12 = gridlist[index]
                    elif boxtext == target_13:
                        target_13 = gridlist[index]
                    elif boxtext == target_14:
                        target_14 = gridlist[index]
                    elif boxtext == target_15:
                        target_15 = gridlist[index]
                    elif boxtext == target_16:
                        target_16 = gridlist[index]
                    elif boxtext == target_17:
                        target_17 = gridlist[index]
                    elif boxtext == target_18:
                        target_18 = gridlist[index]
                    elif boxtext == target_19:
                        target_19 = gridlist[index]
                    elif boxtext == target_20:
                        target_20 = gridlist[index]
                    elif boxtext == target_21:
                        target_21 = gridlist[index]
                    elif boxtext == target_22:
                        target_22 = gridlist[index]
                    elif boxtext == target_23:
                        target_23 = gridlist[index]
                    elif boxtext == target_24:
                        target_24 = gridlist[index]
                    elif boxtext == target_25:
                        target_25 = gridlist[index]
                    elif boxtext == target_26:
                        target_26 = gridlist[index]
                    elif boxtext == target_27:
                        target_27 = gridlist[index]
                    elif boxtext == target_28:
                        target_28 = gridlist[index]
                    elif boxtext == target_29:
                        target_29 = gridlist[index]
                    elif boxtext == target_30:
                        target_30 = gridlist[index]
                    elif boxtext == target_31:
                        target_31 = gridlist[index]
                    elif boxtext == target_32:
                        target_32 = gridlist[index]
                    elif boxtext == target_33:
                        target_33 = gridlist[index]
                    elif boxtext == target_34:
                        target_34 = gridlist[index]
                    elif boxtext == target_35:
                        target_35 = gridlist[index]
                    elif boxtext == target_36:
                        target_36 = gridlist[index]
                    elif boxtext == target_37:
                        target_37 = gridlist[index]
                    elif boxtext == target_38:
                        target_38 = gridlist[index]
                    elif boxtext == target_39:
                        target_39 = gridlist[index]
                    elif boxtext == target_40:
                        target_40 = gridlist[index]





                    else:
                        print('target out of range?')
                index += 1
            masterindex += 1

        try:
            target_1.click()
            target_2.click()
            target_3.click()
            target_4.click()
            target_5.click()
            target_6.click()
            target_7.click()
            target_8.click()
            target_9.click()
            target_10.click()
            target_11.click()
            target_12.click()
            target_13.click()
            target_14.click()
            target_15.click()
            target_16.click()
            target_17.click()
            target_18.click()
            target_19.click()
            target_20.click()
            target_21.click()
            target_22.click()
            target_23.click()
            target_24.click()
            target_25.click()
            target_26.click()
            target_27.click()
            target_28.click()
            target_29.click()
            target_30.click()
            target_31.click()
            target_32.click()
            target_33.click()
            target_34.click()
            target_35.click()
            target_36.click()
            target_37.click()
            target_38.click()
            target_39.click()
            target_40.click()
        except:
            print('all clicked')
    def chimprepeater():
        while True:
            time.sleep(.25)
            masternum = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div[1]/h1')
            masternum = masternum.text
            masternum = str(masternum)
            masternum = int(masternum)
            nextbutton = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button').click()
            try:
                allchimps(masternum=masternum)
            except:
                print('fin')

    google = webdriver.Chrome('/Users/neil/Downloads/chromedriver')
    google.get('https://humanbenchmark.com/tests/chimp')

    time.sleep(1)

    start = google.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div[1]/div[2]/button').click()

    firstchimp()

    chimprepeater()

'''
google = webdriver.Chrome('/Users/neil/Downloads/chromedriver')
google.get('https://humanbenchmark.com/tests/reactiontime')

time.sleep(1)
start = google.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div[1]').click()

target = WebDriverWait(google, 10).until(
    EC.presence_of_element_located(By.XPATH, '/html/body/div/div/div[4]/div[1]'))

wait = WebDriverWait(google, 10)
while True:
    try:
        target = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'view-go e18o0sx0 css-saet2v e19owgy77')))
        target.click()
    except:
        continue

red = google.find_element_by_xpath('view-waiting e18o0sx0 css-saet2v e19owgy77')
green = google.find_element_by_class_name('view-go e18o0sx0 css-saet2v e19owgy77').click()
'''

print('                                           ______')
print('|        |    |        |    |\      /|    /      \     |\      |')
print('|        |    |        |    | \    / |   /        \    | \     |')
print('|________|    |        |    |  \  /  |   |        |    |  \    |')
print('|        |    |        |    |   \/   |   |--------|    |   \   |')
print('|        |    |        |    |        |   |        |    |    \  |')
print('|        |    |        |    |        |   |        |    |     \ |')
print('|        |    \________/    |        |   |        |    |      \|')
print('')
print(' ______       ________                     _____                                   ______       ____')
print('|      \     |            |\      |       /     \    |        |    |\      /|     /      \     |    \     |      /')
print('|       |    |            | \     |      /           |        |    | \    / |    /        \    |     |    |     /')
print('|______/     |______      |  \    |     /            |________|    |  \  /  |    |        |    |____/     |    /')
print('|      \     |            |   \   |    |             |        |    |   \/   |    |--------|    |  \       |___/')
print('|       |    |            |    \  |     \            |        |    |        |    |        |    |   \      |   \ ')
print('|       |    |            |     \ |      \           |        |    |        |    |        |    |    \     |    \ ')
print('|______/     |________    |      \|       \_____/    |        |    |        |    |        |    |     \    |     \ ')
print('')
print('')
print('a = Aim Trainer')
print('t = Typing')
print('c = Chimp')
userchoice = str(input('Enter Command: '))

if userchoice == 'a':
    aimtrainer()
elif userchoice == 't':
    typing()
elif userchoice == 'c':
    chimptest()
else:
    print('Invalid Command. Please Rerun.')