def calcAngle(hour, minutes):
  # Calculate the angle formed by the handle
    # The angle between each hour is 30 -> 12hr = 360
    #                                  -> 1hr  = 30
    # 30 degrees per hour
    h = (hour + minutes/60)*30
    # Calculate the angle formed by the minute
    # The angle between each minute is 6 -> 60 minute = 360
    #                                       1 minute = 6
    # 6 degrees per hour
    m = minutes*6
    alpha = abs(h-m)
    if alpha > 180:
        alpha = 360 - alpha
    return alpha


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
