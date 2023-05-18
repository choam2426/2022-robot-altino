from AltinoLite import *
# 1 좌전방 2 전방 3 우전방 센서 4 오른쪽, 센서 5 왼쪽 6 후방
# 조향 좌 음수 우 양수
def l_f(spd=350): # 좌회전 전진
    steering(-127)
    go(spd,spd)

def r_f(spd=350): # 우회전 전진
    steering(127)
    go(spd,spd)

def r_b(spd=400): # 우회전 후진
    steering(127)
    go(-spd,-spd)

def l_b(spd=400): # 좌회전 후진
    steering(-127)
    go(-spd,-spd)

def tempo(s): #s에 센서값 저장
    for i in range(1,7):
        s[i]=sensor.IR[i]
    return s

def led_print(S, time): #문자 출력
    display(S)
    delay(time)
    display(0)

def dot_print(x,y,time): #점 출력
    for i in range(len(x)):
        displayon(x[i],y[i])
    delay(time)
    display(0)

def line_print(S,time): # 라인 출력
    displayline(S[0],S[1],S[2],S[3],S[4],S[5],S[6],S[7])


def led_light(S, time): #라이트 켜기 함수 + 끄기는 dirve에서 따로 해야댐
    led(S)
    delay(time)

def sing(um, time): #소리 내기
    sound(um)
    delay(time)
    sound(0)


def Drive(spd,dit,h_t):
    s=[0x38,0x7c,0xfb,0xfe,0xfe,0xfb,0x7c,0x38,0,0,0,0,0,0,0,0]
    flags=0 #터널 통과 횟수 측정용
    while True:
        if sensor.IR[4]>200 and sensor.IR[5]>200:
            break
    while True:
        temp=[0,0,0,0,0,0,0]
        i=0
        if sensor.CDS<15 and flags==0: #첫번째 터널 도착
            stop()
            for i in range(3):
                sing(37, 100)
                sing(41, 100)
            flags+=1
        elif sensor.CDS>30 and flags==1: #첫번째 터널 통과
            flags+=1
        elif sensor.CDS<30 and flags==2: #두번째 터널 도착
            stop()
            led_light(1,500)
            led_light(8,500)
            led_light(4,500)
            led_light(2,500)
            led(0)
            flags+=1
        elif sensor.CDS>30 and flags==3: #두번째 터널 통과
            flags+=1
        elif sensor.CDS<30 and flags==4:
            stop()
            led_print("D",500)
            led_print("A",500)  
            led_print("E",500)
            led_print("J",500)
            led_print("E",500)
            led_print("O",500)
            led_print("N",500)
            display(0)
            flags+=1
        elif sensor.CDS>30 and flags==5: #두번째 터널 통과
            flags+=1
        elif flags==6:
            displayline(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7])
            imsi=s[0]
            s.append(imsi)
            del s[0]
            if sensor.CDS<30 and flags==6:
                flags+=1
                display(0)
            delay(100)
        elif sensor.CDS>30 and flags==7:
            flags+=1

        elif flags==8 and sensor.IR[1]>dit and sensor.IR[2]>dit and sensor.IR[3]>dit:
            stop()
            sing(42,200)
            sing(44,200)
            sing(46,400)
            sing(44,200)
            sing(37,100)
            sing(39,100)
            sing(39,400)
            sing(42,200)
            sing(44,200)
            sing(46,400)
            sing(42,200)
            sing(37,100)
            sing(39,100)
            sing(39,400)
            sing(42,200)
            sing(44,200)
            sing(48,200)
            sing(46,200)
            sing(46,200)
            sing(44,200)
            sing(44,200)
            sing(42,200)
            sing(41,200)
            sing(42,200)
            sing(49,800)
        if sensor.IR[1]>dit and sensor.IR[2]>dit and sensor.IR[3]>dit: #전방센서 모두 장애물 인식
            temp=tempo(temp)
            if temp[4]>temp[5]:
                r_b()
                delay(h_t)
                steering(0)
            if temp[5]>temp[4]:
                l_b()
                delay(h_t)
                steering(0)
            i=1
        elif sensor.IR[1]>dit and sensor.IR[2]>dit: # 1,2 센서만 장애물 인식
            temp=tempo(temp)
            l_b()
            delay(h_t)
            steering(0)
            i=1
        elif sensor.IR[2]>dit and sensor.IR[3]>dit: # 2,3 센서만 장애물 인식
            temp=tempo(temp)
            r_b()
            delay(h_t)
            steering(0)
            i=1
        if i:
            if temp[4]>temp[5] or (temp[3]>temp[1] and temp[3]>100):
                l_f()
                delay(h_t)
                i=0
            elif temp[5]>temp[4] or (temp[1]>temp[3] and temp[1]>100):
                r_f()
                delay(h_t)
                i=0
            steering(0)
        if sensor.IR[4]>sensor.IR[5]:#오른쪽 너무 가까우면 왼쪽으로 5도
            if sensor.IR[5]<=50 or sensor.IR[4]>=150:
                steering(-53)
                go(spd,spd)
                delay(100)
            else:
                steering(-22)
                go(spd,spd)
                delay(100)
            steering(0)
        elif sensor.IR[5]>sensor.IR[4]:#왼쪽 너무 가까우면 오른쪽으로 5도
            if sensor.IR[4]<=50 or sensor.IR[5]>=150:
                steering(53)
                go(spd,spd)
                delay(100)
            else:
                steering(22)
                go(spd,spd)
                delay(100)
            steering(0)

        else:
            go(spd,spd)



Open()
distance=20
speed=350
halfsec=450

Drive(speed,distance,halfsec)


close()

