import requests
from bs4 import BeautifulSoup
import numpy
import pandas
import time
import warnings
import plotly.express as px

pages = numpy.arange(1, 5, 50) # Agrupar os itens
headers = {'Accept-Language':'pt-BR,pt;q=0.8'}
titles = []
years = []
genres = []
runtimes = []
votes = []
ratings = []
imdb_ratings = []

for page in pages:
    req = requests.get("https://www.imdb.com/search/title?genres=sci-fi&" + "start=" + str(page)
     + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
    time.sleep(5)
    if req.status_code != 200:
        warnings(f'Algo deu errado, erro: {req.status_code}')

    page_html = BeautifulSoup(req.text, 'html.parser')

    movie_containers = page_html.find_all('div', class_='lister-item mode-advanced')

    for container in movie_containers:
        if container.find('div', class_='ratings-metascore') is not None:
            title = container.h3.a.text
            titles.append(title)
        else:
            titles.append(None)

        if container.h3.find('span', class_ = 'lister-item-year text-muted unbold') is not None:
            year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
            years.append(year)
        else:
            years.append(None)

        if container.p.find('span', class_ = 'certificate') is not None:
            rating = container.p.find('span', class_ = 'certificate').text
            ratings.append(rating)
        else:
            ratings.append(None)

        if container.p.find('span', class_ = 'genre') is not None:
            genre = container.p.find('span', class_ = 'genre').text.replace('\n', '').strip()
            genres.append(genre)
        else:
            genres.append(None)

        if container.p.find('span', class_ = 'runtime') is not None:
            runtime = container.p.find('span', class_ = 'runtime').text
            runtimes.append(runtime)
        else:
            runtimes.append(None)

        if container.find('div', class_= 'inline-block ratings-imdb-rating') is not None:
            imdb = container.strong.text
            imdb_ratings.append(imdb)
        else:
            imdb_ratings.append(None)

        #bug ao receber um voto vazio.
        #if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:
        #   vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
        #    votes.append(vote)
        #else:
        #    votes.append(None)

data = pandas.DataFrame({'Filme':titles,
'Ano':years,
'Genero':genres,
'Duração':runtimes,
'imdb':imdb_ratings})
#'Votos':votes

#contagem de gêneros
qtdFilmes = data['Filme'].value_counts()
qtdGeneros = data['Genero'].value_counts()

#Montar gráficos
px.pie(names= qtdFilmes.index, values= qtdGeneros.values)