import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Function for the first app (Energy and Concentration Calculation)
def calculate_values(diameter, height):
    E_rate = 0.00196  # W/cm^2
    V_m = (height * (math.pi * diameter ** 2) / 4) / 2  # m^3
    V = V_m * float(1e9)  # mm^3
    SA_ratio = 20  # mm^2/mm^3
    SA = V * SA_ratio * 0.01  # cm^2
    P_9g = E_rate * SA  # W
    P_per_g = P_9g / 9  # W/(g/L)
    
    Conc = np.linspace(0, 2, 100)  # Glucose concentrations
    P = P_per_g * Conc  # W
    E_year = P * float(24 * 365 * 1e-6)  # MWh
    return Conc, E_year

# Function for the second app (Glucose Conversion)
def convert_glucose(mM_concentration):
    molar_mass_glucose = 180.16  # molar mass of glucose in mg/mmol
    return mM_concentration * molar_mass_glucose

# Streamlit app UI setup with 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.title("Interactive XY Plot")
    diameter = st.slider('Diameter (m)', 0.1, 10.0, 3.57, key='diameter')
    height = st.slider('Height (m)', 0.1, 10.0, 5.0, key='height')
    if st.button('Calculate', key='calculate1'):
        Conc, E_year = calculate_values(diameter, height)
        fig, ax = plt.subplots()
        ax.plot(Conc, E_year)
        ax.set_xlabel('Glucose Concentration (g/L)')
        ax.set_ylabel('Energy per year (MWh)')
        ax.set_title('Glucose Concentration vs Annual Energy')
        st.pyplot(fig)

with col2:
    st.title('Glucose Concentration Converter')
    mM_input = st.number_input('Enter the glucose concentration in mM:', min_value=0.0, format='%f', key='mM_input')
    if st.button('Convert', key='convert'):
        mg_L_result = convert_glucose(mM_input)
        st.write(f'{mM_input} mM is equivalent to {mg_L_result} mg/L.')

with col3:
    # This column is intentionally left blank
    st.write("")

