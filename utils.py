from config import N


def printLayout(battlefield, soldiers, missile_position=None, impact_radius=None, commander_id=None):
    # Create a copy of the battlefield to modify for printing
    display_field = [row.copy() for row in battlefield]

    # Mark the missile's impact zone on the display field
    if missile_position and impact_radius:
        x, y = missile_position
        for dx in range(-(impact_radius-1), impact_radius):
            for dy in range(-(impact_radius-1), impact_radius):
                if 0 <= (x + dx) < N and 0 <= (y + dy) < N:
                    display_field[x + dx][y + dy] = 'X'

    # Place soldiers on the battlefield
    for soldier in soldiers:
        if soldier["alive"]:
            display_field[soldier["x"]][soldier["y"]] = str(soldier["id"])

    # Print the display field
    for row in display_field:
        print(' '.join(str(cell) for cell in row))

    # Print additional information
    print("\nSoldiers:")
    for soldier in soldiers:
        status = "Alive" if soldier["alive"] else "Dead"
        role = "Commander" if soldier["id"] == commander_id else "Soldier"
        print(
            f"ID: {soldier['id']}, Position: ({soldier['x']}, {soldier['y']}), Status: {status}, Role: {role}")

    if missile_position and impact_radius:
        print(
            f"\nMissile landed at: {missile_position} with impact radius: {impact_radius}")
        casualties = [soldier["id"] for soldier in soldiers if not soldier["alive"] and abs(
            soldier["x"] - x) <= impact_radius and abs(soldier["y"] - y) <= impact_radius]
        if casualties:
            print(
                f"Soldiers {', '.join(map(str, casualties))} died due to the missile.")
