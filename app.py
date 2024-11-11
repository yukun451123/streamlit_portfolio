import streamlit as st

# タイトルの設定
st.title('StreamlitによるApp')
st.header('レッスン3: テキスト要素の追加')

# テキストの表示
st.text('これは通常のテキストです。')

# Markdown形式のテキスト
st.markdown('これは **太字** で、*イタリック* です。')

# LaTeX形式の数式
st.latex(r'\sqrt{x^2 + y^2} = z')

# 情報メッセージ（⻘⾊）
st.info('データの読み込みが完了しました。')

# 警告メッセージ（⻩⾊）
st.warning('ファイルのサイズが⼤きいため、処理に時間がかかる可能性があります。')

# エラーメッセージ（⾚⾊）
st.error('ファイルの形式が正しくありません。CSVファイルをアップロードしてください。')

# 成功メッセージ（緑⾊）
st.success('グラフの作成が完了しました。')

code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')