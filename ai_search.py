import os

def search_files(keyword):
    source_dir = "extracted_texts"
    results = []

    # 抽出済みテキストフォルダを確認
    if not os.path.exists(source_dir):
        print("エラー: extracted_texts フォルダが見つかりません。")
        return

    print(f"🔍 『{keyword}』 で検索中...\ def search_files(keyword):
    for filename in os.listdir(source_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(source_dir, filename), "r", encoding="utf-8") as f:
                content = f.read()
                # キーワードが含まれているかチェック
                if keyword in content:
                    results.append(filename)

    if results:
        print(f"✅ 見つかったファイル ({len(results)}件):")
        for res in results:
            print(f" - {res}")
    else:
        print("❌ 該当するファイルはありませんでした。")

if __name__ == "__main__":
    word = input("検索したいワードを入力してください: ")
    search_files(word)