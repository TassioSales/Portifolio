#usar api para procurar eventos de artistas
#api = ticketmaster



import requests
import json
import sys


#realizar conexão com a api
def get_eventos(artista):
    url = "https://app.ticketmaster.com/discovery/v2/attractions.json?"
    api_key = 'api_key=fQaxm94rnT1qMHHY1meGNpvAuEmn5KnF'
    #mostrar conexão com a api
    print('Conectando com a API...')
    #realizar conexão com a api
    



if __name__ == '__main__':
    artista = perguntar()
    eventos = get_eventos(artista)
    print(json.dumps(eventos, indent=4))
