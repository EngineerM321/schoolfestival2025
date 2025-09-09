# 必要なライブラリをインポート
import streamlit as st
import time
import google.generativeai as genai
import base64

# 入力文字数の最大値を設定
maxword = 20

# StreamlitのsecretsからAPIキーを取得
api = st.secrets['secrets']['API_KEY']

# Gemini APIの初期化
genai.configure(api_key=api)
model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite')
chat = model.start_chat()

# 背景画像のURLをsecretsから取得
back = st.secrets['secrets']['Background_Image']

# 背景画像を適用する関数
def render():
    bg_img = '<style>.stApp{background-image: url(' + back +');background-repeat: no-repeat;}</style>'
    return st.markdown(bg_img, unsafe_allow_html=True)

#フォントを指定する関数
def font():
    font_css = """
    @font-face {
        font-family: 'WDXL Lubrifont JP N';
        src: url('./static/fonts/WDXLLubrifontJPN-Regular.woff2') format('woff2');
        font-weight: normal;
        font-style: normal;
    }
    body, .css-1v3fvcr {
        font-family: 'WDXL Lubrifont JP N', sans-serif;
    }
    """
    
    return st.markdown(f'<style>.stApp{font_css}</style>', unsafe_allow_html=True)

# 背景をレンダリング

font()
render()

# アプリのタイトルを表示
st.title('中二病ジェネレーター')

# 入力された文を中二病風の単語に変換する関数
def gemini(word):
  response = chat.send_message('"{}"を中二病っぽくして言葉だけを１つ出力して'.format(word))
  return response.text


# アプリの使い方を表示
st.write("###### 1.入力欄に変換したい文を入力(20文字以内)  \n###### 2.変換ボタンをクリック  \n###### 3.中二病チックな文が生成されます")

# ユーザーからの入力を受け取るテキストボックス
text_input = st.text_input('###### 文の入力', placeholder="例：このラーメンは実は食品サンプルです")

# 「変換」ボタンがクリックされたときの処理
if st.button('変換'):
    # 入力文字数が上限を超えている場合は警告を表示
    if len(text_input) > maxword:
        overword = len(text_input) - maxword
        st.warning(str(overword) + "文字オーバーしています")
    else:
        # Geminiに問い合わせて変換結果を表示
        with st.spinner('変換中...'):
            time.sleep(3)  # スピナー表示のための待機時間
            result = gemini(text_input)
            st.success("生成された中二病ワード:" + result)
