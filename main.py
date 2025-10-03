"""Leecture de données d'un fichier csv"""
#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', newline="", encoding="utf-8") as f:
        r = csv.reader(f, delimiter = ';')
        l = [[int(x) for x in ligne] for ligne in r] # l'itérable est converti en liste
        return l

def get_list_k(data, k):
    """Renvoie la kième ligne de la liste data"""
    return data[k]

def get_first(l):
    """Renvoie la première ligne de la liste data"""
    return l[0]

def get_last(l):
    """Renvoie la dernière ligne de la liste data"""
    return l[-1]

def get_max(l):
    """Renvoie le maximum la liste data"""
    return max(l)

def get_min(l):
    """Renvoie le minimum la liste data"""
    return min(l)

def get_sum(l):
    """Renvoie la somme la liste data"""
    return sum(l)

#### Fonction principale


def main():
    """Fais des appels pour tester la fonction"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
