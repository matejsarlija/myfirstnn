
### ZADATAK 1:
1. Cilj je napraviti app koji za bilo koji tekst prepoznaje koji token pripada “food temi”
2. Dva su izvora podatka:
- Restaurants i food ordering dialozi iz taskmaster dataseta - https://github.com/google-research-datasets/Taskmaster/tree/master/TM-2-2020 
- Food-related riječi csv file (https://drive.google.com/file/d/1EPC5p7RxpTzn0jYg03uIx9bDj8Lveqsi/view?usp=sharing)


3. Morate isparsirati json fileove (food ordering iz taskmaster dataseta) u tablični prikaz koji:
- Sadrži pojedinačne rečenice (vidi https://github.com/google-research-datasets/Taskmaster/tree/master/TM-2-2020#structure) 
- Sadrži teme iz gore navedenog datasets (vidi polja: utterance[‘segments’][‘text’] i utterance[‘segments’][“annotations”][“name”] --> https://github.com/google-research-datasets/Taskmaster/blob/master/TM-2-2020/ontology/food-ordering.json) - dva stupca
- Za svaki token iz rečenice napraviti labelu/oznaku u obliku LabelEncodera (npr. Rečenica: “Your order is two burritos (one chicken and one beef); an enchilada with refried beans, chips and salsa.” bi imala za svaki token oznaku 0 ili 1 (nije “food” ili je “food”)
    - → to ćete napraviti ILI pomoću Food-related.csv → iteriranjem kroz rečenice dataseta (ukoliko se token nalazi csv-u, onda je food)
    - -> ILI samo korištenjem oznaka iz taskmaster jsona (svakako morate napisati skriptu za parsing tih podataka)
    - → po želji: iskoristiti TextBlob (ili neki drugi library) koji omogućuje spelling correction na csv-u prije nego se krene “matchati” 

4. Nakon parsiranja, potrebno je vektorizirati svaki token
- Ili uzeti gotove embeddinge (spacy, stanford glove, google word2vec, …)
- Ili napraviti svoje embeddinge (koristeći gensim ili fasttext)
- Ili napraviti svoje embeddinge (koristeći neki frequency vectorizer)

5. Isto tako, potrebno je vektorizirati i bilo kakve kategoričke oznake - LABELE (točka 3.b)

6. Za svaku rečenicu (liniju csv-a) imat ćete listu vektora → [[“vektor”][“vektor”][“vektor”]],[[“vektor]...],[...]
- Sve rečenice bi trebale biti iste dužine, što znači da trebamo odrediti max_len i dodajemo “PADDING” vektor za sve kraće rečenice
7. S obzirom da je riječ o token-level treningu, dužina svake rečenice (broj tokena/vektora) mora biti ista kao i dužina oznaka/labela za tu rečenicu (taj sequence) 
- https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python 


8. Spremiti datu 
- kao pickle file - https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict 
- ili kao .csv 
- ili kao dataclass (https://docs.python.org/3/library/dataclasses.html)

9. Sad imamo input za treniranje :) 

10. Izrada modela za klasifikaciju tokena: 
- https://www.researchgate.net/post/What_is_the_best_classifier_of_Deep_Learning_techniques_in_Text_Classification 
- https://paperswithcode.com/task/text-classification 
- https://towardsdatascience.com/named-entity-recognition-ner-meeting-industrys-requirement-by-applying-state-of-the-art-deep-698d2b3b4ede 

11. Dodatni izvori podataka:
- https://data.world/datasets/restaurant 
- https://metatext.io/datasets 
- https://www.kaggle.com/datasets?search=food&page=2 
- https://www.kaggle.com/snap/amazon-fine-food-reviews 


