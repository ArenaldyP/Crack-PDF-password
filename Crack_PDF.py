import pikepdf
from concurrent.futures import ThreadPoolExecutor
import logging
import concurrent.futures

# Set up logging
logging.basicConfig(filename='pdf_decryption.log', level=logging.INFO)

def decrypt_pdf(password, pdf_file):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            # Password decrypted successfully, log and return the password
            logging.info(f"[+] Password ditemukan: {password}")
            return password
    except pikepdf.PasswordError as e:
        # Wrong password, log and return None
        logging.info(f"[-] Password salah: {password}")
        return None
    except Exception as ex:
        # Log other errors
        logging.error(f"Error: {ex}")
        return None

def main():
    # Load Daftar Password
    passwordss = input("Masukkan direktori password: ")
    passwords = [line.strip() for line in open(f"{passwordss}")]
    pdf_file = input("Masukkan file PDF: ")

    # Gunakan ThreadPoolExecutor untuk pemrosesan paralel
    with ThreadPoolExecutor() as executor:
        # Kirimkan tugas untuk setiap password
        futures = [executor.submit(decrypt_pdf, password, pdf_file) for password in passwords]

        # Iterasi atas tugas yang selesai
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                # Password ditemukan, keluar dari loop
                print(f"[+] Password ditemukan: {result}")
                break

if __name__ == "__main__":
    main()
