def is_leap(year):
    leap = False
    if 1900<=year<=(10**5):
      if year%4==0 and year%100!=0:
        return True 
      elif year%100==0 and year%400==0:
        return True
    
    return leap