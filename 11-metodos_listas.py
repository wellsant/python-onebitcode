gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]
print(gamesList)

# 1 - Tamanho da Lista 
print(len(gamesList))

# 2 - recuperar um item da Lista pelo índice
print(gamesList.index("Red Dead 2"))

# 3 - Adicionar item ao final da Lista 
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordenar a Lista
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("Star Wars")
print(gameReset)

# 6 - Remove todos os itens da Lista 
gamesList.clear()
print(gamesList)
