ef is_leap(year):
    if((year%4==0) & ((year%100!=0) | (year%400==0))):
        leap=True
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))
