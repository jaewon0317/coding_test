def search(mat, e_rows, e_cols, park) :
    for i in range(mat) :
        for j in range(mat) :
            if park[e_rows + i][e_cols + j] == '-1' :
                continue
            else :
                return -1
    return 1

def solution(mats, park) :

    mats.sort(reverse=True)

    rows = len(park)
    cols = len(park[0])

    for mat in mats :
        for e_rows in range((rows - mat) + 1) :
            for e_cols in range((cols - mat) + 1) :
                if park[e_rows][e_cols] == '-1' :
                    if search(mat, e_rows, e_cols, park) == -1 :
                        continue
                    else :
                        return mat
    return -1