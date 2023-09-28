import xmlrpc.server
import xmlrpc.client
from config import N, M, t, Si, T
from utils import printLayout
import random
import time

# Global state for the battlefield
battlefield = [[0 for _ in range(N)] for _ in range(N)]
# Initialize the commander to a valid soldier ID
commander = random.randint(1, M)
client_url = "http://172.17.49.76:8000/"


def missile_approaching():
    # x, y = random.randint(3, N-4), random.randint(3, N-4)
    x, y = random.randint(0, N-1), random.randint(0, N-1)
    impact_radius = random.choice([1, 2, 3, 4])

    print(
        f"Missile approaching at ({x}, {y}) with impact radius {impact_radius}")

    # Notify the client about the missile
    try:
        client = xmlrpc.client.ServerProxy(client_url)
        client.notify_missile_approach(x, y, impact_radius)
    except Exception as e:
        print(f"Failed to notify client at {client_url}. Error: {e}")

    # Check for casualties and update the commander if necessary
    check_commander_status()
    return x, y, impact_radius


def check_commander_status():
    global commander
    print(f"Checking status of commander: Soldier {commander}")
    try:
        client = xmlrpc.client.ServerProxy(client_url)
        if not client.is_alive(commander):
            print("\nCommander died!")
            commander = client.elect_new_commander()
            print(
                f"Election took place. New commander chosen: Soldier {commander}")
    except Exception as e:
        print(
            f"Failed to check commander status or elect a new commander. Error: {e}")


if __name__ == "__main__":
    print("Server started. Waiting for initial setup...")
    time.sleep(5)  # Wait for 5 seconds before starting missile strikes

    # Calculate the number of iterations based on the missile strike interval `t`
    num_iterations = T // t

    for _ in range(num_iterations):
        time.sleep(t)
        x, y, impact_radius = missile_approaching()
        client = xmlrpc.client.ServerProxy(client_url)
        soldiers = client.get_soldiers_status()
        printLayout(battlefield, soldiers, (x, y), impact_radius, commander)
