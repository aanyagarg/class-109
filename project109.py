import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as p
import statistics
import random


f = p.read_csv("studentsperformance.csv")

data = f["reading score"].tolist()

total = len(data)

#------------------- Calculating mean,median , mode and stdev---------------------

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev= statistics.stdev(data)

print("Mean --> " , mean)
print("Median --> " , median)
print("Mode --> " , mode)
print("-------------------------------------")

print("Std dev --> " , stdev)
print("-------------------------------------")

# -------------------------- first/secon/third std dev ----------------------------------

firstStdevStart , firstStdevEnd = mean-stdev , mean+stdev

secondStdevStart , secondStdevEnd = mean-(2*stdev) , mean+(2*stdev)

thirdStdevStart , thirdStdevEnd = mean-(3*stdev) , mean+(3*stdev)

# ------------------------- finding the list of datas withing the stdev -----------------------

listOfDataWithinStdev1 = [
    result for result in data if result > firstStdevStart and result < firstStdevEnd
]

listOfDataWithinStdev2 = [
    result for result in data if result > secondStdevStart and result < secondStdevEnd
]

listOfDataWithinStdev3 = [
    result for result in data if result > thirdStdevStart and result < thirdStdevEnd
]

# ------------------------------ percentage of list of datas -------------------------

a1 = len(listOfDataWithinStdev1)
a2 = len(listOfDataWithinStdev2)
a3 = len(listOfDataWithinStdev3)

percentage1 = (a1*100.0)/total
percentage2 = (a2*100.0)/total
percentage3 = (a3*100.0)/total

print("Percentage: of data lies within 1 standard deviation : " , percentage1)
print("------------------------------------------------------------------")

print("Percentage: of data lies within 2 standard deviation : " , percentage2)
print("------------------------------------------------------------------")

print("Percentage: of data lies within 3 standard deviation : " , percentage3)
print("------------------------------------------------------------------")
