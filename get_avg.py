def get_avg_dict(dict, steps = 10):

    from op_r import op_r

    dict_r = {}
    min_ip = max_ip = (dict.get(2, {}).get('ip')) 
    
    for i, values in dict.items():
        ip = (dict.get(i, {}).get('ip')) 
        if (ip > max_ip):
            max_ip = ip
        elif (ip < min_ip):
            min_ip = ip
    window = (max_ip - min_ip) / steps
    #ToDo: skip outliers

    for i, values in dict.items():
        ip = (dict.get(i, {}).get('ip')) 
        op_est = (dict.get(i, {}).get('op_est'))
        op = (dict.get(i, {}).get('op'))
        op_r_value = op_r(op_est, op)
        
        for j in range(steps + 1):
            ip_window = (min_ip + (j * window))
            total = (dict_r.get(j, {}).get('total'))
            count = (dict_r.get(j, {}).get('count'))
            
            if(total is None or count is None ):
                dict_r[j] = {'ip_window' : ip_window, 'total': 0, 'count': 0}
                total = count = 0
                
            if(abs(ip - ip_window) <= (window / 2)):
                dict_r[j] = {'ip_window' : ip_window, 'total': (total + op_r_value), 'count': (count + 1)}
                break
    
    return dict_r 