def library_fine(returned, due):
    day_returned, month_returned, year_returned = map(int, returned)
    day_due, month_due, year_due = map(int, due)

    if year_returned > year_due or (year_returned == year_due and month_returned > month_due) or (year_returned == year_due and month_returned == month_due and day_returned > day_due):
        if year_returned == year_due and month_returned == month_due:
            fine = 15 * (day_returned - day_due)
        elif year_returned == year_due:
            fine = 500 * (month_returned - month_due)
        else:
            fine = 10000
    else:
        fine = 0

    return fine

returned = list(map(int, input().split()))
due = list(map(int, input().split()))

result = library_fine(returned, due)
print(result)
