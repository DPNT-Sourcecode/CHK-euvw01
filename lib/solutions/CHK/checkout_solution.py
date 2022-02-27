

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    c_A=skus.count('A')
    c_B=skus.count('B')
    c_C=skus.count('C')
    c_D=skus.count('D')
    c_E=skus.count('E')
    total_c=len(skus)

    After_offer_c_B=c_B-int(c_E/2)
    if After_offer_c_B<=0:
        After_offer_c_B=0

    p_a=int(c_A/5)*200+int((c_A%5)/3)*130+((c_A%5)%3)*50
    p_b=int(After_offer_c_B/2)*45+(After_offer_c_B%2)*30
    p_c=c_C*20
    p_d=c_D*15
    p_e=c_E*40
    if c_A+c_B+c_C+c_D+c_E!=total_c:
        return -1
    else:
        return p_a+p_b+p_c+p_d+p_e
