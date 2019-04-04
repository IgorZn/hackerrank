import time, re

def timeConversion(s):
    key_pm = [num for num in range(0, 13)]
    key_am = [num for num in range(0, 13)]
    key_am.reverse()

    val_am = ["%.2d" % num for num in range(13)]
    val_am.reverse()
    val_am[0] = '00'

    val_pm = ["%.2d" % num for num in range(12, 25)]
    val_pm[len(val_pm)-1] = 12

    pm_pairs = dict(zip(key_pm, val_pm))
    am_pairs = dict(zip(key_am, val_am))
    print(am_pairs)
    print(pm_pairs)

    if s[8:].lower() == 'pm':
        start_with = s.split(':')[0]
        formatted_time = re.sub(r'^\w+', str(pm_pairs[int(start_with)]), s[:8])
        print(formatted_time)
        return formatted_time

    if s[8:].lower() == 'am':
        start_with = s.split(':')[0]
        formatted_time = re.sub(r'^\w+', str(am_pairs[int(start_with)]), s[:8])
        print(formatted_time)
        return formatted_time




s = '12:40:22AM'
timeConversion(s)