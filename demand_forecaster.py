def demand_forecaster():

    import csv
    from get_avg import get_avg_dict
    from get_op import get_op
    j = 0
    dict = {}
    
    with open("product_history2.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            dict[j] = {'ip' : int(row[1]), 'op_est': int(row[3]), 'op': int(row[4])}
            j = j + 1

    steps = 11 #number of months starting from 0
    r_dict = get_avg_dict(dict, steps)

    j = 0
    while(j < 10):
        ip = float(input("forecast for: "))
        #ip = 3 #get forecasted output value for March month
        op_est = float(input("estimated output: "))
        #op_est = 24
    
        print(get_op(r_dict, ip, op_est))
        #print(r_dict)
        j = j + 1
        