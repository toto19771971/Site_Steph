from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True  # <-- Ajoute cette ligne ici
    
import os

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    template_path = os.path.abspath("templates/contact.html")
    print(f"DEBUG: Flask charge le fichier -> {template_path}")
    
    # Vérifier si le fichier existe vraiment
    if not os.path.exists(template_path):
        print("ERREUR: Le fichier contact.html n'existe pas là où Flask le cherche !")



    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        demande = request.form['demande']
        print(f'Nouveau contact: {nom} {prenom}, Adresse: {adresse}, Téléphone: {telephone}, Demande: {demande}')
        return "Merci, nous vous contacterons dès que possible."
    
    with open("templates/contact.html", "r", encoding="utf-8") as f:
        print("----- CONTENU DU FICHIER CHARGÉ -----")
        print(f.read())  # Affiche le contenu du fichier chargé dans la console Flask
        print("-------------------------------------")

    
    return render_template('contact.html')





    return render_template('contact.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5003)
