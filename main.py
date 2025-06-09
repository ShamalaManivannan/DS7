import matplotlib.pyplot as plt

#Histogram
ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,bins,rwidth = 0.8,histtype='bar')
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

#Scatter Plot

x = [1,2,3,4,5,6,7,8,9,10]
y = [0,1,0,1,0,1,0,1,0,1]

plt.scatter(x,y,color = 'r', marker ="o", label = "Scatter Plot", s=50)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()

#Pie chart

activities=["Sleeping","Eating","Playing","Watching Tv", "Reading","School Hours"]

hours = [9,1,4,2,1,7]

clr = ['c','m','r','y','g','b']
plt.pie(hours,labels=activities,colors=clr,startangle=90,shadow=True)
plt.title("Day Chart")
plt.show()

#Stack Plot

days = [1,2,3,4,5]

sleep = [9,8,7,8,9]
eat = [1,2,2,1,1]
playing = [3,4,2,1,2]
watchingtv = [2,3,2,1,3]

plt.plot([],[],color = 'm', label = 'Sleeping', linewidth = 5)
plt.plot([],[],color = 'r', label = 'Eating', linewidth = 5)
plt.plot([],[],color = 'g', label = 'Playing', linewidth = 5)
plt.plot([],[],color = 'b', label = 'Watching TV', linewidth = 5)

plt.stackplot(days,sleep,eat,playing,watchingtv, colors = ['m','r','g','b'])
plt.xlabel("Activities")
plt.ylabel("Hours")
plt.title("Stack Plot")
plt.legend()
plt.show()