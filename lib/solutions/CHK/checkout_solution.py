

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    global p_gr
    c_A=skus.count('A')
    c_B=skus.count('B')
    c_C=skus.count('C')
    c_D=skus.count('D')
    c_E=skus.count('E')
    c_F=skus.count('F')
    total_c=len(skus)

    c_G=skus.count('G')
    c_H=skus.count('H')
    c_I=skus.count('I')
    c_J=skus.count('J')
    c_K=skus.count('K')
    c_L=skus.count('L')
    c_M=skus.count('M')
    c_N=skus.count('N')
    c_O=skus.count('O')
    c_P=skus.count('P')
    c_Q=skus.count('Q')
    c_R=skus.count('R')
    c_S=skus.count('S')
    c_T=skus.count('T')
    c_U=skus.count('U')
    c_V=skus.count('V')
    c_W=skus.count('W')
    c_X=skus.count('X')
    c_Y=skus.count('Y')
    c_Z=skus.count('Z')
    c_gr=c_S+c_T+c_X+c_Z
    c_mp=c_S+c_T+c_Y


    After_offer_c_B=c_B-int(c_E/2)
    if After_offer_c_B<=0:
        After_offer_c_B=0

    After_offer_c_M = c_M - int(c_N / 3)
    if After_offer_c_M <= 0:
        After_offer_c_M = 0

    After_offer_c_Q = c_Q - int(c_R / 3)
    if After_offer_c_Q <= 0:
        After_offer_c_Q = 0

    if c_gr<3:
        p_gr=c_S*20+c_T*20+c_X*17+c_Y*20+c_Z*21
    elif c_gr%3==0:
        p_gr=int(c_gr/3)*45
    elif c_gr%3==1:
        if c_X>0:
            p_gr=int(c_gr/3)*45+17
        elif c_X==0&c_mp>0:
            p_gr = int(c_gr / 3) * 45+20
        else:
            p_gr=int(c_gr / 3) * 45+21
    elif c_gr%3==2:
        if c_X>1:
            p_gr=int(c_gr/3)*45+34
        elif c_X==1:
            if c_mp>0:
                p_gr = int(c_gr / 3) * 45 + 37
            else:
                p_gr = int(c_gr / 3) * 45 +38
        elif c_X==0:
            if c_mp>1:
                p_gr = int(c_gr / 3) * 45+40
            elif c_mp==1:
                p_gr=int(c_gr / 3) * 45+41
            else:
                p_gr=int(c_gr / 3) * 45+42







    p_a=int(c_A/5)*200+int((c_A%5)/3)*130+((c_A%5)%3)*50
    p_b=int(After_offer_c_B/2)*45+(After_offer_c_B%2)*30
    p_c=c_C*20
    p_d=c_D*15
    p_e=c_E*40
    p_f=int(c_F/3)*20+(c_F%3)*10
    p_g=c_G*20
    p_h=int(c_H/10)*80+int((c_H%10)/5)*45+((c_H%10)%5)*10
    p_i=c_I*35
    p_j=c_J*60
    p_k=int(c_K/2)*120+(c_K%2)*70
    p_l=c_L*90
    p_m=After_offer_c_M*15
    p_n=c_N*40
    p_o=c_O*10
    p_p=int(c_P/5)*200+(c_P%5)*50
    p_q=int(After_offer_c_Q/3)*80+(After_offer_c_Q%3)*30
    p_r=c_R*50
    #p_s=c_S*30
    #p_t=c_T*20
    p_u=int(c_U/4)*120+(c_U%4)*40
    p_v=int(c_V/3)*130+int((c_V%3)/2)*90+((c_V%3)%2)*50
    p_w=c_W*20
    #p_x=c_X*90
    #p_y=c_Y*10
    #p_z=c_Z*50


    if c_A+c_B+c_C+c_D+c_E+c_F+c_G+c_H+c_I+c_J+c_K+c_L+c_M+c_N+c_O+c_P+c_Q+c_R+c_S+c_T+c_U+c_V+c_W+c_X+c_Y+c_Z!=total_c:
        return -1
    else:
        return p_a+p_b+p_c+p_d+p_e+p_f+p_g+p_h+p_i+p_j+p_k+p_l+p_m+p_n+p_o+p_p+p_q+p_r+p_u+p_v+p_w+p_gr
