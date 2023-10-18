n = int(input("veuillez entrer un nombre entier:"))
for i in range (2, n):
    for j in range(2, i):
        if i % j == 0 :
            break 
    else:
        print(i,end=' ') # drna print(i, end=' ' ) pour les afficher sur la meme ligne 