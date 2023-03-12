
#Importando as bibliotecas request e BeautifulSoup para realizar requests e formatar dados capturados através de WebScraping
from bs4 import BeautifulSoup
import requests

#informando a URL e os headers, e utilizando ambos para capturar o html do site e indentando ele utilizando BeautifulSoup
site = 'https://www.melhorcambio.com/dolar-hoje'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}
html = requests.get(site, headers=header).text
soup = BeautifulSoup(html, 'html.parser')

#Capturando dados de uma tag específica do HTML da página
precoDolar = soup.find(id='taxa-comercial')
dolarComercial = precoDolar['value']

#Imprimindo o valor capturado no último passo
print(f'Preço dólar comercial: {dolarComercial}')

#Capturando diversos valores de um bloco do HTML
onde = soup.find('div', id='numeros')
dolarOnde = onde.find_all('h5')
precoOnde = onde.find_all('p')

#Informando o que será impresso na sequência
print('Preço de compra do dólar em algumas cidades Brasileiras: ')

#Realizando um loop para impressão dos valores associados as suas respectivas cidades
for i in range(len(dolarOnde)):
    print(f'{dolarOnde[i].string}: {precoOnde[i].string}')


