# API Gallicagram

## Introduction
Pour le projet [Gallicagram](https://shiny.ens-paris-saclay.fr/app/gallicagram), nous avons téléchargé massivement plusieurs corpus :
* Les 3 millions de périodiques (numéros de presse) de Gallica, fiable entre 1789 et 1950
* Les 300 000 monographies (livres) de Gallica, fiable entre 1600 et 1940
* Les 3 millions d'articles des archives du quotidien Le Monde (décembre 1944-décembre 2022)
* Le gros million de documents du Zeitungsportal, qui regroupe les archives de presse de la Deutsche Digitale Bibliothek, équivalent (en moins bien) de Gallica outre-Rhin. 
* Un certain nombre de journaux de Gallica, voire ci-dessous.

|Titre                         |Période (conseillée)      |Volume (en mots)|Code API          |Longueur max|Résolution                    |Seuils                 |
|------------------------------|--------------------------|----------------|------------------|------------|------------------------------|-----------------------|
|Le Monde                      |1944-2023                 |1,5 milliards   |lemonde           |4gram       |Journalière                   |Aucun                  |
|Presse de Gallica             |1789-1950                 |57 milliards    |presse            |3gram       |Mensuelle                     |2gram>1,3gram>1        |
|Livres de Gallica             |1600-1940                 |16 milliards    |livres            |5gram       |Annuelle                      |2gram>1, etc           |
|Deutsches Zeitungsportal (DDB)|1780-1950                 |39 milliards    |ddb               |2gram       |Mensuelle                     |1gram > 1, 2gram>2     |
|American Stories              |1798-1963                 |20 milliards    |american_stories  |3gram       |Annuelle (mensuelle à venir ?)|1gram>1,2gram>2,3gram>3|
|Journal de Paris              |1777-1827                 |86 millions     |paris             |2gram       |Journalière                   |2gram>1                |
|Moniteur Universel            |1789-1869                 |511 millions    |moniteur          |2gram       |Journalière                   |2gram>1                |
|Journal des Débats            |1789-1944                 |1,2 milliards   |journal_des_debats|1gram       |Journalière                   |Aucun                  |
|La Presse                     |1836-1869                 |253 millions    |la_presse         |2gram       |Journalière                   |2gram>1                |
|Le Constitutionnel            |1821-1913 (très lacunaire)|64 millions     |constitutionnel   |2gram       |Journalière                   |2gram>1                |
|Le Figaro                     |1854-1952                 |870 millions    |figaro            |2gram       |Journalière                   |2gram>1                |
|Le Temps                      |1861-1942                 |1 milliard      |temps             |2gram       |Journalière                   |2gram>1                |
|Le Petit Journal              |1863-1942                 |745 millions    |petit_journal     |2gram       |Journalière                   |2gram>1                |
|Le Petit Parisien             |1876-1944                 |631 millions    |petit_parisien    |2gram       |Journalière                   |2gram>1                |
|L’Humanité                    |1904-1952                 |318 millions    |huma              |2gram       |Journalière                   |2gram>1                |
|Opensubtitles (français)      |1935-2020                 |17 millions     |subtitles        |3gram       |Annuelle                      |Aucun                  |
|Opensubtitles (anglais)       |1930-2020                 |102 millions    |subtitles_en      |3gram       |Annuelle                      |Aucun                  |



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

## Nos 7 routes
Les bases de donnée peuvent être interrogées de 7 façons. Si en voyant la structure des données décrites ci-dessus, un autre mode vous vient à l'esprit, n'hésitez pas.

### 1 - Query
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950](https://shiny.ens-paris-saclay.fr/guni/query?mot=patate&corpus=presse&from=1789&to=1950)
Une simple route pour obtenir le nombre d'occurrence de `mot` entre l'année `from` et l'année `to`, dans le `corpus` voulu (qui doit appartenir à "presse", "livres" et "lemonde"). Seul l'argument `mot` est nécessaire; par défaut on cherche dans le corpus "presse", entre 1789 et nos jours. 

### 2 - Contain
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/contain?corpus=lemonde&mot1=patate&mot2=une&from=2015&to=2022](https://shiny.ens-paris-saclay.fr/guni/contain?corpus=lemonde&mot1=patate&mot2=une&from=2015&to=2022&count=True)
Une sorte de mode co-occurrence proche : cette route vous compte le nombre de 3gram (4gram pour le corpus Le Monde) qui contiennent à la fois `mot1` et `mot2`. C'est en particulier utile pour étudier les stéréotypes ([exemple](https://regicid.github.io/masculinite_verbes.html)). 

Si ce qui vous intérese ce n'est pas les comptage mais de jeter un oeil aux bouts de textes qui contiennent ces deux mots (pour comprendre pourquoi deux mots sont associés dans la route `associated` décrite ci-dessous par exemple), vous pouvez glisser `count=False`. On vous retournera les 3 ou 4-gram (selon le corpus) comptés et datés.

### 3 - Joker
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/joker?mot=camarade&corpus=lemonde&from=1945&to=2022&n_joker=200](https://shiny.ens-paris-saclay.fr/guni/joker?mot=camarade&corpus=lemonde&from=1945&to=2022&n_joker=200&after=True&length=2)

Analogue à notre mode Joker sur l'application Gallicagram, inspiré de celui de Ngram Viewer. Vous renvoie ce qui suit (ou ce qui accompagne si `after=False`) le plus souvent `mot`, avec le nombre d'occurrences sur toute la période (`tot`). Par exemple, "camarade" est souvent suivi par "Staline" et "khrouchtchev" dans Le Monde. L'option `after`, activée par défaut, contraint à ne chercher que ce qui vient après le mot ("camarade \*") a. Si on la désactive, on obtient également les groupes de mots "\* camarade". Pour avoir ce qui précède le plus couramment (pas moyen de l'obtenir directement avec fts5), vous pouvez mettre un `n_joker` élevé (ou `n_joker=all`), `after=False` et exclure dans votre code toutes les formes "camarade \*". Avec `n_joker=all`, la route vous renvoie la totalité des jokers (attention aux gros dataframes, surtout sur les corpus gallica, où les erreurs d'OCR sont foison...).

Le paramètre `length` contrôle la taille des ngrams que vous cherchez. Concrètement, avec `length=2` on vous renverra "camarade de", avec `length=3` vous aurez par exemple accès à "camarade de chambre". La taille maximale est 3 sur les corpus Gallica et 4 sur Le Monde (à noter que length=3 produit des calculs interminables sur le corpus presse, qui atteignent parfois le timeout pour les mots fréquents, mais rien ne coûte d'essayer !).

Cette route fonctionne également avec des groupes de mots, dans la mesure des limites des bases de données : cette route est limitée à 2 mots pour les corpus "presse" et "livres" ([par exemple](https://shiny.ens-paris-saclay.fr/guni/joker?mot=le%20camarade&corpus=presse&from=1789&to=1950&n_joker=200&before=False)), et à 3 mots pour Le Monde. A noter que sur le corpus "presse", ce mode est très lent, car la base des 3gram est monumentale. Rappelons également l'exclusion susmentionnée des lignes où `n=1` dans les deux corpus Gallica, qui rend ce mode moins fiable pour les expressions rares.


Dans l'application, nous couplons cette fonctionnalité avec une [liste de "mots vides"](https://regicid.github.io/stopwords.csv), les mots les plus fréquents dans le corpus Gallica. Nous excluons autant de mots vides que l'utilisateur le désire (par défaut 500), puisqu'ils sont souvent peu instructifs ("camarade de" et "camarade qui" sont les plus fréquents, et on s'en fiche pas mal). Cette fonctionalité n'est pas implémentée pour l'instant. 

### 4 - Associated
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/associated?mot=changement%20climatique&corpus=lemonde&from=1945&to=2022&n_joker=200&length=4&stopwords=0](https://shiny.ens-paris-saclay.fr/guni/associated?mot=changement%20climatique&corpus=lemonde&from=1945&to=2022&n_joker=200&length=4&stopwords=0)
Crée sur une idée de [Vincent Bagilet](https://vincentbagilet.github.io/), cette route généralise la route Joker. Elle vous renvoie les mots le plus souvent associés à `mot`, dans un voisinage de `length` (paramètre limité à 3 sur les corpus Gallica). Vous pouvez entrer un nombre de stopwords à ignorer, entre 0 et 1000 (avec `stopwords=500`, on ignorera les 500 mots les plus fréquents, la liste ayant été établie sur le corpus de livres). Cette route est probablement la plus utile, elle vous permet d'explorer l'environnement sémantique de mot, de distinguer selon ses acceptions, etc. Par exemple, Vincent Bagilet l'a utilisée pour quantifier combien on utilisait, au cours du temps, le mot "climatique" en termes d'action, de causes, de conséquences ou de problème.

Cette route peut être un peu lente, surtout si `length` est élevé. Pour des mots extrêmement fréquents (comme "pas") vous risquez d'atteindre le timeout (actuellement fixé à 5000 secondes). Dans ce cas, n'hésitez pas à relancer. SQL garde en cache les calculs déjà faits, alors avec quelques essais, ça finira par marcher. 


### 5 - Associated_article (corpus Le Monde uniquement)
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/associated_article?mot=climatique&from=1945&to=2022&n_joker=200&stopwords=0](https://shiny.ens-paris-saclay.fr/guni/associated_article?mot=climatique&from=1945&to=2022&n_joker=200&stopwords=0)

Egalement due à Vincent, cette route explore aussi l'environnement sémantique d'un mot, mais au niveau de l'article entier (et non du groupe de mot). Deux limites : elle ne fonctionne que sur Le Monde (seul corpus segmenté en articles) et seulement sur un mot : vous pourrez chercher "climatique", mais pas "changement climatique". Cette route est lente sur les mots très fréquents.

### 6 - Coccurrences au niveau de l'article (corpus Le Monde uniquement)
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/cooccur?mot1=climatique&mot2=crise&from=1945&to=2022&resolution=mois](https://shiny.ens-paris-saclay.fr/guni/cooccur?mot1=climatique&mot2=crise+crises&from=1945&to=2022&resolution=mois)

Cette route vous donne le nombre d'articles où figurent deux mots, par exemple où figurent à la fois le mot "crise" et "climatique". Vous pouvez aussi fournir à cette route une collection de mot, auquel cas on sépare les mots par des +, comme dans l'exemple ci-dessus (`crise+crises`. La route vous renvoie aussi le nombre total d'articles à chaque période (`nb_total_article`), afin de pouvoir calculer les fréquences de cooccurrences au cours du temps. 

### 7 - Query_article (corpus Le Monde uniquement)
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query_article?mot=d%C3%A9linquance&from=1960&to=2000](https://shiny.ens-paris-saclay.fr/guni/query_article?mot=d%C3%A9linquance&from=1960&to=2000)

Tout simplement un comptage du nombre d'articles où figure le mot, là où la route query compte le nombre d'occurrences. On vous renvoie aussi bien sûr le nombre total d'articles sur chaque période (`nb_total_article`) pour calculer les fréquences. Cette route peut (entre autre) servir de test de robustesse, ou de comparaison à d'autres corpus où la mesure est "par article" et non "par occurrence". Je ne l'utilise personnellement pas, mais plusieurs personnes nous l'ont demandée, alors la voici.


## Librairies
### pyllicagram
Le seul package que nous avons écrit, car python c'est quand même vachement mieux que R (oui, Gallicagram est codé en R, j'en souffre suffisamment, pas besoin de me le rappeler... Fichue dépendance au sentier. Parenthèse fermée)

Le package contient trois fonctions correspondant aux trois premières routes, il est disponible ici : [https://github.com/regicid/pyllicagram](https://github.com/regicid/pyllicagram).

Pour l'installer : `pip install pyllicagram` si vous êtes sur mac/linux (ou `pip3 install pyllicagram`) . Si vous êtes sur Windows, j'en ai pas la moindre idée et c'est pas ma faute s'il y a encore des gens sur Windows.

### rallicagram
[Vincent Bagilet](https://vincentbagilet.github.io/) a développé ce magnifique package en R
[https://vincentbagilet.github.io/rallicagram/](https://vincentbagilet.github.io/rallicagram/). Comme Vincent est très très fort, il est aujourd'hui plus développé que pyllicagram, et mieux documenté. On va essayer de rattraper le retard.
### Gallicagram gem
Nicolas Roux a eu la bonté de développer une gem Ruby. Pour connaître son stade de devéloppement, rendez-vous sur [https://github.com/nicolrx/gallicagram](https://github.com/nicolrx/gallicagram)

### Autres langages
Si des bonnes volontés veulent développer des packages dans d'autres langages, qu'ils n'hésitent pas à m'envoyer un mail et je les ajouterai à la liste.
