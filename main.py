import requests
import random
import os
from dotenv import load_dotenv

MASTER_LIST_URL = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/crates.json"
ITEM_BASE_URL   = "https://bymykel.github.io/CSGO-API/api/en"


# Load environment variables
load_dotenv()
BASE_URL = os.getenv("API_KEY")

# Track user inventory
inventory = []

cached_crates = []

def get_all_crates():
    """Fetch and list weapon cases only."""
    global cached_crates
    try:
        response = requests.get("https://bymykel.github.io/CSGO-API/api/en/crates.json")
        response.raise_for_status()
        data = response.json()

        # Filter to only real cases
        cached_crates = [c for c in data if c.get("type") == "Case"]

        for i, crate in enumerate(cached_crates, start=1):
            print(f"{i}. {crate['name']} — ID: {crate['id']}")

        print(f"\nTotal Weapon Cases: {len(cached_crates)}")
        return cached_crates

    except Exception as e:
        print(f"Error fetching crates: {e}")
        return []

def open_crate(crate_id):
    "Simulate opening a CS:GO case by picking a random skin from its contents."
    try:
        # Use cached data (from get_all_crates)
        crate = next((c for c in cached_crates if c["id"] == crate_id), None)
        if not crate:
            print(f"Could not find crate with ID: {crate_id}")
            return

        # Combine normal and rare drops
        drops = crate.get("contains", []) + crate.get("contains_rare", [])
        if not drops:
            print(f"⚠️ This crate has no items listed.")
            return

        # Randomly select one
        drop = random.choice(drops)
        rarity = drop.get("rarity", {}).get("name", "Unknown")
        print(f"🎉 You unboxed: {drop['name']} ({rarity})")

        # Optionally add to player’s inventory
        inventory.append({
            "crate": crate["name"],
            "item": drop["name"],
            "rarity": rarity
        })

    except Exception as e:
        print(f"Error opening crate: {e}")

def open_crate_menu():
    crates = cached_crates or get_all_crates()
    if not crates:
        print("No crates available.")
        return
    try:
        choice = int(input("\nEnter the number of the crate you want to open: "))
        if not (1 <= choice <= len(crates)):
            print(" Invalid number.")
            return
        crate_id = crates[choice - 1]["id"]
        open_crate(crate_id)
    except ValueError:
        print("Please enter a valid number.")

def open_crate_menu():
    crates = get_all_crates()
    if not crates:
        print("No crates available.")
        return

    try:
        choice = int(input("\nEnter the number of the crate you want to open: "))
        if choice < 1 or choice > len(crates):
            print("Invalid number.")
            return

        crate_id = crates[choice - 1]["id"]
        open_crate(crate_id)

    except ValueError:
        print("Please enter a valid number.")


def view_inventory():
    "Show all collected skins."
    print("\n=== Your Inventory ===")
    if not inventory:
        print("No items yet. Open Cases for skins.")
    else:
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item['item']} ({item['rarity']}) from {item['crate']}")


def main_menu():
    "Menu loop for interacting with the simulator."
    while True:
        print("\n=== CS:GO Case Simulator ===")
        print("1. List available crates")
        print("2. Open a crate")
        print("3. View inventory")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            get_all_crates()
        elif choice == "2":
            open_crate_menu()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
