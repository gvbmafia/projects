import os
from cryptography.fernet import Fernet

def criptare():
    # Generate encryption key / Genereaza cheia de criptare
    key = Fernet.generate_key()

    # Save the key to a file (depends on where your files are: D:/..., C:/..., etc.)
    # Salveaza cheia in fisier (depinde unde ai fisierele: D:/..., C:/..., etc.)
    with open(r"D:\cheie.key", "wb") as the_key:
        the_key.write(key)
        print("Cheia a fost generata si salvata in fisierul cheie.key")

def main():
    # Call encryption function / Apeleaza functia de criptare
    criptare()

main()

# List files from input folder / Listeaza fisierele din folderul input
list_files = os.listdir("D:/input")

# Iterate through each file / Parcurge fiecare fisier
for file_name in list_files:
    # Optional: encrypt only .txt files / Opțional: cripteaza doar fisiere .txt
    # if file_name.endswith(".txt"):

    # Read the original file / Citeste fisierul original
    with open(f"D:/input/{file_name}", "rb") as file:
        data = file.read()

    # Load the stored key / Incarca cheia salvata
    with open("D:/cheie.key", "rb") as the_key:
        key = the_key.read()

    # Create Fernet object / Creeaza obiectul Fernet
    fernet = Fernet(key)

    # Encrypt the file data / Cripteaza continutul fisierului
    encrypted = fernet.encrypt(data)

    # Save encrypted file to output folder / Salveaza fisierul criptat in folderul output
    with open(f"D:/output/{file_name}", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"Fisierul {file_name} a fost criptat si salvat in folderul output.")

def decryptare():
    # List files from output folder / Listeaza fisierele din folderul output
    list_files = os.listdir("D:/output")

    # Iterate through encrypted files / Parcurge fisierele criptate
    for file_name in list_files:
        # Optional: decrypt only .txt files / Optional: decripteaza doar .txt
        # if file_name.endswith(".txt"):

        # Read encrypted file / Citeste fisierul criptat
        with open(f"D:/output/{file_name}", "rb") as enc_file:
            encrypted = enc_file.read()

        # Load the same key / Incarca aceeasi cheie
        with open("D:/cheie.key", "rb") as the_key:
            key = the_key.read()

        # Create Fernet object / Creeaza obiectul Fernet
        fernet = Fernet(key)

        # Decrypt content / Decripteaza continutul
        decrypted = fernet.decrypt(encrypted)

        # Save decrypted file / Salveaza fisierul decriptat
        with open(f"D:/decrypted/{file_name}", "wb") as dec_file:
            dec_file.write(decrypted)

        print(f"Fisierul {file_name} a fost decriptat si salvat in folderul decrypted.")

decryptare()
print("EN: I was tired so I made the comments in both languages with chatGPT's help.    RO: Am fost obosit asa ca am facut comentariile in ambele limbi cu ajutorul chatGPT.")
