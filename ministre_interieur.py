import urllib
from tqdm import tqdm
import pandas as pd
from pyllicagram import *
import matplotlib.pyplot as plt

ministres = ["Poniatowski","Defferre","Joxe","Pasqua","Quilès","Debré","Chevènement","Sarkozy","Villepin","Baroin","Hortefeux","Guéant","Valls","Cazeneuve","Fekl","Collomb","Castaner","Darmanin","Jospin","Frey","Marcellin","Fouchet"]
score = []
for ministre in tqdm(ministres):
    a = pd.read_csv(f"https://shiny.ens-paris-saclay.fr/guni/cooccur?mot1=d%C3%A9linquance+d%C3%A9linquants+d%C3%A9linquant&mot2={urllib.parse.quote_plus(ministre.lower())}&resolution=annee")
    a["ratio"] = a.nb_articles_cooccur/a.nb_total_article
    score.append(a.nb_articles_cooccur.sum())

pd.DataFrame({"ministre":ministres,"score":score}).sort_values("score",ascending=False).iloc[:10,]
pd.DataFrame({"ministre":ministres,"score":score}).sort_values("score",ascending=False).iloc[:10,].iloc[::-1,].plot.barh(x="ministre",y="score")
plt.title("Nombre de cooccurrences par aentre le ministre de l'intérieur et le mot 'délinquant(ce)'")
