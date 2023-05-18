from AltinoLite import *
# 1 좌전방 2 전방 3 우전방 센서 4 오른쪽, 센서 5 왼쪽 6 후방
# 조향 좌 음수 우 양수
#해결할 문제 무간지옥, 속도,
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
    while True:
        temp=[0,0,0,0,0,0,0]
        i=0
        if sensor.IR[1]>dit and sensor.IR[2]>dit and sensor.IR[3]>dit: #전방센서 모두 장애물 인식
            go(-spd,-spd)
            delay(h_t)
            i=1
            temp=tempo(temp)
        elif sensor.IR[1]>dit and sensor.IR[2]>dit: # 1,2 센서만 장애물 인식
            l_b()
            delay(h_t)
            steering(0)
            i=1
            temp=tempo(temp)
        elif sensor.IR[2]>dit and sensor.IR[3]>dit: # 2,3 센서만 장애물 인식
            r_b()
            delay(h_t)
            steering(0)
            i=1
            temp=tempo(temp)
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
            if sensor.IR[5]<=14 or sensor.IR[4]>=150:
                steering(-63)
                go(spd,spd)
                delay(100)
            else:
                steering(-32)
                go(spd,spd)
                delay(100)
            steering(0)
        elif sensor.IR[5]>sensor.IR[4]:#왼쪽 너무 가까우면 오른쪽으로 5도
            if sensor.IR[4]<=14 or sensor.IR[5]>=150:
                steering(63)
                go(spd,spd)
                delay(100)
            else:
                steering(32)
                go(spd,spd)
                delay(100)
            steering(0)

        else:
            go(spd,spd)



Open()
distance=20
speed=350
halfsec=500

Drive(speed,distance,halfsec)


close()

