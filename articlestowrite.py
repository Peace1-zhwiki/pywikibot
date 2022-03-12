import pywikibot
from pywikibot import pagegenerators

siteen = pywikibot.Site('en','wikipedia')
sitezh = pywikibot.Site('zh','wikipedia')

projname = 'physics'
projname_qual = projname
projname_impo = projname
projnamezh = '[[WikiProject:物理学|物理專題]]'
en_maxsize = 20000 #20000
zh_maxsize = 3000 #3000

cat_fa = pywikibot.Category(siteen,'Category:FA-Class '+ projname_qual +' articles')
cat_fl = pywikibot.Category(siteen,'Category:FL-Class '+ projname_qual +' articles')
cat_ga = pywikibot.Category(siteen,'Category:GA-Class '+ projname_qual +' articles')
cat_a = pywikibot.Category(siteen,'Category:A-Class '+ projname_qual +' articles')
cat_b = pywikibot.Category(siteen,'Category:B-Class '+ projname_qual +' articles')
cat_top = pywikibot.Category(siteen,'Category:Top-importance '+ projname_impo +' articles')
cat_high = pywikibot.Category(siteen,'Category:High-importance '+ projname_impo +' articles')
cat_mid = pywikibot.Category(siteen,'Category:Mid-importance '+ projname_impo +' articles')

page_to_write = pywikibot.Page(sitezh, u"User:和平奮鬥救地球/sandbox_2")

gen_fa = pagegenerators.CategorizedPageGenerator(cat_fa, recurse=True)
gen_fl = pagegenerators.CategorizedPageGenerator(cat_fl, recurse=True)
gen_ga = pagegenerators.CategorizedPageGenerator(cat_ga, recurse=True)
gen_a = pagegenerators.CategorizedPageGenerator(cat_a, recurse=True)
gen_b = pagegenerators.CategorizedPageGenerator(cat_b, recurse=True)
gen_top = pagegenerators.CategorizedPageGenerator(cat_top, recurse=True)
gen_high = pagegenerators.CategorizedPageGenerator(cat_high, recurse=True)
gen_mid = pagegenerators.CategorizedPageGenerator(cat_mid, recurse=True)

#writestr = projnamezh + '待撰條目（英文B級且中重要度以上、少於20,000位元組；中文小於3,000位元組）：\n\n'
writestr = projnamezh + '待撰條目（英文B級且中重要度以上、少於 '+ "{:,}".format(en_maxsize) +' 位元組；中文小於 '+ "{:,}".format(zh_maxsize) +' 位元組）：\n\n'
writestr += '最後更新時間：~~~~~\n\n'

writestr += '== 已有中文對應條目 ==\n'
writestr += '{| class="wikitable sortable"\n|+ 已有中文對應條目\n! 英文條目名 !! 中文條目名 !! 品質 !! 重要度 !! 英文頁面長度（位元組） !! 中文頁面長度（位元組）\n'

writestr1 = '\n== 尚無中文對應條目 ==\n'
writestr1 += '{| class="wikitable sortable"\n|+ 尚無中文對應條目\n! 英文條目名 !! 品質 !! 重要度 !! 英文頁面長度（位元組）\n'


listfa = list(gen_fa)
listfl = list(gen_fl)
listga = list(gen_ga)
lista = list(gen_a)
listb = list(gen_b)

listtop = list(gen_top)
listhigh = list(gen_high)
listmid = list(gen_mid)


count=0
tot_num = (len(listtop)+len(listhigh)+len(listhigh)+len(listmid))
print(tot_num)

impcount = 0
implist=['top','high','mid']

for listimp in [listtop,listhigh,listmid]:
	impo = implist[impcount]
	print('gen_'+impo)

	for page in listimp:
		
		count+=1
		percentage = 100*count/tot_num
		enname = ''
		zhname = ''
		qual = ''
		#impo = ''
		leng = 0
		zhleng=0
	
		#if count%100==0: print('percentage = ',percentage)
	
		if page.isTalkPage()==False: continue
		enname = page.title()[5:]
		#print(enname)
	
		if page in listfa: qual = 'FA'
		elif page in listfl: qual = 'FL'
		elif page in listga: qual = 'GA'
		elif page in lista: qual = 'A'
		elif page in listb: qual = 'B'
		else: continue
	
		
		page_main = pywikibot.Page(siteen,page.title()[5:])
		leng = len(page_main.text.encode("utf8"))
		langlinks = page_main.langlinks()

		for ll in langlinks:
			#print(ll)
			if(ll.site==sitezh):
				zhname = '[[' + ll.title + ']]'
				page_zh = pywikibot.Page(sitezh,ll.title)
				zhleng=len(page_zh.text.encode("utf8"))
				break
		if zhleng>zh_maxsize or leng>en_maxsize: continue
		print(format(percentage, '0.3f'),'%:',enname,zhname,qual,impo,leng)
		if zhleng>1: writestr += '|-\n|[[:en:' + enname + ']]||' + zhname + '||' + qual + '||' + impo + '||' + str(leng)  + '||' + str(zhleng)  + '\n'
		else: writestr1 += '|-\n|[[:en:' + enname + ']]||' + qual + '||' + impo + '||' + str(leng) + '\n'
	impcount+=1

writestr += '|}'
writestr1 += '|}'

writestr+='\n'
writestr+=writestr1

page_to_write.text = writestr
page_to_write.save(u"使用[[mw:Manual:Pywikibot/zh|Pywikibot]]更新數據：" + projnamezh)
print('Done')
