
# There is no code of Python3 type for this problem


"select w1.Id from weather as w1,weather as w2 where w1.Temperature > w2.Temperature and to_days(w1.RecordDate)-to_days(w2.RecordDate)=1;"
