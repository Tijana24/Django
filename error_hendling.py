try:
    a=0/0
except ZeroDivisionError as zero_division_error :
    a=0
    print(zero_division_error)
finally:
    print('Situacija pod kontrolom')