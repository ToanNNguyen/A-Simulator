# A-Simulator
CSGO case simulator - Python
# Issues
Exception has occurred: ModuleNotFoundError No module named 'requests'
Listing every crate instead of just the cases
Can't open the case through the name of the case (use the number instead)
The number is not working, not catching the case
URL link to the API is not working.
Requests aren't going through using the URL link.
Inventory is not catching the skin after opening cases.

#Instructions
Welcome to the CS:GO Case Simulator!

This program lets you open virtual CS:GO weapon cases, 
see what items you unbox, and track them in your inventory.

-------------------------------------------
HOW TO USE
-------------------------------------------

1. Run the program:
   python main.py

2. You’ll see the main menu:

   === CS:GO Case Simulator ===
   1. List available crates
   2. Open a crate
   3. View inventory
   4. Exit
   Select an option:

-------------------------------------------
OPTION 1 — LIST AVAILABLE CRATES
-------------------------------------------
Type 1 and press Enter.

This will show you a list of all available CS:GO weapon cases.

Example:
  1. Kilowatt Case --> ID: crate-4904
  2. Revolution Case --> ID: crate-4880
  3. Operation Bravo Case --> ID: crate-4003
  ...
  Total Weapon Cases: 42

Each case has a number next to it — you’ll use that number to open it.

-------------------------------------------
OPTION 2 — OPEN A CRATE
-------------------------------------------
Type 2 and press Enter.

You’ll be asked:
  Enter the number of the crate you want to open:

Type the number of the case you want (for example, 3) and press Enter.

Example:
  Enter the number of the crate you want to open: 3

The program will simulate opening the case and show what you unboxed.

Example result:
  You unboxed: AWP | Duality (Covert)

The item will automatically be added to your inventory.

-------------------------------------------
OPTION 3 — VIEW INVENTORY
-------------------------------------------
Type 3 and press Enter.

This shows all the items you’ve unboxed during this session.

Example:
  === Your Inventory ===
  1. AWP | Duality (Covert) from Revolution Case
  2. P2000 | Ocean Foam (Classified) from Operation Bravo Case

If you haven’t opened any cases yet, you’ll see:
  No items yet — go open some cases!

-------------------------------------------
OPTION 4 — EXIT
-------------------------------------------
Type 4 and press Enter to close the program.

Your inventory is reset when you exit.

-------------------------------------------
EXAMPLE SESSION
-------------------------------------------

=== CS:GO Case Simulator ===
1. List available crates
2. Open a crate
3. View inventory
4. Exit
Select an option: 1

1. Kilowatt Case --> ID: crate-4904
2. Revolution Case --> ID: crate-4880
3. Operation Bravo Case --> ID: crate-4003
Total Weapon Cases: 42

Select an option: 2
Enter the number of the crate you want to open: 3
You unboxed: P2000 | Ocean Foam (Classified)

Select an option: 3
=== Your Inventory ===
1. P2000 | Ocean Foam (Classified) from Operation Bravo Case

Select an option: 4
Goodbye!

-------------------------------------------
NOTES
-------------------------------------------
- You must have an internet connection.
- Only weapon cases are listed (no capsules or graffiti).
- The data comes from ByMykel’s public CS:GO API.
- Inventory is temporary and resets each time the program restarts.

-------------------------------------------
END OF GUIDE
-------------------------------------------
