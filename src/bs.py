import numpy as np
from scipy.stats import norm

def d1_calc(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2_calc(S, K, T, r, sigma):
    return d1_calc(S, K, T, r, sigma) - sigma * np.sqrt(T)

def bs_call(S, K, T, r, sigma):
    d1 = d1_calc(S, K, T, r, sigma)
    d2 = d2_calc(S, K, T, r, sigma)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def bs_put(S, K, T, r, sigma):
    d1 = d1_calc(S, K, T, r, sigma)
    d2 = d2_calc(S, K, T, r, sigma)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)