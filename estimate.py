n=int(input())
def wallis(n):
 value=1
 t=1
 for t in range(1,n):
  value = value*(4*t**2)/((4*t**2)-1)
  t=+1
 print(2*value)
wallis(n)
