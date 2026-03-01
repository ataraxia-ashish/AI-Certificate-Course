def leap_year(year): 
    if year%4==0 : 
        return True
    else : 
        return False
def day_of_week(day): 
    match day: 
        case 1 :        
            return "Monday"
        case 2 :        
            return "Tuesday"
        case 3 :        
            return "Wednesday"
        case 4 :        
            return "Thursday"
        case 5 :        
            return "Friday"
        case 6 :        
            return "Saturday"        
        case 7 :        
            return "Sunday"
        case _:              
            return "Invalid number !!" 
def weekend(day) :                
    if day_of_week(day)=="Saturday" or day_of_week(day)=="Sunday" : 
        return "It is weekend !! "
    else : 
        return "It is not weekend !! "
def festival(day,month) : 
     if day==14 and month==1: 
         return "The kite Festival !! "  
     elif day==25 and month==12: 
         return "The Chrismas festival"  
     elif day==1 and month==1 : 
         return "The New year !!"      
     elif day==26 and month==1 : 
         return "Repuplic day !!"
     elif day==15 and month==8 : 
         return "Independence day !!"    
     else : 
         return "No festival in the data !! "    
def month_name(month) : 
    match month : 
        case 1 : 
            return "January"
        case 2 : 
            return "February"    
        case 3 : 
            return "March"
        case 4 : 
            return "April"    
        case 5 : 
            return "May"
        case 6 : 
            return "June"    
        case 7 : 
            return "July"
        case 8 : 
            return "August"    
        case 9 : 
            return "September"
        case 10 : 
            return "October"    
        case 11 : 
            return "November"
        case 12 : 
            return "December"    
        case _: 
             return "Invalid month !!"  
def days_per_month(month):
    if month<8 :
        if month==2: 
                return "The month February has 28 days!!"
        elif month%2!=0 :  
            return month_name(month)+" has 31 Days !!"
        else:
            return month_name(month)+" has 30 days!!"
    else:
        if month%2==0 : 
            return month_name(month)+" has 31 Days !!"
        else:
            return month_name(month)+" has 30 days!!"
def age_calculate(birth_year) : 
    age = 2026 - birth_year
    return age      
def season(month): 
    if month>12 : 
        return "Invalid month"
    else : 
        if month<3 or month>10 : 
            return "Winter"    
        elif month>=3 and month<=6 : 
            return "Summer"
        else : 
            return "Monsoon"    
def greetings(hour) :           
    if hour<12 and hour>=4 : 
        return "Good Morning !!"  
    elif hour>=12 and hour<16 : 
        return "Good afternoon !! "
    elif hour>=16 and hour<20 :     
        return "Good evening !!" 
    elif hour>=20 or hour<4 : 
        return "Good night !!"
def days_in_year(year) : 
    if leap_year(year) : 
        return f"{year} is a leap year, it has 366 days !!"
    else : 
        return f"{year} is not a leap year, it has 365 days !!"