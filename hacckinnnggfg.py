import time
import random
import sys

def infinite_scroll_text():
    chars = "/-\|"
    while True:
        for char in chars:
            sys.stdout.write('\r' + 'Hacking in progress ' + char)
            sys.stdout.flush()
            time.sleep(0.1)

def main():
    print("Initializing hacking sequence...")
    time.sleep(2)
    print("Establishing connection to mainframe...")
    time.sleep(3)
    print("Bypassing firewalls...")
    time.sleep(2)
    print("Cracking encryption...")
    time.sleep(4)
    print("Injecting malicious code...")
    time.sleep(3)
    print("Access granted!")
    time.sleep(1)
    print("\nHacking successful. Initiating data transfer...")
    time.sleep(2)
    print("Downloading sensitive data...")
    time.sleep(4)
    print("Data transfer complete.")
    time.sleep(2)
    print("Covering tracks...")
    time.sleep(3)
    print("Initiating self-destruct sequence...")
    time.sleep(2)
    print("Self-destruct sequence activated. Exiting...")
    time.sleep(3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        sys.exit()
