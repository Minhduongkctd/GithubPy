from datetime import date

begin_date = date(2014,7,2)
end_date = date(2014,7,11)
delta = end_date - begin_date

print(delta.days, "days")
