# Sympy：符号计算神器（Spyder已预装）

# 数值计算与符号计算的区别
# 数值计算
import math
print(math.sin(math.pi)) # 和理论值相比，结果有误差

# 符号计算
from sympy import *  #导入所有工具
sin(pi)

# 定义符号
x = Symbol('x')
y = Symbol('y')
print(solve([2 * x - y - 3, 3 * x + y - 7],[x, y]))

#或者导入所有拉丁希腊字母
from sympy.abc import *

# 指定定义域
x = symbols('x', positive = True)

# 批量导入
vars = symbols('x_1:5')
print(vars)

#例子

#展开
expand((x + 1)**2) # expand() 是展开函数

#分解
factor(x**3 - x**2 + x - 1)

#合并同类项
expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
collect(expr, x)

#分式化简
cancel((x**2 + 2*x + 1)/(x**2 + x))

#分式展开
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
apart(expr)

#代入 
expr = cos(x) + 1
expr.subs(x, 0)

#化简
simplify(sin(x)**2 + cos(x)**2)

simplify(2*sin(alpha)*cos(alpha))

simplify(cos(theta) * cos(theta) - sin(theta)*sin(theta))

# 微积分
#极限
limit(sin(x)/x, x, 0)

limit(1/x, x, 0, '+')

#求导
diff(cos(x), x)
diff(x**4, x, 3)

expr = cos(x)
expr.diff(x, 2)

#偏导数
expr = exp(x*y*z)
diff(expr, x)

# 求不定积分
integrate(cos(x), x)

# 求定积分
integrate(exp(-x), (x, 0, oo)) #oo表示正无穷

# 二重积分
integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))

#级数
expr = sin(x)
expr.series(x, 0, 4)

#解方程
Eq(x**2 - x, 0)
solveset(Eq(x**2 - x, 0), x, domain = Reals)

#微分方程
f = symbols('f', cls = Function)
diffeq = Eq(f(x).diff(x, 2) - 2*f(x).diff(x) + f(x), sin(x))
a=dsolve(diffeq, f(x))
print(a)

#矩阵
# 构造矩阵
Matrix([[1, -1], [3, 4], [0, 2]])

# 构造列向量
Matrix([1, 2, 3])

# 构造行向量
Matrix([[1], [2], [3]]).T

# 构造单位矩阵
eye(4)

# 构造零矩阵
zeros(4)

# 构造壹矩阵
ones(4)

# 构造对角矩阵
diag(1, 2, 3, 4)

#矩阵转置
a = Matrix([[1, -1], [3, 4], [0, 2]])
a.T

# 求矩阵 M 的 2 次幂
M = Matrix([[1, 3], [-2, 3]])
M**2

# 求矩阵 M 的逆
M**-1

# 行列式
M = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
M.det()

M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
M.eigenvals()
p = M.charpoly(lamda)
factor(p)

#  Laplace (拉普拉斯)变换
expr = sin(t)
laplace_transform(expr, t, s)

expr = 1/(s - 1)
inverse_laplace_transform(expr, s, t)

# 画图（能力一般）
plot(x**2, (x, -2, 2))

plot_implicit(Eq(x**2 + y**2, 1))

plot3d(x*exp(-x**2 - y**2), (x, -3, 3), (y, -2, 2))


# 例：
# 公式推导：机器人运动学

def RZ(theta):
    '''绕Z轴旋转'''
    return Matrix(
    [[cos(theta), -sin(theta), 0, 0], 
     [sin(theta), cos(theta), 0, 0], 
     [0, 0, 1, 0],
     [0, 0, 0, 1]])

def RX(gamma):
    '''绕X轴旋转'''
    return Matrix([
        [1, 0, 0, 0],
        [0, cos(gamma), -sin(gamma), 0],
        [0, sin(gamma), cos(gamma), 0],
        [0, 0, 0, 1]])

def DX(l):
    '''绕X轴平移'''
    return Matrix(
    [[1, 0, 0, l], 
     [0, 1, 0, 0], 
     [0, 0, 1, 0],
     [0, 0, 0, 1]])

def DZ(l):
    '''绕Z轴'''
    return Matrix(
    [[1, 0, 0, 0], 
     [0, 1, 0, 0], 
     [0, 0, 1, l],
     [0, 0, 0, 1]])

theta_1, theta_2,theta_3, l_2, l_3 = symbols('theta_1, theta_2, theta_3, l_2, l_3')

T04 = RZ(theta_1)*RX(-pi/2)*RZ(theta_2)*DX(l_2)*RZ(theta_3)*DX(l_3)
a=simplify(T04)

# 输出latex形式公式
print_latex(a)
# 用latex工具输出得到公式
# 如 https://www.latexlive.com/






