import requests, getpass, time, subprocess, requests, os

def weryfikacja():
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    ip = data["ip"]

    print("Witaj użytkowniku!")
    print("Nick:")
    user = input(">> ")
    print("Hasło:")
    haslo = getpass.getpass(">> ")
    
    with open("C:\\niesl\\dane\\konto.txt", "r") as plik:
        for linia in plik:
            kontoo = linia.strip().split(",")
            if ip == kontoo[0] and user == kontoo[1] and haslo == kontoo[2]:
                print("Logowanie udane!")
                time.sleep(3)
                select_vpn_server()

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def check_for_updates(local_version, github_url):
    response = requests.get(github_url)
    latest_version = response.text.strip()
    return latest_version != local_version

def update_vpn_program(github_url, local_path):
    print("Pobieranie najnowszej wersji...")
    download_file(github_url, local_path)
    print("Aktualizacja zakończona pomyślnie.")

def select_vpn_server():
    print("jebanie disa?:")
    print("1. Tak jebać disa 1")
    print("2. Jebać tą kurwe 2")
    # Tutaj możesz dodać więcej serwerów VPN do wyboru
    choice = input("wybierz: ")
    if choice == "1":
        return "vpn_server1_address"
    elif choice == "2":
        return "vpn_server2_address"
    else:
        print("Błędny wybór. Wybierz ponownie.")
        return select_vpn_server()

def main():
    local_version = "1.0"  # Wersja lokalna Twojej aplikacji
    github_url = 'https://raw.githubusercontent.com/Foczkaexe/niesl/main/test.py'
    local_path = 'C:\\niesl\\test.py'

    if check_for_updates(local_version, github_url):
        update_vpn_program(github_url, local_path)

    vpn_server_address = weryfikacja()

    print(f"Uruchamianie aplikacji VPN z serwerem {vpn_server_address}...")
    subprocess.run(["python", local_path, vpn_server_address])  # Uruchomienie aktualizowanej aplikacji z wybranym serwerem VPN

if __name__ == "__main__":
    main()

weryfikacja()
