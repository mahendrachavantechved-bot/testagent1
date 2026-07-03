
from agents.agent import DeliveryAgent
agents=[DeliveryAgent(i) for i in range(1,4)]
lines=["Food Delivery Simulation\n"]
print("Food Delivery Simulation")
for t in range(1,5):
    print(f"\nTime Step {t}")
    lines.append(f"Time Step {t}")
    for a in agents:
        s=a.step()
        out=f"Rider {a.id}: {s}"
        print(out); lines.append(out)
open("output/results.txt","w").write("\n".join(lines))
print("\nResults saved to output/results.txt")
