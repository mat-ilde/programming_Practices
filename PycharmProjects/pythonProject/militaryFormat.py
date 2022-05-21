import re

def militaryFormat(s):

    spliting_time=s.split(":")
    hour=spliting_time[0]
    final_minutes = spliting_time[1]
    seconds = spliting_time[2]
    final_seconds = re.findall('[0-9]+', seconds)
    am_pm_format = re.findall('[A-Z]+', seconds)
    str_am_pm_format = ''.join(am_pm_format).rstrip('\n')
    if hour == "12" and str_am_pm_format == "AM":
        hour="00"
    if hour == "12" and str_am_pm_format == "PM":
        hour = "12"
    if hour != "12" and str_am_pm_format == "AM":
        hour=hour
    if hour != "12" and str_am_pm_format == "PM":
        hour=int(hour)+12


    str_military_seconds = ''.join(final_seconds).rstrip('\n')
    military_format = str(hour)+":"+final_minutes+":"+str_military_seconds
    print(military_format)

    return military_format
if __name__ == '__main__':
    time= "10:05:45PM"
    militaryFormat(time)