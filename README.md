<h1>Keylogger-simple</h1>

<p>Este projeto é uma implementação básica de um keylogger, criado para <strong>fins educacionais</strong>. Ele demonstra como capturar eventos de teclas digitadas, cliques do mouse e capturas de tela em um sistema.</p>

<h2>Bibliotecas Necessárias</h2>

<p>Para começarmos a falar sobre o nosso keylogger, vamos abordar as bibliotecas necessárias para fazê-lo rodar corretamente. Abaixo estão listadas as bibliotecas e suas funções:</p>

<h3>Instalação rápida</h3>
<p>Para instalar todas as bibliotecas de uma vez, use o seguinte comando:</p>

Essênciais:
<pre><code>pip install pynput mss pyzipper</code></pre>

Por via das dúvidas:
<pre><code>pip install platform time datetime os subprocess</code></pre>

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
  <li><strong>platform</strong>: Essa biblioteca é essencial para que o programa funcione em diferentes sistemas operacionais. Ela identifica o SO da vítima e aplica soluções específicas para ocultar arquivos.</li>
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
<p>(Em construção)</p>
