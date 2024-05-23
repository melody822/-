pace_sec1 = (8 * 60 + 15) * 1
pace_sec2 = (7 * 60 + 12) * 1.6
total_sec = pace_sec1 + pace_sec2
run_minutes = total_sec // 60
run_seconds = total_sec % 60
breakfast_hour = 6 + (52 + run_minutes) // 60
breakfast_minute = (52 + run_minutes) % 60
print("吃早餐時間為", int(breakfast_hour), "時", int(breakfast_minute), "分")