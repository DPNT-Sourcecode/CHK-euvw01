

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    c_A=skus.count('A')
    c_B=skus.count('B')
    c_C=skus.count('C')
    c_D=skus.count('D')
    total_c=len(skus)
    p_a=int(c_A/3)*130+c_A%3*50
    p_b=int(c_B/2)*45+c_B%2*30
    p_c=c_C*20
    p_d=c_D*15
    if c_A+c_B+c_C+c_D!=total_c:
        return -1
    else:
        return p_a+p_b+p_c+p_d

