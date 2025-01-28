import pandas as pd
import os

def regional_LDARSim_resultprocessing():

    regions = ['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']

    annual_regional_average_cost = pd.DataFrame()
    triannual_regional_average_cost = pd.DataFrame()

    for region in regions:

        annual_regional_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/annual_LDARSim4_{region}/Cost Summary.csv'
        annual_regional_raw_data = pd.read_csv(annual_regional_path)
        annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
        annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
        annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
        annual_regional_average_cost = pd.concat([annual_regional_average_cost,annual_regional_combined_data])
        annual_regional_average_cost['Region'] = region

        triannual_regional_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/annual_LDARSim4_{region}/Cost Summary.csv'
        triannual_regional_raw_data = pd.read_csv(triannual_regional_path)
        triannual_regional_combined_data = triannual_regional_raw_data.groupby('Program Name').mean()
        triannual_regional_combined_data = triannual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
        triannual_regional_combined_data = triannual_regional_combined_data.reset_index(names=['Program Name'])
        triannual_regional_average_cost = pd.concat([triannual_regional_average_cost,triannual_regional_combined_data])
        triannual_regional_average_cost['Region'] = region

    annual_regional_average_cost.to_csv('LDAR_Sim_regional_annual.csv')

    triannual_regional_average_cost.to_csv('LDAR_Sim_regional_triannual.csv')
    return

def run_LDAR_sim():
    regionslist = ['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']
    annualnumberlist = ['triannual', 'annual']
    for region in regionslist:
        for annualnumber in annualnumberlist:
            filename = f' python C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/src/ldar_sim_run.py --in_dir ./simulations/Sim_1crewsOGI/{region}/{annualnumber}'
            os.system(filename)

    return

if __name__ == '__main__':
    regional_LDARSim_resultprocessing()
    # run_LDAR_sim()
