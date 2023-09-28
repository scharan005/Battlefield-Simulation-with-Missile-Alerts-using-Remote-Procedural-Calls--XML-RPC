import xmlrpc.server
from config import N, M, Si
from utils import printLayout
import random
from server import battlefield

soldiers = [{"id": i, "x": random.randint(0, N-1), "y": random.randint(
    0, N-1), "speed": random.choice(Si), "alive": True} for i in range(1, M+1)]


def is_in_impact_zone(soldier_x, soldier_y, x, y, impact_radius):
    return abs(soldier_x - x) < impact_radius and abs(soldier_y - y) < impact_radius


def notify_missile_approach(x, y, impact_radius):
    print(
        f"Received missile approach notification at ({x}, {y}) with impact radius {impact_radius}")
    for soldier in soldiers:
        if soldier["alive"]:
            take_shelter(soldier, x, y, impact_radius)
    printLayout(battlefield, soldiers, (x, y), impact_radius)


def take_shelter(soldier, x, y, impact_radius):
    if is_in_impact_zone(soldier["x"], soldier["y"], x, y, impact_radius):
        possible_moves = [(i, j) for i in range(-soldier["speed"], soldier["speed"] + 1)
                          for j in range(-soldier["speed"], soldier["speed"] + 1)
                          if 0 <= soldier["x"] + i < N and 0 <= soldier["y"] + j < N]
        safe_moves = [(i, j) for i, j in possible_moves if not is_in_impact_zone(
            soldier["x"] + i, soldier["y"] + j, x, y, impact_radius)]
        if safe_moves:
            dx, dy = random.choice(safe_moves)
            soldier["x"] += dx
            soldier["y"] += dy
        else:
            soldier["alive"] = False


def is_alive(soldier_id):
    print(f"Checking if Soldier {soldier_id} is alive")
    soldier = next((s for s in soldiers if s["id"] == soldier_id), None)
    return soldier["alive"] if soldier else False


def elect_new_commander():
    alive_soldiers = [s for s in soldiers if s["alive"]]
    new_commander = random.choice(alive_soldiers)
    return new_commander["id"]


def get_soldiers_status():
    return soldiers


if __name__ == "__main__":
    client_server = xmlrpc.server.SimpleXMLRPCServer(
        ("0.0.0.0", 8000), allow_none=True)
    client_server.register_function(
        notify_missile_approach, "notify_missile_approach")
    client_server.register_function(is_alive, "is_alive")
    client_server.register_function(elect_new_commander, "elect_new_commander")
    client_server.register_function(get_soldiers_status, "get_soldiers_status")
    print(f"Client server started on port 8000")
    client_server.serve_forever()
