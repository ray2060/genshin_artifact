'''
CHC  暴击率
CHD  暴击伤害
ED   元素伤害
CE   元素充能效率
ATKP 攻击力百分比
ATKV 攻击力数值
EM   元素精通
HP   生命值百分比
HN   生命值数值
DEFP 防御力百分比
DEFV 防御力数值
'''

from tkinter import *
from tkinter.ttk import *
from time import strftime, localtime

DEBUG = False

ATTR_DICT = {
	'暴击率':'CHC',
	'暴击伤害':'CHD',
	'元素充能效率':'CE',
	'攻击力百分比':'ATKP',
	'攻击力数值':'ATKV',
	'元素精通':'EM',
	'生命值百分比':'HP',
	'生命值数值':'HN',
	'防御力百分比':'DEFP',
	'防御力数值':'DEFV',
	'':'NONE'
}

ATTR_TUP = (
	'暴击率',
	'暴击伤害',
	'元素伤害',
	'元素充能效率',
	'攻击力百分比',
	'攻击力数值',
	'元素精通',
	'生命值百分比',
	'生命值数值',
	'防御力百分比',
	'防御力数值',
	''
)

window = Tk()
window.title('圣遗物评分计算器 v1.0')
window.geometry('800x450')
window.configure(background='#b0bec5')

frame_settings = Frame(window)
frame_settings.pack(pady=20)

frame_attrqs = Frame(window)
frame_attrqs.pack(pady=20)

frame_input = Frame(window)
frame_input.pack(pady=20)

frame_calc = Frame(window)
frame_calc.pack(pady=20)

label_CHC = Label(frame_settings, text='暴击率')
label_CHD = Label(frame_settings, text='暴击伤害')
label_CE = Label(frame_settings, text='元素充能效率')
label_ATKP = Label(frame_settings, text='攻击力百分比')
label_ATKV = Label(frame_settings, text='攻击力数值')
label_EM = Label(frame_settings, text='元素精通')
label_HP = Label(frame_settings, text='生命值百分比')
label_HN = Label(frame_settings, text='生命值数值')
label_DEFP = Label(frame_settings, text='防御力百分比')
label_DEFV = Label(frame_settings, text='防御力数值')

label_CHC.grid(column=0, row=0)
label_CHD.grid(column=1, row=0)
label_CE.grid(column=2, row=0)
label_ATKP.grid(column=3, row=0)
label_ATKV.grid(column=4, row=0)
label_EM.grid(column=5, row=0)
label_HP.grid(column=6, row=0)
label_HN.grid(column=7, row=0)
label_DEFP.grid(column=8, row=0)
label_DEFV.grid(column=9, row=0)

var_CHC = DoubleVar()
var_CHD = DoubleVar()
var_CE = DoubleVar()
var_ATKP = DoubleVar()
var_ATKV = DoubleVar()
var_EM = DoubleVar()
var_HP = DoubleVar()
var_HN = DoubleVar()
var_DEFP = DoubleVar()
var_DEFV = DoubleVar()

spin_CHC = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_CHC)
spin_CHD = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_CHD)
spin_CE = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_CE)
spin_ATKP = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_ATKP)
spin_ATKV = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_ATKV)
spin_EM = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_EM)
spin_HP = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_HP)
spin_HN = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_HN)
spin_DEFP = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_DEFP)
spin_DEFV = Spinbox(frame_settings, values=(0, 0.5, 1), width=3, wrap=True, textvariable=var_DEFV)

var_CHC.set(1)
var_CHD.set(1)
var_CE.set(1)
var_ATKP.set(1)
var_ATKV.set(1)
var_EM.set(0)
var_HP.set(0)
var_HN.set(0)
var_DEFP.set(0)
var_DEFV.set(0)

spin_CHC.grid(column=0, row=1)
spin_CHD.grid(column=1, row=1)
spin_CE.grid(column=2, row=1)
spin_ATKP.grid(column=3, row=1)
spin_ATKV.grid(column=4, row=1)
spin_EM.grid(column=5, row=1)
spin_HP.grid(column=6, row=1)
spin_HN.grid(column=7, row=1)
spin_DEFP.grid(column=8, row=1)
spin_DEFV.grid(column=9, row=1)

ATTRQS = (
	'01.充精 辅助枫原万叶 辅助砂糖（暂不支持）',
	'02.折攻充精双暴 点香菱（暂不支持）',
	'03.折攻生充 珊瑚宫心海（暂不支持）',
	'04.折攻生精双暴 胡桃（暂不支持）',
	'05.折攻防充双暴 荒泷一斗（暂不支持）',
	'06.攻充 辅助琴 申鹤（暂不支持）',
	'07.攻充双暴 琴 输出班尼特 副C甘雨 雷电将军 北斗',
	'08.攻充折精双暴 行秋（暂不支持）',
	'09.攻充暴击 西风申鹤（暂不支持）',
	'10.攻充精双暴 温迪 枫原万叶 砂糖 香菱',
	'11.攻双暴 宵宫 甘雨（暂不支持）',
	'12.攻精双暴 蒸发宵宫 融化甘雨（暂不支持）',
	'13.攻折充双暴 神里绫华（暂不支持）',
	'14.攻折精双暴 达达利亚（暂不支持）',
	'15.攻生折充双暴 钟离（暂不支持）',
	'16.生充 班尼特（暂不支持）',
	'17.防双暴 阿贝多（暂不支持）'
)

def attrqs():
	try:
		if combobox_attrqs.get()[:2] == '07':
			var_CHC.set(1)
			var_CHD.set(1)
			var_CE.set(1)
			var_ATKP.set(1)
			var_ATKV.set(1)
			var_EM.set(0)
			var_HP.set(0)
			var_HN.set(0)
			var_DEFP.set(0)
			var_DEFV.set(0)
		elif combobox_attrqs.get()[:2] == '10':
			var_CHC.set(1)
			var_CHD.set(1)
			var_CE.set(1)
			var_ATKP.set(1)
			var_ATKV.set(1)
			var_EM.set(1)
			var_HP.set(0)
			var_HN.set(0)
			var_DEFP.set(0)
			var_DEFV.set(0)
		elif int(combobox_attrqs.get()[:2]) in range(1, 18):
			raise RuntimeError('Not currently supported')
		else:
			raise RuntimeError('Invalid input')
	except RuntimeError as e:
		txt_attrqs_err.configure(state='normal')
		txt_attrqs_err.delete('1.0', '2.0')
		txt_attrqs_err.insert('end', f'{strftime("%H:%M:%S", localtime())}: {e}\n')
		txt_attrqs_err.configure(state='disabled')
		if DEBUG:
			print(type(e), e)
	except Exception as e:
		txt_attrqs_err.configure(state='normal')
		txt_attrqs_err.delete('1.0', '2.0')
		txt_attrqs_err.insert('end', f'{strftime("%H:%M:%S", localtime())}: Error\n')
		txt_attrqs_err.configure(state='disabled')
		if DEBUG:
			print(type(e), e)
	else:
		txt_attrqs_err.configure(state='normal')
		txt_attrqs_err.delete('1.0', '2.0')
		txt_attrqs_err.insert('end', f'{strftime("%H:%M:%S", localtime())}: Success\n')
		txt_attrqs_err.configure(state='disabled')

var_attrqs = StringVar()

label_attrqs = Label(frame_attrqs, text='快速设置有效词条')

label_attrqs.grid(column=0, row=0)

var_attrqs.set('07.攻充双暴 琴 输出班尼特 副C甘雨 雷电将军 北斗')

combobox_attrqs = Combobox(frame_attrqs, textvariable=var_attrqs, width=40, value=ATTRQS)

combobox_attrqs.grid(column=0, row=1)

btn_attrqs = Button(frame_attrqs, text='应用', command=attrqs)

btn_attrqs.grid(column=0, row=2)

txt_attrqs_err = Text(frame_attrqs, height=1, width=35)
txt_attrqs_err.insert('0.0', '--:--:--: ---')
txt_attrqs_err.configure(state='disabled')

txt_attrqs_err.grid(column=0, row=3)

label_input = Label(frame_input, text='输入副词条')

label_input.grid(column=0, row=0)

var_attr1 = StringVar()
var_attr2 = StringVar()
var_attr3 = StringVar()
var_attr4 = StringVar()

combobox_attr1 = Combobox(frame_input, textvariable=var_attr1, width=10, value=ATTR_TUP)
combobox_attr2 = Combobox(frame_input, textvariable=var_attr2, width=10, value=ATTR_TUP)
combobox_attr3 = Combobox(frame_input, textvariable=var_attr3, width=10, value=ATTR_TUP)
combobox_attr4 = Combobox(frame_input, textvariable=var_attr4, width=10, value=ATTR_TUP)

var_attr1.set('暴击率')
var_attr2.set('暴击伤害')
var_attr3.set('攻击力百分比')
var_attr4.set('元素充能效率')

combobox_attr1.grid(column=0, row=1)
combobox_attr2.grid(column=1, row=1)
combobox_attr3.grid(column=2, row=1)
combobox_attr4.grid(column=3, row=1)

txt_attr1 = Entry(frame_input, width=10)
txt_attr2 = Entry(frame_input, width=10)
txt_attr3 = Entry(frame_input, width=10)
txt_attr4 = Entry(frame_input, width=10)

txt_attr1.grid(column=0, row=2)
txt_attr2.grid(column=1, row=2)
txt_attr3.grid(column=2, row=2)
txt_attr4.grid(column=3, row=2)

txt_attr1.insert(0, '11.7')
txt_attr2.insert(0, '23.4')
txt_attr3.insert(0, '10.0')
txt_attr4.insert(0, '6.5')

def calc():
	try:
		ans = 0.0
		a_ls = [ATTR_DICT[i] for i in [var_attr1.get(), var_attr2.get(), var_attr3.get(), var_attr4.get()]]
		b_ls = [float(i) for i in [txt_attr1.get(), txt_attr2.get(), txt_attr3.get(), txt_attr4.get()]]
		for i in range(4):
			if a_ls[i] == 'CHC':
				ans += b_ls[i] / 1.0 * float(spin_CHC.get())
			elif a_ls[i] == 'CHD':
				ans += b_ls[i] / 2.0 * float(spin_CHD.get())
			elif a_ls[i] == 'CE':
				ans += b_ls[i] / 1.67 * float(spin_CE.get())
			elif a_ls[i] == 'ATKP':
				ans += b_ls[i] / 1.5 * float(spin_ATKP.get())
			elif a_ls[i] == 'ATKV':
				ans += b_ls[i] / 10.0 * float(spin_ATKV.get())
			elif a_ls[i] == 'EM':
				ans += b_ls[i] / 6.0 * float(spin_EM.get())
			elif a_ls[i] == 'HP':
				ans += b_ls[i] / 1.5 * float(spin_HP.get())
			elif a_ls[i] == 'HN':
				ans += b_ls[i] / 154.0 * float(spin_HN.get())
			elif a_ls[i] == 'DEFP':
				ans += b_ls[i] / 1.87 * float(spin_DEFP.get())
			elif a_ls[i] == 'DEFV':
				ans += b_ls[i] / 6.0 * float(spin_DEFV.get())
			elif a_ls[i] == 'NONE':
				ans += 0.0
			else:
				raise RuntimeError('Invalid input')
		label_ret.configure(text=f'圣遗物评分：{round(ans, 2)} ')
	except RuntimeError as e:
		label_ret.configure(text=f'Error: {e}')
		if DEBUG:
			print(type(e), e)
	except Exception as e:
		label_ret.configure(text=f'Error')
		if DEBUG:
			print(type(e), e)

btn_calc = Button(frame_calc, text='计算', command=calc)
btn_calc.grid(column=0, row=0)

label_ret = Label(frame_calc)
label_ret.grid(column=0, row=1)

window.mainloop()