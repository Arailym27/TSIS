import re
s='arai/otyr/partada/ekieki/kolyeki/noutta/a/ded1/1234ded1/esepeki/shugardy'

#1
#match for the initial part 
res_non_initial=re.match('eki',s)
#match for the initial part 
res_initial=re.match('ar',s)
print("match:",res_non_initial)
print("match:",res_initial)

#2
#search -print the first one which find
find=re.search('eki',s)
find_2=re.match('ar',s)
print("search:",find)
print("search:",find_2)

#3
#findall-enter the all thing that we search in list
all=re.findall('ar',s)
all_2=re.findall('eki',s)
print("findall:",all)
print("findall:",all_2)

#4
#split
spl=re.split("/",s)
spl_with_limit=re.split("/",s,maxsplit=3)
print("split:",spl)
print("split,maxsplit:",spl_with_limit)

#5
#sub-change substring 
chn=re.sub("eki",'bir',s)
print(chn)

#6
#fullmatch-чекает будет ли весь шаблон равен тому что я буду вводить
check=re.fullmatch("arai/otyr/partada/ekieki/kolyeki/noutta/a/ded1/1234ded1/esepeki/shugardy",s)
print(check)