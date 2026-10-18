from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

x = np.linspace(-1, 3, 600)
feasible_x = x[x >= 1]

plt.figure(figsize=(7.2, 4.4))
plt.axvspan(-1, 1, alpha=0.12)
plt.plot(feasible_x, feasible_x**2, linewidth=2,
         label=r'$g(x)=x^2$ for $x\geq1$')
plt.axvline(1, linestyle='--', linewidth=1, label='$x=1$ boundary')
plt.scatter([1], [1], s=45, zorder=3, label='minimum $(1,1)$')
plt.text(-0.55, 5.5, r'$g(x)=+\infty$ for $x<1$', ha='center')
plt.xlim(-1, 3)
plt.ylim(0, 9.5)
plt.xlabel('$x$')
plt.ylabel('$g(x)$')
plt.title('Q1(c): Extended-valued primal function')
plt.grid(alpha=0.25)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'q1c_primal.png', dpi=220, bbox_inches='tight')
plt.show()
