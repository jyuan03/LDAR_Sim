import pandas as pd
import os

from LDAR_Sim.testing.unit_testing.test_sensitivity_analysis.test_parameter_variator.test_vary_parameter_values import \
    get_simulation_parameters_1


def regional_LDARSim_resultprocessing():
    basecase_df = pd.DataFrame()
    triannual_df = pd.DataFrame()
    crew_count_df = pd.DataFrame()
    mdl_df = pd.DataFrame()
    site_num_df = pd.DataFrame()
    site_num_180_df = pd.DataFrame()
    ogi_persite_high_df = pd.DataFrame()
    ogi_sensor_df = pd.DataFrame()
    johnson_df = pd.DataFrame()
    all_tech_df = pd.DataFrame()

    simulation_versions = ['basecase', 'crew_count', 'mdl', 'site_num', 'site_num_180', 'ogi_persite_high', 'ogi_sensor', 'triannual', 'johnson']
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
                all_tech_df = pd.concat([all_tech_df,annual_regional_combined_data])

            elif simulation == 'triannual':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/triannual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                triannual_df = pd.concat([triannual_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'crew_count':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                crew_count_df = pd.concat([crew_count_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df,annual_regional_combined_data])

            elif simulation == 'mdl':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                mdl_df = pd.concat([mdl_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'site_num':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                site_num_df = pd.concat([site_num_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'site_num_180':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                site_num_180_df = pd.concat([site_num_180_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


            elif simulation == 'ogi_persite_high':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                ogi_persite_high_df = pd.concat([ogi_persite_high_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


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
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


            elif simulation == 'johnson':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').mean()
                annual_regional_combined_data = annual_regional_combined_data.sort_values(
                    by=['Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                johnson_df = pd.concat([johnson_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

    ldarsim_simulation_all = pd.concat([basecase_df, triannual_df, crew_count_df, mdl_df, site_num_df, site_num_180_df, ogi_persite_high_df, ogi_sensor_df, johnson_df])

    figure1_difference_regionvscases = ldarsim_simulation_all.pivot(index='Region', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    simulations_nobasecase = ['crew_count', 'mdl', 'site_num', 'site_num_180', 'ogi_persite_high',
                           'ogi_sensor', 'triannual', 'johnson']
    for simulation in simulations_nobasecase:
        figure1_difference_regionvscases[simulation] = figure1_difference_regionvscases[simulation] - figure1_difference_regionvscases['basecase']

    figure1_difference_regionvscases = ldarsim_simulation_all.pivot(index='Region', columns='Simulation', values='Program Name')
    figure1_label_regionvscases = ldarsim_simulation_all.pivot(index='Region', columns='Simulation', values='Program Name')

    bv_samplecase = all_tech_df[all_tech_df['Region'] == 'BV']
    bv_samplecase = bv_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        bv_samplecase[simulation] = bv_samplecase[simulation] - bv_samplecase['basecase']
    dv_samplecase = all_tech_df[all_tech_df['Region'] == 'DV']
    dv_samplecase = dv_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        dv_samplecase[simulation] = dv_samplecase[simulation] - dv_samplecase['basecase']
    edm_samplecase = all_tech_df[all_tech_df['Region'] == 'EDM']
    edm_samplecase = edm_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        edm_samplecase[simulation] = edm_samplecase[simulation] - edm_samplecase['basecase']
    gp_samplecase = all_tech_df[all_tech_df['Region'] == 'GP']
    gp_samplecase = gp_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        gp_samplecase[simulation] = gp_samplecase[simulation] - gp_samplecase['basecase']
    mdp_samplecase = all_tech_df[all_tech_df['Region'] == 'MDP']
    mdp_samplecase = mdp_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        mdp_samplecase[simulation] = mdp_samplecase[simulation] - mdp_samplecase['basecase']
    mh_samplecase = all_tech_df[all_tech_df['Region'] == 'MH']
    mh_samplecase = mh_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        mh_samplecase[simulation] = mh_samplecase[simulation] - mh_samplecase['basecase']
    rd_samplecase = all_tech_df[all_tech_df['Region'] == 'RD']
    rd_samplecase = rd_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        rd_samplecase[simulation] = rd_samplecase[simulation] - rd_samplecase['basecase']
    sl_samplecase = all_tech_df[all_tech_df['Region'] == 'SL']
    sl_samplecase = sl_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        sl_samplecase[simulation] = sl_samplecase[simulation] - sl_samplecase['basecase']
    ww_samplecase = all_tech_df[all_tech_df['Region'] == 'WW']
    ww_samplecase = ww_samplecase.pivot(index='Program Name', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    for simulation in simulations_nobasecase:
        ww_samplecase[simulation] = ww_samplecase[simulation] - ww_samplecase['basecase']


    basecase_df.to_csv('basecase1.csv')
    triannual_df.to_csv('sensitivity_triannual1.csv')
    crew_count_df.to_csv('sensitivity_crew_count1.csv')
    mdl_df.to_csv('sensitivity_mdl1.csv')
    site_num_df.to_csv('sensitivity_site_num1.csv')
    site_num_180_df.to_csv('sensitivity_site_num_1801.csv')
    ogi_persite_high_df.to_csv('sensitivity_ogi_persite_high1.csv')
    ogi_sensor_df.to_csv('sensitivity_ogi_sensor1.csv')
    johnson_df.to_csv('johnson1.csv')
    ldarsim_simulation_all.to_csv('ldarsim_simulation_all.csv')
    figure1_difference_regionvscases.to_csv('heatmap_difference_regionvscases.csv')
    figure1_label_regionvscases.to_csv('heatmap_label_regionvscases.csv')
    bv_samplecase.to_csv('heatmap_casesvstech_BV.csv')
    dv_samplecase.to_csv('heatmap_casesvstech_DV.csv')
    edm_samplecase.to_csv('heatmap_casesvstech_EDM.csv')    gp_samplecase.to_csv('heatmap_casesvstech_GP.csv')
    mdp_samplecase.to_csv('heatmap_casesvstech_MDP.csv')
    mh_samplecase.to_csv('heatmap_casesvstech_MH.csv')
    rd_samplecase.to_csv('heatmap_casesvstech_RD.csv')
    sl_samplecase.to_csv('heatmap_casesvstech_SL.csv')
    ww_samplecase.to_csv('heatmap_casesvstech_WW.csv')


    return

def run_LDAR_sim():
    simulation_versions = ['basecase','basecase_emissions_johnson_test','cost_sensitivity','crew_sensitivity','mdl_sensitivity','OGI_sensor', 'triannual_survey', 'site_number' , 'site_number_180'] #'site_number' , 'site_number_180'
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
