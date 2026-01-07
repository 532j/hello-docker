import streamlit as st
import os
import glob
from openai import OpenAI

# APIキーを環境変数から読み込む設定
# Dockerで実行時は --env-file で渡された環境変数が読まれる
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI文書アシスタント")

keyword = st.text_input("検索ワードを入力してください")

if keyword:
    st.write(f"🔍 '{keyword}' について調べています...")

    # --- ステップ1: extracted_textsフォルダからテキストを読み込む ---
    all_text = ""
    # Dockerのマウント先は /app なので、/app/extracted_texts/ 以下のファイルを読み込む
    # glob.glob("extracted_texts/*.txt") で相対パス指定OK
    text_files = glob.glob("extracted_texts/*.txt")
    
    if not text_files:
        st.warning("テキストファイルが見つかりません。 extracted_texts フォルダを確認してください。")
    else:
        st.info(f"{len(text_files)} 個のファイルを読み込みました。")
        for filename in text_files:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                    all_text += f"---\nFile: {filename}\nContent:\n{content}\n\n"
            except Exception as e:
                st.error(f"ファイル読み込みエラー ({filename}): {e}")

    # --- ステップ2: AIに「この中身を読んで答えて」と依頼する ---
    if all_text:
        st.subheader("🤖 AIの回答")
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini", # 安価なモデルを指定
                messages=[
                    {"role": "system", "content": "あなたは優秀な社内文書アシスタントです。提供されたテキストコンテキスト「のみ」に基づいて、ユーザーの質問に答えてください。コンテキストに関連する情報がない場合は、正直に「その情報は文書内に見つかりません」と答えてください。"},
                    {"role": "user", "content": f"以下のドキュメントを参考に回答してください。\n\n# コンテキスト\n{all_text}\n\n# 質問\n{keyword}"}
                ]
            )
            st.write(response.choices[0].message.content) # 回答を表示
        except Exception as e:
            st.error(f"OpenAI APIエラー: {e}")
            if not os.getenv("OPENAI_API_KEY"):
                st.error("APIキーが設定されていない可能性があります。.envファイルを確認してください。")