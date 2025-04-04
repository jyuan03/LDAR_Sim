import pandas as pd
import os
import numpy as np


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
    coverage_df = pd.DataFrame()
    multisimulation_df = pd.DataFrame()
    all_tech_df = pd.DataFrame()
    mdl_lowogi_df = pd.DataFrame()
    mdl_lowdrone_df = pd.DataFrame()
    mdl_lowstationary_df = pd.DataFrame()
    multiyear_df = pd.DataFrame()

    GWP = 28

    simulation_versions = ['basecase', 'multisimulation','coverage','crew_count', 'mdl', 'site_num', 'site_num_180',
                           'ogi_persite_high', 'ogi_sensor', 'triannual', 'johnson', 'mdl_lowogi', 'mdl_lowdrone',
                           'mdl_lowstationary', 'multiyear']
    regionslist = ['BV', 'DV', 'EDM','GP','MDP', 'MH', 'RD','SL','WW']
    for simulation in simulation_versions:
        for region in regionslist:
            if simulation == 'basecase':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                basecase_df = pd.concat([basecase_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df,annual_regional_combined_data])

            elif simulation == 'triannual':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/triannual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                triannual_df = pd.concat([triannual_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'crew_count':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                crew_count_df = pd.concat([crew_count_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df,annual_regional_combined_data])

            elif simulation == 'mdl':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data[
                                                                                           'Total Cost ($)'] / (
                                                                                                   annual_regional_combined_data[
                                                                                                       'Mitigated Methane (kg)'] * GWP / 1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(
                    by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                mdl_df = pd.concat([mdl_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'site_num':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data[
                                                                                           'Total Cost ($)'] / (
                                                                                                   annual_regional_combined_data[
                                                                                                       'Mitigated Methane (kg)'] * GWP / 1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(
                    by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                site_num_df = pd.concat([site_num_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'site_num_180':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                site_num_180_df = pd.concat([site_num_180_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


            elif simulation == 'ogi_persite_high':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                ogi_persite_high_df = pd.concat([ogi_persite_high_df,annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


            elif simulation == 'ogi_sensor':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                ogi_sensor_df = pd.concat([ogi_sensor_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'coverage':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                coverage_df = pd.concat([coverage_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'multisimulation':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                multisimulation_df = pd.concat([multisimulation_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


            elif simulation == 'johnson':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                johnson_df = pd.concat([johnson_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'mdl_lowogi':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                mdl_lowogi_df = pd.concat([mdl_lowogi_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])

            elif simulation == 'mdl_lowdrone':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                mdl_lowdrone_df = pd.concat([mdl_lowdrone_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])
            elif simulation == 'mdl_lowstationary':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                mdl_lowstationary_df = pd.concat([mdl_lowstationary_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])
            elif simulation == 'multiyear':
                datapath_path = f'C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/outputs/sensitivity/{simulation}/annual_LDARSim4_{region}/Cost Summary.csv'
                annual_regional_raw_data = pd.read_csv(datapath_path)
                annual_regional_combined_data = annual_regional_raw_data.groupby('Program Name').sum()
                annual_regional_combined_data = annual_regional_combined_data.reset_index(names=['Program Name'])
                annual_regional_combined_data['NEW Mitigation Ratio ($/tonne CO2e)'] = annual_regional_combined_data['Total Cost ($)']/(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000)
                annual_regional_combined_data = annual_regional_combined_data.sort_values(by=['NEW Mitigation Ratio ($/tonne CO2e)'])
                annual_regional_combined_data['Region'] = region
                annual_regional_combined_data['Simulation'] = simulation
                annual_regional_combined_data['netmitigation cost $/tCO2'] \
                    = ((annual_regional_combined_data['Total Cost ($)'] - annual_regional_combined_data['Value of Mitigated Methane ($)'])
                       /(annual_regional_combined_data['Mitigated Methane (kg)']*GWP/1000))
                annual_regional_combined_data['mitigated methane Mt'] = annual_regional_combined_data['Mitigated Methane (kg)']/10**9
                multiyear_df = pd.concat([multiyear_df, annual_regional_combined_data.head(1)])
                all_tech_df = pd.concat([all_tech_df, annual_regional_combined_data])


    ldarsim_simulation_all = pd.concat([basecase_df, triannual_df, crew_count_df, mdl_df, site_num_df, site_num_180_df,
                                        ogi_persite_high_df, ogi_sensor_df, johnson_df, coverage_df, multisimulation_df,
                                        mdl_lowogi_df, mdl_lowdrone_df, mdl_lowstationary_df, multiyear_df])
    ldarsim_simulation_all = ldarsim_simulation_all.sort_values('Region')

    figure1_difference_regionvscases = ldarsim_simulation_all.pivot(index='Region', columns='Simulation', values='Mitigation Ratio ($/tonne CO2e)')
    simulations_nobasecase = ['multisimulation', 'coverage', 'crew_count', 'mdl', 'site_num', 'site_num_180', 'ogi_persite_high',
                           'ogi_sensor', 'triannual', 'johnson',  'mdl_lowogi', 'mdl_lowdrone', 'mdl_lowstationary', 'multiyear']

    for simulation in simulations_nobasecase:
        figure1_difference_regionvscases[simulation] = figure1_difference_regionvscases[simulation] - figure1_difference_regionvscases['basecase']

    figure1_label_regionvscases = ldarsim_simulation_all.pivot(index='Region', columns='Simulation', values='Program Name')

    bv_samplecase = all_tech_df[all_tech_df['Region'] == 'BV']
    bv_samplecase = bv_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     bv_samplecase[simulation] = bv_samplecase[simulation] - bv_samplecase['basecase']
    dv_samplecase = all_tech_df[all_tech_df['Region'] == 'DV']
    dv_samplecase = dv_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     dv_samplecase[simulation] = dv_samplecase[simulation] - dv_samplecase['basecase']
    edm_samplecase = all_tech_df[all_tech_df['Region'] == 'EDM']
    edm_samplecase = edm_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     edm_samplecase[simulation] = edm_samplecase[simulation] - edm_samplecase['basecase']
    gp_samplecase = all_tech_df[all_tech_df['Region'] == 'GP']
    gp_samplecase = gp_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     gp_samplecase[simulation] = gp_samplecase[simulation] - gp_samplecase['basecase']
    mdp_samplecase = all_tech_df[all_tech_df['Region'] == 'MDP']
    mdp_samplecase = mdp_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     mdp_samplecase[simulation] = mdp_samplecase[simulation] - mdp_samplecase['basecase']
    mh_samplecase = all_tech_df[all_tech_df['Region'] == 'MH']
    mh_samplecase = mh_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     mh_samplecase[simulation] = mh_samplecase[simulation] - mh_samplecase['basecase']
    rd_samplecase = all_tech_df[all_tech_df['Region'] == 'RD']
    rd_samplecase = rd_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     rd_samplecase[simulation] = rd_samplecase[simulation] - rd_samplecase['basecase']
    sl_samplecase = all_tech_df[all_tech_df['Region'] == 'SL']
    sl_samplecase = sl_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     sl_samplecase[simulation] = sl_samplecase[simulation] - sl_samplecase['basecase']
    ww_samplecase = all_tech_df[all_tech_df['Region'] == 'WW']
    ww_samplecase = ww_samplecase.pivot(index='Program Name', columns='Simulation', values='NEW Mitigation Ratio ($/tonne CO2e)')
    # for simulation in simulations_nobasecase:
    #     ww_samplecase[simulation] = ww_samplecase[simulation] - ww_samplecase['basecase']

    all_tech_df.to_csv('all_tech.csv')
    basecase_df.to_csv('basecase1.csv')
    triannual_df.to_csv('sensitivity_triannual1.csv')
    crew_count_df.to_csv('sensitivity_crew_count1.csv')
    mdl_df.to_csv('sensitivity_mdl1.csv')
    site_num_df.to_csv('sensitivity_site_num1.csv')
    site_num_180_df.to_csv('sensitivity_site_num_1801.csv')
    ogi_persite_high_df.to_csv('sensitivity_ogi_persite_high1.csv')
    ogi_sensor_df.to_csv('sensitivity_ogi_sensor1.csv')
    coverage_df.to_csv('coverage1.csv')
    johnson_df.to_csv('johnson1.csv')
    mdl_lowogi_df.to_csv('mdl_lowogi.csv')
    mdl_lowdrone_df.to_csv('mdl_lowdrone.csv')
    mdl_lowstationary_df.to_csv('mdl_lowstationary.csv')
    multiyear_df.to_csv('multiyear.csv')

    ldarsim_simulation_all.to_csv('ldarsim_simulation_all.csv')
    figure1_difference_regionvscases.to_csv('heatmap_difference_regionvscases.csv')
    figure1_label_regionvscases.to_csv('heatmap_label_regionvscases.csv')
    bv_samplecase.to_csv('heatmap_casesvstech_BV.csv')
    dv_samplecase.to_csv('heatmap_casesvstech_DV.csv')
    edm_samplecase.to_csv('heatmap_casesvstech_EDM.csv')
    gp_samplecase.to_csv('heatmap_casesvstech_GP.csv')
    mdp_samplecase.to_csv('heatmap_casesvstech_MDP.csv')
    mh_samplecase.to_csv('heatmap_casesvstech_MH.csv')
    rd_samplecase.to_csv('heatmap_casesvstech_RD.csv')
    sl_samplecase.to_csv('heatmap_casesvstech_SL.csv')
    ww_samplecase.to_csv('heatmap_casesvstech_WW.csv')


    return

def run_LDAR_sim():
    simulation_versions = ['multiyear'] #'cost_sensitivity','crew_sensitivity','mdl_sensitivity',  'mdl_lowdrone','mdl_sensitivity_lowogi', 'mdl_lowstationary', 'multiyear''coverage','multisimulation','triannual_survey','basecase','site_number','site_number_180' ,'OGI_sensor' 'basecase_emissions_johnson_test',,,
    regionslist = ['DV', 'EDM','GP','MDP','MH', 'RD','SL','WW']
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

        print(region + " " + simulation)
# "python C:/Users/jyuan/OneDrive/Documents/GitHub/LDAR_Sim/LDAR_Sim/src/ldar_sim_run.py --in_dir ./simulations/mdl_sensitivity/EDM/annual"


    return

if __name__ == '__main__':
    num = 'plot'
    if num == 'plot':
        regional_LDARSim_resultprocessing()
    else:
        run_LDAR_sim()
