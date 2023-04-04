import sys
import pandas as pd
import os

#def average_duration(group):
#    stage = group['Stage'].iloc[0]
#    if stage in [2,4,5,7]:
#        return group.iloc[:4]['Duration'].mean()
#    else:
#        return group['Duration'].mean()

input_dir = 'Uncleaned Data Files'
output_dir = 'Cleaned Data Files'

input_files = os.listdir(input_dir)
input_files = [file for file in input_files if os.path.splitext(file)[1] == ".xlsx"]

for input_file in input_files:
    input_path = os.path.join(input_dir, input_file)
    output_path = os.path.join(output_dir,input_file)

    #filepath = "C:\\Users\\Benjamin\\Desktop\\Python\\WMDataCleanerTestingFile (2).xlsx"
    rawdata = pd.read_excel(input_path,sheet_name="RAW")
    platform_raw = rawdata[["Animal","Stage","Trial","Duration","Distance (cm)","Speed (cm/s)"]]
    probe_raw = rawdata[["Animal","Stage","Trial","Duration","Target Site : entries","%Time in Target Quadrant","%Time in Ann40cm","%Time in Ann20cm","%Time in Target Site"]]
    platform_stage1 = platform_raw.loc[platform_raw['Stage'] == 1].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage2 = platform_raw.loc[(platform_raw['Stage'] == 2) & (platform_raw['Trial'] != 5)].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage3 = platform_raw.loc[platform_raw['Stage'] == 3].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage4 = platform_raw.loc[(platform_raw['Stage'] == 4) & (platform_raw['Trial'] != 5)].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage5 = platform_raw.loc[(platform_raw['Stage'] == 5) & (platform_raw['Trial'] != 5)].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage6 = platform_raw.loc[platform_raw['Stage'] == 6].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    platform_stage7 = platform_raw.loc[(platform_raw['Stage'] == 7) & (platform_raw['Trial'] != 5)].groupby('Animal').agg(
        {'Duration':'mean','Distance (cm)': 'mean', 'Speed (cm/s)':'mean'})
    #learning index

    #rename columns
    platform_stage1.rename(columns={'Duration':'LAT1','Distance (cm)':'PL1','Speed (cm/s)':'SPD1'},inplace=True)
    platform_stage2.rename(columns={'Duration':'LAT2','Distance (cm)':'PL2','Speed (cm/s)':'SPD2'},inplace=True)
    platform_stage3.rename(columns={'Duration':'LAT3','Distance (cm)':'PL3','Speed (cm/s)':'SPD3'},inplace=True)
    platform_stage4.rename(columns={'Duration':'LAT4','Distance (cm)':'PL4','Speed (cm/s)':'SPD4'},inplace=True)
    platform_stage5.rename(columns={'Duration':'LAT5','Distance (cm)':'PL5','Speed (cm/s)':'SPD5'},inplace=True)
    platform_stage6.rename(columns={'Duration':'LAT6','Distance (cm)':'PL6','Speed (cm/s)':'SPD6'},inplace=True)
    platform_stage7.rename(columns={'Duration':'LAT7','Distance (cm)':'PL7','Speed (cm/s)':'SPD7'},inplace=True)
    #merge dataframes Merge is breaking?
    merged_platform = platform_stage1.merge(platform_stage2,on='Animal')
    if not platform_stage3.empty:
        merged_platform = merged_platform.merge(platform_stage3,on='Animal')
    if not platform_stage4.empty:
        merged_platform = merged_platform.merge(platform_stage4,on='Animal')
    if not platform_stage5.empty:
        merged_platform = merged_platform.merge(platform_stage5,on='Animal')
    if not platform_stage6.empty:
        merged_platform = merged_platform.merge(platform_stage6,on='Animal')
    if not platform_stage7.empty:
        merged_platform = merged_platform.merge(platform_stage7,on='Animal')
    merged_platform.reset_index(inplace=True)
    print(merged_platform)
    merged_platform = merged_platform.reindex(columns=['Animal','LAT1','LAT2','LAT3','LAT4','LAT5','LAT6','LAT7','PL1','PL2','PL3','PL4','PL5','PL6','PL7','SPD1','SPD2','SPD3','SPD4','SPD5','SPD6','SPD7'])
    merged_platform['LI'] = merged_platform[['PL2','PL3','PL4']].mean(axis=1)
    print(merged_platform)
    #platform is complete
    
    #begin probe
    probe_stage2 = probe_raw.loc[(probe_raw['Stage'] == 2) & (probe_raw['Trial'] == 5)]
    probe_stage4 = probe_raw.loc[(probe_raw['Stage'] == 4) & (probe_raw['Trial'] == 5)]
    probe_stage5 = probe_raw.loc[(probe_raw['Stage'] == 5) & (probe_raw['Trial'] == 5)]
    probe_stage7 = probe_raw.loc[(probe_raw['Stage'] == 7) & (probe_raw['Trial'] == 5)]
    #drop un-needed columns
    probe_stage2.drop(['Stage','Trial','Duration'],axis=1,inplace=True)
    probe_stage4.drop(['Stage','Trial','Duration'],axis=1,inplace=True)
    probe_stage5.drop(['Stage','Trial','Duration'],axis=1,inplace=True)
    probe_stage7.drop(['Stage','Trial','Duration'],axis=1,inplace=True)
    #rename columns
    probe_stage2.rename(columns={'Target Site : entries': 'TE-2', '%Time in Target Quadrant':'TQ-2','%Time in Ann40cm':'AN40-2','%Time in Ann20cm':'AN20-2','%Time in Target Site':'TS-2'},inplace=True)
    probe_stage4.rename(columns={'Target Site : entries': 'TE-4', '%Time in Target Quadrant':'TQ-4','%Time in Ann40cm':'AN40-4','%Time in Ann20cm':'AN20-4','%Time in Target Site':'TS-4'},inplace=True)
    probe_stage5.rename(columns={'Target Site : entries': 'TE-5', '%Time in Target Quadrant':'TQ-5','%Time in Ann40cm':'AN40-5','%Time in Ann20cm':'AN20-5','%Time in Target Site':'TS-5'},inplace=True)
    probe_stage7.rename(columns={'Target Site : entries': 'TE-7', '%Time in Target Quadrant':'TQ-7','%Time in Ann40cm':'AN40-7','%Time in Ann20cm':'AN20-7','%Time in Target Site':'TS-7'},inplace=True)
    #merge probe data
    merged_probe = probe_stage2.merge(probe_stage4,on='Animal')
    if not probe_stage5.empty:
        merged_probe = merged_probe.merge(probe_stage5,on='Animal')
    if not probe_stage7.empty:
        merged_probe = merged_probe.merge(probe_stage7,on='Animal')
    #merged_probe.reset_index(inplace=True)
    #print(merged_probe)
    print(rawdata)
    print(platform_raw)
    print(probe_raw)
    print(merged_platform)
    print(merged_probe)
    merged_probe = merged_probe.reindex(columns=['Animal','TE-2','TE-4','TE-5','TE-7','TQ-2','TQ-4','TQ-5','TQ-7','AN40-2','AN40-4','AN40-5','AN40-7','AN20-2','AN20-4','AN20-5','AN20-7','TS-2','TS-4','TS-5','TS-7'])
    with pd.ExcelWriter(output_path, mode = 'w',engine='openpyxl') as writer:
        merged_platform.to_excel(writer, sheet_name='Cleaned_Platform',index=False)
        merged_probe.to_excel(writer,sheet_name='Cleaned_Probe',index=False)

#merged_platform.to_excel(writer,sheet_name='Platform Cleaned', index=False)
#writer.save()

#platform_cleaned = pd.DataFrame(platform_lat1,columns=['Animal'])
#platform_cleaned['LAT1'] = platform_lat1.index('Animal')
#platform_pivot = platform_grouped.pivot(index='Animal', columns='Stage',values='Duration')

#LAT1 = platform_raw.loc['Animal','Duration'].mean()
#print(platform_lat1)

