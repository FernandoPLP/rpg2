print("Bem vindo ao jogo ao Calabouço da Morte")
print("Diga seu nome herói: ")
nomepersonagem = input (">")

print(f"Seja bem vindo {nomepersonagem}!")

print("Você spawno em Fang")
print("Vamos explorar esse mundo cheio de surpresa!")

print("No interior do labirinto escuro e sinuoso de Fang há horrores desconhecidos à sua espera. Concebido pela mente diabólica do Barão Sukumvit, o labirinto está infestado de armadilhas demoníacas e monstros sedentos de sangue, os quais submeterão suas habilidades a testes quase além do limite possível de resistência. Inúmeros aventureiros aceitaram o desafio da Prova dos Campeões e atravessaram a porta talhada em forma de boca do labirinto para nunca mais voltar. Aperte Enter caso você se atreva a entrar!")
enter = input(">")


if enter == "":
    print(f"Então, Sukumvit anunciou a primeira Prova dos Campeões. Emissários e editais divulgaram o desafio: 10 mil Peças de Ouro, e a libertação de Chiang Mai, para qualquer pessoa que sobrevivesse aos perigos do labirinto de Fang. No primeiro ano, 17 bravos guerreiros tentaram A CAMINHADA, como ficou mais tarde conhecida a prova. Ninguém retornou. Com o passar dos anos, a Prova dos Campeões atraía mais e mais desafiantes e espectadores. Fang prosperou e se preparava com meses de antecedência para o espetáculo que patrocinava a cada mês de maio. Acidade era decorada, contratavam-se músicos, dançarinos, comedores de fogo, ilusionistas e todo tipo de artistas, e se registravam as inscrições de indivíduos esperançosos que pretendiam realizar A CAMINHADA. Na última semana de abril, as pessoas de Fang e seus visitantes iniciavam uma desvairada comemoração. Cantavam, bebiam, dançavam e riam até o raiar do dia 12 de maio, quando a cidade se amontoava nos portões do labirinto para ver o primeiro desafiante do ano avançar para enfrentar a Prova dos Campeões.")
    print("Aperte enter para continuar")
    continar = input("")
    print("Tendo visto um dos comunicados de Sukumvit pregado em uma árvore, você resolve que este ano tentará A CAMNHADA. Durante os últimos cinco anos, você tem-se sentido atraído, não pelas recompensas, mas pelo simples fato de que ninguém até hoje conseguiu emergir vitorioso do labirinto. Você pretende fazer com que este seja o ano no qual um Campeão será coroado! Reunindo uns poucos pertences, você parte imediatamente. Dois dias de caminhada para o oeste levam-no à costa, onde você entra na maldita Port Blacksand. Sem perder tempo nessa cidade de ladrões, você compra sua passagem em um pequeno barco que veleja em direção ao norte, para a foz do rio Kok; de lá, você sobe o rio de jangada por quatro dias, até finalmente chegar a Fang.")
    print("Aperte enter para continuar")
    continar = input("")
    print("A Prova começa dentro de três dias, e a cidade está num clima quase histérico de excitação. Você faz sua inscrição e recebe um lenço roxo para amarrar em volta do braço, o qual informa a todos sua condição de candidato. Durante três dias, você goza da melhor hospitalidade de Fang, sendo tratado como um semideus. Durante a longa celebração, quase esquece seu propósito; mas, na noite anterior à Prova, a magnitude da tarefa à sua frente começa a dominar-lhe os pensamentos. Mais tarde, você é levado para um alojamento especial e conduzido a seu quarto. Há uma esplêndida cama de quatro colunas com lençóis de cetim para ajudá-lo a repousar. Mas há pouco tempo para dormir.")
    print("E assim começou-se a prova")
    print("Aperte enter para continuar")
    continar = input("")
    print("O clamor dos espectadores excitados some gradualmente atrás de você, que se aventura cada vez mais fundo na penumbra do túnel da caverna.")
    print("Grandes cristais pendem do teto do túnel a intervalos de 20 metros, irradiando uma luz suave, apenas suficiente para que se veja por onde anda. À medida que seus olhos vão pouco a pouco se acostumando à quase escuridão, você começa a ver movimentos à sua volta. Aranhas e besouros sobem e descem pelas paredes entalhadas, desaparecendo em frestas e gretas ao sentir sua aproximação; ratazanas e ratos correm pelo chão à sua frente. Pingos de água caem em pequenas poças com um sinistro som gotejante que ecoa pelo túnel. O ar é frio, úmido e pesado. Depois de caminhar lentamente pelo túnel por uns cinco minutos, você chega a uma mesa de pedra encostada contra a parede à sua esquerda. Nela há seis caixas, uma das quais tem o seu nome pintado na tampa. Se você quiser abrir a caixa. Se preferir continuar caminhando para o norte")
    print("Qual é sua escolha? (abrir caixa/continuar)")
    escolharota1 = input(">").lower()
    if escolharota1 == "abrir caixa":
        print("você escolheu abrir a caixa")
        print("A tampa da caixa sai facilmente. Dentro, você acha duas Peças de Ouro e um bilhete, escrito num pequeno pedaço de pergaminho, endereçado a você. Depois de colocar o ouro no bolso, você lê a mensagem: Muito bem. Pelo menos você tem o bom senso de parar e tirar proveito da ajuda simbólica que lhe é dada. Agora, posso avisá-lo da necessidade de encontrar e usar diversos itens, se espera sair-se bem no meu Calabouço da Morte. Assinado “Sukumvit.” Guardando de cor o aviso do bilhete, você o rasga em pequenos pedaços e continua para o norte pelo túnel.")
        print("Aperte enter para continuar")
        continar = input("")
        escolharota1 = "continuar"
    elif escolharota1 == "continuar":
        print("você esolheu continuar para o norte")
        print("Depois de caminhar pelo túnel por alguns minutos, você chega a uma encruzilhada. Uma seta branca pintada na parede aponta para o oeste. No chão, você vê pegadas molhadas, feitas por aqueles que entraram antes de você. É difícil ter certeza, mas parece que três deles seguiram a direção da seta, enquanto um resolveu ir para o leste.")
        print("Aperte enter para continuar")
        continar = input("")
        print("Qual é sua escolha ?(leste/oeste)")
        escolharota2 = input(">")
        if escolharota2 == "leste":
            print("você escolheu ir para o leste")
            print("Adiante, você pode ver um grande obstáculo no chão do túnel, embora esteja escuro demais para saber exatamente o que é. As pegadas molhadas que você vem seguindo continuam até a obstrução. Se você quiser continuar para o leste, volte para 56. Se preferir voltar para a encruzilhada e seguir para o oeste, vá para 293.")
            print("Faça sua escolha (leste/oeste):")
            escolharota3 = input(">").lower()
            if escolharota3 == "leste":
                print("Você vê que a obstrução é causada por um objeto grande e marrom, parecendo um rochedo. Você o toca com a mão e fica surpreso ao descobrir que é macio e esponjoso. Se você quiser tentar subir por cima dele, vá para 373. Se preferir cortá-lo ao meio com sua espada, vá para 215.")
                print("Faça sua escolha (subir/cortar)")
                escolharota4 = input(">").lower()
                if escolharota4 == "subir":
                    print("você escolheu subir")
                    print("Você sobe pelo rochedo macio, temendo ser absorvido por ele a qualquer momento. É difícil passar por cima da coisa, pois seus membros afundam na casca mole, mas, por fim, você consegue chegar ao outro lado. Aliviado por estar de novo em terreno firme, você se dirige para o leste. Volte para 13.")
                    print("Aperte enter para continuar")
                    continar = input("")    
                    escolharota4 = "leste"
                elif escolharota4 == "cortar":
                    print("você escolheu cortar")
                    print("Sua espada arrebenta facilmente a fina casca externa da gigantesca bola de esporos. Uma espessa nuvem de esporos saída da bola se espalha e o envolve. Alguns dos esporos grudam- se à sua pele, que começa a coçar terrivelmente. Aparecem grandes caroços no seu rosto e braços, e sua pele parece estar em fogo. Você perde 2 pontos de ENERGIA. Coçando freneticamente os caroços, você passa por cima da bola de esporos, agora murcha, e segue para o oeste. Volte para 13.")
                    print("Aperte enter para continuar")
                    continar = input("")    
                    escolharota4 = "leste"
                elif escolharota4 == "leste":
                    print()

            elif escolharota3 == "oeste":
                print("Seguindo os três pares de pegadas molhadas pela passagem oeste do túnel, você logo chega a uma encruzilhada. Se quiser continuar para o oeste, seguindo dois pares de pegadas, volte para 137. Se quiser se dirigir para o norte, seguindo o terceiro par de pegadas, vá para 387.")
            
        elif escolharota2 == "oeste":
            print("você escolheu ir para o oeste")
            print("Seguindo os três pares de pegadas molhadas pela passagem oeste do túnel, você logo chega a uma encruzilhada. Se quiser continuar para o oeste, seguindo dois pares de pegadas, volte para 137. Se quiser se dirigir para o norte, seguindo o terceiro par de pegadas, vá para 387.")
            print("Faça a sua escolha, deseja continuar para o oeste ou seguir para o norte?(oeste/norte)")
            escolharota5 = input(">").lower()
            if escolharota5 == "oeste":
                print("")


pagina = ""
if escoolharota == oeste:
    pagina == 137
if pagina == 137:
    print("ola")