# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:43:26 2018

@author: Bing
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:03:59 2018

@author: Bing
"""



import math



#主函数部分
def main(fc,fr,N,t,layer,B,H,Eg,Ig,Ec,tt,M00,M01):
    H0=146#板中心到顶板
    H1=143#混凝土厚度
    cd=int(30/layer)#初定层数
    cdd=int(H1/layer)
    
    As=3.1413*6*6*5
    Es=196000
    f1=H0*6*Eg*B-cd*layer*Eg*6*B#frpD底板
    f2=0#混凝土顶板
    f3=Es*As*(cd*layer-30)#钢筋
    f4=0# frp承拉侧板
    for i in range(cd,cdd):                      #'i是混凝土受压层数
        if(((f1+f4)>1.01*(f2+f3))):#|((f1+f4)<0.95*(f2+f3))):           #'如果超出限度，则执行
            f2=0
            f1=f1-layer*6*Eg*B 
            f3=f3+layer*As*Es
            f4=0           #'数字2为初期定义的分层厚度
            for j in range(1,i+1):
                f2=f2+layer*(layer*j-layer/2)*Ec[j]*B
            #if(i)
            for js in range(int((H1-74)/layer-i),int(H1/layer-i)+1):
                f4=f4+layer*(layer*js-layer/2)*Eg*24 #'第一和二个2为分层厚度，第一个1为厚度的一半
            s1=f1+f4
            s2=f2+f3
        else:
            break
    
    i=i-1
    M1=0                                         #'M1为混凝土受压弯矩
    M2=(H0-layer*i)**2*Eg*B*6                              #'M2为frp底板弯矩，2为分层厚度
    M3=(i*layer-30)**2*Es*As
    for k in range(1,i+1):
         M1=M1+layer*B*(layer*i-layer*(k-1)-layer/2)**2*Ec[k]           #'M1为混凝土弯矩，2为分层厚度，倒数第一个1为分层厚度一半
    M4=0
    for js in range(int((H1-74)/layer-i),int(H1/layer-i)+1):
        M4=M4+layer*(layer*js-layer/2)**2*Eg*24
    M1=M1+M3
    M2=M2+M4
    M3=M1+M2                                      #'M3为混凝土和FRP弯矩和
    K0=M00/M3                                     
    K1=M01/M3
    deta0=[0]*(i+1)
    deta1=[0]*(i+1)
    detaave=[0]*(i+1)
    detarange=[0]*(i+1)
    strain=[0]*(i+1)
    En=[0]*(i+1)
    En[0]=28000
    nee=[0]*(i+1)
    e0=[0]*(i+1)
    e1=[0]*(i+1)
    e3=[0]*(i+1)
    for kr in range(1,i+1):
        e0[kr]=K1*(layer*i-layer*1+layer/2)*10**6
        e1[kr]=K1*(layer*(cdd-i)-layer*1+layer)*10**6
        e3[kr]=K1*(layer*(cdd-i)+3)*10**6
        deta0[kr]=Ec[kr]*K0*(layer*i-layer*kr+layer/2)#'第k层最小应力，2为分层厚度，1为分层厚度一半
        deta1[kr]=Ec[kr]*K1*(layer*i-layer*kr+layer/2)              #'第k层最大应力，2为分层厚度，1为分层厚度一半
        detaave[kr]=(deta0[kr]+deta1[kr])/2/fc        # '第k层平均应力
        detarange[kr]=(deta1[kr]-deta0[kr])/fc        # '第k层应力幅值                         
        strain[kr]=(129*detaave[kr]*t[tt]**(1/3)+17.8*detaave[kr]*detarange[kr]*N[tt]**(1/3))/1000000#'应变
        En[kr]=deta1[kr]/(deta1[kr]/Ec[0]+strain[kr])   #'折损弹性模量
        nee[kr]=Ec[0]/En[kr]
#    En.append()

    return En,i,strain,nee,e0,e1,e3

#参数部分    
fc=29
fr=2.80
N=[0,0.0001,1.0,2.0,3.0,5.0,10.0,20.0,50.0,100.0,150.0,200.0]
#'N=list(N)'
t=[ii/4/3600*10000 for ii in N]
layer=0.1#input("输入分层厚度：")'
B=600
H=150
Eg=32000
Ig=B*H**3/12
Ec=[28000]*(int(146/layer+1))
E0=28000
test1=[]
test1=[33000,33000,33000,33000,33000,33000,33000,33000,33000,33000,33000,33000]
f1=150*6*Eg
f2=0
a=550
l=1600
H0=146#板中心到顶板
H1=140#混凝土厚度
M00=20*0.55*10**6                                    #'M00为加载下限弯矩
M01=50*.55*10**6                                   #'M01为加载上限弯矩
F=[50000,50000,50000,50000,50000,50000,60000,70000,80000,90000,100000,200000,300000]
"""
print 'hello'
strain = [[] for ist  in range(9)]
EN = [[] for ien  in range(9)]
for kkk in range(1,9):
    strain[kkk].append(0)'应变
    EN[kkk].append(0)    '折损弹性模量
"""
naodu = [[] for ist  in range(14)]
ybs= [[] for ist  in range(14)]
ybx= [[] for ist  in range(14)]
#主要运算部分
for tt in range(1,12):
    
    Ec,i,test1,neee,ee0,ee1,ee3=main(fc,fr,N,t,layer,B,H,Eg,Ig,Ec,tt,M00,M01)
    for mmm in range(1,10000):
        Ec.append(28000)
    
    
    frN=fr*(1-math.log10(N[tt])/10.954)
                     
    ii=744
    ne=E0/Eg
    Ig=B*(H1*1)**3/12+B*H1*(layer*ii-H1/2)**2+B/ne*6**3/12+B/ne*6*(H0-layer*ii)**2+24/ne*74**3/12+74/ne*24*(H1-layer*ii-74/2)**2
    McrN=Ig*fr/(H1-layer*ii)
    fddd=McrN/550
    IcrN1=0
    for kr in range(1,i+1):
        IcrN1=IcrN1+B/neee[kr]*(layer*1)**3/12+B/neee[kr]*(layer*1)*(layer*i-layer*kr+layer/2)**2
    IcrN=B/ne*6**3/12+B/ne*6*(H0-layer*i)**2+24/ne*74**3/12+74/ne*24*(H1-layer*i-74/2)**2
    IcrN=IcrN+IcrN1
    IeN=IcrN+(McrN/M01)**3*(Ig-IcrN)
    for kk in range(1,13):
        naodu[tt].append(F[kk]*a*(3*l*l-4*a*a)/24/E0/IeN)
        ybs[tt].append(ee0[kk])
        ybx[tt].append(ee3[kk])
#    for kk in range(1,13)
#        naodu[tt].append(F[kk]*a*(3*l*l-4*a*a)/(24*Ec[1]*IeN))
