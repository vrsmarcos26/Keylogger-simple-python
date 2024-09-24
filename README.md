<h1>Keylogger-simple</h1>

<p>Este projeto é uma implementação básica de um keylogger, criado para <strong>fins educacionais</strong>. Ele demonstra como capturar eventos de teclas digitadas, cliques do mouse e capturas de tela em um sistema.</p>

<h2>Bibliotecas Necessárias</h2>

<p>Para começarmos a falar sobre o nosso keylogger, vamos abordar as bibliotecas necessárias para fazê-lo rodar corretamente. Abaixo estão listadas as bibliotecas e suas funções:</p>

<h3>Instalação rápida</h3>
<p>Para instalar todas as bibliotecas de uma vez, use o seguinte comando:</p>

Essênciais:
<pre><code>pip install pynput mss pyzipper</code></pre>

Por via das dúvidas:
<pre><code>pip install platform time datetime os subprocess sys win32com.client webbrowser signal smtplib email</code></pre>

<h3>Teclado e Mouse</h3>

<ul>
  <li><strong>pynput</strong>: Esta biblioteca é capaz de ouvir (Listener), controlar (Controller) e automatizar processos no mouse e no teclado. Como estamos criando um keylogger, usaremos a função <code>Listener</code>, que nos ajuda a capturar e registrar o que está sendo digitado. Além disso, usamos a função <code>Key</code> para definir testes e parar o programa. Com essa biblioteca, capturamos quando o alvo pressiona ou solta uma tecla, assim como registramos coordenadas de cliques de mouse e qual botão (esquerdo ou direito) foi pressionado. Também é possível capturar o movimento e a rolagem do mouse, mas isso consome mais memória, podendo causar lentidão e alertar o alvo.</li>
  <li><strong>os</strong>: Usamos essa biblioteca para manipulação de arquivos, como salvar logs em arquivos ocultos no Windows. No Linux, os arquivos não serão ocultos automaticamente.</li>
</ul>

<h3>Captura de Tela</h3>

<ul>
  <li><strong>mss/mss.tools</strong>: Esta biblioteca permite capturar prints da tela e salvá-los. A <code>mss.tools</code> oferece mais flexibilidade, como salvar em diferentes formatos e locais.</li>
  <li><strong>os</strong>: Também usada para criar uma pasta oculta onde as capturas de tela serão armazenadas, tornando-as mais difíceis de serem encontradas e mantendo o projeto organizado.</li>
  <li><strong>subprocess</strong>: Utilizado para ocultar a pasta criada para armazenar as imagens.</li>
  <li><strong>platform</strong>: Essa biblioteca é essencial para que o programa funcione em diferentes sistemas operacionais. Ela identifica o SO do alvo e aplica soluções específicas para ocultar arquivos.</li>
  <li><strong>time</strong>: Usamos o <code>time.sleep</code> para definir um intervalo de 30 segundos entre cada captura de tela.</li>
  <li><strong>datetime</strong>: Permite salvar as imagens com nomes únicos, no formato <code>Dia.Mês.Ano_Hora_Minuto_Segundo</code>, evitando que sejam sobrescritas.</li>
</ul>

<h3>Compactação com Senha</h3>

<ul>
  <li><strong>pyzipper</strong>: Usada para criar pastas zipadas protegidas por senha. Além disso, podemos manipular arquivos dentro do ZIP, como a biblioteca <code>os</code> faz para diretórios normais. Isso garante que o arquivo zip seja atualizado constantemente e permaneça oculto.</li>
  <li><strong>os</strong>: Usada para apagar e recriar a pasta zipada, garantindo que os arquivos sejam sempre novos e difíceis de detectar.</li>
  <li><strong>platform</strong>: Para verificar se o sistema é Windows ou Linux.</li>
  <li><strong>time</strong>: Utilizado para definir tempos de espera.</li>
</ul>

<h3>Envio de E-mails</h3>

<ul>
  <li><strong>smtplib</strong>: Usado para criarmos uma linha diretamente com o script e o e-mail da pessoa. Com isso, basta setar as informações necessárias (e-mail, porta, server e senha) para que possa haver a ligação.</li>
  <li><strong>email</strong>: Introduzido exatamente por conta de mandar e-mail. Ele é usado para que possamos fazer uma ligação segura com a extenção <code>encoders</code> que faz ter criptografia na ligação.</li>
  <li><strong>email.mime.multipart / email.mime.text / mail.mime.base</strong>: Essas três sã utilizadas unicamente para encorporar o nosso e-mail com Título, Corpo e mandar arquivos para o e-mail.</li>
  <li><strong>time</strong>: Como nos outros arquivos, ele basicamente está lá para automatizar de tempos em tempos o envio do e-mail.</li>
</ul>

<h3>Inicialização ao iniciar Windows</h3>

<ul>
  <li><strong>os</strong>: Usamos essa biblioteca, pois o método que fazemos é para ele iniciar junto com o windows é basicamente ele criar um arquivo de atalho que aponta para o nosso script e que é colocado na pasta de inicialização.</li>
  <li><strong>sys</strong>: Módulo que fornece acesso a algumas variáveis e funções que interagem diretamente com o interpretador Python, como <code>sys.argv</code>, que contém os argumentos de linha de comando.</li>
  <li><strong>win32.com.client</strong>: Módulo da biblioteca <code>pywin32</code>, que permite interagir com a automação COM do Windows. O <code>Dispatch</code> é usado para criar e manipular objetos COM.</li>
</ul>

<h3>Compilação</h3>

<ul>
  <li><strong>pyinstaller</strong>: Usamos essa biblioteca, pois o com ela podemos dar o nosso comando <code>pyinstaller --onefile --name Google --icon=google.ico main.py</code>
    Com esse código, transformamos o projeto em um arquivo executável com o nome de nossa escolha (no exemplo dado foi Google) e colocamos o icone de nossa preferência.</li>
</ul>
