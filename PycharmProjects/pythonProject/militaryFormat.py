import re
"""
    Function as a time in 12 hour format and return a military format 24 hour
"""

def militaryFormat(s):

    #spliting the time in hour, minutes, seconds
    spliting_time=s.split(":")
    #saving the hour
    hour=spliting_time[0]
    #saving the minutes
    final_minutes = spliting_time[1]
    #saving the seconds
    seconds = spliting_time[2]
    #spliting the seconds of am and pm
    final_seconds = re.findall('[0-9]+', seconds)
    # splitting the am, pm and the seconds
    am_pm_format = re.findall('[A-Z]+', seconds)
    #converting am and pm to strings
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