import json
import os
import sys
import time

# Pfad zur JSON-Datei im Submodul definieren
SUBMODULE_PATH = os.path.join("ai_specs_sub", "neurolink_protocols.json")

def load_ai_specs(filepath: str) -> dict:
    """Lädt die Spezifikationen aus dem AI-Specs Submodul."""
    if not os.path.exists(filepath):
        print(f"[FATAL ERROR] Submodule file not found: {filepath}")
        print("[SUGGESTION] Did you forget to initialize the submodule?")
        sys.exit(1)
        
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def boot_sequence():
    """Simuliert die Startsequenz von NEON-SYS."""
    print("\033[31m" + "=== [NEON-SYS: META-OS BOOT ACTIVE] ===" + "\033[0m")
    time.sleep(0.5)
    print("Loading core kernel...")
    time.sleep(0.5)
    
    # Hier zapfen wir das Submodul an:
    print(f"Reading protocols from Submodule: '{SUBMODULE_PATH}'...")
    specs = load_ai_specs(SUBMODULE_PATH)
    time.sleep(0.5)
    
    print("\n\033[32m" + "--- SYNAPSEN-LINK AKTIV ---" + "\033[0m")
    print(f"Modell:        {specs.get('codename')}")
    print(f"Sicherheitsstufe: {specs.get('security_level')}")
    print(f"Synchronisation:  {specs.get('neural_sync_rate')}")
    print("Aktive Knotenpunkte:")
    for node in specs.get("active_nodes", []):
        print(f"  [-] {node}")
    print("\033[32m" + "---------------------------" + "\033[0m\n")

if __name__ == "__main__":
    boot_sequence()
