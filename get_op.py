def get_op(dict_r, ip, op_est):
    
    op_r_value = 1
    step = len(dict_r)
    
    for j in range(step):
        ip_window = (dict_r.get(j, {}).get('ip_window'))
        
        if(abs(ip - ip_window) <= (step / 2)):
            total = (dict_r.get(j, {}).get('total'))
            count = (dict_r.get(j, {}).get('count'))
            if(total == 0 or count == 0):
                total = count = 1
            op_r_value = total / count
            
    return op_est * op_r_value