num = int(input(" Enter Any Five Digit Number : "))

temp = num

rem = temp % 10
sum = rem
temp = temp // 10

rem = temp % 10
sum = sum + rem
temp = temp // 10

rem = temp % 10
sum = sum + rem
temp = temp // 10

rem = temp % 10
sum = sum + rem
temp = temp // 10

rem = temp % 10
sum = sum + rem
temp = temp // 10

print(" Sum of Digit of Given Number [" , num , "] : " , sum )