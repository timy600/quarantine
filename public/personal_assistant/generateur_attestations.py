"""Definir les variables""" 

# Les infos de la personne consernée
name = "Felix"
birthday = ""
birthplace = "Paris 75000"
residence = "10 rue ... , 75010 Paris"

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

# Date
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

# créer un fichier, ou écraser le précedent
with open("nouvelle_attestation.txt", "w") as fichier:
    fichier.write("Attestation de déplacement\n")

# ouvrir un document
with open("nouvelle_attestation.txt", "a") as fichier:
    fichier.write("\nJe soussigné:\n")
    fichier.write(name)
    fichier.write("\nné le: ")
    fichier.write(birthday)
    fichier.write("\nné à: ")
    fichier.write(birthplace)

"""
with open("nouvelle_attestation.txt", "r") as fichier:
    content = fichier.read()
    print(content)
"""
