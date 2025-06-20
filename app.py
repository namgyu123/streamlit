import streamlit as st

st.title("This is the app title")
st.header("This is the markdown")
st.markdown("This is the header")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

import streamlit as st

st.checkbox('yes')
st.button('Click')
gender = st.radio('Pick your gender', ['Male', 'Female'])
planet = st.selectbox('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
score = st.slider('Pick a number', 0, 50)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

import streamlit as st

st.image("image.png")  # 같은 폴더에 image.png 파일이 있을 때
st.audio("audio.mp3")  # 같은 폴더에 audio.mp3 파일이 있을 때
st.video("video.mp4")  # 같은 폴더에 video.mp4 파일이 있을 때
