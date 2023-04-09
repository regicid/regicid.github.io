# API Gallicagram
Pour le projet [Gallicagram](https://shiny.ens-paris-saclay.fr/app/gallicagram), nous avons téléchargé massivement 3 corpus :
* Les 3 millions de périodiques (numéros de presse) de Gallica, fiable entre 1789 et 1950
* Les 300 000 monographies (livres) de Gallica, fiable entre 1600 et 1940
* Les 3 millions d'articles des archives du quotidien Le Monde (décembre 1944-décembre 2022)

Pour les besoins du site, nous avons constitué des bases de données dénombrant le nombre d'occurrences des mots et groupes de mots sur chaque corpus, sur chaque période. Ces bases de données étant trop vastes pour être téléchargeables (2 téras au total), nous les rendons interrogeables à travers cette API, qui vous envoie les données au format csv. Vous pouvez l'utiliser (par exemple en insérant dans votre code R la ligne suivante:
``
tableau = read.csv("https://shiny.ens-paris-saclay.fr/guni/query?mot=patate")
``

Les bases sont structurées avec les colonnes suivantes : n (nombre d'occurrences, gram (mot ou syntagme recherché), année, mois et jour (selon le corpus). Les bases ont été constituées légèrement différement selon le corpus :
* Le corpus "presse" a une résolution temporelle mensuelle, le corpus Le Monde une résolution journalière, le corpus "livres" une résolution annuelle.
* A cause de l'explosion combinatoire et des tailles inégales des différentes corpus, nous avons calculé jusqu'au 3gram pour le corpus "presse", 4gram pour Le Monde et 5gram pour le corpus "livres". Autrement dit, on pourra chercher "une belle patate" dans le corpus presse, mais pas "une très belle patate". 
* Dans les corpus Gallica (presse et livres), nous avons exclu toutes les lignes où n=1. Cela permettait de réduire massivement la taille de la base : l'océrisation étant imparfaite, l'immense majorité des lignes sont des erreurs d'OCR. Pas besoin dans Le Monde, où l'OCR a manifestement été relu et corrigé à la main.
* A noter aussi que nous avons considéré l'apostrophe comme une lettre. 

## Routes
### Query
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950](https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950)
Une simple route pour obtenir le nombre d'occurrence de `mot` entre l'année `from` et l'année `to`, dans le `corpus` voulu (qui doit appartenir à "presse", "livres" et "lemonde"). Seul l'argument `mot` est nécessaire; par défaut on cherche dans le corpus "presse", entre 1789 et nos jours. 

### Contain

Une sorte de mode co-occurrence

