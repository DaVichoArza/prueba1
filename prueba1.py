meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
while True:
    word = input("¿que palabra moderna no logras comprender?")
    if word in meme_dict.keys():
        print("el significado de esta palabra es:", meme_dict[word])
    else:
        print("¡Wow! te inventaste otra palabra. esa no la tenemos registrada.")
        x = input("¿Quieres agregarle algun significado a esa palabra?")
    if x == "si":
        y = input("¿Que significado tiene?")
        meme_dict.append(word)
        meme_dict[word].append(y)


