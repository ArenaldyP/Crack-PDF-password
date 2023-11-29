import pikepdf
from tqdm import tqdm

# load Password List
passwordss = input("masukan direktory password: ")
passwords = [line.strip() for line in open(f"{passwordss}")]
pdf_file = input("Masukan file PDF: ")

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open(f"{pdf_file}", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print(f"[+] Password found ", password)
            break
    except pikepdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
