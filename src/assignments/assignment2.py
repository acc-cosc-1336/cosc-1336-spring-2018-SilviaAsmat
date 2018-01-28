def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    # Write code to calculate faculty evaluation rating according to asssignment instructions
    total = nev + rar + som + oft + voft + alw

    nev_ratio = nev / total
    rar_ratio = rar / total
    som_ratio = som / total
    oft_ratio = oft / total
    voft_ratio = voft / total
    alw_ratio = alw / total

    excellent_sum_check = voft_ratio + alw_ratio
    very_good_sum_check = oft_ratio + voft_ratio + alw_ratio
    good_sum_check = som_ratio + oft_ratio + voft_ratio + alw_ratio
    needs_improv_sum_check = rar_ratio + som_ratio + oft_ratio + voft_ratio + alw_ratio

    if excellent_sum_check >= .9:
        return "Excellent"
    elif very_good_sum_check >= .8:
        return "Very Good"
    elif good_sum_check >= .7:
        return "Good"
    elif needs_improv_sum_check >= .6:
        return "Needs Improvement"
    else:
        return "Unacceptable"


def get_ratings(nev, rar, som, oft, voft, alw):
    # Students aren't expected to know this material yet

    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings



    

    
