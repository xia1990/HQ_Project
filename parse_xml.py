#!/usr/bin/python
#_*_ coding:utf-8 _*_

import xml.etree.ElementTree as ET
import xlwt


name_list=[]
path_list=[]
revision_list=[]
title=['name','path','revision']
wb=xlwt.Workbook()
sheet1=wb.add_sheet("sheet1",cell_overwrite_ok=True)


def set_style(name,height,bold=False):
    style=xlwt.XFStyle()
    pattern=xlwt.Pattern()
    pattern.pattern=xlwt.Pattern.SOLID_PATTERN
    #设置背景颜色
    pattern.pattern_fore_colour=3
    style.pattern=pattern
    #设置边框(为实线)
    borders=xlwt.Borders()
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    borders.top=xlwt.Borders.THIN
    borders.bottom=xlwt.Borders.THIN
    style.borders=borders
    return style

def get_project_info():
	XML_FILE="new_mainfest.xml"
	tree=ET.parse("new_manifest.xml")
	root=tree.getroot()

	for p in root.iter("project"):
		project_name=p.get("name")
		project_path=p.get("path")
		project_revision=p.get("revision")
		#将项目名称添加到列表中
		name_list.append(project_name)
		path_list.append(project_path)
		revision_list.append(project_revision)

def write_excel():
	for i in range(len(title)):
		sheet1.write(0,i,title[i],set_style('Times New Roman',220,True))

	get_project_info()
	for i in range(len(name_list)):
		sheet1.write(i+1,0,name_list[i])
		sheet1.write(i+1,1,path_list[i])
		sheet1.write(i+1,2,revision_list[i])


##################################
if __name__=="__main__":	
	write_excel()
wb.save("manifest.xls")


