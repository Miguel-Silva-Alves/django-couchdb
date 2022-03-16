from datetime import datetime

def getTimeEditado():
    now = datetime.now() # current date and time
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Yas%H:%M")
    return dt_string.split("as")