import os
from eppy import modeleditor
from eppy.modeleditor import IDF
import pandas as pd
import json

import sys

# print (sys.path)
sys.path.append('C:\EnergyPlusV9-6-0')
# print (sys.path)
# 设置EnergyPlus的idd文件路径
# iddfile = 'path_to_your_idd_file.idd'
# idf_file = 'path_to_your_idf_file.idf'
# weather_file = 'path_to_your_weather_file.epw'

iddfile = "C:/EnergyPlusV9-6-0/Energy+.idd"
idf_file = "C:/Users/jidus/Desktop/day04/day04.idf"
weather_file = 'C:/EnergyPlusV9-6-0/WeatherData/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw'

# 初始化IDF对象
IDF.setiddname(iddfile)
idf = IDF(idf_file)

# EnergyPlus API路径设置
energyplus_exe_path = 'path_to_energyplus/energyplus'
output_dir = 'output_directory'

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 运行EnergyPlus模拟
def run_energyplus(idf_file, weather_file, output_dir):
    import pyenergyplus.api  # Import EnergyPlus API

    api = pyenergyplus.api.EnergyPlusAPI()
    state = api.state_manager.new_state()

    # 运行模拟
    api.runtime.run_energyplus(state, [
        '-w', weather_file,
        '-r',
        '-d', output_dir,
        idf_file
    ])

# 读取输出文件并提取热力学指标

# 读取输出文件并提取热力学指标
def extract_thermo_metrics(output_dir):
    # 假设你需要从eplusout.eso文件中提取数据
    eso_file = os.path.join(output_dir, 'eplusout.eso')
    data = []

    with open(eso_file, 'r') as file:
        for line in file:
            if 'YourMetric' in line:  # 替换为你要提取的具体指标
                data.append(line.strip().split(','))

    # 使用pandas处理和展示数据
    df = pd.DataFrame(data, columns=['Time', 'MetricValue'])
    return df


# def extract_thermo_metrics(output_dir):
#     sql_file_path = os.path.join(output_dir, 'eplusout.sql')
#     if not os.path.isfile(sql_file_path):
#         raise FileNotFoundError(f'{sql_file_path} not found. EnergyPlus simulation may have failed.')

#     # 使用sqlite3读取.sql文件
#     import sqlite3

#     conn = sqlite3.connect(sql_file_path)
#     query = "SELECT * FROM ReportVariableData WHERE ReportVariableDataDictionaryIndex IN (SELECT ReportVariableDataDictionaryIndex FROM ReportVariableDataDictionary WHERE VariableName = 'YourMetricName');"
#     df = pd.read_sql_query(query, conn)
#     conn.close()
    
#     return df

# 运行模拟并提取数据
run_energyplus(idf_file, weather_file, output_dir)
thermo_metrics_df = extract_thermo_metrics(output_dir)

# 输出结果
print('lllll')
print(thermo_metrics_df)
