import requests

url ='https://br.investing.com/rss/news_25.rss'
result = requests.get(url)
result_dict = result.json()
click.echo(result_dict['chart']['result'][0]['meta']['regularMarketPrice'])