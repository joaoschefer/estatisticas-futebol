import requests
import pandas as pd

url = 'https://www.sofascore.com/api/v1/event/12437859/statistics'

# headers para simular navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    all_data = []

    for match_stat in data['statistics']:
        period = match_stat['period']

        for group in match_stat['groups']:
            group_name = group['groupName']

            for item in group['statisticsItems']:
                stat_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')

                all_data.append({
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stat_name,
                    'Home': home_value,
                    'Away': away_value
                })

    df = pd.DataFrame(all_data)

    excel_file = 'futebol_stats.xlsx'
    df.to_excel(excel_file, index=False)

    print(f'Dados exportados para {excel_file}')
