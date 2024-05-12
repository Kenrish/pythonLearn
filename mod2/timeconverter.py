#!/usr/bin/env python3

def timeconver(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds - hours * 3600 - minutes * 60
    return hours, "hours", minutes, "minutes", seconds, "seconds"

time = timeconver(int(input("Enter time to convert: ")))

print(time)
