# 徐也的猪
# 开发时间:2021/10/11   23
import math

t=input('纸张类型：')
n=int(t[1])
long = math.floor(1189/(2**n))
wide = math.floor(841/(2**n))
print(long)
print(wide)