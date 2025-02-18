import streamlit as st

st.write("Hello, let's learn how to build a streamlit app")

#styles

st.title("text elements") # for title

st.header("header in streamlit ") # for header 
st.subheader("This is subheader ")

#markdown

# display text in bold
st.markdown("**hello** my name is Laraib")
#display in italix 
st.markdown("Hello! _Laraib_")

# code block
codes = '''
def add(a,b):
    print("a+b = ", a+b)'''

st.code(codes,language='python')

# latex 
st.latex('''(a+b)^2 = a^2 + b^2 + 2*a*b ''')


## image audio video

st.image('images.jpeg', caption = 'Bike')
#st.audio() for audio
#st.video('path')  for video

# widgets
st.checkbox('yes')
st.button('Clickme')
st.radio('pick you gender', ['male','female'])
st.selectbox('pick a fruit' , ['apple','banana', 'kela'])
# st.multiselect
st.select_slider('Pick a mark' , ['Bad', 'Good' , 'Excellent'])
st.slider('pick a number' ,0,50)
st.number_input('pick a number', 0 , 10)
st.text_input('Email address')
st.date_input('School time ')
st.text_area('Description')
st.file_uploader('Upload')
st.color_picker('choose your favourite color')
#similarly you can go for sidebar
st.sidebar.title('sidebar')
st.markdown("hello guys")
