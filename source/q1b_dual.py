from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

mu = np.linspace(0, 5, 500)
d = mu - mu**2 / 4

plt.figure(figsize=(7.2, 4.4))
plt.plot(mu, d, label=r'$d(\mu)=\mu-\mu^2/4$')
plt.scatter([2], [1], s=45, zorder=3, label=r'$(\mu^*,d^*)=(2,1)$')
plt.axvline(2, linestyle='--', linewidth=1)
plt.axhline(1, linestyle='--', linewidth=1)
plt.xlabel(r'$\mu$')
plt.ylabel(r'$d(\mu)$')
plt.title('Q1(b): Dual function')
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'q1b_dual.png', dpi=220, bbox_inches='tight')
plt.show()
