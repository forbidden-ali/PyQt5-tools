import random

foolstr = ['1','11','111','1111','11111','111111','1111111','11111111','6','66','666','6666','66666','666666','6666666','66666666','8','88','888','8888','88888','888888','8888888','88888888',
           '12','123','1234','12345','123456','1234567','123456789','987654321','87654321','7654321','654321','54321','4321','321','21',
           '012','234','345','456','567','678','789','890','098','987','876','765','654','543','432','210','147','258','369','963','852','741',
           '159','357','951','753','2684','2486','2468','8642','4862','4268','8624','8426','6248','6842','1793','1397','7931','7139','9317','9713','3179','3917','1357','13579',
           '96321','12369','98741','14789','78963','36987','74123','32147']

    
def namej(name):
    n2l = []
    lenn = len(name)
    for i in range(0, lenn, 1):
        n2l.append(name[i:i+1])
    return n2l

def mob(pho):
    mobl = []
    for i in range(0, 8, 1):
        mobl.append(pho[i:i+4])
    for i in range(0, 6, 1):
        mobl.append(pho[i:i+6])
    mobl.append(pho)
    return mobl

def qq(qqnum):
    qql = []
    qlen = len(qqnum)
    if qlen>3:
        for i in range(0, (qlen-3), 1):
            qql.append(qqnum[i:i+4])
    if qlen>5:
        for i in range(0, (qlen-5), 1):
            qql.append(qqnum[i:i+6])
    qql.append(qqnum)
    return qql
    
def secr(li, lev, seclen):
    li = li + foolstr
    e = []
    for i in range(0, lev, 1):
        while 1:
            d = random.choice(li)
            if len(d) == seclen:
                if d not in e:
                    e.append(d)
                    break
            elif len(d) < seclen:
                while 1:
                    f = random.choice(li)
                    if len(f) == (seclen-len(d)):
                        e.append(d+f)
                        break
                    elif len(f) < (seclen-len(d)):
                        while 1:
                            ff = random.choice(li)
                            if len(ff) == (seclen-len(d)-len(f)):
                                e.append(d+f+ff)
                                break
                            elif len(ff) < (seclen-len(d)-len(f)):
                                while 1:
                                    fff = random.choice(li)
                                    if len(fff) == (seclen-len(d)-len(f)-len(ff)):
                                        e.append(d+f+fff)
                                        break
                                    elif len(fff) < (seclen-len(d)-len(f)-len(ff)):
                                        while 1:
                                            ffff = random.choice(li)
                                            if len(ffff) == (seclen-len(d)-len(f)-len(ff)-len(fff)):
                                                e.append(d+f+ff+fff+ffff)
                                                break
                                            else:
                                                continue
                                        break
                                    else:
                                        continue
                                break
                            else:
                                continue
                        break
                    else:
                        continue
                break
            else:
                continue
    return e
