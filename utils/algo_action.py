def algo(seq):
    seq = seq[1:]
    ans = [None]*19
    curr = 0
    for i in range(17):
        fur = seq[i+2]-seq[i+1]
        if curr == 0:
            if fur > 0:
                ans[i] = 1
                curr += 1
            elif fur < 0:
                ans[i] = -1
                curr -= 1
            else: ans[i] = 0
        elif curr == 1:
            if fur >= 0:
                ans[i] = 0
            else:
                ans[i] = -1
                curr -= 1
        elif curr == -1:
            if fur <= 0:
                ans[i] = 0
            else: 
                ans[i] = 1
                curr += 1
        else:
            print('error: current={}'.format(curr))
    ans[18] = 0
    ans[17] = 0

    return ans