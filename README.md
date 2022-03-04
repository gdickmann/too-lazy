## AVISO ⚠
### Esse script foi feito apenas como uma piada. Usá-lo para seu benefício próprio está sob sua responsabilidade.

Programa feito em Python para automaticamente bater ponto no site da SeniorX. O script marcará ponto nos seguintes horários:

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
	# The URL for "Senior Sistemas". It can change for each user.
	WEBSITE_URL = "https://platform.senior.com.br/login/..."
	# Your login e-mail
	EMAIL = ''
	# Your password
	PASSWORD = ''	
	# ======================================== Changes these lines ========================================  
	
* EMAIL: Seu e-mail (atualmente, @hbsis) de login da SeniorX.
* PASSWORD = Sua senha de login da SeniorX.
