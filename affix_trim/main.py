# 芙宁娜
'''
攻略
HP 6.3
CE 5.3
CHC 9.2
CHD 9
'''
# 产球 后台同色6 后台无色5
power = 6 * 1.8 + 5 * 1.2
# 词条数
affix_num = 30
# 初始词条
hp = 15307
ex_hp = 0.466 * hp + 0.466 * hp + 4780
atk = 244 + 510
ex_atk = 311
ce = 1 + 0.459
chc = 0.242 + 0.311 + 0.16
chd = 0.5

mxd = [0, 0, 0, 0, 0]
for A in range(affix_num * 10):
    for C in range(affix_num * 10 - A):
        D = affix_num * 10 - A - C
        a = A / 10
        c = C / 10
        d = D / 10
        nhp = hp + ex_hp + hp * 0.0583 * a
        natk = atk + ex_atk + atk * 0.0583 * 0
        nce = ce + 0.0648 * 0
        nchc = chc + 0.0389 * c
        nchd = chd + 0.0777 * d
        dmg = 0.1409 * nhp * (1 + nchc*nchd) * min(1.28, 1 + 0.007 * (nhp//1000))
        if dmg > mxd[0]:
            print(f'new max\ndmg:{dmg}\nhp:{a}({nhp})\nchc:{c}({nchc})\nchd:{d}({nchd})')
            mxd = [dmg, a, 0, c, d]
        #print(f'dmg:{dmg}\nhp:{0}({nhp})\nchc:{c}({nchc})\nchd:{d}({nchd})')
print(f'max:\ndmg{mxd[0]}\nhp:{mxd[1]}({hp + ex_hp + hp * 0.0583 * mxd[1]})\nchc:{mxd[3]}({chc + 0.0389*mxd[3]})\nchd:{mxd[4]}({chd + 0.0777 * mxd[4]})')