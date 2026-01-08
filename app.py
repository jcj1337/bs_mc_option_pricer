import streamlit as st

from src.bs import bs_call, bs_put
from src.mc import mc_call, mc_put

st.title("Option Pricer: Black–Scholes vs Monte Carlo")

S = st.number_input("Spot price S", value=100.0)
K = st.number_input("Strike K", value=100.0)
T = st.number_input("Time to maturity T (years)", value=1.0, min_value=1e-6)
R = st.number_input("Risk-free rate R", value=0.05)
sigma = st.number_input("Volatility sigma", value=0.2, min_value=1e-6)

N = st.slider("Monte Carlo simulations N", 0,  10000, 1000, step=100)
seed = st.number_input("Seed", value=0, step=1)

# Black–Scholes
bsC = bs_call(S, K, T, R, sigma)
bsP = bs_put(S, K, T, R, sigma)

# Monte Carlo
mcC, ciC = mc_call(S, K, T, R, sigma, N=N, seed=seed)
mcP, ciP = mc_put(S, K, T, R, sigma, N=N, seed=seed)

col1, col2 = st.columns(2)

# Display
with col1:
    st.subheader("Call")
    st.write(f"Black–Scholes: **{bsC:.4f}**")
    st.write(f"Monte Carlo: **{mcC:.4f}**")
    st.write(f"95% CI: ({ciC[0]:.4f}, {ciC[1]:.4f})")

with col2:
    st.subheader("Put")
    st.write(f"Black–Scholes: **{bsP:.4f}**")
    st.write(f"Monte Carlo: **{mcP:.4f}**")
    st.write(f"95% CI: ({ciP[0]:.4f}, {ciP[1]:.4f})")
import streamlit as st

from src.bs import bs_call, bs_put
from src.mc import mc_call, mc_put

st.title("Option Pricer: Black–Scholes vs Monte Carlo")

S = st.number_input("Spot price S", value=100.0)
K = st.number_input("Strike K", value=100.0)
T = st.number_input("Time to maturity T (years)", value=1.0, min_value=1e-6)
R = st.number_input("Risk-free rate R", value=0.05)
sigma = st.number_input("Volatility sigma", value=0.2, min_value=1e-6)

N = st.slider("Monte Carlo simulations N", 0, 500_000, 100_000, step=1_000)
seed = st.number_input("Random seed", value=0, step=1)

# Black–Scholes
bsC = bs_call(S, K, T, R, sigma)
bsP = bs_put(S, K, T, R, sigma)

# Monte Carlo
mcC, ciC = mc_call(S, K, T, R, sigma, N=N, seed=seed)
mcP, ciP = mc_put(S, K, T, R, sigma, N=N, seed=seed)

col1, col2 = st.columns(2)

# Display
with col1:
    st.subheader("Call")
    st.write(f"Black–Scholes: **{bsC:.4f}**")
    st.write(f"Monte Carlo: **{mcC:.4f}**")
    st.write(f"95% CI: ({ciC[0]:.4f}, {ciC[1]:.4f})")

with col2:
    st.subheader("Put")
    st.write(f"Black–Scholes: **{bsP:.4f}**")
    st.write(f"Monte Carlo: **{mcP:.4f}**")
    st.write(f"95% CI: ({ciP[0]:.4f}, {ciP[1]:.4f})")