#二元搜索函数
def search(sequence, number, lower, upper):
    if lower ==upper:
        assert number == sequence[upper]
        return upper
    else:
        middle =(lower + upper ) // 2
	if number > sequence[middle]:
	    return search(sequence, number, middle+1, upper)
	else:
	    return search(sequence, number, low, middlw)
