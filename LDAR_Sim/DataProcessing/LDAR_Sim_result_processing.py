import pandas as pd
import os

def regional_LDARSim_resultprocessing():
    basecase_df = pd.DataFrame()
    triannual_df = pd.DataFrame()
    crew_count_df = pd.DataFrame()
    mdl_df = pd.DataFrame()
    site_num_df = pd.DataFrame()
    site_num_180_df = pd.DataFrame()
    ogi_persite_high_df = pd.DataFrame()
    ogi_sensor_df = pd.DataFrame()

    simulation_versions = ['basecase', 'crew_count', 'mdl', 'site_num', 'site_num_180', 'ogi_persite_high', 'ogi_sensor', 'triannual']
    regionslist = ['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']
    for simulation in simulation_versions:
        for region in regionslist:
            if simulation == 'basecase':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                basecase_df = pd.concat([basecase_df,annual_regional_combined_data.head(1)])

            elif simulation == 'triannual':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/triannual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                triannual_df = pd.concat([triannual_df,annual_regional_combined_data.head(1)])

            elif simulation == 'crew_count':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                crew_count_df = pd.concat([crew_count_df,annual_regional_combined_data.head(1)])

            elif simulation == 'mdl':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                mdl_df = pd.concat([mdl_df,annual_regional_combined_data.head(1)])

            elif simulation == 'site_num':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                site_num_df = pd.concat([site_num_df,annual_regional_combined_data.head(1)])

            elif simulation == 'site_num_180':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                site_num_180_df = pd.concat([site_num_180_df,annual_regional_combined_data.head(1)])

            elif simulation == 'ogi_persite_high':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                ogi_persite_high_df = pd.concat([ogi_persite_high_df,annual_regional_combined_data.head(1)])

            elif simulation == 'ogi_sensor':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(
                    by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                ogi_sensor_df = pd.concat([ogi_sensor_df, annual_regional_combined_data.head(1)])

    ldarsim_simulation_all = pd.concat([basecase_df, triannual_df, crew_count_df, mdl_df, site_num_df, site_num_180_df, ogi_persite_high_df, ogi_sensor_df])

    basecase_df.to_csv('basecase1.csv')
    triannual_df.to_csv('sensitivity_triannual1.csv')
    crew_count_df.to_csv('sensitivity_crew_count1.csv')
    mdl_df.to_csv('sensitivity_mdl1.csv')
    site_num_df.to_csv('sensitivity_site_num1.csv')
    site_num_180_df.to_csv('sensitivity_site_num_1801.csv')
    ogi_persite_high_df.to_csv('sensitivity_ogi_persite_high1.csv')
    ogi_sensor_df.to_csv('sensitivity_ogi_sensor1.csv')
    ldarsim_simulation_all.to_csv('ldarsim_simulation_all.csv)')

    return

def run_LDAR_sim():
    simulation_versions = ['OGI_sensor'] #'crew_sensitivity', 'cost_sensitivity'], 'basecase', 'mdl_sensitivity', 'triannual_survey']#, 'site_number' , 'site_number_180'] #'site_number' , 'site_number_180'
    regionslist = ['BV','DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']#
    for simulation in simulation_versions:
        for region in regionslist:
            if simulation == 'triannual_survey':
                annualnumber = 'triannual'
            else:
                annualnumber = 'annual'

            if simulation == 'cost_sensitivity':
                for cost_type in ['OGI_persitehigh']: #'OGI_perhour',
                    filename = f'python C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/src/ldar_sim_run.py --in_dir ./simulations/{simulation}/{region}/{annualnumber}/{cost_type}'
                    os.system(filename)

            else:
                filename = f'python C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/src/ldar_sim_run.py --in_dir ./simulations/{simulation}/{region}/{annualnumber}'
                os.system(filename)
# "python C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/src/ldar_sim_run.py --in_dir ./simulations/triannual_survey/BV/triannual"


    return

if __name__ == '__main__':
    regional_LDARSim_resultprocessing()
    # run_LDAR_sim()
