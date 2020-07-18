"""
Name:  Phan Ben
Class: 18THD1
MSSV:  105180273
phone: 0399742099
link github : https://github.com/phanben110phanben110/KTDL
"""
import math
#lưu giá trị vào đây
dataResistor = (140.25,140.5,141.75,139.25,139.5,140.25,140.0,126.75,141.15,142.25,140.75,144.15,140.15,142.75)

#Kỳ vọng toán học của đại lượng
M_x = 0

#sai số dư
Vi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# tổng sai số dư
totalVi = 0

#Độ lệch bình quân phương
errorCube = 0

#độ lệch bình quân phương của giá trị trung bình đại số
errorCubeAverage = 0

#sai số phép đo
denta =  0

#hệ số Hst
Hst = 1.3

#hệ số K
k = 1.2

def average(data, so_thap_phan ):
	sum = 0
	for i in range(len(data)):
		# print(type(data[i]))
		sum = sum + float(data[i])
	variable = sum / len(data)
	return round(variable , so_thap_phan)
def error(data, M_x , so_thap_phan ):
	Ai=  [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(len(data)):
		# print(type(data[i]))
		Ai[i] = round(abs(float (M_x - data[i])) , so_thap_phan )
	return Ai
def sum( data ):
	sum =  0
	for i in range(len(data)):
		sum = sum + data[i]
	return sum
def sumCube(data ):
	sum = 0
	for i in range(len(data)):
		sum = sum + data[i]*data[i]
	return sum

if __name__ == "__main__" :
	so_thap_phan = 3
	M_x = average(dataResistor , so_thap_phan)
	Vi = error(dataResistor , M_x ,so_thap_phan )
	totalVi = sum(Vi)
	check = 1
	while ( check == 1 ):
		if totalVi != 0:
			errorCube = math.sqrt(sumCube(Vi) / (len(dataResistor) - 1))
			errorCubeAverage = errorCube / math.sqrt(len(dataResistor))

			check = 0
		else:
			i = 1
			M_x = average(dataResistor, so_thap_phan + i)
			Vi = error(dataResistor, M_x, so_thap_phan + i)
			totalVi = sum(Vi)
			errorCube = math.sqrt(sumCube(Vi) / (len(dataResistor) - 1))
			i += 1
			check = 1
	if len(dataResistor) >= 20 :
		denta = errorCubeAverage*k
	else:
		denta =errorCubeAverage*Hst

	print("Phan Ben 18TDH1")
	print("Kết quả phép đo là {} +- {}  (Omh) ".format(M_x,round(denta , 3)))














