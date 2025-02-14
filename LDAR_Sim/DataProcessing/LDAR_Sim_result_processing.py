import pandas as pd
import os

def regional_LDARSim_resultprocessing():
    basecase_df = pd.DataFrame()
    triannual_df = pd.DataFrame()
    crew_count_df = pd.DataFrame()
    mdl_df = pd.DataFrame()
    site_num_df = pd.DataFrame()
    ogi_persite_high_df = pd.DataFrame()

    simulation_versions = ['basecase', 'crew_count', 'mdl', 'site_num', 'ogi_persite_high', 'triannual']
    regionslist = ['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']
    for simulation in simulation_versions:
        for region in regionslist:
            if simulation == 'basecase':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_raw_data =
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                basecase_df = pd.concat([basecase_df,annual_regional_combined_data.head(1)])

            elif simulation == 'triannual':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/triannual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                triannual_df = pd.concat([triannual_df,annual_regional_combined_data.head(1)])

            elif simulation == 'crew_count':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                crew_count_df = pd.concat([crew_count_df,annual_regional_combined_data.head(1)])

            elif simulation == 'mdl':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                mdl_df = pd.concat([mdl_df,annual_regional_combined_data.head(1)])

            elif simulation == 'site_num':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                site_num_df = pd.concat([site_num_df,annual_regional_combined_data.head(1)])

            elif simulation == 'ogi_persite_high':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                ogi_persite_high_df = pd.concat([ogi_persite_high_df,annual_regional_combined_data.head(1)])

    basecase_df.to_csv('basecase.csv')
    triannual_df.to_csv('sensitivity_triannual.csv')
    crew_count_df.to_csv('sensitivity_crew_count.csv')
    mdl_df.to_csv('sensitivity_mdl.csv')
    site_num_df.to_csv('sensitivity_site_num.csv')
    ogi_persite_high_df.to_csv('sensitivity_ogi_persite_high.csv')


    return

def run_LDAR_sim():
    simulation_versions = ['basecase', 'cost_sensitivity', 'mdl_sensitivity', 'site_number', 'triannual_survey'] #, 'crew_sensitivity']
    regionslist = ['DV'] #['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']
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

    return

if __name__ == '__main__':
    # regional_LDARSim_resultprocessing()
    run_LDAR_sim()
