from datetime import datetime,timedelta

def calc(start_date, end_date):
    
    display={}
    if start_date >end_date :
        print("Invalid Input")
        choose()
    current_date = start_date+timedelta(days=1)
    while(current_date < end_date):
        current_month = current_date.strftime("%B")
        if current_date.strftime("%Y") == start_date.strftime("%Y"):
            if current_month not in display:
                display[current_month]=[]
            display[current_month].append(current_date.strftime("%d"))
        else : 
            display_month(display)
            display={}
            start_date+=timedelta(weeks=52)
            display[current_month]=[]
            display[current_month].append(current_date.strftime("%d"))  
        current_date +=timedelta(days=1)
    display_month(display)
    choose()
    exit()
def dates_entry():
    try:
        print("Enter first date")
        date_1=input()
        date_format = '%d/%m/%Y' #date  format
        start_date=datetime.strptime(date_1, date_format)
    
        print("Enter Sencond date")
        date_2 = input()
        end_date=datetime.strptime(date_2, date_format)
        calc(start_date,end_date)
    except ValueError:
        print("Invalid Input")
        choose()
    
    

def choose():
    print("Do you have continue[y/n]")
    choice=input()
    if choice == "y":   
        dates_entry()
    elif choice == "n":
        exit()
    elif choice.isdigit() == True:
        print("Invalid Input")
        choose()
    elif choice == " ":
        exit()
    else:
        print("Invalid Input")
        choose()
    exit()
    
def display_month(display):
    for month,days in display.items():
        print(f"{month}:", days)
    return

dates_entry()

