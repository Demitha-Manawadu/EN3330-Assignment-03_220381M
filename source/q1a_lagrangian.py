from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

x = np.linspace(-1, 3, 500)
plt.figure(figsize=(7.2, 4.6))

for mu in [0, 1, 2, 3]:
    L = x**2 + mu * (1 - x)
    plt.plot(x, L, label=fr'$\mu={mu}$')

    x_min = mu / 2
    L_min = x_min**2 + mu * (1 - x_min)
    plt.scatter([x_min], [L_min], s=35)

plt.axvline(1, linestyle='--', linewidth=1, label='$x=1$ boundary')
plt.xlabel('$x$')
plt.ylabel(r'$L(\mu,x)$')
plt.title('Q1(a): Lagrangian curves and their minimizers')
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'q1a_lagrangian.png', dpi=220, bbox_inches='tight')
plt.show()
