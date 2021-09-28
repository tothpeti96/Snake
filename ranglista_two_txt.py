class rank:
    def __init__(self, pos, name, pont):
        self.pos = pos
        self.name = name
        self.pont = pont

def main(Name, Pont):

    nev_pont = []
    ranklist = []

    with open("ranglista_two_player.txt", "rt", encoding="utf-8") as f:
        for sor in f:
            hely_nev_pont = sor.split()
            nev_pont.append(((hely_nev_pont[1]),int((hely_nev_pont[2].rstrip("\n")))))


    if (Name, Pont) in nev_pont:
        return
    
    nev_pont.append((Name, Pont))

    for i in range(len(nev_pont)):
        min = nev_pont[i][1]
        min_idx = i
        for j in range(i+1, len(nev_pont)):
            if nev_pont[j][1] < min:
                min = nev_pont[j][1]
                min_idx = j

        temp = nev_pont[i]
        nev_pont[i] = nev_pont[min_idx]
        nev_pont[min_idx] = temp

    nev_pont.reverse()
    last_point = 0
    helyezes = 0

    for i in range(len(nev_pont)):

        if nev_pont[i][1] == last_point:
            helyezes = helyezes
        else:
            helyezes += 1

        ranklist.append(rank(helyezes, nev_pont[i][0], nev_pont[i][1]))
        last_point = nev_pont[i][1]

    open("ranglista_two_player.txt", "w").close()

    f = open("ranglista_two_player.txt", "wt", encoding="utf-8")

    for i in range(len(ranklist)):
        f.write("{}. {} {}\n".format(ranklist[i].pos, ranklist[i].name, ranklist[i].pont))
    f.close()
