from eppy import modeleditor
from eppy.modeleditor import IDF
iddfile = "./V9-0-0-Energy+.idd"
try:
    IDF.setiddname(iddfile)
except modeleditor.IDDAlreadySetError as e:
    pass

# fname1 = "./ElectricChiller.idf"
fname1 = "C:/Users/jidus/Desktop/day04/day04.idf"
idf1 = IDF(fname1)

idf1.printidf()

building = idf1.idfobjects['BUILDING'][0]
print(building.Name)
idf1.newidfobject("BUILDING")

wall_name = 'Surface 11'  # 替换为你要修改的墙的名称
wall = idf1.getobject('BUILDINGSURFACE:DETAILED', wall_name)

# 平移墙的顶点

for i in range(1, 9, 3):  # 假设墙有四个顶点，i对应顶点的Y坐标
    y_coordinate = 'Vertex_{}_Ycoordinate'.format(i)
    if isinstance(wall[y_coordinate], float):
        wall[y_coordinate] += 3.0

# 保存修改后的idf文件
idf1.save('modified_idf_file.idf')