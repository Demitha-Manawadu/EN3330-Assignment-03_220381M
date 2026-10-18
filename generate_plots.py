from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parent / "plots"
OUTPUT_DIR.mkdir(exist_ok=True)

# ---------- Q1(a): L(mu, x) for mu = 0, 1, 2, 3 ----------
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
plt.close()

# ---------- Q1(b): dual function ----------
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
plt.close()

# ---------- Q1(c): primal function g(x) ----------
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
plt.close()

# ---------- Q2(a): saddle-point plots ----------
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
plt.close(fig)

# ---------- Q3(b): three lines + lower envelope ----------
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
plt.close()

print(f'Plots saved in: {OUTPUT_DIR}')
for name in [
    'q1a_lagrangian.png',
    'q1b_dual.png',
    'q1c_primal.png',
    'q2a_saddle.png',
    'q3b_lower_envelope.png',
]:
    print(f'  - {name}')
