
import random
import serial
import cv2
from cv2.cv2 import *
import numpy as np
import serial
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import time

app = QtWidgets.QApplication([])
ui = uic.loadUi(r'C:\Users\79687\Desktop\Projekt\design.ui')
serial = QSerialPort()
serial.setBaudRate(9600)
portList = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comL.addItems(portList)

def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    print(rxs)
def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)

def onClose():
    serial.close()

serial.readyRead.connect(onRead)
ui.openB.clicked.connect(onOpen)
ui.closeB.clicked.connect(onClose)
ui.show()
ui.exec()





doska=[
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
#print(doska)
xa = []
b = []
c = []
d = []

mark = cv2.imread(r'C:\Users\79687\Desktop\mark.jpg', cv2.IMREAD_UNCHANGED)
mark2 = cv2.imread(r'C:\Users\79687\Desktop\mark2.jpg', cv2.IMREAD_UNCHANGED)
mark3 = cv2.imread(r'C:\Users\79687\Desktop\mark3.jpg', cv2.IMREAD_UNCHANGED)
#foto = cv2.imread(r'C:\Users\79687\Desktop\foto.jpg', cv2.IMREAD_UNCHANGED)
#foto1 = cv2.imread(r'C:\Users\79687\Desktop\foto.jpg', cv2.IMREAD_UNCHANGED)
#result = cv2.matchTemplate(foto, mark, cv2.TM_CCOEFF_NORMED)

t = 2
while t>0:


    doska = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    cam = VideoCapture(1)
    s, img = cam.read()
    # cv2.imshow('Result', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    result = cv2.matchTemplate(img, mark, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(img, mark2, cv2.TM_CCOEFF_NORMED)
    result3 = cv2.matchTemplate(img, mark3, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = .64
    yloc, xloc = np.where(result >= 0.70)
    yloc2, xloc2 = np.where(result2 >= 0.65)
    yloc3, xloc3 = np.where(result3 >= 0.62)
    w = mark.shape[0]
    h = mark.shape[1]

    rectangles = []
    rectangles2 = []
    rectangles3 = []

    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    for (x, y) in zip(xloc2, yloc2):
        rectangles2.append([int(x), int(y), int(w), int(h)])
        rectangles2.append([int(x), int(y), int(w), int(h)])

    for (x, y) in zip(xloc3, yloc3):
        rectangles3.append([int(x), int(y), int(w), int(h)])
        rectangles3.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    # print(len(rectangles))
    rectangles2, weights = cv2.groupRectangles(rectangles2, 1, 0.2)
    # print(len(rectangles2))
    rectangles3, weights = cv2.groupRectangles(rectangles3, 1, 0.2)

    for (x, y, w, h) in rectangles:
        #print(x, y)
        xa.append(int(x))
        b.append(int(y))

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    for (x, y, w, h) in rectangles2:
        #print('b', x, y)

        rasp1 = (int(x) - int((xa[0]))) / 48.625
        rasp1 = int(rasp1)
        rasp2 = (y - int((b[0]))) / 48.625
        rasp2 = int(rasp2)
        doska[rasp1][7 - rasp2] = 1

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for (x, y, w, h) in rectangles3:
        #print('ch', x, y)

        rasp3 = (int(x) - int((xa[0]))) / 48.625
        rasp3 = int(rasp3)
        rasp4 = (y - int((b[0]))) / 48.625
        rasp4 = int(rasp4)
        doska[rasp3][7 - rasp4] = 2

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)









    # rasp1 = (int(c[0]) - int((a[0])))/ ((int((a[1])) - int((a[0]))) / 8)
    # rasp1 = 9 - int(rasp1 + 0.5)-1
    # rasp2 = (int(d[0]) - int((b[0])))/ (((int((b[2])) - int((b[0]))) / 8))
    # rasp2 = int(rasp2 + 1)-1
    # doska[rasp1][rasp2]=1

    # serial.setPortName('COM3')
    # serial.open(QIODevice.ReadWrite)
    # pusk = '333'
    # serial.write(pusk.encode())
    for i in range(0, 8):
        hod = 1
        for j in range(0, 8):
            if i - 2 >= 0 and j + 2 <= 7 and doska[i][j] == 2 and doska[i - 1][j + 1] == 1 and doska[i - 2][j + 2] == 0:
                action1 = 'k'+str(7-i)+str(j)+str(7-(i-2))+str(j+2)+str(7-(i-1))+str(j+1)
                hod = 0
                break
            elif i - 2 >= 0 and j - 2 >= 0 and doska[i][j] == 2 and doska[i - 1][j - 1] == 1 and doska[i - 2][
                j - 2] == 0 :
                action1 = 'k'+str(7-i)+str(j)+str(7-(i-2))+str(j-2)+str(7-(i-1))+str(j-1)
                hod = 0
                break
        if hod == 0:
            break

    if hod == 1:

        for i in range(0, 8):
            rand = random.randrange(1, 3, 1)
            hod = 1
            if rand == 2:
                for j in range(0, 8):
                    if i - 1 >= 0 and j + 1 <= 7 and doska[i][j] == 2 and doska[i - 1][j + 1] == 0:
                        action1='m'+str(7-i)+str(j)+str(7-(i-1))+str(j+1)
                        hod = 0
                        break
                    elif doska[i][j] == 2 and doska[i - 1][j - 1] == 0 and i - 1 >= 0 and j - 1 >= 0:
                        action1='m'+str(7-i)+str(j)+str(7-(i-1))+str(j-1)
                        hod = 0
                        break
            else:
                for j in range(0, 8):

                    if doska[i][j] == 2 and doska[i - 1][j - 1] == 0 and i - 1 >= 0 and j - 1 >= 0:
                        action1='m'+str(7-i)+str(j)+str(7-(i-1))+str(j-1)
                        hod = 0
                        break
                    elif i - 1 >= 0 and j + 1 <= 7 and doska[i][j] == 2 and doska[i - 1][j + 1] == 0:
                        action1='m'+str(7-i)+str(j)+str(7-(i-1))+str(j+1)
                        hod = 0
                        break
            if hod == 0:
                break

    #for i in range(0, 8):
    #    print(doska[i][0], doska[i][1], doska[i][2], doska[i][3], doska[i][4], doska[i][5], doska[i][6], doska[i][7])
    #print(action1)
    action=list(action1)
    if action[2] == '7':
        action[2]='h'
    if action[2] == '6':
        action[2]='g'
    if action[2] == '5':
        action[2]='f'
    if action[2] == '4':
        action[2]='e'
    if action[2] == '3':
        action[2]='d'
    if action[2] == '2':
        action[2]='c'
    if action[2] == '1':
        action[2]='b'
    if action[2] == '0':
        action[2]='a'

    if action[4] == '7':
        action[4]='h'
    if action[4] == '6':
        action[4]='g'
    if action[4] == '5':
        action[4]='f'
    if action[4] == '4':
        action[4]='e'
    if action[4] == '3':
        action[4]='d'
    if action[4] == '2':
        action[4]='c'
    if action[4] == '1':
        action[4]='b'
    if action[4] == '0':
        action[4]='a'
    if action[0] == 'k':
        if action[6] == '7':
            action[6] = 'h'
        if action[6] == '6':
            action[6] = 'g'
        if action[6] == '5':
            action[6] = 'f'
        if action[6] == '4':
            action[6] = 'e'
        if action[6] == '3':
            action[6] = 'd'
        if action[6] == '2':
            action[6] = 'c'
        if action[6] == '1':
            action[6] = 'b'
        if action[6] == '0':
            action[6] = 'a'

    action1=''.join(action)


    action1 = action1.replace('0h', '01', 1)
    action1 = action1.replace('2h', '02', 1)
    action1 = action1.replace('4h', '03', 1)
    action1 = action1.replace('6h', '04', 1)

    action1 = action1.replace('1g', '05', 1)
    action1 = action1.replace('3g', '06', 1)
    action1 = action1.replace('5g', '07', 1)
    action1 = action1.replace('7g', '08', 1)

    action1 = action1.replace('0f', '09', 1)
    action1 = action1.replace('2f', '10', 1)
    action1 = action1.replace('4f', '11', 1)
    action1 = action1.replace('6f', '12', 1)

    action1 = action1.replace('1e', '13', 1)
    action1 = action1.replace('3e', '14', 1)
    action1 = action1.replace('5e', '15', 1)
    action1 = action1.replace('7e', '16', 1)

    action1 = action1.replace('0d', '17', 1)
    action1 = action1.replace('2d', '18', 1)
    action1 = action1.replace('4d', '19', 1)
    action1 = action1.replace('6d', '20', 1)

    action1 = action1.replace('1c', '21', 1)
    action1 = action1.replace('3c', '22', 1)
    action1 = action1.replace('5c', '23', 1)
    action1 = action1.replace('7c', '24', 1)

    action1 = action1.replace('0b', '25', 1)
    action1 = action1.replace('2b', '26', 1)
    action1 = action1.replace('4b', '27', 1)
    action1 = action1.replace('6b', '28', 1)

    action1 = action1.replace('1a', '29', 1)
    action1 = action1.replace('3a', '30', 1)
    action1 = action1.replace('5a', '31', 1)
    action1 = action1.replace('7a', '32', 1)

    a = ''
    if action1[0] == 'm':
        a += '112,'
        a += str(int(action1[1:3])) + ','
        a += '99,'
        a += '111,'
        a += str(int(action1[3:5])) + ','
        a += '112,'
        a += '333'

    if action1[0] == 'k':
        a += '112,'
        a += str(int(action1[1:3])) + ','
        a += '99,'
        a += '111,'
        a += str(int(action1[3:5])) + ','
        a += '112,'
        a += str(int(action1[5:7])) + ','
        a += '99,'
        a += '111,'
        a += '222,'
        a += '112,'
        a += '333'

    serial.write(a.encode())

    #print(action1)
    namedWindow('Result')
    imshow('Result', img)
    waitKey(0)
    destroyWindow('Result')



'''
connected = False
ser = serial.Serial("COM3", 9600)
while not connected:
    serin = ser.read()
    connected = True
ser.write(b'\x010333') #меняем последнии 3 цифры
ser.close()
'''







