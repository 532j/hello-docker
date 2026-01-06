import requests
import json

def main():
    # PokeAPIからピカチュウのデータを取得
    url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    print(f"Fetching data from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        # データの表示
        print("\n--- 取得したデータ ---")
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        # 全データは大きすぎるので一部のみ表示
        print("----------------------")

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
