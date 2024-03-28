#Python
def timeConversion(s):
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    return str(ntime[:-2])

#Julia
function timeConversion(s::AbstractString)
    time = split(s, ":")
    if s[end-1:end] == "PM"
        if time[1] != "12"
            time[1] = string(parse(Int, time[1]) + 12)
        end
    else
        if time[1] == "12"
            time[1] = "00"
        end
    end
    ntime = join(time, ":")
    return ntime[1:end-2]
end
