<link rel="stylesheet" type="text/css" href="custom.css">
# API Gallicagram

## Introduction
Pour le projet [Gallicagram](https://shiny.ens-paris-saclay.fr/app/gallicagram), nous avons téléchargé massivement plusieurs corpus, en particulier :
* Les 3 millions de périodiques (numéros de presse) de *Gallica*, fiable entre 1789 et 1950
* Les 300 000 monographies (livres) de *Gallica*, fiable entre 1600 et 1940
* Les 3 millions d'articles des archives du quotidien Le Monde (décembre 1944-décembre 2022)
* Le gros million de documents du Zeitungsportal, qui regroupe les archives de presse de la Deutsche Digitale Bibliothek, équivalent (en moins bien) de Gallica outre-Rhin. 

En voici la liste complète, ainsi que quelques détails sur les corpus - en particulier la date où nous les avons téléchargés :

<table>
  <thead>
    <tr>
      <th>Titre</th>
      <th>Période (conseillée)</th>
      <th>Volume (en mots)</th>
      <th>Code API</th>
      <th>Longueur max</th>
      <th>Résolution</th>
      <th>Seuils</th>
      <th>Date de téléchargement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Le Monde</td>
      <td>1944-2023</td>
      <td>1,5 milliards</td>
      <td>lemonde</td>
      <td>4gram</td>
      <td>Journalière</td>
      <td>Aucun</td>
      <td>Janvier 2023</td>
    </tr>
    <tr>
      <td>Presse de Gallica</td>
      <td>1789-1950</td>
      <td>57 milliards</td>
      <td>presse</td>
      <td>3gram</td>
      <td>Mensuelle</td>
      <td>2gram>1,3gram>1</td>
      <td>Avril 2021</td>
    </tr>
    <tr>
      <td>Livres de Gallica</td>
      <td>1600-1940</td>
      <td>16 milliards</td>
      <td>livres</td>
      <td>5gram</td>
      <td>Annuelle</td>
      <td>2gram>1, etc</td>
      <td>Avril 2021</td>
    </tr>
    <tr>
      <td>Deutsches Zeitungsportal (DDB)</td>
      <td>1780-1950</td>
      <td>39 milliards</td>
      <td>ddb</td>
      <td>2gram</td>
      <td>Mensuelle</td>
      <td>1gram > 1, 2gram>2</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>American Stories</td>
      <td>1798-1963</td>
      <td>20 milliards</td>
      <td>american_stories</td>
      <td>3gram</td>
      <td>Annuelle (mensuelle à venir ?)</td>
      <td>1gram>1,2gram>2,3gram>3</td>
      <td>Octobre 2023</td>
    </tr>
    <tr>
      <td>Journal de Paris</td>
      <td>1777-1827</td>
      <td>86 millions</td>
      <td>paris</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Moniteur Universel</td>
      <td>1789-1869</td>
      <td>511 millions</td>
      <td>moniteur</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Journal des Débats</td>
      <td>1789-1944</td>
      <td>1,2 milliards</td>
      <td>journal_des_debats</td>
      <td>1gram</td>
      <td>Journalière</td>
      <td>Aucun</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>La Presse</td>
      <td>1836-1869</td>
      <td>253 millions</td>
      <td>la_presse</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Le Constitutionnel</td>
      <td>1821-1913 (très lacunaire)</td>
      <td>64 millions</td>
      <td>constitutionnel</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Le Figaro</td>
      <td>1854-1952</td>
      <td>870 millions</td>
      <td>figaro</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Le Temps</td>
      <td>1861-1942</td>
      <td>1 milliard</td>
      <td>temps</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Le Petit Journal</td>
      <td>1863-1942</td>
      <td>745 millions</td>
      <td>petit_journal</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Le Petit Parisien</td>
      <td>1876-1944</td>
      <td>631 millions</td>
      <td>petit_parisien</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>L’Humanité</td>
      <td>1904-1952</td>
      <td>318 millions</td>
      <td>huma</td>
      <td>2gram</td>
      <td>Journalière</td>
      <td>2gram>1</td>
      <td>Août 2023</td>
    </tr>
    <tr>
      <td>Opensubtitles (français)</td>
      <td>1935-2020</td>
      <td>17 millions</td>
      <td>subtitles</td>
      <td>3gram</td>
      <td>Annuelle</td>
      <td>Aucun</td>
      <td>Juillet 2023</td>
    </tr>
    <tr>
      <td>Opensubtitles (anglais)</td>
      <td>1930-2020</td>
      <td>102 millions</td>
      <td>subtitles_en</td>
      <td>3gram</td>
      <td>Annuelle</td>
      <td>Aucun</td>
      <td>Juillet 2023</td>
    </tr>
    <tr>
      <td>Rap (Genius)</td>
      <td>1989-février 2024</td>
      <td>20 millions</td>
      <td>rap</td>
      <td>5gram</td>
      <td>Annuelle</td>
      <td>Aucun</td>
      <td>Mars 2024</td>
    </tr>
    <tr>
      <td>Persée</td>
      <td>1789-2023</td>
      <td>1 milliard</td>
      <td>route à part (query_persee)</td>
      <td>2gram</td>
      <td>Annuelle</td>
      <td>Aucun</td>
      <td>Décembre 2023</td>
    </tr>
  </tbody>
</table>

Pour l'application, nous avons constitué des bases de données dénombrant le nombre d'occurrences des mots et groupes de mots sur chaque corpus, sur chaque période. Ce sont ces mêmes bases que l'application utilise pour afficher ses graphes (s'il fallait compter à chaque fois les occurrences dans le corpus, cela prendait des semaines). Bref, nous avons fait des calculs interminables pour compter le nombre d'occurrences de chaque mot, et cette information pourrait être utile à d'autres. 
Ces bases de données étant trop vastes pour être téléchargeables (2 téras au total) et manipulables. À titre d'exemple, nous avons déposé la base des 1grams des archives du *Monde* sur Huggingface au format parquet, à [cette adresse](https://huggingface.co/datasets/regicid/1gram_lemonde), et rendons les autres interrogeables à travers cette API, qui vous envoie les données au format csv. 

Mettons d'emblée les pieds dans le plat. Cette API est simple d'usage, voyez plutôt :

```
tableau = read.csv("https://shiny.ens-paris-saclay.fr/guni/query?mot=patate")
```

En insérant cette ligne dans votre code R, vous obtiendrez un dataframe de la fréquence mensuelle du mot patate dans la presse de *Gallica*.

Pour encore plus d'ergonomie, vous pouvez utiliser les packages R, python et Ruby (voir ci-dessous), qui sont des "wrappers" de cette API. Nos bases sont stockées en SQLite, et structurées avec les colonnes suivantes : n (nombre d'occurrences), gram (mot ou syntagme recherché), année, mois et jour (selon le corpus). À titre d'exemple, nous avons déposé la base des 1grams des archives du *Monde* sur Huggingface au format parquet, à [cette adresse](https://huggingface.co/datasets/regicid/1gram_lemonde). Le code de l'API (une banale application codée en python/flask) est disponible à [cette adresse](https://github.com/regicid/api_gallicagram).


Là où c'est nécessaire, les bases sont doublées d'une structure fulltext (sqlite fts5), qui permet des interrogations plus complexes. L'API ajoute aussi une colonne "total", qui donne le nombre total de mots ou groupes de mots de cette taille dans le corpus, sur chaque période. On peut donc calculer la fréquence en divisant la colonne "n" par la colonne "total". Ces fichiers de totaux sont situés à [cette adresse](https://github.com/regicid/docker_gallicagram/tree/master/gallicagram), avec le code source de l'application. Elles ont pour nom de fichier "{code_corpus}{n}.csv" - les 1gram du *Monde* s'appellent donc lemonde1.csv.

Les bases ont été constituées légèrement différement selon le corpus :
* La résolution diffère : journalière pour *Le Monde* et les sous-corpus *Gallica*, mensuelle pour la presse de *Gallica*, annuelle pour les livres de *Gallica*, *Persée*, le corpus rap et nos corpus en langue étrangère.
* A cause de l'explosion combinatoire et des tailles inégales des  corpus, nous avons calculé jusqu'au 3gram pour le corpus "presse", 4gram pour Le Monde et 5gram pour le corpus "livres". Autrement dit, on pourra chercher "une belle patate" dans le corpus presse, mais pas "une très belle patate". 
* Dans les corpus Gallica (presse et livres), nous avons exclu toutes les lignes où n=1. Cela permettait de réduire massivement la taille de la base : l'océrisation étant imparfaite, l'immense majorité des lignes sont des erreurs d'OCR. Pas besoin dans Le Monde, où l'OCR a manifestement été relu et corrigé à la main.

## Construction des bases de données
Voici la procédure que nous avons suivie pour constituer ces bases de données :
* *Scraping* du corpus
* Tokénisation du corpus (en python, avec pour tokenizer `nltk.RegexpTokenizer(r"[0-9a-zà-ÿ']+")`) (notons que nous avons considéré l'apostrophe comme une lettre).
* Comptage des ngrams par tranche temporelle (jour, mois ou année), ainsi que par revue dans le cas du corpus *Persée*.
* Indexation de la table en sqlite : `CREATE UNIQUE INDEX index_bla on gram (gram,annee,mois,jour);` (selon la résolution temporelle).
* Création des fichiers totaux pour normaliser les fréquences (en sqlite : `select sum(n) as n,annee,mois,jour from gram group by annee,mois,jour;`). 
* C'est tout !


## Nos routes
Les bases de données peuvent être interrogées de plusieurs façons. Si en voyant la structure des données décrites ci-dessus, un autre mode vous vient à l'esprit, n'hésitez pas à nous écrire (cette API est essentiellement constituée d'idées d'autres personnes, et son existence même est due à une demande d'Etienne Brunet, que je salue).

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

### 7 - query_article (corpus Le Monde uniquement)
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query_article?mot=d%C3%A9linquance&from=1960&to=2000](https://shiny.ens-paris-saclay.fr/guni/query_article?mot=d%C3%A9linquance&from=1960&to=2000)

Tout simplement un comptage du nombre d'articles où figure le mot, là où la route query compte le nombre d'occurrences. On vous renvoie aussi bien sûr le nombre total d'articles sur chaque période (`nb_total_article`) pour calculer les fréquences. Cette route peut (entre autre) servir de test de robustesse, ou de comparaison à d'autres corpus où la mesure est "par article" et non "par occurrence". Je ne l'utilise personnellement pas, mais plusieurs personnes nous l'ont demandée, alors la voici.

### 8 - query_persee (corpus Persée)
Syntaxe : [https://shiny.ens-paris-saclay.fr/guni/query_persee?mot=in%C3%A9galit%C3%A9s&from=1789&to=2000&by_revue=False&revue=arss+ahess+rfs+dreso+ds](https://shiny.ens-paris-saclay.fr/guni/query_persee?mot=in%C3%A9galit%C3%A9s&from=1789&to=2000&by_revue=False&revue=arss+ahess+rfs+dreso+ds)

Une route à part pour compter les occurrences dans le corpus Persée. Sa particularité est d'avoir été indexé non seulement par année, mais aussi par revue. Vous pouvez donc chercher dans une seule revue, ou dans un bouquet de revue que vous vous constituez. Par exemple, pour étudier la diffusion d'un concept sociologique, il serait plus pertinent de chercher dans une dizaine de revues canoniques en sociologie, plutôt que dans le corpus tout entier, qui contient également des géosciences. Les revues disponibles sont renseignées [ici](https://github.com/regicid/regicid.github.io/blob/master/revues_persee_full.csv). La colonne "Codes" du tableau vous donne l'identifieur des revues, que vous fournisser au paramètre `nb_total_article` dans l'API. Vous pouvez chercher dans plusieurs revues en séparant les revues par des + (dans l'exemple ci-dessus, on cherche dans les *Actes de la Recherche en Sciences sociales*, les *Annales*, la *RFS*, *Droit et Société* et *Déviance et société*. Avec `by_revue=False` (la valeur par défaut), les occurrences sont agrégées par année. Avec `by_revue=True`, on conserve leur ventilation dans les différentes revues. Avec `by_revue=True` et un champ `revue` non renseigné, vous pouvez chercher d'où proviennent les occurrences dans la totalité du corpus.

Une limite : on ne peut pour l'instant pas chercher de syntagme de plus de deux mots. 

Pour plus d'informations sur le corpus Persée, les revues qu'il contient et les périodes de disponibilité, ça se passe [ici](https://regicid.github.io/persee).


## Librairies
### pyllicagram
Le seul package que nous avons écrit, car python c'est quand même vachement mieux que R (oui, Gallicagram est codé en R, j'en souffre suffisamment, pas besoin de me le rappeler... Fichue dépendance au sentier. Parenthèse fermée)

Le package contient trois fonctions correspondant aux trois premières routes, il est disponible ici : [https://github.com/regicid/pyllicagram](https://github.com/regicid/pyllicagram).

Pour l'installer : `pip install pyllicagram` si vous êtes sur mac/linux (ou `pip3 install pyllicagram`) . Si vous êtes sur Windows, j'en ai pas la moindre idée et c'est pas ma faute s'il y a encore des gens sur Windows.

Note : le package n'est vraiment pas à jour et il faudrait que je travaille dessus.

### rallicagram
[Vincent Bagilet](https://vincentbagilet.github.io/) a développé ce magnifique package en R
[https://vincentbagilet.github.io/rallicagram/](https://vincentbagilet.github.io/rallicagram/). Comme Vincent est très très fort, il est aujourd'hui plus développé que pyllicagram, et mieux documenté. On va essayer de rattraper le retard.
### Gallicagram gem
Nicolas Roux a eu la bonté de développer une gem Ruby. Pour connaître son stade de devéloppement, rendez-vous sur [https://github.com/nicolrx/gallicagram](https://github.com/nicolrx/gallicagram)

### Autres langages
Si des bonnes volontés veulent développer des packages dans d'autres langages, qu'ils n'hésitent pas à m'envoyer un mail et je les ajouterai à la liste.
