# Keylogger-simple
Este projeto é uma implementação básica de um keylogger, criado para fins educacionais. Ele demonstra como capturar eventos de teclas digitadas, cliques de mouse e capturas de tela em um sistema.

Para começarmos a falar sobre o nosso keylogger, primeiro vamos abordar as bibliotecas necessárias para faze-lo rodar com perfeição. Dito isto, abaixo está listado as bibliotecas e o que elas fazem:

Teclado e mouse:

- pynput: Está biblioteca é capaz de Ouvir(Listener), Controlar(Controller) e Automatizar processos no seu mouse e no seu teclado. Como estamos fazendo um keylogger usaremos a função de Listener que nos ajuda a ouvir e registrar o que está sendo digitado (Usamos a função Key também para testes e fazer o programa parar). Com essa biblioteca, estamos caputando quando o nosso alvo pressionar e quando ele soltar a tecla. Também estamos registrando quando o nosso alvo pressioan/solta, coordenadas da tela de onde ele clicou e o botão que foi pressionado (Esquerdo ou Direito).
