#importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep #estou importando esta biblioteca para meu código parecer mais humano
import csv #para importa tudo para um csv

#aqui vou fazer ele ficar mudando o ip, está em processo kkkkkkkkk

#preparando para importação csv
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

#chamando o chrome driver
driver = webdriver.Chrome('./chromedriver')

#acessando o lkd
driver.get('https://www.linkedin.com/') #aqui estou usando o comando get para acessar o lkd
sleep(2)

#clicando para fazer o login
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

#preenchendo o user e senha
user = driver.find_element_by_name('session_key')
user.send_keys('digite seu email aqui')
passw = driver.find_element_by_name('session_password')
user.send_keys('digite sua senha aqui')

#fazendo usar o botão "enter" após digitar a senha 
passw.send_keys(Keys.ENTER) #simulando teclado do notebook
sleep(4) #ficando mais humano

#abrindo o google 
driver.get('https://google.com')
sleep(2)

#selecionando o campo para a busca no google
busca_in = driver.find_element_by_name('q')

#fazendo a busca
busca_in.send_keys('site:linkedin.com/in/ AND "Engenheiro" and "Belo Horizonte"') #aqui estou usando um hack de busca no google
busca_in.send_keys(Keys.ENTER)
sleep(3)

#aqui vou fazer uma extração de perfis encontrados
lista_de_perfil = driver.find_element_by_xpath('//div[class="r"]/a') #aqui estou selecionando os perfis encontrados
lista_de_perfil = [perfil.get_atribute('href') for perfil in lista_de_perfil]

#aqui eu vou fazer ir para proxima pagina, ainda está em processo kkkkkkkkk

#aqui vou fazer extração das informações individuais
for perfil in lista_de_perfil:
    driver.get(perfil)
    sleep(4)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//title/text()').extract_first().split(' | ')[0]
    headline = response.xpath('//h2/text()')[1].extract().strip()
    url_perfil = driver.current_url

    #criando o arquivo CSV
    writer.writerow([nome, headline, url_perfil])

#saindo do driver
driver.quit()
