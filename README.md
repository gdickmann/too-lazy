Software para automaticamente bater ponto no site da SeniorX.

O script marcará ponto nos seguintes horários:		

* 08:00
* 12:00
* 13:00
* 17:00

Os horários nunca serão fixos, ou seja, eles terão ~2 minutos de antecedência ou atraso para simular melhor uma marcação de ponto imprecisa.

### Download
    git clone https://github.com/Biscoitinhoo/lazzy-enough
    pip3 install selenium

Abra o 'Executar' do Windows (Windows + R) e digite:  

	shell:startup  
	
Dentro dessa pasta, todos os arquivos inicializarão automaticamente junto com o Windows. Isso quer dizer que quando você iniciar o sistema operacional, o programa
irá inicializar junto e rodar em segundo plano. 

	Selecione o arquivo lazzyenough.pyw que você clonou e cole dentro dessa pasta.  

Agora, o arquivo será executado quando o computador ser reiniciado. O último passo é inserir suas credenciais da SeniorX no programa.  

	Inserindo credenciais  
	

	# ======================================== Changes these lines ========================================	
	WEBSITE_URL = "https://platform.senior.com.br/login/..."
	# Your login e-mail
	EMAIL = ''
	# Your password
	PASSWORD = ''	
	# ======================================== Changes these lines ========================================  
	
Caso você queira que o script bata ponto mesmo sem o seu computador estar ligado, utilize o [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview).
Vale lembrar que, por se tratar de um web scrapping, o programa pode falhar caso o HTML da Senior seja alterado. Sinta-se livre para alterar o código, no entanto.
