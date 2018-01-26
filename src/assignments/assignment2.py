def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    # Write code to calculate faculty evaluation rating according to asssignment instructions
    total = 197

    nev_ratio = nev / total
    rar_ratio = rar / total
    som_ratio = som / total
    oft_ratio = oft / total
    voft_ratio = voft / total
    alw_ratio = alw / total

    if voft_ratio + alw_ratio >= .9:
        return "Excellent"
    elif oft_ratio + voft_ratio + alw_ratio >= .8 and oft_ratio + voft_ratio + alw_ratio < .9:
        return "Very Good"
    elif som_ratio + oft_ratio + voft_ratio + alw_ratio >= .7 and som_ratio + oft_ratio + voft_ratio + alw_ratio < .8:
        return "Good"
    elif rar_ratio + som_ratio + oft_ratio + voft_ratio + alw_ratio >= .6 and rar_ratio + som_ratio + oft_ratio + voft_ratio + alw_ratio < .7:
        return "Needs Improvement"
    elif nev_ratio <.6:
        return "Unacceptable"
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

    

    
