#!/usr/bin/python
#_*_ coding:utf-8 _*_

import xml.etree.ElementTree as ET
import xlwt


XML_FILE="new_mainfest.xml"
tree=ET.parse("new_manifest.xml")
root=tree.getroot()

def get_project_info():
	name_list=[]
	path_list=[]
	revision_list=[]

	for p in root.iter("project"):
		project_name=p.get("name")
		project_path=p.get("path")
		project_revision=p.get("revision")
		#将项目名称添加到列表中
		name_list.append(project_name)
		path_list.append(project_path)
		revision_list.append(project_revision)
		print(len(name_list))

def write_excel():
	get_project_info()
	for i in range(len(name_list)):
		sheet1.write(i+1,0,name_list[i])
		sheet1.write(i+1,1,path_list[i])
		sheet1.write(i+1,2,revision_list[i])


##################################
if __name__=="__main__":	
	wb=xlwt.Workbook()
	#创建一个excel表格
	sheet1=wb.add_sheet("sheet1",cell_overwrite_ok=True)
	sheet1.write(0,0,"name")
	sheet1.write(0,1,"path")
	sheet1.write(0,2,"revision")

wb.save("manifest.xls")


