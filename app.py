#link para site - https://consulta-empresa.netlify.app/
#XPATH = //tag[@atributo='valor']
#1= entrar no site
#2- fazer o login (clicar no campo usuario, digitar o usuario, clicar no campo senha, digitar a senha, e clicar em entrar.
#3- fazer o download dos pdfs das empresas e após isso renomear para o nome da empresa dona do relatório.
#4- repetir passo 3 até acabar os pdfs.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

chrome_options = Options()
chrome_options.add_experimental_option('prefs',{
    #não pedir permissao para fazer download
    'download.prompt_for_download': False,
    #setar local padrao para armazenar downloads
    'download.default_directory':r'C:\Users\Usefr\OneDrive\Documentos\Automação do site\relatorios',
    #nao pedir permissao para realizar multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://consulta-empresa.netlify.app/')
sleep(5)

campo_usuario = driver.find_element(By.XPATH,"//input[@id='username']")
sleep(1)
campo_usuario.click()
campo_usuario.send_keys('jhonatan')

campo_senha = driver.find_element(By.XPATH,"//input[@id='password']")
sleep(1)
campo_senha.click
campo_senha.send_keys('12345678')

botao_entrar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg']")
botao_entrar.click() 
sleep(5)

def baixar_relatorios_empresas(driver):
# 1- Extrair o nome de cada empresa e guarda numa lista
    nomes_empresas = driver.find_elements(By.XPATH,"//td[@name='nome_empresa']")
    sleep(2)
    botoes_download_pdf = driver.find_elements(By.XPATH,"//button[@class='download-btn']")
    sleep(2)

    for nome, botao_pdf in zip(nomes_empresas, botoes_download_pdf):
        botao_pdf.click()
        sleep(2)

        diretorio = r'C:\Users\Usefr\OneDrive\Documentos\Automação do site\relatorios'
        nome_antigo = 'perfil_empresa.pdf'
        novo_nome = f'{nome.text}.pdf'

        caminho_completo_antigo = os.path.join(diretorio,nome_antigo)
        caminho_completo_novo = os.path.join(diretorio,novo_nome)

        os.rename(caminho_completo_antigo,caminho_completo_novo)

baixar_relatorios_empresas(driver=driver)

botao_proxima_pagina = driver.find_element(By.XPATH,"//button[@id='nextBtn']")

while botao_proxima_pagina.get_attribute('disabled') == None:
    botao_proxima_pagina.click()
    baixar_relatorios_empresas(driver=driver)




input('Aperte ENTER para fechar')
