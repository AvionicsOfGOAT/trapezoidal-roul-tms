import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

y = [] # newton
x = [] # time
start = 659 # 연소 시작 인덱스
end = 714 # 연소 종료 인덱스
# 데이터 읽기
f = open("tms_data_txt", 'r')
datas = f.read()

# 데이터 추출
tms_datas = datas.split('\n')[start:end] # 연소 하는 범위
start_time = int(tms_datas[0].split()[0])
for i in tms_datas:
    time_and_newton = i.split()
    y.append(float(time_and_newton[1]))
    x.append(int(time_and_newton[0])-start_time) # 영점 맞추기

# 구간
A = x[0]
B = x[-1]
# 델타 x
n = 20
delta_x = (B-A)//n

# 보간
interpolation = interp1d(x, y, kind='linear') # 선형 보간 함수 생성
x = range(A, B)
y = interpolation(x) # 보간한 y
t_x = x[::delta_x]
t_y = y[::delta_x]

#사다리꼴 공식 계산
area = 0
for i in range(n):
    trapezoidal = delta_x*((y[i*delta_x]+y[(i+1)*delta_x])/2)
    area += trapezoidal
    plt.vlines(x=i*delta_x, ymin=0, ymax=y[i*delta_x],color="blue",linewidth=0.5)
    plt.vlines(x=(i+1)*delta_x ,ymin=0, ymax=y[(i+1)*delta_x],color="blue",linewidth=0.5)

# 터미널 출력
print("Area : {:.2f}(s)".format(area/1000))
print("Highest Newton :",max(y),"n",sep="")
print("Combustion Time : ",2.5,"s",sep="")

# 그래프 출력
plt.plot(x, y, color="red")
plt.plot(t_x, t_y, color="blue",linewidth=0.5)
plt.xlabel("Time(ms)")
plt.ylabel("Newton")
plt.title("Trapezoidal Roul on TMS")
plt.show()
