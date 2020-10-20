from django.shortcuts import render
from selenium import webdriver

def main(request):

    # Dicionário que receberá o título e o texto da matéria
    materia = {}

    # Inserido local do driver
    driver = webdriver.Chrome('C:/Users/new12/Desktop/drivers/chromedriver')

    # Definido variável com a URL do site
    site = 'https://www.acordacidade.com.br/noticias/233733/hoje-17-e-o-dia-d-da-campanha-de-vacinacao-de-criancas-e-adolescentes.html'
    driver.get(site)

    # Passado 20 segundos de tempo para aguardar o site carregar
    driver.implicitly_wait(20)

    # Inserindo os IDs dos elementos HTML nas variáveis de título e cada parágrafo da matéria, além da data de publicação e fonte
    materia_titulo = driver.find_element_by_xpath('//*[@id="post"]/h1').text
    p1 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[2]').text
    p2 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[3]').text
    p3 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[4]').text
    p4 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[5]').text
    p5 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[6]').text
    p6 = driver.find_element_by_xpath('//*[@id="tamanhotexto"]/p[7]').text
    data = driver.find_element_by_xpath('//*[@id="post"]/div[1]').text
    fonte = driver.current_url

    # Inserindo os elementos da matéria em seu dicionário
    materia['titulo'] = materia_titulo
    materia['p1'] = p1
    materia['p2'] = p2
    materia['p3'] = p3
    materia['p4'] = p4
    materia['p5'] = p5
    materia['p6'] = p6
    materia['data'] = data
    materia['fonte'] = fonte

    # Linha para fechar a URL após copiar a matéria para o dicionário
    driver.close()
    return render(request, 'main.html', materia)