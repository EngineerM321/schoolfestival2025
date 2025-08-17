import streamlit as st
import time
import google.generativeai as genai
from google.colab import userdata


api = st.secrets['secrets']['API_KEY']
genai.configure(api_key=api)
model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite')
chat = model.start_chat()

back = st.secrets['secrets']['Background_Image']
st.title('中二病ジェネレーター')

def render()->st:
    bg_img = '<style>.stApp {background-image: url(' +back+ ');object-fit: cover;background-repeat: no-repeat;}</style>'
    return st.markdown(bg_img, unsafe_allow_html=True)

def gemini(word):
  response = chat.send_message('"{}"を中二病っぽくしてそれと読み方だけ出力して'.format(word))
  return response.text

render()
genai.configure(api_key=api)

text_input = st.text_input('文の入力', '変換前の文の入力をしてください')

if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        result = gemini(text_input)
        st.write(result)
