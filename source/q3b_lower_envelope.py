from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

mu = np.linspace(0, 5, 600)
L0 = mu
L1 = np.ones_like(mu)
L2 = 4 - mu
lower_envelope = np.minimum(np.minimum(L0, L1), L2)
exact_dual = mu - mu**2 / 4

plt.figure(figsize=(7.5, 4.6))
plt.plot(mu, L0, label=r'$L(\mu,0)=\mu$')
plt.plot(mu, L1, label=r'$L(\mu,1)=1$')
plt.plot(mu, L2, label=r'$L(\mu,2)=4-\mu$')
plt.plot(mu, lower_envelope, linewidth=3,
         label='lower envelope of the three lines')
plt.plot(mu, exact_dual, linestyle='--', linewidth=1.5,
         label=r'exact dual $d(\mu)$')
plt.xlabel(r'$\mu$')
plt.ylabel('value')
plt.title('Q3(b): Lower envelope and concavity')
plt.grid(alpha=0.25)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'q3b_lower_envelope.png', dpi=220, bbox_inches='tight')
plt.show()
