def timeConversion(s):
    # Write your code here
    while len(s)>0:
        parts=s.split(":")
        hour=parts[0]
        minute=parts[1]
        second=parts[2][:2]
        time_format=parts[2][2:]
        if time_format=="PM":
            if hour=="12":
                new_time=hour+":"+minute+":"+second
                return new_time
            elif hour!="12":
                new_hour=int(hour)+12
                new_time=str(new_hour)+":"+minute+":"+second
                return new_time
        else:
            if hour=="12":
                hour="00"
                new_time=hour+":"+minute+":"+second
                return new_time
            else:
                new_time=hour+":"+minute+":"+second
                return new_time



s = "07:05:45PM"
print(timeConversion(s))



#output  19:05:45