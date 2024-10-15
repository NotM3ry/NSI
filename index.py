def nb_solutions(score):
    if score == 0 or score == 3 or score == 6 or score == 5:
        return 1
    if score == 1 or score == 2 or score == 4:
        return 0
    return nb_solutions(score - 7) + nb_solutions(score - 5) + nb_solutions(score - 3)

print(nb_solutions(11))