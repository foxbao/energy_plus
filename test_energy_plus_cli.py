import os
from eppy import modeleditor
from eppy.modeleditor import IDF
import pandas as pd

# 设置EnergyPlus的idd文件路径
iddfile = "C:/EnergyPlusV9-6-0/Energy+.idd"
idf_file = "C:/Users/jidus/Desktop/day04/day04.idf"
weather_file = 'C:/EnergyPlusV9-6-0/WeatherData/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw'

# 初始化IDF对象
IDF.setiddname(iddfile)
idf = IDF(idf_file)

# 运行EnergyPlus模拟
def run_energyplus(idf_file, weather_file):
    output_dir = 'output_directory'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    command = f'energyplus -w {weather_file} -r -d {output_dir} {idf_file}'
    os.system(command)

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

# 运行模拟并提取数据
run_energyplus(idf_file, weather_file)
thermo_metrics_df = extract_thermo_metrics('output_directory')

# 输出结果
print(thermo_metrics_df)
