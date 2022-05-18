import csv
with open('SOCR-HeightWeight.csv', newline = '') as f:
    read = csv.reader(f)
    fileData = list(read)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))
n = len(newData)
total = 0
for a in newData:
    total = total + a
mean = total / n
print('Mean value is ' + str(mean))