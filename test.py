import pwinput


constant = "PAROLA"
parola = pwinput.pwinput(prompt='Introdu parola: ', mask='*')
if parola == constant: