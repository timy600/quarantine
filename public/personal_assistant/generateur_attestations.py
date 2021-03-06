"""
Voici un exemple pour apprendre à générer tes propres attestations de déplacement.
Pour appeler ce programme, il faut le lancer dans le terminal (ton PowerShell) avec la commande suivante:
>py generateur_attestation
La liste des motifs se déroulera, il faudra choisir un des motifs.
L'attestation sera générée en format .txt
"""

""" 0: Importer les modules nécessaires"""
# Normalement les modules sont tous importés au début de ton code.
# Nous allons commencé par les découvrir au fur et à mesure,
# puis tous les regrouper ici

""" 1: Definir les variables"""
#Les infos de la personne consernée
name = "Felix"
birthday = ""
birthplace = "Paris 75000"
residence = "10 rue ... , 75010 Paris"

""" 2: Dont les dictionnaires (ce serait la partie pour télécharger les données)"""
# Créer la liste avec les motifs de sortie
motifs_dict = [
    "Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle, lorsqu'ils sont indispensables à l'exercice d’activités ne pouvant être organisées sous forme de télétravail ou déplacements professionnels ne pouvant être différés.",
    "Déplacements pour effectuer des achats de fournitures nécessaires à l’activité professionnelle et des achats de première nécessité dans des établissements dont les activités demeurent autorisées.",
    "Consultations et soins ne pouvant être assurés à distance et ne pouvant être différés ; consultations et soins des patients atteints d'une affection de longue durée.",
    "Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables ou la garde d’enfants.",
    "Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.",
    "Convocation judiciaire ou administrative.",
    "Participation à des missions d’intérêt général sur demande de l’autorité administrative."
]

# Modifier la liste en dictionnaire
motifs_dict = {
    "professionnel": "Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle, lorsqu'ils sont indispensables à l'exercice d’activités ne pouvant être organisées sous forme de télétravail ou déplacements professionnels ne pouvant être différés.",
    "achats": "Déplacements pour effectuer des achats de fournitures nécessaires à l’activité professionnelle et des achats de première nécessité dans des établissements dont les activités demeurent autorisées.",
    "docteur": "Consultations et soins ne pouvant être assurés à distance et ne pouvant être différés ; consultations et soins des patients atteints d'une affection de longue durée.",
    "familial": "Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables ou la garde d’enfants.",
    "bref": "Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.",
    "judiciaire": "Convocation judiciaire ou administrative.",
    "mission d'intérêt" : "Participation à des missions d’intérêt général sur demande de l’autorité administrative."
}

""" 3: Autre type de données spécifiques: les dates"""
from datetime import date, datetime
excursion_day = date.today()
excursion_day_and_hour = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

"""
# arrondir à 5 minutes
from datetime import timedelta
tm = datetime.now()
tm = tm - datetime.timedelta(minutes=tm.minute % 10,
                             seconds=tm.second,
                             microseconds=tm.microsecond)

# other option:
tm += datetime.timedelta(minutes=5)
tm -= datetime.timedelta(minutes=tm.minute % 10,
                         seconds=tm.second,
                         microseconds=tm.microsecond)
"""

""" 4: Demander inputs (les entrées)"""
print("Voici les motifs: choisissez en un:")
for x in motifs_dict:
    print(x)

# Ajouter des input pour le choix de paragraphe
choix = input()

""" 5: Vérifier les inputs"""
if choix in motifs_dict:
    print("OK!!!!!!!!!!!!!")
else:
    choix = "bref"

""" 6: La gestion du document"""
# créer un fichier, ou écraser le précedent
with open("nouvelle_attestation.txt", "w") as fichier:
    fichier.write("Attestation de déplacement\n")

# ouvrir un document
with open("nouvelle_attestation.txt", "a") as fichier:
    fichier.write("\nJe soussigné:\n")
    fichier.write(name)
    fichier.write("\nNé le: ")
    fichier.write(birthday)
    fichier.write("\nNé à: ")
    fichier.write(birthplace)
    fichier.write("\n\n")
    fichier.write("certifie que mon déplacement est lié au motif suivant autorisé par l’article 3 du décret du 23 mars 2020 prescrivant les mesures générales nécessaires pour faire face à l’épidémie de Covid19 dans le cadre de l’état d’urgence sanitaire:\n")
    fichier.write(motifs_dict[choix])

"""
with open("nouvelle_attestation.txt", "r") as fichier:
    content = fichier.read()
    print(content)
"""


"""
Note: pour créer un document Word de la suite office, il faudrait que tu passes une librairie: Docx
Puis écrire la ligne suivante pour bosser sur le document:
from docx import Document
"""
