import requests
import pywikibot

projectnum=requests.get('https://api.scratch.mit.edu/projects/count/all').json()['count']
pjnum_fix1=str(projectnum)
pjnum_tmp=len(pjnum_fix1)
pjnum_fix2=str(pjnum_fix1[0]) + str(pjnum_fix1[1]) + str(pjnum_fix1[2])
pjnum_fix3=pjnum_fix2.ljust(pjnum_tmp,'0')

page=pywikibot.Page(pywikibot.Site(),'Template:Now/projects')
page.text=pjnum_fix3
page.save('Update Project Numbers(bot)')