import appuifw2 as ui,os,e32,graphics,sysinfo,TopWindow
zt=e32.ao_sleep
Image=graphics.Image
patha=(ui.app.full_name()[:3]+u'system\\apps\\FarmHelper\\').encode('u8')
x,y=sysinfo.display_pixels()
try:
  logo=Image.open(patha+'logo\\HelperLogo.png')
  win=TopWindow.TopWindow()
  win.size=(x,y)
  win.position=(0,0)
  win.add_image(logo,(0,0,x,y))
  win.show()
except:
  os.abort()
zt(0)
cn=lambda x,:x.decode('utf-8')
en=lambda x,:x.encode('utf-8')
ui.app.body=m=ui.Text(skinned=1)
ui.app.title='QQ农牧帮手'.decode('u8')
ui.app.screen='normal'
m.focus=False
def readfq():
  try:
    fi=open(patha+u'farmq.txt','r')
    fd=fi.read().split('|')
    fi.close()
    sytd=int(fd[0])
    qita=int(fd[1])
    szl=int(fd[2])
    szz=int(fd[3])
    htts=int(fd[4])
    mcolor=int(fd[5])
    mstyle=int(fd[6])
    mfont=int(fd[7])
    tqyzm=int(fd[8])
    tq=int(fd[9])
    zdtl=int(fd[10])
    qaa=int(fd[11])
    qab=int(fd[12])
    taa=int(fd[13])
    tab=int(fd[14])
  except:
    sytd=0
    qita=0
    szl=0
    szz=0
    htts=1
    mcolor=0
    mstyle=0
    mfont=3
    tqyzm=1
    tq=0
    zdtl=1
    qaa=120
    qab=240
    taa=200
    tab=200
  global sytd,qita,szl,szz,htts,mcolor,mstyle,mfont,tqyzm,tq,zdtl,qaa,qab,taa,tab
readfq()
def font():
  if mfont==0:
    m.font=('dense',11)
  elif mfont==1:
    m.font=('dense',12)
  elif mfont==2:
    m.font=('dense',13)
  elif mfont==3:
    m.font=('dense',14)
  elif mfont==4:
    m.font=('dense',15)
  elif mfont==5:
    m.font=('dense',16)
  elif mfont==6:
    m.font=('dense',17)
  elif mfont==7:
    m.font=('dense',18)
  elif mfont==8:
    m.font=('dense',19)
  elif mfont==9:
    m.font=('dense',20)
def color():
  if mcolor==0:
    m.color=random.randrange(16777215)
  elif mcolor==1:
    m.color=16711680
  elif mcolor==2:
    m.color=65280
  elif mcolor==3:
    m.color=255
  elif mcolor==4:
    m.color=16711935
  elif mcolor==5:
    m.color=65535
  elif mcolor==6:
    m.color=16776960
  elif mcolor==7:
    m.color=0
  elif mcolor==8:
    m.color=7396243
  elif mcolor==9:
    m.color=10444703
  elif mcolor==10:
    m.color=11904578
  elif mcolor==11:
    m.color=14276889
  elif mcolor==12:
    m.color=3100463
  elif mcolor==13:
    m.color=8855416
  elif mcolor==14:
    m.color=5526612
  elif mcolor==15:
    m.color=9380643
  elif mcolor==16:
    m.color=2330147
  elif mcolor==17:
    m.color=13467442
  elif mcolor==18:
    m.color=14408560
  elif mcolor==19:
    m.color=12638681
  elif mcolor==20:
    m.color=16777215
def style():
  if mstyle==1:
    m.style=ui.STYLE_STRIKETHROUGH
  elif mstyle==2:
    m.style=ui.HIGHLIGHT_ROUNDED
  elif mstyle==3:
    m.style=ui.HIGHLIGHT_SHADOW
  elif mstyle==4:
    m.style=ui.HIGHLIGHT_STANDARD
  elif mstyle==5:
    m.style=ui.STYLE_BOLD
  elif mstyle==6:
    m.style=ui.STYLE_ITALIC
  elif mstyle==7:
    m.style=ui.STYLE_UNDERLINE
  else:
    pass
def impor(mk):
  ui.note(cn('缺少%s模块！\n无法正常运行软件！\n请下载py2.5平台！！') % mk,'error',1)
def A(x):
  font()
  color()
  style()
  m.add(x)
def B(x):
  m.set('')
  A(x)
try:
  import envy
  envy.set_app_system(1)
except:
  impor('envy')
try:
  import re
except:
  impor('re')
try:
  import time
except:
  impor('time')
try:
  import msys
except:
  impor('msys')
try:
  import socket
except:
  impor('socket')
try:
  import audio
except:
  impor('audio')
try:
  import urllib
except:
  impor('urllib')
try:
  import httplib
except:
  impor('httplib')
try:
  import uitricks
except:
  impor('uitricks')
def exit():
  e=ui.query(cn('是否退出软件？'),'query')
  if e:
    os.abort()
def aw():
  msys.send_bg()
try:
  from miso import vibrate as vibrate
except:
  impor('miso')
try:
  import random
except:
  impor('random')
try:
  from key_tricks import *
except:
  impor('key_tricks')
def clserror():
  er=[]
  zaii=[]
  global er,zaii
clserror()
mjy1=[]
try:
  if not(os.path.exists(patha+u'nm\\')):
    os.mkdir(patha+u'nm\\')
  qq=os.listdir(patha+u'nm\\')
  if os.path.isfile(patha+u'time'):
    ff=open(patha+u'time','r')
    c=ff.read()
    if c==None:
      cc=[]
    else:
      cc=c.split('/')
    ff.close()
    if len(qq)!=len(cc):
      cc=[]
    pass
  else:
    cc=[]
except:
  os.abort()
def menu5():
  uitricks.set_text(cn('菜单'),EAknSoftkeyOptions)
  if qita==0:
    envy.set_app_hidden(0)
    uitricks.set_text(cn('后台'),EAknSoftkeyExit)
  elif qita==1:
    envy.set_app_hidden(1)
    uitricks.set_text(cn('隐藏'),EAknSoftkeyExit)
  ui.app.exit_key_handler=aw
menu5()
zt(0.1)
win.hide()
ui.app.screen='normal'
m.focus=False
def set_ac():
  ui.note(cn('请设置默认接入点'))
  apids=socket.access_points()
  list=[]
  for id in apids:
    list.append(id['name'])
  iaps=ui.popup_menu(list,cn('请选择接入点：'))
  if iaps>-1:
    apin=apids[iaps]['name']
    apid=apids[iaps]['iapid']
    apd=cn('cmwap')
    a=ui.popup_menu([cn('免流(超Q.黄钻)'),cn('WAP接入点'),cn('WIFI或NET接入点')],cn('请选择接入点：'))
    if a==1:
      apd=cn('wap')
    elif a==2:
      apd=cn('net')
    apo=socket.access_point(apid)
    socket.set_default_access_point(apo)
    zt(0.1)
    if apd=='cmwap':
      jrd=2
    elif apd=='wap':
      jrd=1
    elif apd=='net':
      jrd=0
    t=open(patha+u'apid.txt','w')
    t.write(en(apin)+'|'+en(apd))
    t.close()
    ui.note(cn('新的接入点设置成功！'))
  else:
    ui.note(cn('新的接入点设置失败！'))
  global apo,jrd
try:
  s=open(patha+u'apid.txt','r')
  f=s.read()
  s.close()
  ff=f.split('|')
  iap=cn(ff[0])
  iap=[iap]
  apd=ff[1]
  apd=cn(apd)
  a=socket.access_points()
  b,c,d=([],{},{})
  for i in a:
    b+=[i['name']]
    c[i['iapid']]=i['name']
    d[i['name']]=i['iapid']
  apid=-1
  for i in b:
    if i in iap:
      apid=d[i]
      break
  if apid==-1:
    set_ac()
  else:
    apo=socket.access_point(apid)
    socket.set_default_access_point(apo)
    zt(0.1)
    if apd=='cmwap':
      jrd=2
    elif apd=='wap':
      jrd=1
    elif apd=='net':
      jrd=0
    else:
      set_ac()
except:
  set_ac()
def cltime():
  try:
    os.remove(patha+u'time')
    clos()
    ui.note(cn('清除定时成功'))
    cc=[]
  except:
    ui.note(cn('没有定时可清除'))
  global cc
def delsid():
  import Helper
  a=Helper.delsid()
  if a:
    cc=[]
  global cc
def editsid():
  import Helper
  Helper.editsid()
def sid():
  list=[cn('增加农场'),cn('增加牧场'),cn('增加餐厅'),cn('增加鱼塘')]
  index=ui.popup_menu(list,cn('手动提取'))
  if index==0:
    import Helper
    Helper.sid()
  if index==1:
    import Helper
    Helper.msid()
  if index==2:
    import Helper
    Helper.csid()
  if index==3:
    import Helper
    Helper.ysid()
def asid():
  import Helper
  if not(os.path.exists(patha+u'qqpwd\\')):
    os.mkdir(patha+u'qqpwd\\')
  qqa=os.listdir(patha+u'qqpwd\\')
  qqg=[]
  for q in range(0,len(qqa)):
    qqg.append(qqa[q].decode('utf8'))
  if len(qqg)==0:
    tqsida()
  elif ui.query(cn('是否使用保存了密码的QQ账号'),'query'):
    tqsidb()
  else:
    tqsida()
  apo.stop()
def tqsida():
  import Helper
  qq=ui.query(cn('请输入qq号码'),'text',cn('1123817754'))
  if qq>10000:
    qq=str(qq)
    pwd=ui.query(cn('请输入密码'),'text')
    if pwd!=None:
      no2=0
      no3=0
      no4=0
      if ui.query(cn('是否还有添加牧场'),'query'):
        no2=1
      if ui.query(cn('是否还有添加餐厅'),'query'):
        no3=1
      if ui.query(cn('是否还有添加鱼塘'),'query'):
        no4=1
      if ui.query(cn('请问你保存密码,方便书签过期后修复,你也可不存'),'query'):
        qpath=patha+u'qqpwd\\'
        if not(os.path.exists(qpath)):
          os.mkdir(qpath)
        f=open(qpath+qq,'w')
        f.write(qq+'|'+pwd+'|'+str(no2)+'|'+str(no3)+'|'+str(no4))
        f.close()
      uid=dkj(qq,pwd)
      if uid!='no':
        Helper.naid(qq,newsid,uid)
        if no2:
          Helper.maid(qq,newsid)
        if no3:
          Helper.caid(qq,newsid)
        if no4:
          Helper.yaid(qq,newsid,uid)
        cc=[]
        run=0
        ui.note(cn('QQ:')+qq+cn('提取书签成功，请开启收菜或继续提取书签'))
      else:
        ui.note(cn('QQ:')+qq+cn('失败！请用手动提取！'))
      pass
    pass
  global cc,run
def tqsidb():
  import Helper
  if not(os.path.exists(patha+u'qqpwd\\')):
    os.mkdir(patha+u'qqpwd\\')
  qqa=os.listdir(patha+u'qqpwd\\')
  qqg=[]
  for q in range(0,len(qqa)):
    qqg.append(qqa[q].decode('utf8'))
  qqb=ui.popup_menu(qqg,cn('需要提取书签的QQ号'))
  if qqb>-1:
    qqc=qqa[qqb].decode('utf8')
    f=open(patha+u'qqpwd\\'+qqc,'r')
    a=f.read().decode('utf-8').split('|')
    f.close()
    qq=a[0]
    pwd=a[1]
    no2=a[2]
    no3=a[3]
    no4=a[4]
    uid=dkj(qq,pwd)
    if uid!='no':
      Helper.naid(qq,newsid,uid)
      if no2:
        Helper.maid(qq,newsid)
      if no3:
        Helper.caid(qq,newsid)
      if no3:
        Helper.yaid(qq,newsid,uid)
      cc=[]
      run=0
      ui.note(cn('QQ:')+qq+cn('提取书签成功，请开启收菜或继续提取书签'))
    else:
      ui.note(cn('QQ:')+qq+cn('失败！请用手动提取！'))
    pass
  global cc,run
def w1(h1,h2):
  try:
    ho=h1.split('/')
    fw1={'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
    if jrd:
      con=httplib.HTTPConnection('10.0.0.172',80)
      con.request('POST',h1,h2,fw1)
    else:
      con=httplib.HTTPConnection(ho[2])
      con.request('POST',h1.replace('http://'+ho[2],''),h2,fw1)
    r=con.getresponse()
    data=r.read().decode('utf8').replace('&amp;','&').replace('\n','').replace(' ','').replace('\r','').replace('\t','').replace('&nbsp;','')
    con.close()
  except:
    data='no'
  return data
def juz1():
  juz()
  A(cn('\n10秒后自动返回'))
  zt(10)
def juz():
  B(cn('　　　　　农牧帮手\n　　本软件由绝、恋根据专程大哥的农牧场助理发布的，请支持专程和绝恋。\n　　有问题请到絶、恋空间留言！QQ：1123817754\n　　　　　　絶恋'))
juz()
def guoq(buid):
  if len(er)==0:
    er.append(buid)
  else:
    b=0
    for j in range(0,len(er)):
      k=er[j]
      if k.find(buid)>-1:
        b=1
        break
    if b==0:
      er.append(buid)
    pass
def satime():
  try:
    ff=open(patha+u'time','w')
    b=cc[0]
    for i in range(1,len(cc)):
      b=b+'/'
      b=b+cc[i]
    ff.write(b)
    ff.close()
  except:
    pass
def showtime(du1):
  m.add((cn(' %02d时%02d分%02d秒') % ((du1/3600),((du1 % 3600)/60),((du1 % 3600) % 60))))
def mload2():
  try:
    context=cai.split('<br/>')
    for i in range(0,len(context)):
      k=context[i]
      if k.find(cn('秒后'))>0 or k.find(cn('秒至'))>0:
        try:
          se=k.split(cn('秒'))
          sjm=int(se[0])
        except:
          sjm=56
        A(cn('等待')+str(sjm)+cn('秒后收获…\n'))
        zt(sjm)
        if k.find(cn('秒后成'))>0:
          url=u'http://nc.z.qq.com/farm/harvest_all.jsp?sid='+mysid+u'&B_UID='+buid+u'&myuid='+myuid
        if k.find(cn('秒至'))>0:
          url='http://nc.z.qq.com/fish/index.jsp?B_UID='+buid+'&uid='+myuid+'&myuid='+myuid+'&sid='+mysid
        elif k.find(cn('后可'))>0:
          if k.find(cn('秒后可收获'))>0:
            ifmz=1
            url=u'http://pasture.z.qq.com/mc/op.jsp?sid='+mysid+u'&B_UID='+buid+u'&p=5&m=0&op=1'
          else:
            url=u'http://pasture.z.qq.com/mc/op.jsp?sid='+mysid+u'&B_UID='+buid+u'&p=1&a=1&m=0&op=1'
          pass
        elif k.find(cn('秒后到'))>0:
          url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
        break
    for i1 in range(0,len(context)):
      k=context[i1]
      if k.find(cn('小时'))<0 and k.find(cn('分'))>0:
        sjf1=k.split(cn('分'))
        sf=int(sjf1[0])
        if sf<4:
          sj=(sf*60)
          A(cn('在等待')+str(sj)+cn('秒后收获…\n'))
          if k.find(cn('后可收获'))>0:
            ifmz=1
          break
        pass
    del context
    return url
  except:
    pass
  global ifmz
def min(li):
  n=len(li)
  for i in range(0,n):
    for j in range(0,(n-1)):
      if li[j]>li[(j+1)]:
        a=li[j]
        li[j]=li[(j+1)]
        li[(j+1)]=a
  return li
def zid(qqd):
  try:
    qh=open(qqd,'r')
    qhr=qh.read().decode('utf8')
    qh.close()
    qhre=qhr.split('|')
    mysid=qhre[1]
    nmbu=qhre[0].split('_')
    nm=nmbu[0]
    buid=nmbu[1]
    if nm=='n':
      t1=qhre[2]
      myuid=qhre[3]
      cid=qhre[4]
      rcid=qhre[5]
      hcid=qhre[6]
    elif nm==u'y':
      myuid=qhre[2]
      fid=qhre[3]
    elif nm==u'c':
      zx=(int(qhre[2])*60)
      zd=(int(qhre[3])*60)
      csgs=int(qhre[4])
    elif nm==u'm':
      t1=qhre[2]
      mon=qhre[3]
      pcid=qhre[4]
      wcid=qhre[5]
  except:
    os.remove(qqd.encode('utf-8'))
  global mysid,nm,buid,t1,myuid,cid,rcid,hcid,fid,zx,zd,csgs,mon,pcid,wcid
def qhqqd():
  qqa=os.listdir(patha+u'nm\\')
  if len(qqa)==0:
    ui.note(cn('没有设置qq农场登陆信息！'))
    clos()
    zt(1)
  else:
    cc=[]
    delothers()
    zt(0.1)
    B(cn('正在连接网络，请稍候……'))
    zt(0.1)
    for q in range(len(qqa)):
      qqc=qqa[q].decode('utf8')
      qqd=patha+u'nm\\'+qqc
      zid(qqd)
      menu2()
      if nm==u'c':
        zt(0.1)
        sj=cshou()
      elif nm==u'y':
        yshou()
        sj=readtime()
        zt(0.5)
      elif nm=='n':
        nshou()
        sj=readtime()
        zt(0.5)
      elif nm=='m':
        mshou()
        if ifmz and mon!=u'n':
          for ba in range(3):
            mzai()
            mshou()
            if ifmz==0:
              break
          pass
        else:
          pass
        mzait()
        sj=readtime()
      if sj<1:
        guoq(nm+'_'+buid+cn('没有定时！'))
        continue
      cc.append(str(time.time()+sj)+'|'+nm+'_'+buid)
      cc=min(cc)
    pass
  apo.stop()
  menu1()
  if len(cc)>0:
    return cc[0]
  else:
    return 0
  global cc
def qqtou2():
  run1=1
  menu3()
  list=[cn('偷取好友.朋友'),cn(' 偷取 QQ 好友 '),cn(' 偷取 QQ 朋友 ')]
  index=ui.popup_menu(list,cn('选择偷取类型：'))
  if index==0:
    ui.note(cn('请选择你要偷的农牧场\n'))
    tl=1
    qqd(2)
  if index==1:
    ui.note(cn('请选择你要偷的农牧场\n'))
    tl=2
    qqd(2)
  if index==2:
    ui.note(cn('请选择你要偷的农牧场\n'))
    tl=3
    qqd(2)
  f=open(patha+u'others\\tao.txt','w')
  f.write(time.ctime(time.time()).encode('utf8'))
  f.close()
  menu1()
  global run1,tl
def qqtou():
  list=[cn('偷取好友.朋友'),cn(' 偷取 QQ 好友 '),cn(' 偷取 QQ 朋友 ')]
  index=ui.popup_menu(list,cn('选择偷取类型：'))
  if index==0:
    tl=0
    qqt(tl)
  if index==1:
    tl=1
    qqt(tl)
  if index==2:
    tl=2
    qqt(tl)
def qqt(xztl):
  run1=1
  menu3()
  if len(er)>0:
    for j in range(0,len(er)):
      k=er[j]
      if k.find(cn('验证码'))>-1:
        tq=0
        ui.note(cn('请按删除(C)键，消除验证码提示！'))
        return None
    pass
  qqa=os.listdir(patha+u'nm\\')
  if len(qqa)==0:
    ui.note(cn('没有设置qq农牧场登陆息！'))
  else:
    zt(0.1)
    B(cn('正在连接网络，请稍候……\n'))
    A(cn('小提示！可按拨号键中止偷\n按8键可查看最近一次自动偷\n'))
    zt(0.1)
    for q in range(len(qqa)):
      if not(os.path.isdir(patha+u'nm\\'+qqa[q])):
        if qqa[q][:1]==u'm' or qqa[q][:1]==u'n':
          qqc=qqa[q].decode('utf8')
          qqd=patha+u'nm\\'+qqc
          zid(qqd)
          djs=int(time.strftime('%H'))
          if nm==u'm':
            if t1==u'yn' and 8<djs<24 and run1==1:
              f=open(patha+u'others\\autotao.txt','w')
              f.write(time.ctime(time.time()).encode('utf8'))
              f.close()
              if tq==3:
                continue
              A(cn('正在进行牧场偷取！\n'))
              if xztl==0:
                kjmtou()
                xymtou()
              elif xztl==1:
                kjmtou()
              elif xztl==2:
                xymtou()
              pass
            elif t1==u'y' and run1==1:
              f=open(patha+u'others\\autotao.txt','w')
              f.write(time.ctime(time.time()).encode('utf8'))
              f.close()
              if tq==3:
                continue
              A(cn('正在进行牧场偷取！\n'))
              if xztl==0:
                kjmtou()
                xymtou()
              elif xztl==1:
                kjmtou()
              elif xztl==2:
                xymtou()
              pass
            pass
          elif nm==u'n':
            if t1==u'yn' and 8<djs<24 and run1==1:
              f=open(patha+u'others\\autotao.txt','w')
              f.write(time.ctime(time.time()).encode('utf8'))
              f.close()
              if tq==2:
                continue
              A(cn('正在进行农场偷取！\n'))
              if xztl==0:
                kjtou()
                xytou()
              elif xztl==1:
                kjtou()
              elif xztl==2:
                xytou()
              pass
            elif t1==u'y' and run1==1:
              f=open(patha+u'others\\autotao.txt','w')
              f.write(time.ctime(time.time()).encode('utf8'))
              f.close()
              if tq==2:
                continue
              A(cn('正在进行农场偷取！\n'))
              if xztl==0:
                kjtou()
                xytou()
              elif xztl==1:
                kjtou()
              elif xztl==2:
                xytou()
              pass
            pass
          pass
      pass
  apo.stop()
  menu1()
  global run1,tq
ym1=0
def ym2():
  ym1=1
  global ym1
def w3(url):
  ho=url.split('/')
  if jrd:
    con=httplib.HTTPConnection('10.0.0.172',80)
  else:
    con=httplib.HTTPConnection(ho[2])
    url=url.replace('http://'+ho[2],'')
  con.putrequest('GET',url)
  con.putheader('Accept','*/*')
  con.endheaders()
  r=con.getresponse()
  data=r.read()
  con.close()
  f=open('d:\\1.gif','w')
  f.write(data)
  f.close()
def yzm():
  ym1=0
  fc=cai.split(u'<imgsrc="')
  fd=fc[1].split(u'"')
  url=fd[0]
  urt=url.split(u'9001/')
  urw=urt[1][:-4]
  w3(url)
  if htts:
    wd=TopWindow.TopWindow()
    img=graphics.Image.new((100,17))
    img.clear(10444703)
    img.text((5,16),cn('[发现验证码]'),16777215,font=u'Sans MT 936_S60')
    wd.size=(100,19)
    wd.add_image(img,(0,0,100,17))
    wd.position=(60,0)
    wd.show()
  if szl:
    try:
      xa=open(patha+u'farmok.txt')
      ea=xa.read().decode('utf-8')
      xa.close()
      x=audio.Sound.open(ea)
      x.play()
    except:
      pass
    pass
  A(cn('按2键查看验证码\n'))
  yno=u'3524'
  for i in range(60):
    if ym1:
      try:
        x.stop()
      except:
        pass
      if htts:
        wd.hide()
      if tqyzm:
        window=TopWindow.TopWindow()
        img=graphics.Image.open('d:\\1.gif')
        w,h=img.size
        window.size=((w+2),(h+2))
        window.background_color=0
        window.add_image(img,(1,1))
        window.corner_type='square'
        window.shadow=0
        window.position=(20,0)
        window.show()
        yno=ui.query(cn('输入看到的验证码'),'number')
        if not(yno==None):
          yno=str(yno).decode('u8')
        break
      else:
        d_file=u'D:\\1.gif'
        viewer=ui.Content_handler()
        viewer.open(d_file)
        yno=ui.query(cn('输入看到的验证码'),'number')
        if not(yno==None):
          yno=str(yno).decode('u8')
        break
      pass
    else:
      if szz:
        try:
          vibrate(500,100)
        except:
          pass
        pass
      else:
        zt(0.5)
      zt(0.3)
  if yno==None:
    yno=u'1115'
  else:
    pass
  try:
    window.hide()
    os.remove('d:\\1.gif')
  except:
    pass
  h2=u'&iv_verify='+yno+u'&r_sid='+urw+u'&bid=PastureSac'
  return h2
  global ym1
def semn():
  import Helper
  Helper.semn()
def delmn():
  import Helper
  Helper.delmn()
def se5():
  import Helper
  Helper.se5()
def dww(mc):
  PATH=patha+u'mc\\'+buid
  if not(os.path.exists(PATH)):
    os.makedirs(PATH)
  ab=mc.split(cn('、'))
  for i in range(len(ab)):
    ac=ab[i].split(cn('×'))
    try:
      ff=open((PATH+u'\\'+ac[0]+u'.txt').encode('u8'),'r')
      c=int(ff.read())
      ff.close()
      c=c+int(ac[1])
    except:
      c=int(ac[1])
    ff=open((patha+u'mc\\'+buid+u'\\'+ac[0]+u'.txt').encode('u8'),'w')
    ff.write(str(c))
    ff.close()
def kjmtou():
  if run1==1:
    B(cn('正在向服务器提交QQ好友偷取数据！！\n'))
    cai=w1(u'http://app40.z.qq.com/qzone_app/index.jsp?sid='+mysid,u'&appid=353')
    if cai!=u'no':
      A(cn('正在偷')+buid+cn('的QQ好友牧场\n'))
      mtou()
    else:
      guoq(buid+cn('牧偷连接网络失败！'))
def xymtou():
  if run1==1:
    B(cn('正在向服务器提交QQ朋友偷取数据！！\n'))
    cai=w1(u'http://app20.z.qq.com/qzone_app/index.jsp?B_UID='+buid+u'&sid='+mysid,u'&appid=353&xy=1')
    if cai!=u'no':
      A(cn('正在偷')+buid+cn('的QQ朋友牧场\n'))
    else:
      guoq(buid+cn('牧偷连接网络失败！'))
def mtou():
  url=u'http://pasture.z.qq.com/mc/friends.jsp?sid='+mysid+u'&B_UID='+buid+u'&op=1'
  r1=r2=r3=r6=r7=r8=r9=r10=r4=0
  r5=600
  while 1:
    try:
      if r1:
        cai=w0(h1+h2)
        r1=0
      else:
        cai=w0(url)
      r5+=1
      fcai=cai.split('<br/>')
      for i in range(6):
        k=fcai[i]
        if k.find(cn('我的牧场'))>-1:
          pass
        elif k.find(cn('的牧场'))>-1:
          if r4>(taa-1):
            A(cn('已成功终止摘取\n'))
            zt(1)
            return None
          r4+=1
          k2=k.split(cn('的牧'))
          A((cn('摘取: %s. ') % r4))
          A(k2[0])
        elif k.find(cn('(经验'))>-1:
          k2=k.split(cn('(经验'))
          A(' ('+k2[0]+')\n')
          break
      if cai.find(cn('成功收获了'))>-1:
        fcai=cai.split(cn('成功收获了'))
        uid1=fcai[1].split(cn('。'))
        A(uid1[0]+u'\n')
        dww(uid1[0])
      elif cai.find(cn('赶去生产，'))>-1:
        fcai=cai.split(cn('成功将'))
        uid1=fcai[1].split(cn('，'))
        A(uid1[0]+u'\n')
      elif cai.find(cn('抓动物的时候被看守员'))>-1:
        fcai=cai.split(cn('的时候'))
        uid1=fcai[1].split(cn('。'))
        A(uid1[0]+u'\n')
      elif cai.find(cn('成功地清理了'))>-1:
        fcai=cai.split(cn('清理了'))
        uid1=fcai[1].split(',')
        A(uid1[0]+u'\n')
      if run1==0:
        return None
      elif cai.find('<divclass="')>0:
        url='http://blog60.z.qq.com/app_list.jsp?B_UID='+buid+'&sid='+mysid+'&g_ut=1'
      elif cai.find(cn('一键操作功能还没有全面开放'))>0:
        os.remove(patha+'qqbrowser.db')
        if r10:
          guoq(cn(' 注意！一键补丁已失效'))
          return None
        r10=1
      elif cai.find(cn('(可收获)'))>-1 or cai.find(cn('(可生产)'))>-1 or cai.find(cn('(可操作)'))>-1:
        fcai=cai.split(cn('】<br'))
        uid1=fcai[1].split(u'<ahref="')
        tuid=uid1[1].split(u'">')
        url=tuid[0]
      elif cai.find(cn('>生产<'))>0 or cai.find(cn('>收获<'))>0:
        if cai.find(cn('>生产<'))>0:
          r2=time.time()
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
      elif cai.find(cn('>清扫</'))>-1:
        fcai=cai.split(cn('个<ahref="'))
        tuid=fcai[1].split('">')
        url=tuid[0]
      elif cai.find(cn('验证码'))>0:
        menu4()
        r1=1
        h1=url
        h2=yzm()
        menu3()
        if ym1==0:
          guoq(buid+cn('需验证码!暂停50秒'))
          return None
        pass
      elif cai==u'no':
        url=u'http://pasture.z.qq.com/mc/friends.jsp?sid='+mysid+u'&B_UID='+buid+u'&op=1'
        zt(2)
        r7+=1
        if r7>2:
          guoq(buid+cn('牧偷 糟糕！网络错误'))
          return None
        pass
      elif cai.find(cn('下一个可操作好友'))>0:
        A(cn('没有可操作的动物及产品\n'))
        fcai=((cai.split(cn('好友牧场'))[1]).split(cn('下一个可操作好友'))[0]).split(u'</a><br/>')
        uid1=fcai[len(fcai)-1].split(u'<ahref="')
        tuid=uid1[1].split(u'">')
        url=tuid[0]
      else:
        r9=(time.time()-r2)
        if 1<>r9<>22:
          zt(22-r9)
          url=u'http://pasture.z.qq.com/mc/friends.jsp?sid='+mysid+u'&B_UID='+buid+u'&op=1'
        elif cai.find(cn('没有好友牧场可操作'))>0:
          try:
            del fcai
            del uid1
          except:
            pass
          A(cn('结束！当前没有可偷好友'))
          zt(1)
          return None
        else:
          url=u'http://pasture.z.qq.com/mc/friends.jsp?sid='+mysid+u'&B_UID='+buid+u'&op=1'
          r8+=1
          if r8>2:
            return None
          pass
    except:
      url=u'http://pasture.z.qq.com/mc/friends.jsp?sid='+mysid+u'&B_UID='+buid+u'&op=1'
      r6+=1
      if r6>2:
        return None
      pass
  global cai
def ncc(nc):
  try:
    PATH=patha+u'nc\\'+buid
    if not(os.path.exists(PATH)):
      os.makedirs(PATH)
    ac=nc.split(',')
    for ia in range(len(ac)):
      ab=ac[ia].split(cn('个'))
      try:
        ff=open((PATH+u'\\'+ab[1]+u'.txt').encode('u8'),'r')
        c=int(ff.read())
        ff.close()
        c=c+int(ab[0])
      except:
        c=int(ab[0])
      ff=open((patha+u'nc\\'+buid+u'\\'+ab[1]+u'.txt').encode('u8'),'w')
      ff.write(str(c))
      ff.close()
  except:
    pass
def kjtou():
  if run1==1:
    B(cn('正在向服务器提交QQ好友偷取数据！！\n'))
    cai=w1(u'http://app40.z.qq.com/qzone_app/index.jsp?sid='+mysid,u'&appid=353')
    if cai!=u'no':
      A(cn('正在偷QQ:')+buid+cn('的QQ好友农场\n'))
      tou()
    else:
      guoq(buid+cn('农偷连接网络失败！'))
def xytou():
  if run1==1:
    B(cn('正在向服务器提交QQ朋友偷取数据！！\n'))
    cai=w1(u'http://app20.z.qq.com/qzone_app/index.jsp?B_UID='+buid+u'&sid='+mysid,u'&appid=353&xy=1')
    if cai!=u'no':
      A(cn('正在偷QQ:')+buid+cn('的QQ朋友农场\n'))
      tou()
    else:
      guoq(buid+cn('农偷连接网络失败！'))
def tou():
  r0=r1=r6=r2=r4=0
  r3=r8=1
  url=u'http://nc.z.qq.com/farm/friend_list.jsp?sid='+mysid+u'&myuid='+myuid
  r5=100
  tlist=[]
  A(cn('正在提取可偷取列表！\n请稍候……\n'))
  while run1:
    cai=w0(url)
    zt(1)
    r0+=1
    A((cn('正在提取第%s ') % r0)+cn('页好友列表！\n'))
    r5+=1
    if run1==0:
      A(cn('已成功终止摘取\n'))
      zt(1)
      return None
    elif cai.find('<divclass="')>0:
      url='http://blog60.z.qq.com/app_list.jsp?B_UID='+buid+'&sid='+mysid+'&g_ut=1'
      r2=1
      continue
    elif r2==1:
      url=u'http://nc.z.qq.com/farm/friend_list.jsp?sid='+mysid+u'&myuid='+myuid
      r2=0
      continue
    scai=cai.split('<anchor>')
    for i in range(1,len(scai)):
      try:
        fcai=scai[i].split('value="')
        tuid=fcai[1].split('"/>')
        tbuid=fcai[2].split('"/>')
        tmoney=fcai[4].split('"/>')
        if scai[i].find(cn('（摘取）'))>0 or scai[i].find(cn('（捞鱼）'))>0:
          d9='y'
        else:
          d9='n'
        tlist.append('http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&B_UID='+tbuid[0]+'&uid='+tuid[0]+'&myuid='+myuid+'&money='+tmoney[0]+'|'+d9)
      except:
        pass
    if cai.find(cn('">下页<'))>-1:
      r3+=1
      url='http://nc.z.qq.com/farm/friend_list.jsp?sid='+mysid+'&myuid='+myuid+'&pageNo='+str(r3)
    else:
      break
  if tlist==None:
    A(cn('目前没有好友可摘\n'))
    zt(1)
    return None
  A((cn('本次共有%s个好友可操作\n') % len(tlist)))
  for ig in range(len(tlist)):
    ur=tlist[ig].split('|')
    url=ur[0]
    if ur[1]=='n' and r2==1:
      continue
    r1=1
    fish=None
    while 1:
      cai=w0(url)
      r5+=1
      r7=0
      if cai.find(cn('【好友土地】'))>-1:
        r7=1
      if cai.find(cn('您的鱼塘还没有开通'))>-1:
        r8=0
        A(cn('对不起，您的鱼塘还没有开通，请在PC端开通鱼塘后再操作。\n'))
        guoq(cn('对不起，您的鱼塘还没有开通，请在PC端开通鱼塘后再操作。'))
        break
      elif cai.find(cn('>好友池塘</a>(捞取)<br/>'))>-1:
        fcai=cai.split(cn('【好友土地】<ahref="'))
        uid1=fcai[1].split(u'">')
        fish=uid1[0]
      fcai=cai.split('<br/>')
      for i in range(5):
        k=fcai[i]
        if k.find(cn('我的农场'))>-1:
          pass
        elif k.find(cn('的农场'))>-1 and r7==1:
          if r4>(taa-1):
            A(cn('已成功终止摘取\n'))
            zt(1)
            return None
          r4+=1
          k2=k.split(cn('的农'))
          A((cn('摘取: %s. ') % r4))
          A(k2[0])
        elif k.find(cn('(经验'))>-1 and r7==1:
          k2=k.split(cn('(经验'))
          A(' ('+k2[0]+')\n')
          break
      if cai.find(cn('继续操作将不再累加'))>-1:
        r2=1
      if cai.find(cn('成功偷取好友的'))>-1:
        fcai=cai.split(cn('成功偷取好友的'))
        uid1=fcai[1].split(cn('<br/>'))
        A(uid1[0]+u'\n')
        ncc(uid1[0])
      elif cai.find(cn('成功摘取好友'))>-1:
        fcai=cai.split(cn('摘取好友的'))
        uid1=fcai[1].split(cn(',其他土地没'))
        A(uid1[0]+u'\n')
        ncc(uid1[0])
      elif cai.find(cn('为好友帮忙成功'))>-1:
        fcai=cai.split(cn('帮忙成功'))
        uid1=fcai[1].split(cn('，'))
        A(uid1[0]+u'\n')
      if run1==0:
        A(cn('已成功终止摘取\n'))
        zt(1)
        return None
      elif cai.find(cn('>摘取<'))>0 or cai.find(cn('>捞鱼<'))>0:
        r1=0
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
      elif fish!=None and r8==1:
        url=fish
        fish=None
      elif cai.find(cn('>除草<'))>0 or cai.find(cn('>浇水<'))>0 or cai.find(cn('>杀虫<'))>0:
        r1=0
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
        if r2==1:
          A(cn('满经验，跳过为好友帮忙！\n'))
          break
        pass
      elif cai.find(cn('一键操作功能还没有全面开放'))>0:
        os.remove(patha+u'serviceinfo.dat')
        guoq(cn(' 注意！一键补丁已失效，请反馈告诉我！'))
        return None
      else:
        if r1==1:
          A(cn('已摘取或未成熟\n'))
        break
  try:
    del fcai
    del scai
    del tlist
  except:
    pass
  A(cn('偷取结束\n'))
  zt(2)
  global cai
def qtsz():
  import Helper
  Helper.qtsz()
  readfq()
  menu5()
def mcao():
  try:
    f=cai.split(cn('料:'))
    p=f[1].split('/')
    msf=int(p[0])
    del f
    del p
    if mco and msf<500:
      if msf<50:
        mun=0
      guoq(buid+cn(' 自动加草失败'))
      return None
    elif msf<300:
      mff=(1000-msf)
      url='http://pasture.z.qq.com/mc/add_food.jsp?sid='+mysid+'&B_UID='+buid+'&n='+str(msf)+'&m=0&op=1'
      zt(1)
      cai1=w0(url)
      f=cai1.split(cn('还剩'))
      p=f[1].split(cn('颗'))
      cms=int(p[0])
      del f
      del p
      try:
        f2=open(u'e:\\2\\co.txt','w')
        f2.write(cai1.encode('utf8'))
        f2.close()
      except:
        pass
      A(cn('正在加草…\n'))
      mco=1
      h1=u'http://pasture.z.qq.com/mc/add_food_action.jsp?sid='+mysid
      if (cms-mff)>0:
        h2=u'&m=0&op=1&B_UID='+buid+u'&num='+str(mff)
        f=open(patha+u'others\\dj\\mm_'+buid,'w')
        f.write((time.strftime('  %m-%d %H:%M')+cn(' 仓库中的牧草还剩：')+str((cms-mff))).encode('utf8'))
        f.close()
      else:
        h2=u'&m=0&op=1&B_UID='+buid+u'&num='+str(cms)
        f=open(patha+u'others\\dj\\mm_'+buid,'w')
        f.write((time.strftime('  %m-%d %H:%M')+cn(' 仓库中已经没有牧草，您赶紧去购买或种植')).encode('utf8'))
        f.close()
      zt(1)
      cai1=w1(h1,h2)
      try:
        f=open(u'e:\\2\\c4.txt','w')
        f.write(cai1.encode('utf8'))
        f.close()
      except:
        pass
      pass
  except:
    pass
  global mun,mco
def tid():
  try:
    f=open(patha+u'qqpwd\\'+buid,'r')
    a=f.read().decode('utf-8').split('|')
    f.close()
  except:
    xun=mun=0
    return None
  uid=dkj(a[0],a[1])
  if uid!='no':
    qqd=patha+u'nm\\n_'+a[0]+'.txt'
    if os.path.isfile(qqd):
      zid(qqd)
      k=open(qqd,'w')
      k.write('n_'+buid+'|'+newsid+'|'+t1+'|'+uid+'|'+cid+'|'+rcid)
      k.close()
    if a[2]=='1':
      qqd=patha+u'nm\\m_'+a[0]+'.txt'
      if os.path.isfile(qqd):
        zid(qqd)
        k=open(patha+u'nm\\m_'+buid+'.txt','w')
        k.write(u'm_'+buid+'|'+newsid+'|'+t1+'|'+mon+'|'+pcid+'|'+wcid)
        k.close()
      pass
    if a[3]=='1':
      qqd=patha+u'nm\\c_'+a[0]+'.txt'
      if os.path.isfile(qqd):
        zid(qqd)
        k=open(patha+u'nm\\c_'+buid+'.txt','w')
        k.write(u'c_'+buid+'|'+newsid)
        k.close()
      pass
    if a[4]=='1':
      qqd=patha+u'nm\\y_'+a[0]+'.txt'
      if os.path.isfile(qqd):
        zid(qqd)
        k=open(patha+u'nm\\c_'+buid+'.txt','w')
        k.write(u'y_'+buid+'|'+newsid+'|'+uid+'|'+fid)
        k.close()
      pass
    pass
  else:
    xun=mun=0
  global xun,mun
def dkj(qq,pwd):
  import dialog
  uid='no'
  try:
    zt(1)
    w=dialog.Wait(cn('正在登入手机腾讯网请等会 …'))
    w.show()
    zt(1)
    u1=u'http://pt5.3g.qq.com/handleLogin'
    u2=urllib.urlencode({'sid':'AdyrFmJrIolazXVi7b50Nu8A'.encode('u8'),'qq':qq.encode('u8'),'pwd':pwd.encode('u8'),'q_from':''.encode('u8'),'bid':'0'.encode('u8'),'modifySKey':'0'.encode('u8'),'loginType':'3'.encode('u8')})
    data=w1(u1,u2)
    if data.find(cn('成功'))>0:
      a=data.split('sid=')
      b=a[1].split('&')
      newsid=b[0]
      w=dialog.Wait(cn('正在进入QQ农场中请等会 …'))
      w.show()
      zt(1)
      url='http://nc.z.qq.com/farm/index.jsp?sid='+newsid+u'&B_UID='+qq
      data=w2(url)
      a=data.split('&myuid=')
      b=a[1].split('"')
      uid=b[0]
    elif data.find(cn('验证码'))>0:
      url=data.split('<imgsrc="')[1].split('"')[0]
      w3(url)
      window=TopWindow.TopWindow()
      img=graphics.Image.open('d:\\1.gif')
      w,h=img.size
      window.size=((w+2),(h+2))
      window.background_color=0
      window.add_image(img,(1,1))
      window.corner_type='square'
      window.shadow=0
      window.position=(20,0)
      window.show()
      yno=ui.query(cn('输入看到的验证码'),'text')
      if yno!=None:
        sid=data.split('sid"value="')[1].split('"')[0]
        status=data.split('q_status"value="')[1].split('"')[0]
        r=data.split('r"value="')[1].split('"')[0]
        extend=data.split('extend"value="')[1].split('"')[0]
        rsid=data.split('r_sid"value="')[1].split('"')[0]
        rip=data.split('rip"value=')[1].split('"')[0]
        w=dialog.Wait(cn('正在提交验证码请等会 …'))
        w.show()
        u1=u'http://pt5.3g.qq.com/handleLogin'
        u2=urllib.urlencode({'qq':qq.encode('u8'),'u_token':'-1','hexpwd':pwd.encode('hex'),'sid':sid,'hexp':'true','auto':'0','loginTitle':'手机腾讯网','q_from':'','modifySKey':'0','q_status':status,'r':r,'loginType':'1','bid_code':'qqchatLogin','imgType':'gif','extend':extend,'r_sid':rsid,'bid':'0','login_url':'http://pt5.3g.qq.com/s?aid=nLogin','verify':yno,'rip':rip})
        data=w1(u1,u2)
        if data.find(cn('成功'))>0:
          a=data.split('sid=')
          b=a[1].split('&')
          newsid=b[0]
          w=dialog.Wait(cn('正在进入QQ农场中请等会 …'))
          w.show()
          zt(1)
          url='http://nc.z.qq.com/farm/index.jsp?sid='+newsid+u'&B_UID='+qq
          data=w2(url)
          a=data.split('&myuid=')
          b=a[1].split('"')
          uid=b[0]
        elif data.find(cn('验证码'))>0:
          ui.note(cn('验证码输入错误！请重新提取！'))
        elif data.find(cn('密码错误'))>0:
          ui.note(cn('密码错误！请重新输入密码！'))
        pass
      pass
    elif data.find(cn('密码错误'))>0:
      ui.note(cn('密码错误！请重新输入密码！'))
      del data
      del a
      del b
  except:
    pass
  return uid
  global newsid
PATH=patha+u'others\\zt'
if not(os.path.exists(PATH)):
  os.makedirs(PATH)
PATH=patha+u'others\\dj\\'
if not(os.path.exists(PATH)):
  os.makedirs(PATH)
del PATH
def readtime():
  ss=[]
  try:
    if nm==u'm':
      try:
        text1=cai.split(cn('动物崽和动物-->'))
        text2=text1[1].split('<ahref')
        text3=text2[0]
      except:
        text3=u'no'
      f=open(patha+u'others\\zt\\mc'+buid,'w')
      f.write((text3+time.ctime(time.time())).encode('utf8'))
      f.close()
    elif nm==u'n':
      try:
        text1=cai.split(cn('刷新</a>'))
        text2=text1[1].split('<ahref')
        text3=text2[0]
      except:
        text3=u'no'
      f=open(patha+u'others\\zt\\nc'+buid,'w')
      f.write((text3+time.ctime(time.time())).encode('utf8'))
      f.close()
    elif nm==u'y':
      try:
        text1=cai.split(cn('刷新</a>'))
        text2=text1[1].split('<ahref')
        text3=text2[0]
      except:
        text3=u'no'
      f=open(patha+u'others\\zt\\yt'+buid,'w')
      f.write((text3+time.ctime(time.time())).encode('utf8'))
      f.close()
    sj=0
    if cai==u'noweb':
      sj=600
      return sj
    context=cai.split('<br/>')
    for i in range(0,len(context)):
      k=context[i]
      if k.find(cn('等级:'))>-1 and k.find(cn('(经验'))>-1:
        try:
          f=open(patha+u'others\\dj\\'+nm+u'_'+buid,'w')
          f.write(k.encode('utf8'))
          f.close()
        except:
          pass
        pass
      elif k.find(cn('小时'))>0 or k.find(cn('分'))>0:
        try:
          if k.find(cn('小时'))>0 and k.find(cn('分'))>0:
            h=k.split(cn('小时'))
            f=h[1].split(cn('分'))
            sh=int(h[0])
            sf=int(f[0])
            sj=(sh*3600)+((sf*60)-3)
          elif k.find(cn('小时'))>0 and k.find(cn('分'))<0:
            sjf1=k.split(cn('小时'))
            sf=int(sjf1[0])
            sj=((sf*3600)-3)
          elif k.find(cn('小时'))<0 and k.find(cn('分'))>0:
            sjf1=k.split(cn('分'))
            sf=int(sjf1[0])
            sj=((sf*60)-3)
        except:
          sj=0
        if sj>0:
          if k.find(cn('后到'))>0:
            sj=(sj+70)
          ss.append(sj)
        pass
    if len(ss)>0:
      ss.sort()
      sj=int(ss[0])
    else:
      sj=0
    del context
  except:
    sj=600
  return sj
def cshou():
  sj=random.randint(zx,zd)
  try:
    B(buid+cn(' 进入餐厅…\n'))
    url='http://ct.qzapp.z.qq.com/ct/cgi-bin/wap_index_cgi?uin='+buid+'&sid='+mysid+'&g_ut=1'
    xun=r2=1
    r=100
    while xun:
      r+=1
      cai=w0(url)
      if jrd==2:
        d=cai.split('ahref="http://ct.qzapp.z.qq.com/ct/cgi-bin')
      else:
        d=cai.split('ahref=".')
      if cai.find(cn('欢迎回来！'))>0:
        Cg=re.compile(cn('欢迎回来！(.*?)<br/>')).findall(cai)[0]
        A(Cg+u'\n')
      if len(d)<2:
        break
      elif r2==1:
        r2=2
        x=cn('>一键加满<')
        A(cn('正在一键加满…\n'))
      elif r2==2:
        r2=3
        x=cn('>雇佣<')
        A(cn('正在查看雇佣…\n'))
      elif r2==3:
        if cai.find(cn('>一键雇佣<'))>0:
          r2=4
          x=cn('>一键雇佣<')
          A(cn('正在一键雇佣…\n'))
        else:
          A(cn('正在到雇员室…\n'))
          r2=5
          x=cn('>到雇员室<')
        pass
      elif r2==4:
        r2=5
        A(cn('正在到雇员室…\n'))
        x=cn('>到雇员室<')
      elif r2==5:
        if cai.find(cn('当前厨师'))>0:
          A(cn('正在提取当前厨师人数…\n'))
          r3=cai.split(cn('当前厨师'))[1].split(cn('人'))[0]
          zt(0.1)
          r4=(csgs-int(r3))
          if r4>0:
            r2=6
          elif r4<0:
            r2=7
          else:
            A(cn('无需安排厨师…\n'))
            zt(1)
            r2=10
          pass
        elif cai.find(cn('>一键喂食</a>'))>0:
          d2=cai.split(cn('>时间：'))
          d3=d2[1].split(cn('小时<br/>体力：'))
          d4=d3[1].split(cn('%'))
          if int(d3[0])>9 and int(d4[0])<16:
            A(cn('正在准备喂食…\n'))
            x=cn('>一键喂食<')
            r2=9
          else:
            break
          pass
        else:
          r2=8
        pass
      elif r2==6:
        r4=(r4-1)
        if r4<0:
          break
        else:
          A(cn('正在安排厨师…\n'))
          x=cn('>安排为厨师<')
        pass
      elif r2==7:
        r4+=1
        if r4>0:
          break
        else:
          A(cn('正在安排服务员…\n'))
          x=cn('>安排为服务员<')
        pass
      else:
        break
      for i in d:
        if i.find(x)>0:
          d1=i.split('"')
          url='http://ct.qzapp.z.qq.com/ct/cgi-bin'+d1[0]
          break
  except:
    cai=u'noweb'
    sj=600
  return sj
  global cai
def mshou():
  url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
  B(cn('正在打开牧场QQ:')+buid+u'\n')
  mun=1
  ifmz=r1=mco=r2=r3=r6=r7=r10=0
  r5=200
  while mun:
    try:
      if r1:
        cai=w0(h1+h2)
        r1=0
      else:
        cai=w0(url)
      zt(1)
      mcao()
      r5+=1
      if cai.find('<divclass="')>0:
        url='http://blog60.z.qq.com/app_list.jsp?B_UID='+buid+'&sid='+mysid+'&g_ut=1'
      elif cai.find(cn('>收获<'))>0 or cai.find(cn('>生产<'))>0:
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
        if cai.find(cn(':收获期'))>0:
          ifmz=1
        if cai.find(cn('>生产<'))>0 and cai.find(cn('>收获<'))<0:
          r3=1
          A(cn('正在生产中…\n'))
        else:
          A(cn('正在收获中…\n'))
        pass
      elif cai.find(cn('>清扫</'))>-1:
        fcai=cai.split(cn('个<ahref="'))
        tuid=fcai[1].split('">')
        url=tuid[0]
        A(cn('清扫便便中…\n'))
      elif cai==u'no':
        url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
        zt(5)
        r7+=1
        if r7>2:
          cai='noweb'
          guoq(buid+cn('牧 糟糕！网络错误'))
          return None
        pass
      elif cai.find(cn('申请号码'))>0:
        tid()
        zid(patha+u'nm\\m_'+buid+'.txt')
        del url
        guoq(buid+cn(' 注意！书签可能过期了'))
      elif cai.find(cn('一键操作功能还没有全面开放'))>0:
        os.remove(patha+u'serviceinfo.dat')
        if r10:
          guoq(cn(' 注意！一键补丁已失效，请反馈告诉我！'))
          return None
        r10=1
      elif cai.find(cn('已经被赶去生产'))>0 or cai.find(cn('秒后可收获农副产品'))>0 or cai.find(cn('秒后生产完成'))>0:
        r3=0
        A(cn('15秒后收…\n'))
        zt(14)
        url=u'http://pasture.z.qq.com/mc/op.jsp?sid='+mysid+u'&B_UID='+buid+u'&p=5&m=0&op=1'
      elif cai.find(cn('刷新'))>-1 and cai.find(cn('牧场目前没有动物'))>0:
        A(cn('没有动物…\n'))
        ifmz=1
        guoq(buid+cn(' 注意！.可能没动物'))
        mun=0
      elif cai.find(cn('验证码'))>0:
        menu4()
        r1=1
        h1=url
        h2=yzm()
        menu2()
        if ym1==0:
          guoq(buid+cn('需验证码!暂停50秒'))
          return None
        pass
      elif cai.find(cn('后可'))>0 or cai.find(cn('后到'))>0:
        if cai.find(cn('秒后可'))>0 or cai.find(cn('秒后到'))>0:
          url=mload2()
        else:
          try:
            del tuid
            del uid1
            del fcai
          except:
            pass
          mun=0
        pass
      elif cai.find(cn('成功收获了'))>0:
        fcai=cai.split(cn('成功'))
        uid1=fcai[1].split(cn('<'))
        A(cn('成功')+uid1[0]+u'\n')
        A(cn('正在返回牧场首页…\n'))
        url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
      elif r2>2:
        try:
          del tuid
          del uid1
          del fcai
        except:
          pass
        mun=0
        guoq(buid+cn(' 牧 可能出错了'))
      else:
        r2+=1
        A(cn('正在返回牧场首页…\n'))
        url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
    except:
      url=u'http://pasture.z.qq.com/mc/index.jsp?sid='+mysid+u'&B_UID='+buid+u'&a=1&m=0'
      cai='noweb'
      r6+=1
      if r6>2:
        guoq(buid+cn(' 牧 10分后重试'))
        return None
      pass
  global mun,ifmz,mco,cai
def w2(url):
  while 1:
    ho=url.split('/')
    headers={'Q-GUID':'00000000000000000000000000000000','Q-UA':'SQB28_GA/281190&SMTT_3/020100&SYM3&152014&(C)NokiaN78&0&6231&V3','Accept':'application/vnd.wap.xhtml+xml, text/vnd.wap.wml, application/xhtml+xml, text/html, image/png, image/jpeg, image/gif, */*;q=0.1','User-Agent':'MQQBrowser/2.8 (NokiaN78;SymbianOS/9.1 Series60/3.0)','Host':ho[2]}
    if jrd==2:
      if ho[2]!=cn('f.10086.cn'):
        url=url_f+urllib.quote(url)
      headers={'Q-UA':'SQB28_GA/281190&SMTT_3/020100&SYM3&152014&(C)NokiaN78&0&6231&V3','Accept':'application/vnd.wap.xhtml+xml, text/vnd.wap.wml, application/xhtml+xml, text/html, image/png, image/jpeg, image/gif, */*;q=0.1','User-Agent':'MQQBrowser/2.8 (NokiaN78;SymbianOS/9.1 Series60/3.0)','Host':'f.10086.cn'}
    if jrd:
      Conn=httplib.HTTPConnection('10.0.0.172',80)
      Conn.request('GET',url,'',headers)
    else:
      Conn=httplib.HTTPConnection(ho[2])
      Conn.request('GET',url.replace('http://'+ho[2],''),'',headers)
    GetResponse=Conn.getresponse()
    data=GetResponse.read().decode('utf8').replace('&amp;','&').replace('\n','').replace('\r','').replace('\t','').replace('&nbsp;','')
    Conn.close()
    zt(1)
    if data.find(u'/go></onevent')>0:
      b=data.split('onenterforward"><go href="')
      c=b[1].split('">')
      url=c[0]
    elif data.find(cn('"forward" ontimer="'))>0:
      b=data.split('"forward" ontimer="')
      c=b[1].split('">')
      url=c[0]
    elif data.find(u'Thedocumenthasmoved')>0:
      zt(1)
      b=data.split('Thedocumenthasmoved<ahref="')
      c=b[1].split('">')
      url=c[0]
    else:
      break
  return data
def serviceinfo():
  try:
    f=open(patha+u'serviceinfo.dat','r')
    a=f.read().decode('utf-8').split('|')
    f.close()
    pa=a[0]
    pg=a[1]
    qtime=int(a[2])
  except:
    qtime=111111
  dtime=(time.time()-qtime)
  quid='MzEzMTMyMzMzODMxMzczNzM1MzQ='
  dat='http://blog30.z.qq.com/blog/blog_detail.jsp?B_UID='+quid.decode('base64').decode('hex')+'&bId=1323672439&cf=&sid='+mysid
  if dtime>86400:
    try:
      data=w2(dat)
      data=data.replace('*','.').replace('#','/').split('||')
      a=data[1].split('|')
      pa=a[0]
      pg=a[1]
      t=str(time.time()).split('.')
      bb=int(a[2])
      try:
        if a[4]!=' ':
          guoq(a[4])
      except:
        pass
      if bb>143:
        guoq(cn('有新版本了！请按7键更新帮手！'))
      f=open(patha+u'serviceinfo.dat','w')
      servicenifo=a[0]+'|'+a[1]+'|'+t[0]
      f.write(servicenifo.encode('utf-8'))
      f.close()
      return 0
    except:
      return 1
    pass
  global pa,pg
def zc_fk():
  try:
    import openurl
    url='http://blog30.z.qq.com/blog/blog_detail.jsp?B_UID=1123817754&bId=1323672439&cf=&sid='
    try:
      openurl.open_ucweb(url)
    except:
      openurl.open_browser(url)
  except:
    impor('openurl')
def lookll():
  import dialog
  w=dialog.Wait(cn('正在检查更新中请等会 …'))
  w.show()
  dat='http://blog30.z.qq.com/blog/blog_detail.jsp?B_UID=1123817754&bId=1323672439&cf=&sid=AdMHXpP8OUpJYVmjv0FumQLF'
  data=w2(dat)
  try:
    if data.find('||')<0:
      zt(2)
      data=w2(dat)
    data=data.replace('*','.').replace('#','/').split('||')
    a=data[1].split('|')
    bb=int(a[2])
    if bb>143:
      dlnew=a[3]
      ui.query(cn('请复制下面网址下载'),'text','http://'+dlnew)
      tiao=ui.query(cn('是否调用浏览器去更新？'),'query')
      if tiao:
        url='http://'+dlnew
        try:
          import openurl
          try:
            openurl.open_ucweb(url)
          except:
            openurl.open_browser(url)
        except:
          impor('openurl')
        pass
      else:
        pass
      pass
    else:
      ui.note(cn('已经是最新版了\n官网是http://yylcd.net\n'))
  except:
    ui.note(cn('检查更新失败！请登入官网查看更新信息！\n官网是http://yylcd.net\n'))
def ltpw():
  try:
    f=open(patha+u'others\\autotao.txt','r')
    at=f.read().decode('utf8')
    f.close()
  except:
    at=cn('暂无记录')
  try:
    f=open(patha+u'others\\tao.txt','r')
    st=f.read().decode('utf8')
    f.close()
  except:
    st=cn('暂无记录')
  B(cn('\n最近一次自动偷的时间是：\n')+at+cn('\n最近一次手动偷的时间是：\n')+st)
  zt(5)
def w0(url):
  serviceinfo()
  try:
    while 1:
      t1=time.time()
      ho=url.split('/')
      headers={'Q-AUTH':pa,'Q-GUID':pg,'Q-UA':'SQB28_GA/281190&SMTT_3/020100&SYM3&152014&(C)NokiaN78&0&6231&V3','Accept':'application/vnd.wap.xhtml+xml, text/vnd.wap.wml, application/xhtml+xml, text/html, image/png, image/jpeg, image/gif, */*;q=0.1','User-Agent':'MQQBrowser/2.8 (NokiaN78;SymbianOS/9.1 Series60/3.0)','Host':ho[2]}
      if jrd==2:
        if ho[2]!=cn('f.10086.cn'):
          url=url_f+urllib.quote(url)
        headers={'Q-UA':'SQB28_GA/281190&SMTT_3/020100&SYM3&152014&(C)NokiaN78&0&6231&V3','Accept':'application/vnd.wap.xhtml+xml, text/vnd.wap.wml, application/xhtml+xml, text/html, image/png, image/jpeg, image/gif, */*;q=0.1','User-Agent':'MQQBrowser/2.8 (NokiaN78;SymbianOS/9.1 Series60/3.0)','Host':'f.10086.cn'}
      if jrd:
        Conn=httplib.HTTPConnection('10.0.0.172',80)
        Conn.request('GET',url,'',headers)
      else:
        Conn=httplib.HTTPConnection(ho[2])
        Conn.request('GET',url.replace('http://'+ho[2],''),'',headers)
      GetResponse=Conn.getresponse()
      data=GetResponse.read().decode('utf8').replace('&amp;','&').replace('\n','').replace(' ','').replace('\r','').replace('\t','').replace('&nbsp;','').replace('<br/><br/>','<br/>')
      Conn.close()
      if (time.time()-t1)<3:
        zt(2)
      zt(0.1)
      if data.find(u'/go></onevent')>0:
        zt(1)
        b=data.split('onenterforward"><gohref="')
        c=b[1].split('">')
        url=c[0]
      elif data.find(u'forward"ontimer')>0:
        zt(1)
        b=data.split('forward"ontimer="')
        c=b[1].split('">')
        url=c[0]
      elif data.find(u'Thedocumenthasmoved')>0:
        zt(1)
        b=data.split('Thedocumenthasmoved<ahref="')
        c=b[1].split('">')
        url=c[0]
      else:
        break
  except:
    data='no'
  return data
def yshou():
  B(cn('开始鱼塘操作 QQ:')+buid+u'\n')
  url=urlhome='http://nc.z.qq.com/fish/index.jsp?B_UID='+buid+'&uid='+myuid+'&myuid='+myuid+'&sid='+mysid
  xun=1
  r1=r2=r3=r4=r6=r7=0
  r5=400
  while xun:
    try:
      if r1:
        cai=w0(h1+h2)
        r1=0
      else:
        cai=w0(url)
      if cai.find(cn('池塘(空余'))>0:
        fcai=cai.split(cn('池塘(空余'))
        k=(len(fcai)-1)
      r5+=1
      if cai.find('<divclass="')>0:
        url='http://blog60.z.qq.com/app_list.jsp?B_UID='+buid+'&sid='+mysid+'&g_ut=1'
      elif cai.find(cn('>捞鱼</a'))>0:
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
        A(cn('正在捞鱼中…\n'))
      elif cai.find(cn('>养殖<'))>0 and cai.find(cn('池塘(空余)'))>0:
        A(cn('正在打开背包…\n'))
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
        uid2=url.split('num=')
        uid3=uid2[1].split('&')
        num=uid3[0]
      elif cai.find(cn('>养殖<'))>0 and cai.find(cn('池塘(空余)'))<0:
        if int(fid)>9999:
          A(cn('正在养殖…\n'))
          fcai=cai.split(cn('ahref="'))
          for i in fcai:
            if i.find(cn('>养殖<'))>0:
              tuid=i.split(u'">')
              url=tuid[0]
              break
          pass
        else:
          url='http://nc.z.qq.com/fish/op_confirm.jsp?sid='+mysid+'&op=1&B_UID='+buid+'&myuid='+myuid+'&all=1&indexs=-1&num='+str(k)+'&fid='+fid
          A(cn('正在养殖(指定鱼苗)中…\n'))
        r3+=1
        if r3>3:
          guoq(buid+cn('可能养殖失败'))
          return None
        pass
      elif cai.find(cn('养殖数量为'))>0 and cai.find(cn('>确定<'))>0:
        A(cn('正在确定养殖…\n'))
        fcai=cai.split(cn('ahref="'))
        for i in fcai:
          if i.find(cn('>确定<'))>0:
            tuid=i.split(u'">')
            url=tuid[0]
            break
        pass
      elif cai==u'no':
        url=urlhome
        zt(5)
        r7+=1
        if r7>2:
          cai=u'noweb'
          guoq(buid+cn('鱼 糟糕！网络错误'))
          return None
        pass
      elif cai.find(cn('验证码'))>0:
        menu4()
        r1=1
        h1=url
        h2=yzm()
        menu3()
        if ym1==0:
          guoq(buid+cn('需验证码!暂停50秒'))
          return None
        pass
      elif cai.find(cn('申请号码'))>0 or cai.find(cn('sid已经过期'))>=0:
        tid()
        zid(patha+'nm\\y_'+buid+'.txt')
        del url
        guoq(buid+cn(' 注意！书签可能过期了'))
      elif cai.find(cn('成熟期'))>0 or cai.find(cn('幼鱼期'))>0:
        if cai.find(cn('秒至'))>0 or cai.find(cn('秒成熟'))>0:
          mload2()
          url=urlhome
          r3=1
        else:
          xun=0
        pass
      else:
        url=urlhome
        A(cn('正在返回鱼塘首页…\n'))
        if cai.find(cn('你成功'))<0 or cai.find(cn('您成功'))<0:
          r4+=1
          if r4>2:
            xun=0
            guoq(buid+cn(' 鱼 出现未知错误'))
          pass
        pass
    except:
      url=urlhome
      cai=u'noweb'
      r6+=1
      if r6>2:
        guoq(buid+cn(' 鱼 错误 10分后重试'))
        return None
      pass
  global xun,cai
def nshou():
  B(cn('开始收菜QQ:')+buid+u'\n')
  url='http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&all=true&B_UID='+buid+'&myuid='+myuid+'&uid='+myuid+'&money=0'
  xun=1
  r=r1=r2=r3=r4=r6=r7=r8=0
  r5=400
  while xun:
    try:
      cai=w0(url)
      r5+=1
      if cai.find('<divclass="')>0:
        url='http://blog60.z.qq.com/app_list.jsp?B_UID='+buid+'&sid='+mysid+'&g_ut=1'
      elif cai.find(cn('>收获</a'))>0 or cai.find(cn('>除草<'))>0 or cai.find(cn('>杀虫<'))>0 or cai.find(cn('>浇水<'))>0:
        fcai=cai.split(cn('一键<ahref="'))
        uid1=fcai[1].split(u'">')
        url=uid1[0]
        if cai.find(cn('>收获<'))>0:
          A(cn('正在收获中…\n'))
        elif cai.find(cn('>除草<'))>0:
          A(cn('正在除草……\n'))
        elif cai.find(cn('>杀虫<'))>0:
          A(cn('正在杀虫…\n'))
        elif cai.find(cn('>浇水<'))>0:
          A(cn('正在浇水……\n'))
        pass
      elif cai.find(cn('>铲除<'))>0 or cai.find(cn('>一键铲除'))>0:
        if int(cid)<1:
          guoq(buid+cn(' 没有选择种子'))
          url='http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&all=true&B_UID='+buid+'&myuid='+myuid+'&uid='+myuid+'&money=0'
          zt(2)
          cai=w0(url)
          xun=0
        else:
          A(cn('正在铲除中…\n'))
          url=u'http://nc.z.qq.com/farm/cleanAllPlace.jsp?sid='+mysid+u'&myuid='+myuid
        pass
      elif cai==u'no':
        url=u'http://nc.z.qq.com/farm/index.jsp?sid='+mysid+u'&B_UID='+buid
        zt(5)
        r7+=1
        if r7>2:
          cai=u'noweb'
          guoq(buid+cn('农 糟糕！网络错误'))
          return None
        pass
      elif cai.find(cn('没有空地可供播种'))>0:
        url=u'http://nc.z.qq.com/farm/seed_all.jsp?sid='+mysid+u'&cid='+rcid+u'&B_UID='+buid+u'&myuid='+myuid+u'&red=1&c=0'
        r2+=1
        if r2>4:
          guoq(buid+cn('可能播种失败'))
          return None
        pass
      elif cai.find(cn('>种植<'))>0:
        if cai.find(cn('黑土地'))>0:
          url=u'http://nc.z.qq.com/farm/seed_all.jsp?sid='+mysid+u'&cid='+hcid+u'&B_UID='+buid+u'&myuid='+myuid+u'&red=2&c=0'
          A(cn('正在黑土地播种中…\n'))
        elif cai.find(cn('红土地'))>0:
          url=u'http://nc.z.qq.com/farm/seed_all.jsp?sid='+mysid+u'&cid='+rcid+u'&B_UID='+buid+u'&myuid='+myuid+u'&red=1&c=0'
          A(cn('正在红土地播种中…\n'))
        else:
          url=u'http://nc.z.qq.com/farm/seed_all.jsp?sid='+mysid+u'&index=1&cid='+cid+u'&B_UID='+buid+u'&isplant=1&myuid='+myuid
          A(cn('正在普通土地播种中…\n'))
        r3+=1
        if r3>4:
          guoq(buid+cn('可能播种失败'))
          return None
        pass
      elif cai.find(cn('>播种<'))>0 or cai.find(cn('>一键播种'))>0: 
        A(cn('正在打开背包…\n'))
        url=u'http://nc.z.qq.com/farm/bag_list_seedall.jsp?sid='+mysid+u'&myuid='+myuid
      elif cai.find(cn('系统繁忙'))>0:
        guoq(buid+cn(' 注意!无自设种子了…'))
        A(cn('随机播种中…\n'))
        r3+=1
        if r3>3:
          guoq(buid+cn('可能播种失败'))
          return None
        cai=w0(u'http://nc.z.qq.com/farm/bag_list_seedall.jsp?sid='+mysid+u'&myuid='+myuid)
        fcai=cai.split(cn('>好友农场<'))
        uid1=fcai[1].split(u'<ahref="')
        tuid=uid1[1].split(u'">')
        url=tuid[0]
      elif cai.find(cn('申请号码'))>0:
        tid()
        zid(patha+'nm\\n_'+buid+'.txt')
        del url
        guoq(buid+cn(' 注意！书签可能过期了'))
      elif cai.find(cn('背包里没有种子了'))>0:
        A(cn('买种中……\n'))
        data=w0('http://nc.z.qq.com/farm/buy_action.jsp?sid=' + mysid + u'&myuid=' + myuid + u'&B_UID=' + buid + u'&num=99&id='+cid.encode('u8'))
        if data.find(cn('购买成功'))!=-1:
          A(cn('买种成功…\n'))
        elif data.find(cn('金币不足'))!=-1:
          guoq(buid+cn('金币不足,自动买种失败'))
          xun=0
        else:
          guoq(buid+cn('未知原因,自动买种失败！背包里没有种子了！'))
          xun=0
        pass
      elif cai.find(cn('>已成熟<'))>0:
        url='http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&all=true&B_UID='+buid+'&myuid='+myuid+'&uid='+myuid+'&money=0'
        A(cn('农场是〖已成熟〗状态 , 等待15秒返回…\n'))
        zt(15)
        r8+=1
        if r8>3:
          xun=0
          cai=u'noweb'
          guoq(buid+cn(' 农 已成熟 收获失败'))
        pass
      elif cai.find(cn('后成熟'))>0:
        if cai.find(cn('秒后'))>0:
          url=mload2()
        else:
          xun=0
        pass
      elif cai.find(cn('你成功'))>0 or cai.find(cn('您成功'))>0:
        fcai=cai.split(cn('成功'))
        uid1=fcai[1].split(cn('<'))
        A(cn('成功')+uid1[0]+u'\n')
        url='http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&all=true&B_UID='+buid+'&myuid='+myuid+'&uid='+myuid+'&money=0'
      else:
        r4+=1
        if r4>2:
          xun=0
          guoq(buid+cn(' 农 出现未知错误'))
        else:
          url='http://nc.z.qq.com/farm/index.jsp?sid='+mysid+'&all=true&B_UID='+buid+'&myuid='+myuid+'&uid='+myuid+'&money=0'
          A(cn('正在返回农场首页…\n'))
    except:
      url=u'http://nc.z.qq.com/farm/index.jsp?sid='+mysid+u'&B_UID='+buid
      cai=u'noweb'
      r6+=1
      if r6>2:
        guoq(buid+cn(' 农 错误'))
        return None
      pass
  global xun,cai
def dji(qqc):
  try:
    f=open(patha+u'others\\dj\\'+qqc,'r')
    f1=f.read().decode('u8')
    f.close()
  except:
    f1=cn('等级:暂无记录')
  try:
    f=open(patha+u'others\\dj\\m'+qqc,'r')
    f2=f.read().decode('u8')
    f1=f1+'\n'+f2
    f.close()
  except:
    pass
  return f1
def zhid():
  jsj=1
  if len(cc)==0:
    jj=qhqqd()
    if jj==0:
      jsj=0
    pass
  else:
    try:
      jj=cc[0]
    except:
      pass
    pass
  try:
    satime()
    hr=jj.split('|')
    jd=hr[0].split('.')
    dst=int(jd[0])
    qqc=hr[1]
    qqd=patha+u'nm\\'+qqc+'.txt'
  except:
    dst=jsj=0
  while run:
    dj=time.time()
    du2=(dst-dj)
    du3=(ttt-dj)
    B(cn(''))
    jsjt=str(time.ctime(dst)).split(' ')
    tqt=str(time.ctime(ttt)).split(' ')
    if jsj:
      if sytd==0:
        A(cn('[☆]自动收获时间：')+cn(jsjt[3]))
      else:
        A(cn('[☆]收获倒计时：'))
        showtime(du2)
      if tq:
        if sytd==0:
          A(cn('\n[★]自动偷取时间：')+cn(tqt[3]))
        else:
          A(cn('[☆]偷取倒计时：'))
          showtime(du3)
        pass
      else:
        pass
      pass
    elif tq:
      if sytd==0:
        A(cn('\n[★]自动偷取时间：')+cn(tqt[3]))
      else:
        A(cn('[☆]偷取倒计时：'))
        showtime(du3)
      pass
    else:
      B(cn('\n[★]没有开启自动收获和自动偷取！'))
    for i in range(0,len(er)):
      A('\n'+er[i])
    if dj>=ttt and tq:
      qqt(zdtl)
      suit()
    elif dj>=dst and jsj:
      menu2()
      zid(qqd)
      zt(0.1)
      B(cn('正在连接网络，请稍候……\n'))
      if nm==u'c':
        zt(0.1)
        sj=cshou()
      elif nm==u'n':
        zt(0.1)
        nshou()
        sj=readtime()
      elif nm==u'y':
        zt(0.1)
        yshou()
        sj=readtime()
      elif nm==u'm':
        A(cn('小提示！立即按6键可进入商店买仔(没满员和有设置买仔下有效)\n'))
        zt(0.1)
        mshou()
        if ifmz and mon!=u'n':
          for ba in range(3):
            mzai()
            mshou()
            if ifmz==0:
              break
          pass
        else:
          pass
        mzait()
        sj=readtime()
      zt(0.1)
      cc.pop(0)
      if sj>0:
        cc.append(str(time.time()+sj)+u'|'+nm+u'_'+buid)
      else:
        guoq(nm+cn('_')+buid+cn('没有定时！'))
      if len(cc)!=0:
        cc=min(cc)
        jj=cc[0]
      if cai==u'noweb':
        zt(2)
      menu1()
      break
    else:
      pass
    apo.stop()
    zt(1)
  global sj,cc
def delothers():
  p=patha+u'others\\dj\\'
  qqa=os.listdir(p)
  for i in range(len(qqa)):
    os.remove((p+qqa[i].decode('utf-8')).encode('u8'))
  p=patha+u'others\\zt\\'
  qqa=os.listdir(p)
  for i in range(len(qqa)):
    os.remove((p+qqa[i].decode('utf-8')).encode('u8'))
def zhinen():
  run=1
  while run:
    zhid()
    e32.ao_yield()
  global run
def about():
  import Helper
  Helper.about()
def clos():
  run=0
  zt(1)
  juz()
  ui.note(cn('收菜功能已关闭'))
  global run
def asid1():
  d=ui.query(cn('是否马上自动提取书签？'),'query')
  if d:
    asid()
  else:
    juz()
def suit():
  tt=random.randint(qaa,qab)
  ttt=time.time()+(tt*60)
  global ttt
suit()
def findzai():
  try:
    context=cai.split('<br/>')
    for i in range(0,len(context)):
      k=context[i]
      if k.find(cn('窝('))>0:
        kk=k.split('(')
        p=kk[2].split(')')
        p=p[0].split('/')
        w=kk[1].split(')')
        w=w[0].split('/')
        p0=int(p[0])
        p1=int(p[1])
        w2=int(w[0])
        w11=int(w[1])
        pp=(p1-p0)
        ww=(w11-w2)
      elif k.find(cn('牧草数量：'))>-1:
        kk=k.split('<')
        kk=kk[0].split(cn('：'))
        f=open(patha+u'others\\dj\\mm_'+buid,'w')
        f.write((time.strftime('  %m-%d %H:%M')+cn('你仓库中的牧草还剩：')+kk[1]).encode('utf8'))
        f.close()
  except:
    pp=ww=0
  global pp,ww
def mzai():
  try:
    A(cn('正在打开商店…\n'))
    url=u'http://pasture.z.qq.com/mc/shop.jsp?B_UID='+buid+u'&sid='+mysid
    cai=w0(url)
    zt(2)
    findzai()
    dwcai=cai.split(cn('>购买<'))
    if pp>0:
      if mon==u'd':
        for i in range(len(dwcai)):
          if dwcai[i].find(cn('(住棚)'))>0:
            bc=dwcai[i].split('cId=')
            bd=bc[1].split('&')
            pcid=bd[0]
            break
        pass
      h1=u'http://pasture.z.qq.com/mc/buy_animal_result.jsp?B_UID='+buid
      h2=u'&amount='+str(pp)+u'&sid='+mysid+u'&shed='+str(pp)+u'&den=0&type=1&cId='+pcid+u'&max='+str(pp)
      A(cn('正在购买棚幼仔…\n'))
      cai=w1(h1,h2)
      if cai.find(cn('购买成功'))>-1:
        pass
      else:
        guoq(buid+cn(' 可能购买幼仔失败'))
      pass
    zt(1)
    if ww>0:
      if mon==u'd':
        for i in range(len(dwcai)):
          if dwcai[i].find(cn('(住窝)'))>0:
            bc=dwcai[i].split('cId=')
            bd=bc[1].split('&')
            wcid=bd[0]
            break
        pass
      A(cn('正在购买窝幼仔…\n'))
      h1=u'http://pasture.z.qq.com/mc/buy_animal_result.jsp?B_UID='+buid
      h2=u'&amount='+str(ww)+u'&sid='+mysid+u'&shed=0&den='+str(ww)+u'&type=0&cId='+wcid+u'&max='+str(ww)
      cai=w1(h1,h2)
      if cai.find(cn('购买成功'))>-1:
        pass
      else:
        guoq(buid+cn(' 可能购买幼仔失败'))
      pass
  except:
    guoq(buid+cn(' 购买幼仔失败'))
  global cai,pcid,wcid
def mzait():
  ss=[]
  sj=0
  try:
    context=cai.split('<br/>')
    for i in range(0,len(context)):
      k=context[i]
      if k.find(cn('后可收获'))>0:
        try:
          if k.find(cn('小时'))>0 and k.find(cn('分'))>0:
            h=k.split(cn('小时'))
            f=h[1].split(cn('分'))
            sh=int(h[0])
            sf=int(f[0])
            sj=(sh*3600)+((sf*60)-10)
          elif k.find(cn('小时'))>0 and k.find(cn('分'))<0:
            sjf1=k.split(cn('小时'))
            sf=int(sjf1[0])
            sj=((sf*3600)-10)
          elif k.find(cn('小时'))<0 and k.find(cn('分'))>0:
            sjf1=k.split(cn('分'))
            sf=int(sjf1[0])
            sj=((sf*60)-10)
        except:
          sj=0
        if sj>0:
          ss.append(sj)
        pass
    if len(ss)>0:
      ss.sort()
      t1=time.time()+int(ss[0])
      stj=str(time.ctime(t1))
      sti=stj[2:-9]
      if len(zaii)==0:
        zaii.append(buid)
        guoq(buid+cn(' ‹')+str(sti)+cn('› ')+cn('买仔'))
      else:
        b=0
        for j in range(0,len(zaii)):
          k=er[j]
          if k.find(buid)>-1:
            b=1
            break
        if b==0:
          zaii.append(buid)
          guoq(buid+cn(' ‹')+str(sti)+cn('› ')+cn('买仔'))
        pass
      pass
  except:
    pass
def clck():
  B(cn('请选择你要卖的农牧场仓库\n'))
  qqd(1)
def mclck():
  import dialog
  url=u'http://pasture.z.qq.com/mc/sale_result.jsp?B_UID='+buid+u'&sid='+mysid+u'&saleAll=1'
  w=dialog.Wait(cn('正在清空牧场QQ:')+buid+cn('的仓库'))
  w.show()
  cai=w0(url)
  if cai.find(cn('卖出成功'))>-1:
    fcai=cai.split(cn('卖出成功'))
    mai=fcai[1].split(cn('金币'))
    ui.note(cn('牧场QQ:')+buid+cn('仓库卖出成功')+mai[0]+cn('金币!'))
  else:
    ui.note(cn('牧场QQ:')+buid+cn('卖出失败，没有东西可卖'))
def nclck():
  import dialog
  url=u'http://nc.z.qq.com/farm/sale_action.jsp?sid='+mysid+u'&B_UID='+buid+u'&type=1&myuid='+myuid
  w=dialog.Wait(cn('正在清空农场QQ:')+buid+cn('的仓库'))
  w.show()
  cai=w0(url)
  if cai.find(cn('卖出成功'))>-1:
    fcai=cai.split(cn('卖出成功'))
    mai=fcai[1].split(cn('金币'))
    ui.note(cn('农场QQ:')+buid+cn('仓库卖出成功')+mai[0]+cn('金币!'))
  else:
    ui.note(cn('农场QQ:')+buid+cn('卖出失败，没有东西可卖'))
def qqd(qd):
  qqa=os.listdir(patha+u'nm\\')
  if len(qqa)==0:
    ui.note(cn('没有设置qq农牧场登陆信息！'))
  else:
    B(cn('可多项选择……\n'))
    zt(2)
    qqg=[]
    for q in range(len(qqa)):
      if not(os.path.isdir(patha+u'nm\\'+qqa[q])):
        if qqa[q][:1]==u'm' or qqa[q][:1]==u'n':
          qqg.append(qqa[q][:-4].decode('utf8'))
    if len(qqg)==0:
      ui.note(cn('没有设置qq农牧场登陆信息！'))
      return None
    index=ui.multi_selection_list(qqg,style='checkbox',search_field=1)
    zt(0.1)
    B(cn('正在连接网络，请稍候……\n'))
    for i in index:
      qqd=patha+u'nm\\'+qqg[i]+'.txt'
      zid(qqd)
      if nm==u'm':
        if qd==1:
          mclck()
        elif qd==2:
          A(cn('正在进行牧场偷取！\n'))
          A(cn('小提示！可按拨号键中止偷！\n'))
          if tl==1:
            kjmtou()
            xymtou()
          elif tl==2:
            kjmtou()
          elif tl==3:
            xymtou()
          pass
        pass
      elif nm==u'n':
        if qd==1:
          nclck()
        elif qd==2:
          A(cn('正在进行农场偷取！\n'))
          A(cn('小提示！可按拨号键中止偷！\n'))
          if tl==1:
            kjtou()
            xytou()
          elif tl==2:
            kjtou()
          elif tl==3:
            xytou()
          pass
        pass
    pass
  apo.stop()
def se():
  try:
    import globalui
    ff=open(patha+u'time','r')
    c=ff.read()
    ff.close()
    cc=c.split('/')
    f=''
    for i in range(0,len(cc)):
      g=cc[i].split('|')
      d2=g[0].split('.')
      du1=(int(d2[0])-time.time())
      e=str((i+1))+': '+g[1]+' ('+(u'%02d:%02d:%02d' % ((du1/3600),((du1 % 3600)/60),((du1 % 3600) % 60)))+')\n'+dji(g[1])
      if len(f)<1:
        f=f+e
      else:
        f=f+'\n\n'+e
    globalui.global_msg_query(f,cn('查看全部倒计时'))
  except:
    ui.note(cn('无时间或无globalui模块请换个PY平台'))
def ifmzo():
  ifmz=1
  global ifmz
def tstop():
  run1=0
  global run1
def menu2():
  ui.app.menu=[(cn('返回主菜单'),menu1)]
def menu4():
  ui.app.menu=[(cn('查看验证码'),ym2),(cn('返回主菜单'),menu1)]
def menu3():
  ui.app.menu=[(cn('立即停止偷'),tstop),(cn('返回主菜单'),menu1)]
def menu1():
  ui.app.menu=[(cn('智能工作'),((cn('开启智能'),zhinen),(cn('关闭智能'),clos))),(cn('农牧管理'),((cn('自动提取'),asid),(cn('手动提取'),sid),(cn('删除农牧场'),delsid),(cn('编辑农牧场'),editsid))),(cn('农牧功能'),((cn('选择偷菜'),qqtou2),(cn('直接偷菜'),qqtou),(cn('仓库卖出'),clck),(cn('删除计时'),cltime))),(cn('其它功能'),((cn('支持.反馈'),zc_fk),(cn('更新帮手'),lookll),(cn('关于软件'),about),(cn('软件设置'),qtsz),(cn('接入点设置'),set_ac))),(cn('查看功能'),((cn('全部倒计时'),se),(cn('农牧场详情'),se5),(cn('查看偷取记录'),semn),(cn('删除偷取记录'),delmn))),(cn('退出程序'),exit)]
menu1()
m.bind(35,qqtou)
m.bind(42,juz1)
m.bind(48,qqtou2)
m.bind(50,ym2)
m.bind(51,se5)
m.bind(53,zc_fk)
m.bind(54,ifmzo)
m.bind(55,lookll)
m.bind(56,ltpw)
m.bind(57,qtsz)
m.bind(8,clserror)
m.bind(63586,tstop)
url_f='http://f.10086.cn/d/dlkjava.fcc?clientId=938&commondownloadUrl='
zhinen()