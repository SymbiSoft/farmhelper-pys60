import appuifw2 as ui,os,e32
patha=(ui.app.full_name()[:3]+u'system\\apps\\FarmHelper\\').encode('u8')
cn=lambda x,:x.decode('utf-8') 
en=lambda x,:x.encode('utf-8') 
def helpsid():
  try:
    import globalui
    f=cn('请用自带浏览器或其他浏览器登录农场，在打开好友农场页面。在存为书签。最后编辑刚才存的书签，就可以看到下面例子的样子。\n例：http://farm2.z.qq.com/farm/friend_list.jsp?sid=HT6sJsslljhFyTS4N6KV5A==&myuid=129674552&KmttWap_Act=1&uin=123456789\n从上面找到\nHT6sJsslljhFyTS4N6KV5A==就是sid了，\n129674552就是myuid\n123456789就是QQ号了。\n牧场方法也差不多')
    globalui.global_msg_query(f,cn('提取农牧场书签的方法'))
  except:
    ui.note(cn('无globalui模块'))
def qhqq():
  qqa=os.listdir(patha+u'nm\\')
  qqg=[]
  for q in range(0,len(qqa)):
    qqg.append(qqa[q][:-4].decode('utf8'))
  if len(qqg)==0:
    ui.note(cn('没有设置qq农牧场登陆信息！'))
  else:
    qqb=ui.popup_menu(qqg,cn('请选择qq农牧场'))
    if qqb>-1:
      qqc=qqa[qqb].decode('utf8')
    else:
      return 0
    qqd=patha+u'nm\\'+qqc
    qh=open(qqd,'r')
    qhr=qh.read().decode('utf8')
    qh.close()
    qhre=qhr.split('|')
    mysid3=qhre[1]
    qnm=qhre[0].split('_')
    nm3=qnm[0]
    buid3=qnm[1]
    if nm3==u'n':
      myuid3=qhre[3]
    elif nm3==u'y':
      myuid3=qhre[2]
    pass
  global mysid3,nm3,buid3,myuid3
def delsid():
  qqa=os.listdir(patha+u'nm\\')
  qqg=[]
  for q in range(0,len(qqa)):
    qqg.append(qqa[q][:-4].decode('utf8'))
  if len(qqg)==0:
    ui.note(cn('没有设置qq农牧场登陆信息！'))
  else:
    qqb=ui.popup_menu(qqg,cn('请选择需删除农牧场'))
    if qqb>-1:
      qqc=qqa[qqb].decode('utf8')
      os.remove(patha+u'nm\\'+qqc)
      ui.note(cn('已删除QQ:')+qqc[:-4]+cn('农(牧)场,请重启软件'))
      return 1
    else:
      return 0
def sid():
  helpsid()
  mybuidno=ui.query(cn('请输入qq号码'),'number')
  if mybuidno>0:
    mysid=ui.query(cn('请输入登录sid'),'text')
    if mysid!=None:
      myuidno=ui.query(cn('请输入农场myuid'),'number')
      if myuidno>0:
        nmysid=str(mysid)
        nbuid=str(mybuidno)
        nmyuid=str(myuidno)
        naid(nbuid,nmysid,nmyuid)
        yes=ui.query(cn('是否还有添加牧场'),'query')
        if yes:
          maid(nbuid,nmysid)
        pass
      pass
    pass
def msid():
  helpsid()
  mybuidno=ui.query(cn('请输入qq号码'),'number')
  if mybuidno>10000:
    mysid3=ui.query(cn('请输入登录sid '),'text')
    if len(mysid3)==24:
      mmysid=str(mysid3)
      mbuid=str(mybuidno)
      maid(mbuid,mmysid)
    else:
      ui.note(cn('登录sid有误'))
    pass
def naid(nbuid,nmysid,nmyuid):
  cd1=[cn('普通种子'),cn('黄钻种子'),cn('有机种子')]
  c1=ui.popup_menu(cd1,cn('请选择播种种类'))
  if c1==0:
    cid=scid()
  elif c1==1:
    hzcid=hzscid()
    cid=hzcid
  elif c1==2:
    yrcid=yrscid()
    cid=yrcid
  if c1!=None:
    cd2=[cn('普通种子'),cn('黄钻种子'),cn('有机种子'),cn('红土地种子')]
    c2=ui.popup_menu(cd2,cn('请选择播种种类'))
    if c2==0:
      cid=scid()
      rcid=cid
    elif c2==1:
      hzcid=hzscid()
      rcid=hzcid
    elif c2==2:
      yrcid=yrscid()
      rcid=yrcid
    elif c2==3:
      rcid=rscid()
    if c2!=None:
      cd3=[cn('普通种子'),cn('黄钻种子'),cn('有机种子'),cn('红土地种子'),cn('黑土地种子')]
      c3=ui.popup_menu(cd3,cn('请选择播种种类'))
      if c3==0:
        cid=scid()
        hcid=cid
      elif c3==1:
        hzcid=hzscid()
        hcid=hzcid
      elif c3==2:
        yrcid=yrscid()
        hcid=yrcid
      elif c3==3:
        rcid=rscid()
        hcid=rcid
      elif c3==4:
        hcid=hscid()
      if c3!=None:
        bb=[cn('是'),cn('否'),cn('8至24点偷')]
        s2=ui.popup_menu(bb,cn('请选择是否偷菜'))
        if s2==0:
          t1=u'y'
        elif s2==2:
          t1=u'yn'
        else:
          t1=u'n'
        kk=open(patha+u'nm\\n_'+nbuid+'.txt','w')
        kk.write(u'n_'+nbuid+'|'+nmysid+'|'+t1+'|'+nmyuid+'|'+cid+'|'+rcid+'|'+hcid)
        kk.close()
        ui.note(cn('qq农场已保存\n如果有设置除草杀虫将会体现倒计时中'))
      pass
    pass
def csid():
  helpsid()
  cybuidno=ui.query(cn('请输入qq号码'),'number')
  if cybuidno>10000:
    cysid3=ui.query(cn('请输入登录sid '),'text')
    if len(cysid3)==24:
      cmysid=str(cysid3)
      cbuid=str(cybuidno)
      caid(cbuid,cmysid)
    else:
      ui.note(cn('登录sid有误'))
    pass
def caid(cbuid,cmysid):
  zx=ui.query(cn('请输入餐厅操作间隔最小值(分钟)，小于60分钟算60分钟'),'number')
  if zx==None or zx<60:
    zx=60
  zd=ui.query(cn('请输入餐厅操作间隔最大值(分钟)，小于60分钟算60分钟'),'number')
  if zd==None or zd<60:
    zd=60
  csgs=ui.query(cn('请输入餐厅雇佣厨师的人数，小于0人算0人！'),'number')
  if csgs==None or csgs<0:
    csgs=0
  kk=open(patha+'nm\\c_'+cbuid+'.txt','w')
  kk.write(u'c_'+cbuid+'|'+cmysid+'|'+str(zx)+'|'+str(zd)+'|'+str(csgs))
  kk.close()
  ui.note(cn('qq餐厅已保存'))
def maid(mbuid,mmysid):
  b=ui.query(cn('是否自动买幼仔'),'query')
  if b:
    d=ui.query(cn('是否买等级相对应的幼仔'),'query')
    if d:
      b=u'd'
      p=u'1001'
      w=u'1501'
    else:
      b=u'y'
      p=pscid()
      w=wscid()
    pass
  else:
    b=u'n'
    p=u'0'
    w=u'0'
  bb=[cn('是'),cn('否'),cn('8至24点偷')]
  s2=ui.popup_menu(bb,cn('请选择是否偷动物'))
  if s2==0:
    t1=u'y'
  elif s2==2:
    t1=u'yn'
  else:
    t1=u'n'
  kk=open(patha+u'nm\\m_'+mbuid+'.txt','w')
  kk.write(u'm_'+mbuid+'|'+mmysid+'|'+t1+'|'+b+'|'+p+'|'+w)
  kk.close()
  ui.note(cn('qq牧场已保存'))
def medi():
  mybuidno=ui.query(cn('请输入qq号码'),'number',int(buid3))
  if mybuidno>10000:
    mysid3=ui.query(cn('请输入登录sid'),'text',mysid3)
    if mysid3!=None:
      mmysid=str(mysid3)
      mbuid=str(mybuidno)
      maid(mbuid,mmysid)
    pass
  global mysid3
def cedi():
  mybuidno=ui.query(cn('请输入qq号码'),'number',int(buid3))
  if mybuidno>10000:
    mysid3=ui.query(cn('请输入登录sid'),'text',mysid3)
    if mysid3!=None:
      cmysid=str(mysid3)
      cbuid=str(mybuidno)
      caid(cbuid,cmysid)
    pass
  global mysid3
def ysid():
  helpsid()
  mybuidno=ui.query(cn('请输入qq号码'),'number')
  if mybuidno>0:
    mysid=ui.query(cn('请输入登录sid'),'text')
    if mysid!=None:
      myuidno=ui.query(cn('请输入渔场myuid'),'number')
      if myuidno>0:
        ymysid=str(mysid)
        ybuid=str(mybuidno)
        ymyuid=str(myuidno)
        yaid(ybuid,ymysid,ymyuid)
      pass
    pass
def yedi():
  mybuidno=ui.query(cn('请输入qq号码'),'number',int(buid3))
  if mybuidno>0:
    mysid=ui.query(cn('请输入登录sid'),'text',mysid3)
    if mysid!=None:
      myuidno=ui.query(cn('请输入农场myuid'),'number',int(myuid3))
      if myuidno>0:
        ymysid=str(mysid)
        ybuid=str(mybuidno)
        ymyuid=str(myuidno)
        yaid(ybuid,ymysid,ymyuid)
      pass
    pass
def yaid(ybuid,ymysid,ymyuid):
  cid=ytcid()
  kk=open(patha+u'nm\\y_'+ybuid+'.txt','w')
  kk.write(u'y_'+ybuid+'|'+ymysid+'|'+ymyuid+'|'+cid)
  kk.close()
  ui.note(cn('qq鱼塘已保存'))
def editsid():
  g=qhqq()
  if g==0:
    return None
  if nm3==u'c':
    cedi()
    return None
  if nm3==u'y':
    yedi()
    return None
  if nm3==u'm':
    medi()
    return None
  mybuidno=ui.query(cn('请输入qq号码'),'number',int(buid3))
  if mybuidno>10000:
    mysid3=ui.query(cn('请输入登录sid'),'text',mysid3)
    if mysid3!=None:
      myuidno=ui.query(cn('请输入农场myuid'),'number',int(myuid3))
      if myuidno>0:
        nmysid=str(mysid3)
        nbuid=str(mybuidno)
        nmyuid=str(myuidno)
        naid(nbuid,nmysid,nmyuid)
      pass
    pass
  global mysid3
def pscid():
  my=1
  try:
    f=open(patha+u'cid\\pcid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择购买棚动物'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      rcid=int(cidn[0])
      rcid=str(rcid)
      ui.note(cn('你选择的动物是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入动物id'),'number')
    if my>0:
      rcid=str(my)
      ui.note(cn('你输入的动物是'+rcid))
    else:
      ui.note(cn('你没选择动物默认是 羊'))
      rcid=u'1501'
    pass
  return rcid
def wscid():
  my=1
  try:
    f=open(patha+u'cid\\wcid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择购买窝动物'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      rcid=int(cidn[0])
      rcid=str(rcid)
      ui.note(cn('你选择的动物是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入动物id'),'number')
    if my>0:
      rcid=str(my)
      ui.note(cn('你输入的动物是'+rcid))
    else:
      ui.note(cn('你没选择动物默认是 鸡'))
      rcid=u'1001'
    pass
  return rcid
def hzscid():
  my=1
  try:
    f=open(patha+'cid\\hzcid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择黑土地种子'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      hzcid=int(cidn[0])
      hzcid=str(hcid)
      ui.note(cn('你选择的种子是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入种子id'),'number')
    if my>-1:
      hzcid=str(my)
      ui.note(cn('你输入的种子是'+hzcid))
    else:
      ui.note(cn('你没选择种子默认是牧草'))
      hzcid=u'40'
    pass
  return hzcid
def hscid():
  my=1
  try:
    f=open(patha+'cid\\hcid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择黑土地种子'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      hcid=int(cidn[0])
      hcid=str(hcid)
      ui.note(cn('你选择的种子是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入种子id'),'number')
    if my>-1:
      hcid=str(my)
      ui.note(cn('你输入的种子是'+hcid))
    else:
      ui.note(cn('你没选择种子默认是牧草'))
      hcid=u'40'
    pass
  return hcid
def rscid():
  my=1
  try:
    f=open(patha+u'cid\\rcid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择红土地种子'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      rcid=int(cidn[0])
      rcid=str(rcid)
      ui.note(cn('你选择的种子是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入种子id'),'number')
    if my>-1:
      rcid=str(my)
      ui.note(cn('你输入的种子是'+rcid))
    else:
      ui.note(cn('你没选择种子默认是牧草'))
      rcid=u'40'
    pass
  return rcid
def yrscid():
  my=1
  try:
    f=open(patha+u'cid\\yrcid.txt','r')
    yrcidtxt=f.read().decode('utf8')
    f.close()
    cait=yrcidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择有机种子'))
    if ids>-1:
      yrcidn=cait[ids].split(cn(':'))
      yrcid=int(yrcidn[0])
      yrcid=str(yrcid)
      ui.note(cn('你选择的种子是:')+yrcidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入种子id'),'number')
    if my>-1:
      yrcid=str(my)
      ui.note(cn('你输入的种子是'+yrcid))
    else:
      ui.note(cn('你没选择种子默认是牧草'))
      yrcid=u'40'
    pass
  return yrcid
def scid():
  my=1
  try:
    f=open(patha+u'cid\\cid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split(cn('|'))
    ids=ui.popup_menu(cait,cn('请选择普通地种子'))
    if ids>-1:
      cidn=cait[ids].split(cn(':'))
      cid=int(cidn[0])
      cid=str(cid)
      ui.note(cn('你选择的种子是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入种子id'),'number')
    if my>-1:
      cid=str(my)
      ui.note(cn('你输入的种子是'+cid))
    else:
      ui.note(cn('你没选择种子默认是牧草'))
      cid=u'40'
    pass
  return cid
def ytcid():
  my=1
  try:
    f=open(patha+u'cid\\ycid.txt','r')
    cidtxt=f.read().decode('utf8')
    f.close()
    cait=cidtxt.split('|')
    ids=ui.popup_menu(cait,cn('请选择鱼苗'))
    if ids>-1:
      cidn=cait[ids].split(':')
      rcid=int(cidn[0])
      rcid=str(rcid)
      ui.note(cn('你选择的鱼苗是:')+cidn[1])
    else:
      my=0
  except:
    my=0
  if my==0:
    my=ui.query(cn('请输入鱼苗id'),'number')
    if my>0:
      rcid=str(my)
      ui.note(cn('你输入的鱼苗是'+rcid))
    else:
      ui.note(cn('你没选择鱼苗默认是 ?'))
      rcid=u'1'
    pass
  return rcid
def delmn():
  list=[cn('删除牧场记录'),cn('删除农场记录')]
  index=ui.popup_menu(list,cn('请选择记录类型：'))
  if index==0:
    pathb=patha+u'mc\\'
  elif index==1:
    pathb=patha+u'nc\\'
  else:
    return None
  try:
    try:
      qqa=os.listdir(pathb)
    except:
      ui.note(cn('没有记录！'))
      return None
    qqg=[]
    for q in range(0,len(qqa)):
      qqg.append(qqa[q].decode('utf8'))
    if len(qqg)==0:
      ui.note(cn('没有记录！'))
    else:
      qqb=ui.popup_menu(qqg,cn('选择要删除的QQ记录'))
      if qqb>-1:
        qqc=qqa[qqb].decode('utf8')
      else:
        return None
    qqa=os.listdir(pathb+qqc)
    for i in range(len(qqa)):
      os.remove((pathb+qqc+u'\\'+qqa[i].decode('utf-8')).encode('u8'))
    os.rmdir(pathb+qqc)
    ui.note(cn('删除记录成功！'))
  except:
    ui.note(cn('删除记录失败！未知错误！'))
def semn():
  list=[cn('查看牧场记录'),cn('查看农场记录')]
  index=ui.popup_menu(list,cn('请选择记录类型：'))
  if index==0:
    se2()
  if index==1:
    se3()
def se2():
  try:
    import globalui
    f=u''
    e=0
    qqa=os.listdir(patha+u'mc\\')
    qqg=[]
    for q in range(0,len(qqa)):
      qqg.append(qqa[q].decode('utf8'))
    if len(qqg)==0:
      pass
    else:
      qqb=ui.popup_menu(qqg,cn('请选择QQ号'))
      if qqb>-1:
        qqc=qqa[qqb].decode('utf8')
      else:
        return None
    qqa=os.listdir(patha+u'mc\\'+qqc)
    for i in range(len(qqa)):
      ff=open((patha+u'mc\\'+qqc+u'\\'+qqa[i].decode('utf-8')).encode('u8'),'r')
      c=ff.read().decode('utf-8')
      ff.close()
      f=f+qqa[i][:-4].decode('utf-8')+cn('×')+c+u'\n'
      e=e+int(c)
    f=f+cn('偷到合计数量：')+str(e)
    globalui.global_msg_query(f,cn('查看偷到动物'))
  except:
    ui.note(cn('没有记录或无globalui模块'))
def se3():
  try:
    import globalui
    f=u''
    e=0
    qqa=os.listdir(patha+u'nc\\')
    qqg=[]
    for q in range(0,len(qqa)):
      qqg.append(qqa[q].decode('utf8'))
    if len(qqg)==0:
      pass
    else:
      qqb=ui.popup_menu(qqg,cn('请选择QQ号'))
      if qqb>-1:
        qqc=qqa[qqb].decode('utf8')
      else:
        return None
    qqa=os.listdir(patha+u'nc\\'+qqc)
    for i in range(len(qqa)):
      ff=open((patha+u'nc\\'+qqc+u'\\'+qqa[i].decode('utf-8')).encode('u8'),'r')
      c=ff.read().decode('utf-8')
      ff.close()
      f=f+qqa[i][:-4].decode('utf-8')+cn('×')+c+u'\n'
      e=e+int(c)
    f=f+cn('偷到合计数量：')+str(e)
    globalui.global_msg_query(f,cn('查看偷到的菜'))
  except:
    ui.note(cn('没有记录或无globalui模块'))
def se5():
  try:
    import globalui
    f=u''
    e=0
    qqa=os.listdir(patha+u'others\\zt\\')
    qqg=[]
    for q in range(0,len(qqa)):
      qqg.append(qqa[q].decode('utf8'))
    if len(qqg)>0:
      qqb=ui.popup_menu(qqg,cn('请选择要查看农牧场'))
      if qqb>-1:
        qqc=qqa[qqb].decode('utf8')
        ff=open(patha+u'others\\zt\\'+qqc,'r')
        c=ff.read().decode('utf-8')
        ff.close()
        f=c.replace('<br/>','\n')
        globalui.global_msg_query(f,cn('查看农牧场'))
      pass
  except:
    ui.note(cn('没有记录或无globalui模块'))
def about():
  try:
    import globalui
    globalui.global_msg_query(cn('软件名称：农牧帮手\n软件版本：v1.43.0版\n软件指导：专程路过\nQQ:34738831\n软件作者：絶恋\nQQ:1123817754\nE-mail: vip_12_vip@163.com\n特别声明：本程序不保证能兼容所有手机硬件，您必须自行担负所有可能因使用本程序而发生的风险！\n　　　　　　 2012-04-15'),cn('关于程序'))
  except:
    ui.note(cn('无globalui模块请换个PY平台'))
def qtsz():
  try:
    f=open(patha+u'farmq.txt','r')
    a=f.read().decode('utf8')
    f.close()
    b=a.split('|')
    x0=int(b[0])
    x1=int(b[1])
    x2=int(b[2])
    x3=int(b[3])
    x4=int(b[4])
    x5=int(b[5])
    x6=int(b[6])
    x7=int(b[7])
    x8=int(b[8])
    x9=int(b[9])
    x10=int(b[10])
    x11=int(b[11])
    x12=int(b[12])
    x13=int(b[13])
    x14=int(b[14])
  except:
    x0=0
    x1=0
    x2=0
    x3=0
    x4=1
    x5=0
    x6=0
    x7=3
    x8=1
    x9=0
    x10=1
    x11=180
    x12=240
    x13=200
    x14=200
  lista=[(cn('计时方式'),'combo',([cn('顺计时'),cn('倒计时')],x0)),(cn('软件右键'),'combo',([cn('后台'),cn('隐藏')],x1)),(cn('音乐提示'),'combo',([cn('关闭'),cn('开启')],x2)),(cn('振动提示'),'combo',([cn('关闭'),cn('开启')],x3)),(cn('后台提示'),'combo',([cn('关闭'),cn('验证码')],x4)),(cn('字体颜色'),'combo',([cn('七   彩'),cn('红   色'),cn('绿   色'),cn('蓝   色'),cn('牡丹红'),cn('青   色'),cn('黄   色'),cn('黑   色'),cn('海   蓝'),cn('海紫色'),cn('青铜色'),cn('亮金色'),cn('深绿色'),cn('深紫色'),cn('淡灰色'),cn('火砖色'),cn('森林绿'),cn('金   色'),cn('浅黄色'),cn('浅蓝色'),cn('白   色')],x5)),(cn('字体模式'),'combo',([cn('不用特殊'),cn('删除线'),cn('高亮圆体'),cn('高亮阴影'),cn('高亮正常'),cn('粗体'),cn('斜体'),cn('下划线')],x6)),(cn('字体大小'),'combo',([cn('十   一'),cn('十   二'),cn('十   三'),cn('十   四'),cn('十   五'),cn('十   六'),cn('十   七'),cn('十   八'),cn('十   九'),cn('二   十')],x7)),(cn('验证码查看方式'),'combo',([cn('浏览器打开'),cn('直接显示')],x8)),(cn('自动偷取'),'combo',([cn('关闭自动偷取'),cn('全部开启自动偷取'),cn('牧场开启自动偷取'),cn('农场开启自动偷取')],x9)),(cn('自动偷取类型'),'combo',([cn('偷取全部好友'),cn('偷取空间好友'),cn('偷取校友好友')],x10)),(cn('自动偷取时间最短数'),'number',x11),(cn('自动偷取时间最长数'),'number',x12),(cn('农场偷取人数最多'),'number',x13),(cn('牧场偷取人数最多'),'number',x14)]
  Ma=ui.Form(lista,(ui.FFormEditModeOnly | ui.FFormDoubleSpaced))
  Ma.execute()
  if Ma[2][2][1]==1:
    t1=ui.query(cn('是否更换音乐？'),'query')
    if t1:
      import powlite_fm
      k=powlite_fm.manager().AskUser('e:\\',ext=['.mp3','.mid','.wma'])
      try:
        k=k.encode('utf-8')
        f=open(patha+u'farmok.txt','w')
        f.write(k)
        f.close()
        ui.note(cn('更换成功！'))
      except:
        ui.note(cn('取消更换！'))
      pass
    else:
      try:
        f=open(patha+u'farmok.txt','r')
        f.close
      except:
        f=open(patha+u'farmok.txt','w')
        f.write(patha+u'ok.mid')
        f.close()
      pass
    pass
  else:
    pass
  f=open(patha+u'farmq.txt','w')
  f.write(str(Ma[0][2][1])+'|'+str(Ma[1][2][1])+'|'+str(Ma[2][2][1])+'|'+str(Ma[3][2][1])+'|'+str(Ma[4][2][1])+'|'+str(Ma[5][2][1])+'|'+str(Ma[6][2][1])+'|'+str(Ma[7][2][1])+'|'+str(Ma[8][2][1])+'|'+str(Ma[9][2][1])+'|'+str(Ma[10][2][1])+'|'+str(Ma[11][2])+'|'+str(Ma[12][2])+'|'+str(Ma[13][2])+'|'+str(Ma[14][2]))
  f.close()