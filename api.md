# API Gallicagram

## Introduction
Pour le projet [Gallicagram](https://shiny.ens-paris-saclay.fr/app/gallicagram), nous avons téléchargé massivement 3 corpus :
* Les 3 millions de périodiques (numéros de presse) de Gallica, fiable entre 1789 et 1950
* Les 300 000 monographies (livres) de Gallica, fiable entre 1600 et 1940
* Les 3 millions d'articles des archives du quotidien Le Monde (décembre 1944-décembre 2022)

Pour l'application, nous avons constitué des bases de données dénombrant le nombre d'occurrences des mots et groupes de mots sur chaque corpus, sur chaque période. Ce sont ces mêmes bases que l'application utilise pour afficher ses graphes (s'il fallait compter à chaque fois les occurrences dans le corpus, cela prendait des semaines). Bref, nous avons fait des calculs interminables pour compter le nombre d'occurrences de chaque mot, et cette information pourrait être utile à d'autres. 
Ces bases de données étant trop vastes pour être téléchargeables (2 téras au total), nous les rendons interrogeables à travers cette API, qui vous envoie les données au format csv. Vous pouvez par exemple l'utiliser en insérant dans votre code R la ligne suivante:
``
tableau = read.csv("https://shiny.ens-paris-saclay.fr/guni/query?mot=patate")
``

Sinon, vous pouvez utiliser les packages R, python et Ruby (voir ci-dessous), qui sont des "wrappers" de cette API.
Nos bases sont en SQLite, et structurées avec les colonnes suivantes : n (nombre d'occurrences), gram (mot ou syntagme recherché), année, mois et jour (selon le corpus). Là où c'est nécessaire, elles sont doublées d'une structure fulltext (fts5), qui permet des interrogations plus complexes. L'API ajoute une colonne "total", qui donne le nombre total de mots ou groupes de mots de cette taille dans le corpus, sur chaque période. On peut donc calculer la fréquence en divisant la colonne "n" par la colonne "total".  Les bases ont été constituées légèrement différement selon le corpus :
* Le corpus "presse" a une résolution temporelle mensuelle, le corpus Le Monde une résolution journalière, le corpus "livres" une résolution annuelle.
* A cause de l'explosion combinatoire et des tailles inégales des  corpus, nous avons calculé jusqu'au 3gram pour le corpus "presse", 4gram pour Le Monde et 5gram pour le corpus "livres". Autrement dit, on pourra chercher "une belle patate" dans le corpus presse, mais pas "une très belle patate". 
* Dans les corpus Gallica (presse et livres), nous avons exclu toutes les lignes où n=1. Cela permettait de réduire massivement la taille de la base : l'océrisation étant imparfaite, l'immense majorité des lignes sont des erreurs d'OCR. Pas besoin dans Le Monde, où l'OCR a manifestement été relu et corrigé à la main.
* Notons que nous avons considéré l'apostrophe comme une lettre. 

## Nos 3 routes
Les bases de donnée peuvent être interrogées de 3 façons. Si en voyant la structure des données décrites ci-dessus, un autre mode vous vient à l'esprit, n'hésitez pas.

### 1 - Query
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950](https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950)
Une simple route pour obtenir le nombre d'occurrence de `mot` entre l'année `from` et l'année `to`, dans le `corpus` voulu (qui doit appartenir à "presse", "livres" et "lemonde"). Seul l'argument `mot` est nécessaire; par défaut on cherche dans le corpus "presse", entre 1789 et nos jours. 

### 2 - Contain
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/contain?corpus=lemonde&mot1=patate&mot2=une&from=2015&to=2022](https://shiny.ens-paris-saclay.fr/guni/contain?corpus=lemonde&mot1=patate&mot2=une&from=2015&to=2022&count=True)
Une sorte de mode co-occurrence proche : cette route vous compte le nombre de 3gram (4gram pour le corpus Le Monde) qui contiennent à la fois `mot1` et `mot2`. C'est en particulier utile pour étudier les stéréotypes ([exemple](https://regicid.github.io/masculinite_verbes.html)). 

Si ce qui vous intérese ce n'est pas les comptage mais de jeter un oeil aux bouts de textes qui contiennent ces deux mots (pour comprendre pourquoi deux mots sont associés dans la route `associated` décrite ci-dessous par exemple), vous pouvez glisser `count=False`. On vous retournera les 3 ou 4-gram (selon le corpus) datés.

### 3 - Joker
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/joker?mot=camarade&corpus=lemonde&from=1945&to=2022&n_joker=200](https://shiny.ens-paris-saclay.fr/guni/joker?mot=camarade&corpus=lemonde&from=1945&to=2022&n_joker=200&after=True&length=2)

Analogue à notre mode Joker sur l'application Gallicagram, inspiré de celui de Ngram Viewer. Vous renvoie ce qui suit (ou ce qui accompagne si `after=False`) le plus souvent `mot`, avec le nombre d'occurrences sur toute la période (`tot`). Par exemple, "camarade" est souvent suivi par "Staline" et "khrouchtchev" dans Le Monde. L'option `after`, activée par défaut, contraint à ne chercher que ce qui vient après le mot ("camarade \*") a. Si on la désactive, on obtient également les groupes de mots "\* camarade". Pour avoir ce qui précède le plus couramment (pas moyen de l'obtenir directement avec fts5), vous pouvez mettre un `n_joker` élevé (ou `n_joker=all`), `after=False` et exclure dans votre code toutes les formes "camarade \*". Avec `n_joker=all`, la route vous renvoie la totalité des jokers (attention aux gros dataframes, surtout sur les corpus gallica, où les erreurs d'OCR sont foison...).

Le paramètre `length` contrôle la taille des ngrams que vous cherchez. Concrètement, avec `length=2` on vous renverra "camarade de", avec `length=3` vous aurez par exemple accès à "camarade de chambre". La taille maximale est 3 sur les corpus Gallica et 4 sur Le Monde (à noter que length=3 produit des calculs interminables sur le corpus presse, qui atteignent parfois le timeout pour les mots fréquents, mais rien ne coûte d'essayer !).

Cette route fonctionne également avec des groupes de mots, dans la mesure des limites des bases de données : cette route est limitée à 2 mots pour les corpus "presse" et "livres" ([par exemple](https://shiny.ens-paris-saclay.fr/guni/joker?mot=le%20camarade&corpus=presse&from=1789&to=1950&n_joker=200&before=False)), et à 3 mots pour Le Monde. A noter que sur le corpus "presse", ce mode est très lent, car la base des 3gram est monumentale. Rappelons également l'exclusion susmentionnée des lignes où `n=1` dans les deux corpus Gallica, qui rend ce mode moins fiable pour les expressions rares.


Dans l'application, nous couplons cette fonctionnalité avec une [liste de "mots vides"](https://regicid.github.io/stopwords.csv), les mots les plus fréquents dans le corpus Gallica. Nous excluons autant de mots vides que l'utilisateur le désire (par défaut 500), puisqu'ils sont souvent peu instructifs ("camarade de" et "camarade qui" sont les plus fréquents, et on s'en fiche pas mal). Cette fonctionalité n'est pas implémentée pour l'instant. 

### 4 - Associated
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/associated?mot=changement%20climatique&corpus=lemonde&from=1945&to=2022&n_joker=200&length=4&stopwords=0](https://shiny.ens-paris-saclay.fr/guni/associated?mot=changement%20climatique&corpus=lemonde&from=1945&to=2022&n_joker=200&length=4&stopwords=0)
Crée sur une idée de [Vincent Bagilet](https://vincentbagilet.github.io/), cette route généralise la route Joker. Elle vous renvoie les mots le plus souvent associés à `mot`, dans un voisinage de `length`. Vous pouvez entrer un nombre de stopwords à ignorer, entre 0 et 1000 (avec `stopwords=500`, on ignorera les 500 mots les plus fréquents, la liste ayant été établie sur le corpus de livres). Cette route est probablement la plus utile, elle vous permet d'explorer l'environnement sémantique de mot, de distinguer selons ses acceptions, etc. Par exemple, Vincent Bagilet l'a utilisée pour quantifier combien on utilisait, au cours du temps, le mot "climatique" en termes d'action, de causes, de conséquences ou de problème.


## Librairies
### pyllicagram
Le package le plus abouti, car python c'est quand même vachement mieux que R (oui, Gallicagram est codé en R, j'en souffre suffisamment, pas besoin de me le rappeler... Fichue dépendance au sentier. Parenthèse fermée)

Le package contient trois fonctions correspondant aux trois routes, il est disponible ici : [https://github.com/regicid/pyllicagram](https://github.com/regicid/pyllicagram).

Pour l'installer : `pip install gallicagram` si vous êtes sur mac/linux. Si vous êtes sur Windows, j'en ai pas la moindre idée et c'est pas ma faute s'il y a encore des gens sur Windows.

### rallicagram
[Vincent Bagilet](https://vincentbagilet.github.io/) a développé ce magnifique package en R
[https://vincentbagilet.github.io/rallicagram/](https://vincentbagilet.github.io/rallicagram/). Comme Vincent est très très fort, il est aujourd'hui plus développé que pyllicagram, et mieux documenté. On va essayer de rattraper le retard.
### Gallicagram gem
Nicolas Roux a eu la bonté de développer une gem Ruby. Pour connaître son stade de devéloppement, rendez-vous sur [https://github.com/nicolrx/gallicagram](https://github.com/nicolrx/gallicagram)

### Autres langages
Si des bonnes volontés veulent développer des packages dans d'autres langages, qu'ils n'hésitent pas à m'envoyer un mail et je les ajouterai à la liste.
