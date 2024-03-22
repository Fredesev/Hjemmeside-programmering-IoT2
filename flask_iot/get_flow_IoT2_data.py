from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

def generate_flow_data():
    # Simulere antal liter vand per time
    hours = np.arange(1, 25)
    water_flow = np.random.randint(1, 10, size=24)  # Tilfældige værdier mellem 1 og 10 liter

    # Generer bar diagrammet
    plt.figure(figsize=(10, 6))
    plt.bar(hours, water_flow, color='pink')  # Pink farve
    plt.xlabel('Time (hours)')
    plt.ylabel('Water Flow (Liters)')
    plt.title('Water Flow Data')

    # Tilføjer dummy tekst på diagrammet
    for i in range(len(hours)):
        plt.text(hours[i], water_flow[i], str(water_flow[i]), ha='center', va='bottom')

    # Gem diagrammet som en BytesIO-objekt
    flow_data = BytesIO()
    plt.savefig(flow_data, format='png')
    flow_data.seek(0)

    plt.close()  # Luk plot for at frigive ressourcer

    return flow_data





            
      