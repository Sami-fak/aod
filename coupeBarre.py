from time import time

def memoize(p,n):
    """
    p est le tableau des prix
    n est la longueur de la barre de départ
    """
    # on initialise le tableau des gains à -1.
    g = [-1 for _ in range(n+1)]
    g[0] = 0
    # on initialise le tableau des choix optimaux a 1 
    # cela correspond a une barre non coupee.
    choix_opt = [[] for _ in range(n)]
    return couperBarreMemo(p,n-1,g, choix_opt), choix_opt, g

def couperBarreMemo(p,n,g, choix_opt):
    """
    Découpe récursivement la barre en deux avec mémoisation.
    """
    # On a déjà calculé le gain pour cette longueur.
    if g[n] != -1:
        return g[n]
    # Une barre de taille 0 rapporte un gain nul.
    if n == 0:
        res = 0
        res_opt = 0
    # Sinon, on calcule la solution au sous-problème et on stocke le résultat dans le tableau des gains.
    else:
        res = 0
        aux = 0
        res_opt = 0
        for i in range(n+1):
            aux = p[i] + couperBarreMemo(p, n-i-1, g, choix_opt)
            if (aux>res):
                res = aux
                res_opt = i+1
    choix_opt[n].append(res_opt)
    choix_opt[n].append(n+1-res_opt)
    g[n] = res
    return res

def couperBarreBottomUp(p,n):
    """
    Bottom up implementation.
    """
    # On initialise le tableau des gains à -1.
    g = [-1 for _ in range(n+1)]
    g[0] = 0
    # On initialise le tableau des choix optimaux
    # On y mettra les longueurs de la premiere barre a couper.
    s = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        res = 0
        for j in range(i):
            if (res<p[j] + g[i-j-1]):
                res = p[j] + g[i-j-1]
                s[i] = j+1
        g[i] = res
    return g[n], s

def couperBarreNaif(p,n):
    if n==0:
        return 0
    res = 0
    for i in range(1, n):
        res = max(res, p[i] + couperBarreNaif(p,n-i-1))
    return res

if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    g = memoize(p,len(p))
    print(f" - Gain maximal pour les prix {p} : {g[0]}.\n - Tableau des gains : {g[2]}.\n - Tableau des longueurs de barres optimales pour obtenir le gain maximum : {g[1]} ") # 30

    print("\n\n--- Bottom up --- \n")
    print(f" - Gain maximal pour les prix {p} : {couperBarreBottomUp(p,len(p))}.") 

    print("\n\n--- Comparaison temps bottom Up et  Naif --- \n")
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 25, 31, 34, 41, 45, 55, 60, 63, 64, 62, 69, 70, 77, 78, 80, 90, 99, 93, 100]
    t = time()
    print(f" - Temps Bottom up : \n") 
    couperBarreBottomUp(p,len(p))
    print(f"    {time()-t} s\n")

    t = time()
    print(f" - Temps Naif : \n")
    couperBarreNaif(p,len(p))
    print(f"    {time()-t} s")