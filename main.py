import random as r
import cv2
import numpy
from PIL import Image
import matplotlib.pyplot as plt

column = 32
def histogram(m, n):
    name = "archive/s" + str(m) + "/" + str(n) + ".pgm"
    image = cv2.imread(name)
    histo, bins = numpy.histogram(image.ravel(), column, [0, 256])
    return histo

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
    path = "archive/s" + str(m) + "/" + str(n) + ".pgm"
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
    path = "archive/s" + str(m) + "/" + str(n) + ".pgm"
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

refs1 = []
for i in range(0, 40):
    h = histogram(i+1, 1)
    refs1.append(h)
refs2 = []
h = []
for i in range(0, 40):
    h = points(i+1, 1)
    refs2.append(h)
refs3 = []
h = []
for i in range(0, 40):
    h = scscale(i+1, 1)
    refs3.append(h)
diff = []
true1 = 0
true2 = 0
true3 = 0
true4 = 0
t = 5
for i in range(t):
    pic_box = plt.figure(figsize=(10, 5))
    s = r.randint(1, 40)
    n = r.randint(1, 10)
    picture = cv2.imread("archive/s" + str(s) + "/" + str(n) + ".pgm")
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2, 5, 1)
    plt.imshow(picture)
    plt.axis('off')
    plt.text(-1, 125, 'Тест')
    test = histogram(s, n)
    diff.clear()
    for g in range(40):
        summ = comparison(test, refs1[g])
        diff.append(summ)
    p = min(diff)
    result1 = diff.index(p)+1
    if result1 == s:
        true1 += 1
    picture = cv2.imread("archive/s" + str(result1) + "/1.pgm")
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2, 5, 2)
    plt.imshow(picture)
    plt.axis('off')
    plt.text(-2, 125, 'Метод гистограмм')
    diff.clear()
    test = points(s, n)
    for g in range(0, 40):
        summ = comparison(test, refs2[g])
        diff.append(summ)
    p = min(diff)
    result2 = diff.index(p)+1
    if result2 == s:
        true2 += 1
    picture = cv2.imread("archive/s" + str(result2) + "/1.pgm")
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2, 5, 3)
    plt.imshow(picture)
    plt.axis('off')
    plt.text(-2, 125, 'Рандомные точки')
    diff.clear()
    test = scscale(s, n)
    for g in range(0, 40):
        summ = comparison(test, refs3[g])
        diff.append(summ)
    p = min(diff)
    result3 = diff.index(p)+1
    if result3 == s:
        true3 += 1
    picture = cv2.imread("archive/s" + str(result2) + "/1.pgm")
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2, 5, 4)
    plt.imshow(picture)
    plt.axis('off')
    plt.text(-2, 125, 'Сжатие')
    a = gol(result1, result2, result3)
    if a == s:
        true4 +=1
    picture = cv2.imread("archive/s" + str(result2) + "/1.pgm")
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2, 5, 5)
    plt.imshow(picture)
    plt.axis('off')
    plt.text(-2, 125, 'Голосование')
plt.show()


print("Точность метода гистограмм:", true1/t*100, "%")
print("Точность метода случайных точек:", true2/t*100, "%")
print("Точность Sc-scale:", true3/t*100, "%")
print("Точность метода голосования:", true4/t*100, "%")