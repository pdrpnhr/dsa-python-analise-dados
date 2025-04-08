import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():

    limpa_tela()
    pokemons = ['BULBASAUR','IVYSAUR','VENUSAUR','CHARMANDER','CHARMELEON','CHARIZARD','SQUIRTLE','WARTORTLE','BLASTOISE','CATERPIE','METAPOD','BUTTERFREE','WEEDLE','KAKUNA','BEEDRILL','PIDGEY','PIDGEOTTO','PIDGEOT','RATTATA','RATICATE','SPEAROW','FEAROW','EKANS','ARBOK','PIKACHU','RAICHU','SANDSHREW','SANDSLASH','NIDORAN','NIDORINA','NIDOQUEEN','NIDORINO','NIDOKING','CLEFAIRY','CLEFABLE','VULPIX','NINETALES','JIGGLYPUFF','WIGGLYTUFF','ZUBAT','GOLBAT','ODDISH','GLOOM','VILEPLUME','PARAS','PARASECT','VENONAT','VENOMOTH','DIGLETT','DUGTRIO','MEOWTH','PERSIAN','PSYDUCK','GOLDUCK','MANKEY','PRIMEAPE','GROWLITHE','ARCANINE','POLIWAG','POLIWHIRL','POLIWRATH','ABRA','KADABRA','ALAKAZAM','MACHOP','MACHOKE','MACHAMP','BELLSPROUT','WEEPINBELL','VICTREEBEL','TENTACOOL','TENTACRUEL','GEODUDE','GRAVELER','GOLEM','PONYTA','RAPIDASH','SLOWPOKE','SLOWBRO','MAGNEMITE','MAGNETON','FARFETCHD','DODUO','DODRIO','SEEL','DEWGONG','GRIMER','MUK','SHELLDER','CLOYSTER','GASTLY','HAUNTER','GENGAR','ONIX','DROWZEE','HYPNO','KRABBY','KINGLER','VOLTORB','ELECTRODE','EXEGGCUTE','EXEGGUTOR','CUBONE','MAROWAK','HITMONLEE','HITMONCHAN','LICKITUNG','KOFFING','WEEZING','RHYHORN','RHYDON','CHANSEY','TANGELA','KANGASKHAN','HORSEA','SEADRA','GOLDEEN','SEAKING','STARYU','STARMIE','MRMIME','SCYTHER','JYNX','ELECTABUZZ','MAGMAR','PINSIR','TAUROS','MAGIKARP','GYARADOS','LAPRAS','DITTO','EEVEE','VAPOREON','JOLTEON','FLAREON','PORYGON','OMANYTE','OMASTAR','KABUTO','KABUTOPS','AERODACTYL','SNORLAX','ARTICUNO','ZAPDOS','MOLTRES','DRATINI','DRAGONAIR','DRAGONITE','MEWTWO','MEW']
    tipos = {'BULBASAUR':'GRASS/POISON','IVYSAUR':'GRASS/POISON','VENUSAUR':'GRASS/POISON','CHARMANDER':'FIRE','CHARMELEON':'FIRE','CHARIZARD':'FIRE/FLYING','SQUIRTLE':'WATER','WARTORTLE':'WATER','BLASTOISE':'WATER','CATERPIE':'BUG','METAPOD':'BUG','BUTTERFREE':'BUG/FLYING','WEEDLE':'BUG/POISON','KAKUNA':'BUG/POISON','BEEDRILL':'BUG/POISON','PIDGEY':'NORMAL/FLYING','PIDGEOTTO':'NORMAL/FLYING','PIDGEOT':'NORMAL/FLYING','RATTATA':'NORMAL','RATICATE':'NORMAL','SPEAROW':'NORMAL/FLYING','FEAROW':'NORMAL/FLYING','EKANS':'POISON','ARBOK':'POISON','PIKACHU':'ELECTRIC','RAICHU':'ELECTRIC','SANDSHREW':'GROUND','SANDSLASH':'GROUND','NIDORAN':'POISON','NIDORINA':'POISON','NIDOQUEEN':'POISON/GROUND','NIDORINO':'POISON','NIDOKING':'POISON/GROUND','CLEFAIRY':'NORMAL','CLEFABLE':'NORMAL','VULPIX':'FIRE','NINETALES':'FIRE','JIGGLYPUFF':'NORMAL','WIGGLYTUFF':'NORMAL','ZUBAT':'POISON/FLYING','GOLBAT':'POISON/FLYING','ODDISH':'GRASS/POISON','GLOOM':'GRASS/POISON','VILEPLUME':'GRASS/POISON','PARAS':'BUG/GRASS','PARASECT':'BUG/GRASS','VENONAT':'BUG/POISON','VENOMOTH':'BUG/POISON','DIGLETT':'GROUND','DUGTRIO':'GROUND','MEOWTH':'NORMAL','PERSIAN':'NORMAL','PSYDUCK':'WATER','GOLDUCK':'WATER','MANKEY':'FIGHTING','PRIMEAPE':'FIGHTING','GROWLITHE':'FIRE','ARCANINE':'FIRE','POLIWAG':'WATER','POLIWHIRL':'WATER','POLIWRATH':'WATER/FIGHTING','ABRA':'PSYCHIC','KADABRA':'PSYCHIC','ALAKAZAM':'PSYCHIC','MACHOP':'FIGHTING','MACHOKE':'FIGHTING','MACHAMP':'FIGHTING','BELLSPROUT':'GRASS/POISON','WEEPINBELL':'GRASS/POISON','VICTREEBEL':'GRASS/POISON','TENTACOOL':'WATER/POISON','TENTACRUEL':'WATER/POISON','GEODUDE':'ROCK/GROUND','GRAVELER':'ROCK/GROUND','GOLEM':'ROCK/GROUND','PONYTA':'FIRE','RAPIDASH':'FIRE','SLOWPOKE':'WATER/PSYCHIC','SLOWBRO':'WATER/PSYCHIC','MAGNEMITE':'ELECTRIC','MAGNETON':'ELECTRIC','FARFETCHD':'NORMAL/FLYING','DODUO':'NORMAL/FLYING','DODRIO':'NORMAL/FLYING','SEEL':'WATER','DEWGONG':'WATER/ICE','GRIMER':'POISON','MUK':'POISON','SHELLDER':'WATER','CLOYSTER':'WATER/ICE','GASTLY':'GHOST/POISON','HAUNTER':'GHOST/POISON','GENGAR':'GHOST/POISON','ONIX':'ROCK/GROUND','DROWZEE':'PSYCHIC','HYPNO':'PSYCHIC','KRABBY':'WATER','KINGLER':'WATER','VOLTORB':'ELECTRIC','ELECTRODE':'ELECTRIC','EXEGGCUTE':'GRASS/PSYCHIC','EXEGGUTOR':'GRASS/PSYCHIC','CUBONE':'GROUND','MAROWAK':'GROUND','HITMONLEE':'FIGHTING','HITMONCHAN':'FIGHTING','LICKITUNG':'NORMAL','KOFFING':'POISON','WEEZING':'POISON','RHYHORN':'GROUND/ROCK','RHYDON':'GROUND/ROCK','CHANSEY':'NORMAL','TANGELA':'GRASS','KANGASKHAN':'NORMAL','HORSEA':'WATER','SEADRA':'WATER','GOLDEEN':'WATER','SEAKING':'WATER','STARYU':'WATER','STARMIE':'WATER/PSYCHIC','MRMIME':'PSYCHIC','SCYTHER':'BUG/FLYING','JYNX':'ICE/PSYCHIC','ELECTABUZZ':'ELECTRIC','MAGMAR':'FIRE','PINSIR':'BUG','TAUROS':'NORMAL','MAGIKARP':'WATER','GYARADOS':'WATER/FLYING','LAPRAS':'WATER/ICE','DITTO':'NORMAL','EEVEE':'NORMAL','VAPOREON':'WATER','JOLTEON':'ELECTRIC','FLAREON':'FIRE','PORYGON':'NORMAL','OMANYTE':'ROCK/WATER','OMASTAR':'ROCK/WATER','KABUTO':'ROCK/WATER','KABUTOPS':'ROCK/WATER','AERODACTYL':'ROCK/FLYING','SNORLAX':'NORMAL','ARTICUNO':'ICE/FLYING','ZAPDOS':'ELECTRIC/FLYING','MOLTRES':'FIRE/FLYING','DRATINI':'DRAGON','DRAGONAIR':'DRAGON','DRAGONITE':'DRAGON/FLYING','MEWTWO':'PSYCHIC','MEW':'PSYCHIC'}
    pokemon = random.choice(pokemons)
    letras_descobertas = ['_' for letra in pokemon]
    tentativas = 10
    letras_erradas = []
    print('\nQUEM É ESSE POKÉMON?')
    print('\nChute uma letra por vez, ou escreva o nome completo para tentar adivinhar em uma jogada.')
    print("\nDigite 'sobre' para saber mais sobre o jogo.")
    
    while tentativas > 0:
        
        print('\nQuem é esse Pokémon?\n')
        print(' '.join(letras_descobertas))
        print('\nTentativas restantes:',tentativas)
        print('\nTentativas erradas:',' '.join(letras_erradas))

        chute = input('Tentativa:',).upper()
        if len(chute)>1:
            if chute == 'TIPO':
                tipo_pkm = tipos[pokemon]
                print('\nO Pokémon é do tipo:',tipo_pkm)
                tentativas -= 2
            elif chute =='SOBRE':
                print("\nSOBRE O JOGO:\n- Apenas Pokémon da primeira geração\n- Nomes grafados em inglês\n- Nome e tipo dos Pokémon retirados do site https://pokemon.fandom.com/wiki/List_of_Generation_I_Pokémon\n- Se estiver com muita dificuldade, digite 'Lista' para ver a lista completa de Pokémon, ou teste pedir ao programa alguma informação sobre o Pokémon ;)")
            elif chute =='LISTA':
                print(pokemons)
            else:
                if chute in pokemons:
                    if chute == pokemon:
                        letras_descobertas = pokemon
                        print('\nParabéns, você ganhou! Esse Pokémon é o',pokemon)
                        break
                    else:
                        letras_erradas.append(chute)
                        tentativas -= 2
                        print('\nPokémon errado!')
                else:
                    print('\nComando não reconhecido.')

        if chute in pokemon:
            index = 0
            for letra in pokemon:
                if chute == letra:
                    letras_descobertas[index] = chute
                index += 1
        else:
                if len(chute)>1:
                    pass
                else:
                    if chute in letras_erradas:
                        print('\nEssa letra já foi descartada.\n')
                    else:
                        letras_erradas.append(chute)
                        tentativas -= 1
        if '_' not in letras_descobertas:
            print(' '.join(letras_descobertas))
            print('\nParabéns, você ganhou! Esse Pokémon é o',pokemon)
            break

    if '_' in letras_descobertas:
        print(' '.join(letras_descobertas))
        print('\nQue pena, você perdeu. Esse Pokémon é ',pokemon)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nJogo desenvolvido no módulo introdutório do curso de Python para Análise de Dados da DSA.\n")