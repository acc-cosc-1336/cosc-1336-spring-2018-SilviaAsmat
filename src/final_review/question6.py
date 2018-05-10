def count_odd_even(list_num):
    even_cnt = 0
    odd_cnt = 0
    
    for num in list_num:
        
        if num % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1

    return (even_cnt, odd_cnt)
            
