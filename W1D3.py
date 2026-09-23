dic = {'Hana': 90, 'Ahmed': 85, 'Menna': 'Absent', 'Ali': 70}

def function_sum (data):
    total_sum = 0
    count = 0
    for value in dic.values() :
        if type(value) == int  :
            total_sum += value
            count += 1
        else :
            continue
    return total_sum ,count

    
def calculate_average_score(data):
    try:
        total,count = function_sum(dic)
        average= total / count
        print (average)

    except ZeroDivisionError :
        pass
        
calculate_average_score(dic)





# calculate_average_score