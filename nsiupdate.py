import pywikibot

site = pywikibot.Site('zh','wikipedia')
site_en = pywikibot.Site('en','wikipedia')

projs = ['Astronomy','physics','chemicals','Chemistry','mathematics','Extinction','electronic','Geology','Computer science','taxonomic','Biology','medicine','meteorology','Environment','Ecology']
projzh = ['天文','物理学','化学物质','化学','数学','灭绝','电子学','地質','电脑和信息技术','生物','生物学','医学','气象','环境','生态']
imps = ['Top','High','Mid','Low','Bottom','No','Unknown']
impzh = ['极高','高','中','低','极低','无','未知']
impzht = ['極高','高','中','低','極低','無','未知']
quals = ['FA','GA','FL','A','B','C','Start','Stub','List','Unaccessed']
qualzh = ['典范','优良','特色列表','甲','乙','丙','初','小作品','列表','未评']
qualzht = ['典範','優良','特色列表','甲','乙','丙','初','小作品','列表','未評']

dats = [] # v1 v2 v3 v1zh v2zh v3zh c1 c2 c3 c4 c5

count=0
for p in range(len(projs)):
	v1, v2, v3 = 0, 0, 0
	v1zh, v2zh, v3zh = 0, 0, 0
	print('Wikiproject',projs[p])
	for q in range(4):
		catname = quals[q] + '-Class ' + projs[p] + ' articles'
		catnamezh = qualzh[q] + '级' + projzh[p] + '条目'
		if(projzh[p]=='地質' and q==0): catnamezh = '典范级地质条目'
		elif(projzh[p]=='地質' and q!=0): catnamezh = qualzht[q] + '級' + projzh[p] + '條目'
		cat = pywikibot.Category(site_en,catname)
		catzh = pywikibot.Category(site,catnamezh)
		v1 += cat.categoryinfo['pages']
		v1zh += catzh.categoryinfo['pages']
	for i in range(len(imps)):
		catname = imps[i] + '-importance ' + projs[p] + ' articles'
		catname1 = imps[i] + '-priority ' + projs[p] + ' articles'
		catnamezh = impzh[i] + '重要度' + projzh[p] + '条目'
		if(projzh[p]=='地質'): catnamezh = impzht[i] + '重要度' + projzh[p] + '條目'
		cat = pywikibot.Category(site_en,catname)
		cat1 = pywikibot.Category(site_en,catname1)
		catzh = pywikibot.Category(site,catnamezh)
		if(i<2): 
			v2+=cat.categoryinfo['pages']+cat1.categoryinfo['pages']
			v2zh+=catzh.categoryinfo['pages']
		v3+=cat.categoryinfo['pages']+cat1.categoryinfo['pages']
		v3zh+=catzh.categoryinfo['pages']
	dats.append([v1,v2,v3,v1zh,v2zh,v3zh,'n','n','n','n','n',count])
	print(dats[-1])
	count+=1

print("c1")
for i in range(len(dats)):
	for j in range(len(dats)-i-1):
		if dats[j][3]/dats[j][0]>dats[j+1][3]/dats[j+1][0]:
			dats[j],dats[j+1] = dats[j+1],dats[j]

for i in range(8):
	print(dats[i][3],dats[i][0],dats[i][3]/dats[i][0])
	if i<4: dats[i][6] = 'r'
	else: dats[i][6] = 'o'

print("c2")
for i in range(len(dats)):
	for j in range(len(dats)-i-1):
		if dats[j][4]/dats[j][1]>dats[j+1][4]/dats[j+1][1]:
			dats[j],dats[j+1] = dats[j+1],dats[j]

for i in range(8):
	print(dats[i][4],dats[i][1],dats[i][4]/dats[i][1])
	if i<4: dats[i][7] = 'r'
	else: dats[i][7] = 'o'

print("c3")
for i in range(len(dats)):
	for j in range(len(dats)-i-1):
		if dats[j][5]/dats[j][2]>dats[j+1][5]/dats[j+1][2]:
			dats[j],dats[j+1] = dats[j+1],dats[j]

for i in range(8):
	print(dats[i][5],dats[i][2],dats[i][5]/dats[i][2])
	if i<4: dats[i][8] = 'r'
	else: dats[i][8] = 'o'

print("c4")
for i in range(len(dats)):
	for j in range(len(dats)-i-1):
		if (dats[j][3]/dats[j][5])/(dats[j][0]/dats[j][2])>(dats[j+1][3]/dats[j+1][5])/(dats[j+1][0]/dats[j+1][2]):
			dats[j],dats[j+1] = dats[j+1],dats[j]

for i in range(8):
	print((dats[i][3]/dats[i][5]),(dats[i][0]/dats[i][2]),(dats[i][3]/dats[i][5])/(dats[i][0]/dats[i][2]))
	if i<4: dats[i][9] = 'r'
	else: dats[i][9] = 'o'

print("sort")
for i in range(len(dats)):
	for j in range(len(dats)-i-1):
		if dats[j][-1]>dats[j+1][-1]:
			dats[j],dats[j+1] = dats[j+1],dats[j]

page = pywikibot.Page(site, u"User:和平奮鬥救地球/自然科學條目提升計劃/表格整理/B")

writestr=""

for i in range(len(dats)):
	if(projzh[i]=='电脑和信息技术'): writestr+="{{User:和平奮鬥救地球/自然科學條目提升計劃/表格整理/T|project=" + projzh[i] + "|projectshow=電腦資訊|enFGA=" + str(dats[i][0]) + "|enTophigh=" + str(dats[i][1])
	else: writestr+="{{User:和平奮鬥救地球/自然科學條目提升計劃/表格整理/T|project=" + projzh[i] + "|enFGA=" + str(dats[i][0]) + "|enTophigh=" + str(dats[i][1])
	writestr+="|enTotal=" + str(dats[i][2]) + "|color1=" + dats[i][6] + "|color2=" + dats[i][7] + "|color3=" + dats[i][8] + "|color4=" + dats[i][9] + "|color5=" + dats[i][10]

	if(projzh[i]=='生物'): writestr+="|note=<ref group=\"註\">不包括英文維基[[:en:WP:TOL|生物專題]]之龐大的子專題（人體解剖學、分子與細胞生物學；魚類、昆蟲、真菌；等等）系統；其中[[:en:WP:MCB|分子與細胞生物學]]或是中文維基百科最薄弱之類別。</ref>"
	writestr += "}}\n"

writestr+="|}\n</center>\n<center><small>本表格由[[User:和平奮鬥救地球]]製作整理，[[User:和平奮鬥救地球/自然科學條目提升計劃|歡迎轉載]]。英文數據最後更新時間：~~~~~"
writestr += '\n<noinclude><references group="註"/></noinclude>'
page.text = writestr
page.save(u"使用[[mw:Manual:Pywikibot/zh|Pywikibot]]更新數據")

print('Done')
