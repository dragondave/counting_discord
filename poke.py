# coding=utf-8
pokedata = """#001 	#001 	Bulbasaur 	Bulbasaur 	Grass 	Poison
#002 	#002 	Ivysaur 	Ivysaur 	Grass 	Poison
#003 	#003 	Venusaur 	Venusaur 	Grass 	Poison
#004 	#004 	Charmander 	Charmander 	Fire
#005 	#005 	Charmeleon 	Charmeleon 	Fire
#006 	#006 	Charizard 	Charizard 	Fire 	Flying
#007 	#007 	Squirtle 	Squirtle 	Water
#008 	#008 	Wartortle 	Wartortle 	Water
#009 	#009 	Blastoise 	Blastoise 	Water
#010 	#010 	Caterpie 	Caterpie 	Bug
#011 	#011 	Metapod 	Metapod 	Bug
#012 	#012 	Butterfree 	Butterfree 	Bug 	Flying
#013 	#013 	Weedle 	Weedle 	Bug 	Poison
#014 	#014 	Kakuna 	Kakuna 	Bug 	Poison
#015 	#015 	Beedrill 	Beedrill 	Bug 	Poison
#016 	#016 	Pidgey 	Pidgey 	Normal 	Flying
#017 	#017 	Pidgeotto 	Pidgeotto 	Normal 	Flying
#018 	#018 	Pidgeot 	Pidgeot 	Normal 	Flying
#019 	#019 	Rattata 	Rattata 	Normal
  	#019 	Rattata 	Rattata 	Dark 	Normal
#020 	#020 	Raticate 	Raticate 	Normal
  	#020 	Raticate 	Raticate 	Dark 	Normal
#021 	#021 	Spearow 	Spearow 	Normal 	Flying
#022 	#022 	Fearow 	Fearow 	Normal 	Flying
#023 	#023 	Ekans 	Ekans 	Poison
#024 	#024 	Arbok 	Arbok 	Poison
#025 	#025 	Pikachu 	Pikachu 	Electric
#026 	#026 	Raichu 	Raichu 	Electric
  	#026 	Raichu 	Raichu 	Electric 	Psychic
#027 	#027 	Sandshrew 	Sandshrew 	Ground
  	#027 	Sandshrew 	Sandshrew 	Ice 	Steel
#028 	#028 	Sandslash 	Sandslash 	Ground
  	#028 	Sandslash 	Sandslash 	Ice 	Steel
#030 	#030 	Nidorina 	Nidorina 	Poison
#031 	#031 	Nidoqueen 	Nidoqueen 	Poison 	Ground
#030 	#030 	Nidorina 	Nidorina 	Poison
#033 	#033 	Nidorino 	Nidorino 	Poison
#034 	#034 	Nidoking 	Nidoking 	Poison 	Ground
#035 	#035 	Clefairy 	Clefairy 	Fairy
#036 	#036 	Clefable 	Clefable 	Fairy
#037 	#037 	Vulpix 	Vulpix 	Fire
  	#037 	Vulpix 	Vulpix 	Ice
#038 	#038 	Ninetales 	Ninetales 	Fire
  	#038 	Ninetales 	Ninetales 	Ice 	Fairy
#039 	#039 	Jigglypuff 	Jigglypuff 	Normal 	Fairy
#040 	#040 	Wigglytuff 	Wigglytuff 	Normal 	Fairy
#041 	#041 	Zubat 	Zubat 	Poison 	Flying
#042 	#042 	Golbat 	Golbat 	Poison 	Flying
#043 	#043 	Oddish 	Oddish 	Grass 	Poison
#044 	#044 	Gloom 	Gloom 	Grass 	Poison
#045 	#045 	Vileplume 	Vileplume 	Grass 	Poison
#046 	#046 	Paras 	Paras 	Bug 	Grass
#047 	#047 	Parasect 	Parasect 	Bug 	Grass
#048 	#048 	Venonat 	Venonat 	Bug 	Poison
#049 	#049 	Venomoth 	Venomoth 	Bug 	Poison
#050 	#050 	Diglett 	Diglett 	Ground
  	#050 	Diglett 	Diglett 	Ground 	Steel
#051 	#051 	Dugtrio 	Dugtrio 	Ground
  	#051 	Dugtrio 	Dugtrio 	Ground 	Steel
#052 	#052 	Meowth 	Meowth 	Normal
  	#052 	Meowth 	Meowth 	Dark
  	#052 	Meowth 	Meowth 	Steel
#053 	#053 	Persian 	Persian 	Normal
  	#053 	Persian 	Persian 	Dark
#054 	#054 	Psyduck 	Psyduck 	Water
#055 	#055 	Golduck 	Golduck 	Water
#056 	#056 	Mankey 	Mankey 	Fighting
#057 	#057 	Primeape 	Primeape 	Fighting
#058 	#058 	Growlithe 	Growlithe 	Fire
#059 	#059 	Arcanine 	Arcanine 	Fire
#060 	#060 	Poliwag 	Poliwag 	Water
#061 	#061 	Poliwhirl 	Poliwhirl 	Water
#062 	#062 	Poliwrath 	Poliwrath 	Water 	Fighting
#063 	#063 	Abra 	Abra 	Psychic
#064 	#064 	Kadabra 	Kadabra 	Psychic
#065 	#065 	Alakazam 	Alakazam 	Psychic
#066 	#066 	Machop 	Machop 	Fighting
#067 	#067 	Machoke 	Machoke 	Fighting
#068 	#068 	Machamp 	Machamp 	Fighting
#069 	#069 	Bellsprout 	Bellsprout 	Grass 	Poison
#070 	#070 	Weepinbell 	Weepinbell 	Grass 	Poison
#071 	#071 	Victreebel 	Victreebel 	Grass 	Poison
#072 	#072 	Tentacool 	Tentacool 	Water 	Poison
#073 	#073 	Tentacruel 	Tentacruel 	Water 	Poison
#074 	#074 	Geodude 	Geodude 	Rock 	Ground
  	#074 	Geodude 	Geodude 	Rock 	Electric
#075 	#075 	Graveler 	Graveler 	Rock 	Ground
  	#075 	Graveler 	Graveler 	Rock 	Electric
#076 	#076 	Golem 	Golem 	Rock 	Ground
  	#076 	Golem 	Golem 	Rock 	Electric
#077 	#077 	Ponyta 	Ponyta 	Fire
  	#077 	Ponyta 	Ponyta 	Psychic
#078 	#078 	Rapidash 	Rapidash 	Fire
  	#078 	Rapidash 	Rapidash 	Psychic 	Fairy
#079 	#079 	Slowpoke 	Slowpoke 	Water 	Psychic
  	#079 	Slowpoke 	Slowpoke 	Psychic
#080 	#080 	Slowbro 	Slowbro 	Water 	Psychic
  	#080 	Slowbro 	Slowbro 	Poison 	Psychic
#081 	#081 	Magnemite 	Magnemite 	Electric 	Steel
#082 	#082 	Magneton 	Magneton 	Electric 	Steel
#083 	#083 	Farfetch'd 	Farfetch'd 	Normal 	Flying
  	#083 	Farfetch'd 	Farfetch'd 	Fighting
#084 	#084 	Doduo 	Doduo 	Normal 	Flying
#085 	#085 	Dodrio 	Dodrio 	Normal 	Flying
#086 	#086 	Seel 	Seel 	Water
#087 	#087 	Dewgong 	Dewgong 	Water 	Ice
#088 	#088 	Grimer 	Grimer 	Poison
  	#088 	Grimer 	Grimer 	Poison 	Dark
#089 	#089 	Muk 	Muk 	Poison
  	#089 	Muk 	Muk 	Poison 	Dark
#090 	#090 	Shellder 	Shellder 	Water
#091 	#091 	Cloyster 	Cloyster 	Water 	Ice
#092 	#092 	Gastly 	Gastly 	Ghost 	Poison
#093 	#093 	Haunter 	Haunter 	Ghost 	Poison
#094 	#094 	Gengar 	Gengar 	Ghost 	Poison
#095 	#095 	Onix 	Onix 	Rock 	Ground
#096 	#096 	Drowzee 	Drowzee 	Psychic
#097 	#097 	Hypno 	Hypno 	Psychic
#098 	#098 	Krabby 	Krabby 	Water
#099 	#099 	Kingler 	Kingler 	Water
#100 	#100 	Voltorb 	Voltorb 	Electric
#101 	#101 	Electrode 	Electrode 	Electric
#102 	#102 	Exeggcute 	Exeggcute 	Grass 	Psychic
#103 	#103 	Exeggutor 	Exeggutor 	Grass 	Psychic
  	#103 	Exeggutor 	Exeggutor 	Grass 	Dragon
#104 	#104 	Cubone 	Cubone 	Ground
#105 	#105 	Marowak 	Marowak 	Ground
  	#105 	Marowak 	Marowak 	Fire 	Ghost
#106 	#106 	Hitmonlee 	Hitmonlee 	Fighting
#107 	#107 	Hitmonchan 	Hitmonchan 	Fighting
#108 	#108 	Lickitung 	Lickitung 	Normal
#109 	#109 	Koffing 	Koffing 	Poison
#110 	#110 	Weezing 	Weezing 	Poison
  	#110 	Weezing 	Weezing 	Poison 	Fairy
#111 	#111 	Rhyhorn 	Rhyhorn 	Ground 	Rock
#112 	#112 	Rhydon 	Rhydon 	Ground 	Rock
#113 	#113 	Chansey 	Chansey 	Normal
#114 	#114 	Tangela 	Tangela 	Grass
#115 	#115 	Kangaskhan 	Kangaskhan 	Normal
#116 	#116 	Horsea 	Horsea 	Water
#117 	#117 	Seadra 	Seadra 	Water
#118 	#118 	Goldeen 	Goldeen 	Water
#119 	#119 	Seaking 	Seaking 	Water
#120 	#120 	Staryu 	Staryu 	Water
#121 	#121 	Starmie 	Starmie 	Water 	Psychic
#122 	#122 	Mr. Mime 	Mr. Mime 	Psychic 	Fairy
  	#122 	Mr. Mime 	Mr. Mime 	Ice 	Psychic
#123 	#123 	Scyther 	Scyther 	Bug 	Flying
#124 	#124 	Jynx 	Jynx 	Ice 	Psychic
#125 	#125 	Electabuzz 	Electabuzz 	Electric
#126 	#126 	Magmar 	Magmar 	Fire
#127 	#127 	Pinsir 	Pinsir 	Bug
#128 	#128 	Tauros 	Tauros 	Normal
#129 	#129 	Magikarp 	Magikarp 	Water
#130 	#130 	Gyarados 	Gyarados 	Water 	Flying
#131 	#131 	Lapras 	Lapras 	Water 	Ice
#132 	#132 	Ditto 	Ditto 	Normal
#133 	#133 	Eevee 	Eevee 	Normal
#134 	#134 	Vaporeon 	Vaporeon 	Water
#135 	#135 	Jolteon 	Jolteon 	Electric
#136 	#136 	Flareon 	Flareon 	Fire
#137 	#137 	Porygon 	Porygon 	Normal
#138 	#138 	Omanyte 	Omanyte 	Rock 	Water
#139 	#139 	Omastar 	Omastar 	Rock 	Water
#140 	#140 	Kabuto 	Kabuto 	Rock 	Water
#141 	#141 	Kabutops 	Kabutops 	Rock 	Water
#142 	#142 	Aerodactyl 	Aerodactyl 	Rock 	Flying
#143 	#143 	Snorlax 	Snorlax 	Normal
#144 	#144 	Articuno 	Articuno 	Ice 	Flying
  	#144 	Articuno 	Articuno 	Psychic 	Flying
#145 	#145 	Zapdos 	Zapdos 	Electric 	Flying
  	#145 	Zapdos 	Zapdos 	Fighting 	Flying
#146 	#146 	Moltres 	Moltres 	Fire 	Flying
  	#146 	Moltres 	Moltres 	Dark 	Flying
#147 	#147 	Dratini 	Dratini 	Dragon
#148 	#148 	Dragonair 	Dragonair 	Dragon
#149 	#149 	Dragonite 	Dragonite 	Dragon 	Flying
#150 	#150 	Mewtwo 	Mewtwo 	Psychic
#151 	#151 	Mew 	Mew 	Psychic"""

# issue: 29 Nidoran_female; 32 Nidoran_male

pokemon_dict = {}
for line in pokedata.split("\n"):
    row = line.split("\t")
    pokemon_dict[row[2].strip().lower()] = (int(row[1].strip("# ")))

pokemon_dict["nidoran♀"] = 29
pokemon_dict["nidoran♂"] = 32
pokemon_dict["missingno"] = 0
pokemon_dict["missing_no"] = 0

def pokemon(s):
    try:
        return pokemon_dict[s.lower()]
    except KeyError:
        return False

if __name__ == "__main__":
    print (pokemon("pikachu"))
    print (pokemon("lapras"))
    print (pokemon("nidoran♀"))
    print (pokemon("missingno"))
