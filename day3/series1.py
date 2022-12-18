#series 1+x+x^2+x^3+x^4+x^5
series=0
x = 5
for i in range(0,6):
    term = x**(i)
    series = series + term
print("the value of series is", series)
