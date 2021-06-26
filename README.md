## LazyEnough
Eu particularmente detesto entrar no site da Senior 4 vezes por dia para apenas pressionar um botão. Caso você trabalhe na Ambev Tech e queira automatizar ou até
mesmo burlar o sistema de horários, agora você pode. 

## Download
    git clone https://github.com/Biscoitinhoo/lazzy-enough
    pip3 install selenium

Abra o CMD (Windows + R) e digite:  

	shell:startup  
	
Dentro dessa pasta, todos os arquivos inicializarão automaticamente junto com o Windows. Isso quer dizer que quando você iniciar o sistema operacional, o programa
irá inicializar junto e rodar em segundo plano.  

	Selecione o arquivo lazzyenough.pyw que você clonou e cole dentro dessa pasta.  

Agora, o arquivo já pode ser executado quando o computador ser reiniciado. O último passo é inserir suas credenciais da SeniorX no programa e instalar o Chromium.  

	Inserindo credenciais  
	

	# ============================================= Changes this files =============================================
	# The URL for "Senior Sistemas". It can change for each user.
	WEBSITE_URL = ""
	# Your login e-mail
	EMAIL = ''
	# Your password
	PASSWORD = ''

	CHROME_LOCATION = '/home/biscoitinho/Documents/softwares/chromedriver/chromedriver'
	# ============================================= Changes this files =============================================  
	
É autoexplicativo, porém:  
* WEBSITE_URL: A URL da página de login da SeniorX.  
* EMAIL: Seu e-mail (atualmente, @hbsis) de login da SeniorX.  
* PASSWORD = Sua senha de login da SeniorX.  
* CHROME_LOCATION = Localização do arquivo chromedriver - última etapa


## Instalando o ChromeDriver  

Primeiramente, abra o site de download do [ChromeDriver](https://chromedriver.chromium.org/downloads)  
Você notará que há download de várias versões. Você terá que fazer o download da mesma versão que o seu Google. Para saber a versão:  


	Três pontos no canto superior direito -> Help -> About Google Chrome  
	
	
Isso irá retornar a versão do Google. Se o seu Google for versão 91.0.4472.114, por exemplo, instale o ChromeDriver versão 91.  

Após clicar no botão de download, baixe o ChromeDriver "chromedriver_win32.zip".  

Após o download, extraia o ChromeDriver para o local que você desejar. Por fim, insira no "CHROME_LOCATION" a localização em que você extraiu seu arquivo. Por exemplo:  

	CHROME_LOCATION = 'C:\chromedriver.exe'
	Nota: não esqueça da extensão ".exe".  
	
	
Você pode alterar os horários em que os pontos são batidos. Por padrão, o sistema irá bater ponto nos seguintes horários:

* 8:00  
* 12:00  
* 13:00  
* 17:00  


Fique livre para modificar, distribuir e adaptar o software da maneira que desejar. 


# - G.
