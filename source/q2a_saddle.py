from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0))

mu = np.linspace(0, 5, 300)
axes[0].plot(mu, np.ones_like(mu))
axes[0].scatter([2], [1], s=40)
axes[0].set_xlabel(r'$\mu$')
axes[0].set_ylabel(r'$L(\mu,1)$')
axes[0].set_title(r'Fix $x^*=1$: $L(\mu,1)=1$')
axes[0].set_ylim(0, 2)
axes[0].grid(alpha=0.25)

x = np.linspace(-1, 3, 400)
L = (x - 1)**2 + 1
axes[1].plot(x, L)
axes[1].scatter([1], [1], s=40)
axes[1].set_xlabel('$x$')
axes[1].set_ylabel('$L(2,x)$')
axes[1].set_title(r'Fix $\mu^*=2$: $L(2,x)=(x-1)^2+1$')
axes[1].grid(alpha=0.25)

fig.suptitle('Q2(a): Saddle-point view')
fig.tight_layout()
fig.savefig(OUTPUT_DIR / 'q2a_saddle.png', dpi=220, bbox_inches='tight')
plt.show()
