# Calculate for one LV
import pandas as pd

def carbon_intensity(fuel_type):
    """Returns the amount of carbon dioxide (CO2) emitted per lt of fuel consumed
    Parameters
    ----------
    fuel_type : str,
        Should be "Petrol" or "Diesel"

    Returns
    -------
    c_int_val : int
    """
    file_path = "pytransportghg/data/carbon_intensity.xlsx"
    c_int = pd.read_excel(file_path)
    fuel_type = fuel_type.lower()
    c_int_val = c_int.loc[c_int['fuel_type']== fuel_type, 'Co2_emission'].values[0]
    return c_int_val

def fuel_eff(veh_type, veh_age):
    """Calculates fuel efficiency, volume of fuel consumed by a vehicle per 
    unit of distance traveled 
    Parameters
    ----------
    veh_type: str
        Type of vehicle. It should be;
            LV for light vehicles;
            MV for medium vehicles;
            HV for heavy vehicles;
            TW for two-wheelers;
        TODO: Add all the vehicle types mentioned in RST Regulations.
    
    veh_age: int
        Age of the vehicle. It should be less than 50 years old. If the value is
        more than 50 years old, it will be converted to 50.
        TODO: Add functionality to cap veh. age at 50.

    Returns
    -------
    current_fuel_eff: int
        Current fuel efficiency of a vehicle of type `veh_type` and `veh_age`
        old. It has unit `lt/km`.

    """
    file_path = "pytransportghg/data/fuel_eff.xlsx"
    fuel = pd.read_excel(file_path)
    initial_fuel_eff = fuel[fuel['Veh_type'] == veh_type]['mileage'].values[0]
    AGE_COEF = 0.02
    current_fuel_eff = 1/(initial_fuel_eff *(1 - AGE_COEF*veh_age))
    return current_fuel_eff

def emission_coef(fuel_type, veh_type, veh_age):
    """The function calculates the emission coefficient which denotes
    the gm. of Co2 emitted per km of distance traveled by a vehicle. 
    
    Parameters
    ----------
    fuel_type : str,
        Should be "Petrol" or "Diesel"

    veh_type: str
        Type of vehicle. It should be;
            LV for light vehicles;
            MV for medium vehicles;
            HV for heavy vehicles;
            TW for two-wheelers;
        TODO: Add all the vehicle types mentioned in RST Regulations.
    
    veh_age: int
        Age of the vehicle. It should be less than 50 years old. If the value is
        more than 50 years old, it will be converted to 50.
        TODO: Add functionality to cap veh. age at 50.
    """
    emission_coef = carbon_intensity(fuel_type) * fuel_eff(veh_type, veh_age)
    return emission_coef