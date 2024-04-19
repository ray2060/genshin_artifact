di = {
	'暴击率':[2.72, 3.11, 3.50, 3.89],
	'暴击伤害':[5.44, 6.22, 6.99, 7.77],
	'攻击力百分比':[4.08, 4.66, 5.25, 5.83],
	'攻击力数值':[13.62, 15.56, 17.51, 19.45],
	'元素精通':[16.32, 18.65, 20.98, 23.31],
	'元素充能效率':[4.53, 5.18, 5.83, 6.48],
	'防御力百分比':[5.10, 5.83, 6.56, 7.29],
	'防御力数值':[16.2, 18.52, 20.83, 23.15],
	'生命值百分比':[4.08, 4.66, 5.25, 5.83],
	'生命值数值':[209.13, 239.0, 268.88, 298.75]
}
res = []
rres = []
def get(tar, now, dep):
	if not round(now, 1) in rres:
		res.append(round(now, 2))
		rres.append(round(now, 1))
	if dep >= 6:
		return
	get(tar, now + di[tar][0], dep + 1)
	get(tar, now + di[tar][1], dep + 1)
	get(tar, now + di[tar][2], dep + 1)
	get(tar, now + di[tar][3], dep + 1)
	
for target in di.keys():
	res = []
	rres = []
	get(target, 0.0, 0)
	res = sorted(res)
	print(f'{target}', end = ' ')
	print(("\n" + f"{target} ").join([str(round(x,1) if target in \
		['暴击率', '暴击伤害', '攻击力百分比', '元素充能效率', '防御力百分比', '生命值百分比']\
		else int(round(x,0)))+" "+str(round(x,2)) for x in res]))
	print('---')