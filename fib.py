#n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	
#xn =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	
def fib(n: int) -> int:
    if n < 2:
        return n
    prev = 0
    curr = 1
    for i in range(2, n + 1):
        prev, curr = curr,  prev + curr
    return curr
