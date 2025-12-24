import numpy as np
from scipy.stats import norm

def mc_call(S, K, T, R, sigma, N=100000, seed=0):
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(N)
    ST = S * np.exp((R - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0.0)
    disc_payoff = np.exp(-R * T) * payoff
    price = disc_payoff.mean()
    ci95 = 1.96 * disc_payoff.std(ddof=1) / np.sqrt(N)
    return price, (price - ci95, price + ci95)

def mc_put(S, K, T, R, sigma, N=100000, seed=0):
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(N)
    ST = S * np.exp((R - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(K - ST, 0.0)
    disc_payoff = np.exp(-R * T) * payoff
    price = disc_payoff.mean()
    ci95 = 1.96 * disc_payoff.std(ddof=1) / np.sqrt(N)
    return price, (price - ci95, price + ci95)

