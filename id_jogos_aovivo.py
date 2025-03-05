import requests

# url que pega os jogos do dia
url = "https://www.sofascore.com/api/v1/sport/football/events/live"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0"
}

# requisição para obter os jogos ao vivo
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    print("Jogos ao vivo disponíveis:")
    
    for event in data['events']:
        match_id = event['id']
        home_team = event['homeTeam']['name']
        away_team = event['awayTeam']['name']
        
        print(f"ID: {match_id} - {home_team} x {away_team}")

    print("\nUse o ID do jogo para obter as estatísticas.")
else:
    print("Falha ao obter a lista de jogos.")
