from perso import * 


player1 = Personnage(
    name="gandalf",
    force=100,
    sante=1000,
    defense=200
)

player2 = Personnage(
    name="Loup",
    force=200,
    sante=1500,
    defense=0
)


player1.affiche_etat()
player2.affiche_etat()

player1.attaquer(player2)

player1.affiche_etat()
player2.affiche_etat()

player2.attaquer(player1)


player1.affiche_etat()
player2.affiche_etat()

player2.attaquer(player1)

player1.affiche_etat()
player2.affiche_etat()


    