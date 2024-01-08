import streamlit as st
import pandas as pd 
import numpy as np  

st.write("## Streamlit Examples")

x=st.slider("x")
st.write(x,"square is",x**2)
st.latex("\sum_{i=1}^{n}x_i=x_1+x_2+\cdots+x_n")


# 只展示代码
code = """
for i in range(5):
    st.write("hello")
"""
st.code(code, language="python")


# 展示代码，和运行结果
with st.echo():
    for i in range(5):
        st.write("hello")


st.write("这是我们使用数据创建表的首次尝试：")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# 甚至不用 st.write()
# 把内容放在代码里就行了。效果如下。

"""
Here's our second attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# 画图

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# 画地图
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [43.84, 87.57],
    columns=['lat', 'lon'])

st.map(map_data)

# 选数字
option = st.sidebar.selectbox(
    '您最喜欢哪个数字？',
     df['first column'])

'You selected: ', option

# 按钮，折叠文本

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander1 = st.expander("FAQ1")
expander1.write("Here you could put in some really, really long explanations...")


# 进度条

import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1000):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress((i+1)//10) # progress 参数范围需要在100以内
  time.sleep(0.02)

'...and now we\'re done!'

