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
newData.sort()
if n % 2 == 0:
    m1 = float(newData[n // 2])
    m2 = float(newData[n // 2 - 1])
    median = (m1 + m2) / 2
else:
    median = newData[n // 2]
print('Median value is ' + str(median))