num = int( input(" Enter Any Five Digit Number : "))

temp = num 

rem = temp % 10
result = ( ( rem + 1 ) % 10 )
temp = temp // 10

rem = temp % 10
result = ( ( rem + 1 ) % 10 ) * 10 + result
temp = temp // 10

rem = temp % 10
result = ( ( rem + 1 ) % 10 ) * 100 + result
temp = temp // 10

rem = temp % 10
result = ( ( rem + 1 ) % 10 ) * 1000 + result
temp = temp // 10

rem = temp % 10
result = ( ( rem + 1 ) % 10 ) * 10000 + result
temp = temp // 10

print(" Result : " , result )