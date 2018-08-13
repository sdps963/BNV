import pandas as pd
df = pd.read_csv('BPR_GS_OP_Forecast_Budget_Final_SQL_Queries_Without_real_dates.csv')
df['Mapping']= df['Mapping'].str.replace("2018-08-01 00:00:00.000", "@startdate@", 1)
df['Mapping']= df['Mapping'].str.replace("2018-08-08 00:00:00.000", "@startdate@", 1)
df['Mapping']= df['Mapping'].str.replace("2018-08-05 00:00:00.000", "@startdate@", 1)
df['Mapping']= df['Mapping'].str.replace("2018-08-01 00:00:00.000", "@enddate@", 2)
df['Mapping']= df['Mapping'].str.replace("2018-08-08 00:00:00.000", "@enddate@", 2)
df['Mapping']= df['Mapping'].str.replace("2018-08-05 00:00:00.000", "@enddate@", 2)
df['Mapping']= df['Mapping'].str.replace("2018-08-01 00:00:00.000", "@startdate@", 3)
df['Mapping']= df['Mapping'].str.replace("2018-08-08 00:00:00.000", "@startdate@", 3)
df['Mapping']= df['Mapping'].str.replace("2018-08-05 00:00:00.000", "@startdate@", 3)
df['Mapping']= df['Mapping'].str.replace("2018-08-01 00:00:00.000", "@enddate@", 4)
df['Mapping']= df['Mapping'].str.replace("2018-08-08 00:00:00.000", "@enddate@", 4)
df['Mapping']= df['Mapping'].str.replace("2018-08-05 00:00:00.000", "@enddate@", 4)


df.to_csv('BPR_GS_OP_Forecast_Budget_Final_SQL_Queries_Without_real_dates_python.csv')
