import streamlit as st
import time
import google.generativeai as genai

api = st.secrets['secrets']['API_KEY']
genai.configure(api_key=api)
model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite')
chat = model.start_chat()

back = st.secrets['secrets']['Background_Image']
#back='https://drive.google.com/uc?export=view&id=18jokNW8ktwfdnb5-3-n7XA7KwtftbVIr'
st.title('中二病ジェネレーター')

def render()->st:
    bg_img = '<style>.stApp {background-image: url(' + back +');background-repeat: no-repeat;}</style>'
    return st.markdown(bg_img, unsafe_allow_html=True)

def gemini(word):
  response = chat.send_message('"{}"を中二病っぽくしてそれと読み方だけ出力して。フォーマットとしては「○○○」という変換後の言葉の後に、改行して「×××」という○○○の読み方を入れる感じ。'.format(word))
  return response.text

render()
genai.configure(api_key=api)

st.write("###### 1.入力欄に変換したい文を入力  \n###### 2.変換ボタンをクリック  \n###### 3.中二病チックな文が生成されます")



text_input = st.text_input('###### 文の入力', placeholder="例：このラーメンは実は食品サンプルです")

if text_input=="":
  text_input="このラーメンは実は食品サンプルです"

if st.button('変換'):
    with st.spinner('変換中...'):
        time.sleep(3)
        result = gemini(text_input)
        st.write(result)
