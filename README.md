# Keylogger-simple
Este projeto é uma implementação básica de um keylogger, criado para fins educacionais. Ele demonstra como capturar eventos de teclas digitadas, cliques de mouse e capturas de tela em um sistema.

Para começarmos a falar sobre o nosso keylogger, primeiro vamos abordar as bibliotecas necessárias para faze-lo rodar com perfeição. Dito isto, abaixo está listado as bibliotecas e o que elas fazem:

Teclado e mouse:

- pynput: Está biblioteca é capaz de Ouvir(Listener), Controlar(Controller) e Automatizar processos no seu mouse e no seu teclado. Como estamos fazendo um keylogger usaremos a função de Listener que nos ajuda a ouvir e registrar o que está sendo digitado (Usamos a função Key também para testes e fazer o programa parar). Com essa biblioteca, estamos caputando quando o nosso alvo pressionar e quando ele soltar a tecla. Também estamos registrando quando o nosso alvo pressioan/solta, coordenadas da tela de onde ele clicou e o botão que foi pressionado (Esquerdo ou Direito).

No caso do mouse, podemos capturar também a movimentação e a rolagem como podemos vê no código, porém isso consumiria mais memória e acarretaria em lentidão e nosso alvo iria descobrir que tem algo de errado.

- os: Uma biblioteca bem famosa para modificação de arquivo. Com ela nós usamos arte manhã para salvarmos os arquivos.txt em arquivos ocultos para ficar mais difícil de achar. Lembrando que nos código de Teclado e mouse só está para deixar oculto caso seja Windows, se sua máquina for linux os arquivos não ficaram ocultos.

Print Tela:

- mss/mss.tools: Esse biblioteca nos permite tirar print da nossa tela e salvalas. Sozinha não faz muita coisa, porém juntamente com as demais, vira uma boa ferramenta. A mss.tools nos permite ter mais liberdade com a nossa imagem, permitindo salvar de diferentes maneiras e de diferentes domínios.

- os: Nós também usamos para deixar oculto, porém dessa vez nós também utilizamos para criar uma pasta e salvar todas as imagens nessa pasta, assim fica não só mais difícil de encontrar como fica mais organizado.
  
- subprocess: Estamos usando o subprocess aqui para usamos o que já tinhamos feito de salvar como oculto e fazer a mesma coisa com nossa pasta.

- platform: Esse aqui é muito importante e essencial para que seu programa funcione em diferentes sistemas operacionais. Com ele analisamos qual o sistema operacional da vítima e com isso, designamos uma alternativa para de colocar a pasta em modo oculto, já que em diferentes sistemas, temos diferentes soluções.

- time: Essa biblioteca é usada para manuseio do tempo, com ela podemos ter total controle do tempo a nosso favor, com isso, usamos o time para dar um intervalo de 30 segundos de um print a outro.

- datetime import datetime: Essa biblioteca nos permite que possamos salvar cada imagem com (Dia.Mês.Ano_Hora_Minuto_Segundo) para que as imagens não sejam subscrevidas uma em cima da outra.

Arquivo RAR com senha

- pyzipper: Com o nome, podemos imaginar para que serve já está biblioteca e sim, com ela nós criamos a nossa pasta zip com alguma senha que nós mesmos escolhemos. Não só isso, mas nós também podemos manusear os arquivos dentro dela como se fosse a biblioteca "os" porém para arquivos zip. Com isso, além de colocarmos a senha, nós também vamos colocar os arquivos/pastas que criarmos dentro desse zip.

- os: Dessa vez, usamos para sempre apagar e criar uma nova pasta zipada, assim sempre teremos coisas novas e nosso alvo nunca irá descobrir tudo que temos, nós também usamos para mandar os arquivos para o zip e deixar-mos o zip oculto.

- platform: Com a mesma finalidade de veriricar se é Windows ou Linux

- time: Tempo de espera

Envio de Email
