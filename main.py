a=3
b=4
c=5
d=7
x=0
z=(a+b)*c/d
print(z)
name="ALex"
age=0
n=int(input("Enter numerator: "))
deno=int(input("Denominator: "))
if (n%deno==0):
    print("divisible")
else:
    print("Not divisible")

mean1=38
wrong_num=36
correct_num=56
total_num=40
sum=mean1*total_num
print("the sum of 40 numbers ",sum)
num2=sum-(wrong_num-correct_num)
print(num2)

mean2=num2/total_num
print(mean2)

s1 = int(input("Enter your first speed : "))
s2 = int(input("Enter your second speed : "))
s3 = int(input("Enter your third speed : "))

average = (s1 + s2 + s3)/3
print("The average speed is : ",average)

if s1<average:
  print("Speed 1 is slower than average with the difference of ", average-s1)

if s2<average:
  print("Speed 2 is slower than average with the difference of ", average-s2)
  
if s3<average:
  print("Speed 3 is slower than average with the difference of ", average-s3)