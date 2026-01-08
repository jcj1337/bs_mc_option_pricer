Introduction to options pricing and streamlit. 

This project prices European call/put options. (1) the Black–Scholes closed-form formula and (2) a Monte Carlo estimate that simulates risk-neutral prices at time t and averages the discounted payoff.

The app takes in the 5 parameters for the Black-Scholes model and number of iterations, N, for Monte-Carlo simulations.

See the IPYNB for more extensive documentation (demo), the app is basically just for academic exercise to confirm that we can use MC simulations to estimate the Black Scholes closed-formed solution and to create some sort of basic UI.

To run: 
- pip install -r requirements.txt 
- streamlit run app.py


The app takes in parameters for the Black-Scholes model and number of iterations, N, for Monte-Carlo simulations.
Both values straight from the Black-Scholes formula and the MC approximation are displayed, see the IPYNB for more extensive documentation (demo).