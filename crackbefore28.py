# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:07:23 2018

@author: Bing
"""
#开裂前的
import math

tt=0
fc=29
fr=2.30
N=[0,0.0001,1.0,3.0,10.0,50.0,100.0,150.0,200.0] # 循环次数
#'N=list(N)'
t=[ii/4/3600*10000 for ii in N]
layer=0.1#input("输入分层厚度：")'
B=600 # 组合板总宽
H=150 # 组合板高度
H0=146#板中心到顶板
H1=140#混凝土厚度
Eg=32600
Ig=B*H**3/12
Ec=[28000]*(int(146/layer+1))
test1=[]
test1=[33000,33000,33000,33000,33000,33000,33000,33000,33000,33000,33000,33000]

a=550
l=1600
M00=10/2*0.55*10**6                                    #'M00为加载下限弯矩
M01=50*0.55*10**6                                   #'M01为加载上限弯矩
F=[0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000]

Es=20000
cd=int(30/layer)#初定层数
cdd=int(H1/layer)#混凝土层数
As=3.1413*6*6*5
f1=H0*6*Eg*B-cd*layer*Eg*6*B#frp
f2=0#混凝土shang
f3=Es*As*(cd*layer-30)#钢筋
f4=0#混凝土xia
f20=0

for i in range(cd,cdd):                      #'i是混凝土受压层数
        if(((f1+f4)>1.001*(f2+f3))):#|((f1+f4)<0.97*(f2+f3))):           #'如果超出限度，则执行
            f2=0
            f4=0
            f1=f1-layer*6*Eg*B                        #'数字2为初期定义的分层厚度
            f3=f3+layer*As*Es
            if(i<int((H1-74)/layer)):
                for j in range(1,i+1):                
                    f2=f2+layer*(layer*j-layer/2)*Ec[j]*B     #'第一和二个2为分层厚度，第一个1为厚度的一半
            else:
                for j in range(1,i+1):                
                    f2=f2+layer*(layer*j-layer/2)*Ec[j]*(B-24)     #'第一和二个2为分层厚度，第一个1为厚度的一半
                for j in range(1,i-int((H1-74)/layer)+1):                
                    f20=f20+layer*(layer*j-layer/2)*Eg*25
                f2=f2+f20
            for js in range(1,cdd-i+1):
                f4=f4+layer*(layer*js-layer/2)*Ec[js]*(B)+layer*(layer*js-layer/2)*Eg*24     #'第一和二个2为分层厚度，第一个1为厚度的一半
            s1=f1+f4
            s2=f2+f3
        else:
            break
i=i-1    
M1=0
M10=0                                         #'M1为混凝土受压弯矩
M2=(H0-layer*i)**2*Eg*B*6                              #'M2为frp底板弯矩，2为分层厚度

for k in range(1,i+1):
        M1=M1+layer*B*(layer*i-layer*(k-1)-layer/2)**2*Ec[k]          #'M1为混凝土弯矩，2为分层厚度，倒数第一个1为分层厚度一半
for k in range(1,i-int((H1-74)/layer)+1):
        M10=M10+layer*24*(layer*k-layer/2)**2*Eg
M1=M1+M10
M3=(i*layer-30)**2*Es*As
M4=0
for js in range(1,cdd-i+1):
        M4=M4+layer*(layer*js-layer/2)**2*Ec[js]*(B-24)+layer*(layer*js-layer/2)**2*Eg*24

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
En[0]=27000
for kr in range(1,2):
    e0=K0*(layer*i-layer*kr+layer/2)*10**6
    e1=K0*(layer*(cdd-i)-layer*kr+layer)*10**6
    e3=K0*(layer*(cdd-i)+3)*10**6
    deta0[kr]=Ec[kr]*K0*(layer*i-layer*kr+layer/2)#'第k层最小应力，2为分层厚度，1为分层厚度一半
    deta1[kr]=Ec[kr]*K1*(layer*i-layer*kr+layer/2)              #'第k层最大应力，2为分层厚度，1为分层厚度一半
    detaave[kr]=(deta0[kr]+deta1[kr])/2/fc        # '第k层平均应力
    detarange[kr]=(deta1[kr]-deta0[kr])/fc        # '第k层应力幅值                         
    strain[kr]=(129*detaave[kr]*t[tt]**(1/3)+17.8*detaave[kr]*detarange[kr]*N[tt]**(1/3))/1000000#'应变
    En[kr]=deta1[kr]/(deta1[kr]/Ec[0]+strain[kr])   #'折损弹性模量
#    En.append()
#    return En,i,strain
ne=Ec[1]/Eg
IcrN=B*(H1*1)**3/12+B*H1*(layer*i-H1/2)**2+B/ne*6**3/12+B/ne*6*(H0-layer*i)**2
naodu=M00*(3*l*l-4*a*a)/24/Ec[1]/IcrN