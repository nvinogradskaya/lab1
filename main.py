import random as r
import cv2
import numpy
import tkinter
from tkinter import *
import time
from PIL import Image, ImageTk


column = 32
def histogram(m, n):
    name = "faces/s" + str(m) + "/" + str(n) + ".pgm"
    image = cv2.imread(name)
    histo, bins = numpy.histogram(image.ravel(), 32, [0, 256])
    return histo
b1 =[]
s1 = []
s0 = []
s2 = []
count = 1000
for i in range(count):
    x = r.randint(0, 91)
    y = r.randint(0, 111)
    s2 = [x, y]
    s1.append(s2)
def points(m,n):
    ss = []
    path = "faces/s" + str(m) + "/" + str(n) + ".pgm"
    img = Image.open(path)
    pix = img.load()
    for i in range(count):
        x = s1[i][0]
        y = s1[i][1]
        val = pix[x, y]
        ss.append(val)
    return ss
def scscale(m, n):
    ss = []
    summ = 0
    path = "faces/s" + str(m) + "/" + str(n) + ".pgm"
    img = Image.open(path)
    pix = img.load()
    kv = 10
    for x in range(0, 92 - 92 // kv, kv):
        for y in range(0, 112 - 112 // kv, kv):
            s = 0
            w = x
            u = y
            while w < x + kv and u < y + kv:
                s += pix[w, u]
                w += 1
                u += 1
            ss.append(s / kv)
    return ss
def comparison(h1, h2):
    summ = 0
    for j in range(len(h2)):
        summ += ((h1[j]-h2[j])**2) ** (1/2)
    return summ
def gol(a1, a2, a3):
    if a1 == a2 or a1 == a3:
        a = a1
    else:
        a = a2
    return a

et = 3

def showimage(mylbl,path): #Функция отображения Lebel изображения в интерфейсе
    img = Image.open(path) # Открывваем изображение с помощью библиотеки PIL
    img = ImageTk.PhotoImage(img)
    mylbl.config(image=img) # Присваиваем Лейбел наше изображение
    mylbl.image = img
    mylbl.pack(side=LEFT) # Отрисовываем лейбел с параметром лево,чтобы изображения были в строчку
def showtext(mylbl):
    mylbl.pack(side=LEFT) #Отрисовываем лейбел текст
def stop():
    time.sleep(15)
def printing(i):
    global a
    k, g = map(int, a[i][0].split())
    showimage(label1, f"faces/s{k}/{g}.pgm")
    showimage(label2, f"faces/s{k}/1.pgm")
    showimage(label3, f"faces/s{a[i][1]}/1.pgm")
    showimage(label4, f"faces/s{a[i][2]}/1.pgm")
    showimage(label5, f"faces/s{a[i][3]}/1.pgm")
    showimage(label6, f"faces/s{a[i][4]}/1.pgm")
    showimage(label7, f"gr/{i}.png")
    showtext(l1txt)
    showtext(l2txt)
    showtext(l3txt)
    showtext(l4txt)
    showtext(l5txt)
    showtext(l6txt)
    showtext(l7txt)
    showimage(label11, f"gist/{k}.{g}.png")
    showimage(label12, f"rand_points/{k}.{g}.pgm")
    showimage(label13, f"mash/{k}.{g}.pgm")
    showtext(l1txt1)
    showtext(l2txt1)
    showtext(l3txt1)
    if i<len(a)-1:
        root.after(1000, printing, i+1)

refs1 = []
refs2 = []
refs3 = []
for i in range(1, et+1):
    for j in range(1, 41):
        h = histogram(j, i)
        refs1.append(h)
        h = points(j, i)
        refs2.append(h)
        h = scscale(j, i)
        refs3.append(h)
diff = []
true1 = 0
true2 = 0
true3 = 0
true4 = 0
t = 400
answers = []
for i in range(t):
    answer = []
    s = r.randint(1, 40)
    n = r.randint(2, 10)
    answer.append(str(s) + " " + str(n))
    test = histogram(s, n)
    diff.clear()
    for g in range(40*et):
        summ = comparison(test, refs1[g])
        diff.append(summ)
    p = min(diff)
    result1 = diff.index(p)+1
    while (result1 > 40):
        result1 = result1 - 40
    if result1 == s:
        true1 += 1
    answer.append(result1)
    diff.clear()
    test = points(s, n)
    for g in range(0, 40*et):
        summ = comparison(test, refs2[g])
        diff.append(summ)
    p = min(diff)
    result2 = diff.index(p)+1
    while (result2 > 40):
        result2 = result2 - 40
    if result2 == s:
        true2 += 1
    answer.append(result2)
    diff.clear()
    test = scscale(s, n)
    for g in range(0, 40*et):
        summ = comparison(test, refs3[g])
        diff.append(summ)
    p = min(diff)
    result3 = diff.index(p)+1
    while result3 > 40:
        result3 = result3 - 40
    if result3 == s:
        true3 += 1
    answer.append(result3)
    b = gol(result1, result2, result3)
    answer.append(b)
    if b == s:
        true4 +=1
    answers.append(answer)
print("Точность метода гистограмм:", true1/t*100, "%")
print("Точность метода случайных точек:", true2/t*100, "%")
print("Точность Sc-scale:", true3/t*100, "%")
print("Точность метода голосования:", true4/t*100, "%")

a = answers
root = Tk()
root.title("Faces")
root.geometry("2000x800")
frm = Frame(root)
frm.pack(side=BOTTOM, padx=25, pady=15)
f_top = Frame(root)
f_bot = Frame(root)
label0 = Label(f_top)
label1 = Label(f_top)
label2 = Label(f_top)
label3 = Label(f_top)
label4 = Label(f_top)
label5 = Label(f_top)
label6 = Label(f_top)
label7 = Label(f_top)
l1txt = Label(f_bot, width=14, text="Тестовое")
l2txt = Label(f_bot, width=12, text="Эталон")
l3txt = Label(f_bot, width=12, text="МГ")
l4txt = Label(f_bot, width=15, text="МСТ")
l5txt = Label(f_bot, width=10, text="Sc-scale")
l6txt = Label(f_bot, width=20, text="Голосование")
l7txt = Label(f_bot, width=69, text="График точности")

f_top.pack()
f_bot.pack()
f1_top = Frame(root)
f1_bot = Frame(root)
label11 = Label(f1_top)
label12 = Label(f1_top)
label13 = Label(f1_top)
l1txt1 = Label(f1_bot, width=50, text="МГ (кр-тест, зел-эталон, с-выбранная, если выбран не эталон)")
l2txt1 = Label(f1_bot, width=18, text="МСТ")
l3txt1 = Label(f1_bot, width=15, text="Sc-scale")

f1_top.pack()
f1_bot.pack()
btn1 = Button(frm, text="Stop", command=lambda: stop())
btn1.pack(side=tkinter.LEFT, padx=40)

root.after_idle(printing, 0) # start loop
root.after(60*100000, root.destroy)
root.mainloop()
