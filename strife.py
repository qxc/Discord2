import csv

def createCard(name, cardType, cost, text, negative, image,hp):
    code = "\\begin{tikzpicture} \n\cardbackground{" +cardType 
    if negative:
        code += "Curse} \n"
    else:
        code += "} \n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
    code += "\cardprice{" + str(cost) + "} \n"
    if hp != "":
        code += "\cardhp{" + hp + "} \n"
    code += "\end{tikzpicture}\n\hspace{5mm}\n"
    return code

def processCards(fileName = "cardList.csv"):
    f = open("cards.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name of card']
            cost = row['cost']
            cardType = row['type'].capitalize()
            neg = ( row['pos/neg'] == 'negative')
            image = row['Image']
            text = row['description']
            hp = row['HP']
            if cardType == "":
                continue
            if row['Expansion'] != "First":
                continue
            if row['Card Status'] != "changed":
                continue
            card = createCard(name, cardType, cost, text, neg, image,hp)
            #f.write(card)
            number = row['supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
    return

processCards()
