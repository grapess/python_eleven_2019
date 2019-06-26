val1 = [ 11 , 22 ]
val2 = [ 11 , 22 ]

print( id(val1))
print( id(val2))

val1 = ( 11 , 22 )
val2 = ( 11 , 22 )
print( id(val1))
print( id(val2))

val1 = { 11 , 22 }
val2 = { 11 , 22 }
print( id(val1))
print( id(val2))

val1 = { "o" : 11 , "t" : 22 }
val2 = { "o" : 11 , "t" : 22 }
print( id(val1))
print( id(val2))