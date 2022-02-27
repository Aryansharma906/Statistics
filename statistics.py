from collections import  Counter
import csv


#collection data from the file
with open('SOCR-HeightWeight.csv', newline='') as f:
     reader = csv.reader(f)
     data = list(reader)


data.pop(0)

new_data = []

for i in range(len(data)):
     n_num = data[i][2]
     new_data.append(float(n_num))
     
n = len(new_data)
total = 0
for x in new_data:
     total += x 
     


if n//2 ==0 :
     median1 = float(new_data[n//2])
     median2 = float(new_data[n//2 -1 ])
     median = median1 + median2/2
else :
     median =float(new_data[n//2])
     print(n)

# calculation mode
mode_data =[]
for a in range(len(data)):
     n_num = data[a][1]
     mode_data.append(n_num)
     
data.Counter(mode_data)

mode_data_for_range={
     "75-85": 0,
     "85-95": 0,
     "95-105": 0 ,
     "105-115": 0,
     "115-125": 0,
     "125-135": 0,
     "1355-145": 0,
     "145-155": 0,
     "155-165": 0,
     "165-175": 0
}


for weight, occurence in mode_data.items():
     if 75 < float(Height) <85:
          mode_data_for_range["55-65"] += occurence
     elif 85 < float(Height) < 95:
          mode_data_for_range["85-95"] += occurence
     elif 95 < float(Height) < 105:
          mode_data_for_range["95-115"] += occurence
     elif 115 < float(Height) < 125:
          mode_data_for_range["115-125"] += occurence
     elif 125 < float(Height) < 135:
          mode_data_for_range["70-80"] += occurence
     elif 135 < float(Height) < 145:
          mode_data_for_range["70-80"] += occurence
     elif 145 < float(Height) < 155:
          mode_data_for_range["70-80"] += occurence
     elif 155 < float(Height) < 165:
          mode_data_for_range["70-80"] += occurence
     elif 165 < float(Height) < 175:
          mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
      if occurence > mode_occurence:
          mode_range, mode_occurence =[int(range.split("-")[1], int(range.split("-")[2]))], occurence
           
mode = float(mode_range[1] + mode_range[2] /2)
     

mean = total/n
print("mean is : "+ str(mean))
print("median is : "+ str(median))
print("mode is :" + str(mode))









     
