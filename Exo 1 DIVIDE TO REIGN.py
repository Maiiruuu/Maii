def research(tableau): 
    if len(tableau) == 2: 
        if tableau[0] > tableau[1]:
            maximum = tableau[0]
            minimum = tableau[1]
        else: 
            maximum = tableau[1]
            minimum = tableau[0]
    elif len(tableau) == 1: 
        maximum = tableau[0]
        minimum = tableau[0]
    else: 
        maximum = max(tableau)
        minimum = min(tableau)
    return (minimum, maximum)

def divide_research(tableau_complet): 
    if len(tableau_complet) <= 2:
        return research(tableau_complet)

    centre = len(tableau_complet) // 2
    min_g, max_g = divide_research(tableau_complet[:centre])
    min_d, max_d = divide_research(tableau_complet[centre:])

    return research([min_g, max_g, min_d, max_d])

tab = [25, 36, 98, 12, 7, 32, 9, 1]
print(divide_research(tab))  # (1, 98) # complexité de log(n)
#EXERCICE 2 
def 