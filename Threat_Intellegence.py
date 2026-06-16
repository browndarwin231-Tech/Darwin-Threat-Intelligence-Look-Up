threat = input("Enter threat type: ").lower()

if threat == "phishing":
    print("Phishing: Attempts to steal sensitive information.")
elif threat == "malware":
    print("Malware: Malicious software designed to damage systems.")
elif threat == "ransomware":
    print("Ransomware: Encrypts files and demands payment.")
elif threat == "trojan":
    print("Trojan: Malware disguised as legitimate software.")
else:
    print("Threat not found.")

print("Created by Darwin Brown")