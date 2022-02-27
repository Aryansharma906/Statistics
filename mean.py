import csv

def  mean():
     with open('SOCR-HeightWeight.csv', newline='') as f:
      reader = csv.reader(f)
      data = list(reader)
      
     data.pop(0)
     new_data = []

  for i in range(len(data)):
     n_num = data[i][1]
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
     
     
 mean = total/n
 print("mean is : "+ str(mean))
 
 mean()