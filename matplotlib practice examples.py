import matplotlib.pyplot as plt
x=[1,2]
y=[1,2]

plt.plot(x,y)
############################################
import numpy as np
x=np.array([1,2])
y=np.array([1,2])
plt.plot(x,y)
#########################################
import torch
x=torch.tensor([1,2])
y=torch.tensor([1,2])
plt.plot(x,y)
###########################################
x=torch.tensor([1.,2.], requires_grad=True)
print(x)
x=x.detach()
print(x)
y=torch.tensor([1.,2.])
plt.plot(x,y)
#########################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'o')
###########################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'x')
############################################3
plt.plot([1,2,3,4,5],[1,2,3,4,5],'s') # square의 s
##################################################3
plt.plot([1,2,3,4,5],[1,2,3,4,5],'r') # red 라서 r
###################################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'ro')
################################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'ro-')
#############################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'ro--')
###########################################
plt.plot([1,2,3,4,5],[1,2,3,4,5],'r-.')
################################################
plt.subplot(2,3,1) # 행의 수, 열의 수, 인덱스
plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.subplot(2,3,2)
plt.plot([1,2,3,4,5],[1,2,3,4,5],'rh')
plt.subplot(2,3,3)
plt.plot([1,2,3,4,5],[1,2,3,4,5],'gp')
plt.subplot(2,3,4)
plt.plot([1,2,3,4,5],[1,2,3,4,5],'b+')
plt.subplot(2,3,5)
plt.plot([1,2,3,4,5],[1,2,3,4,5],'^')
plt.subplot(2,3,6)
plt.plot([1,2,3,4,5],[1,2,3,4,5],'<')
###################################################3
color = ["b", "k", "y", "c", "m", "g"]
marker = [".","*","v",">","8","P"]
line_style = ["-","--","-.",":","","-"]
print(color[0]+marker[0]+line_style[0])
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.plot([1,2,3,4,5],[1,2,3,4,5],color[i]+marker[i]+line_style[i])
  ######################################################################
fig, ax = plt.subplots(nrows=2, ncols=3) # object-oriented
for i in range(2):
    for j in range(3):
        ax[i,j].plot([1,2,3,4,5],[1,2,3,4,5],color[3*i+j]+marker[3*i+j]+line_style[3*i+j])
#############################################################################################
# red, 별모양, dash선으로 sin 그리기
# green, 동그라미, 실선으로 cos 그리기
theta=np.linspace(0,2*np.pi,20)
plt.plot(theta,np.sin(theta),"r*--",markersize=10, label="sin")
# plt.figure() # 새창 열기. 이거 없으면 겹쳐 그리기
plt.plot(theta,np.cos(theta),"go-",markersize=10, label="cos")
plt.xlabel("theta")
plt.ylabel("value")
plt.title("sin and cos",color="b")
plt.legend()
plt.grid()
# plt.xlim([0, np.pi])
# plt.ylim([-2, 2])
plt.axis([0, np.pi, -2,2])
########################################################
plt.plot(theta,np.sin(theta),"r*--",markersize=10, label="sin")
plt.plot(theta,np.cos(theta),"go-",markersize=10, label="cos")
plt.xlabel("theta",fontsize=20)
plt.ylabel("value",fontsize=20)
plt.title("sin and cos",color="b",fontsize=20)
plt.legend(fontsize=20)
plt.grid()
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#############################################################
plt.bar(range(5),[3,2,3,4,5], width=0.8)
plt.xticks(range(5),["a","b","c","d","e"])
plt.xlabel("layer")
plt.ylabel("value")
############################################################
x=range(5)
y1=[i for i in range(1,6)]
y2=[i+100 for i in range(1,6)]

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)

plt.figure()
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
p1=ax1.plot(x,y1,'b')
p2=ax2.plot(x,y2,'r')
ax1.set_ylim([-10, 10])
ax1.set_xlabel("x")
ax1.set_ylabel("y1")
ax2.set_ylabel("y2")
ax1.set_title("y1 and y2")
ax1.grid()
plt.legend(p1+p2,["y1","y2"], loc="right")
##########################################################
a=np.linspace(-1,1,100)
b=np.linspace(-1,1,100)
A, B=np.meshgrid(a,b)
L = A**2 + B**2
plt.contour(a,b,L,20) # 20 -> 등고선 개수
plt.xlabel('a'); plt.ylabel('b'); plt.grid()

plt.figure()
plt.contourf(a,b,L,5)
########################################################
fig, ax = plt.subplots(figsize=[10, 9])
CS = ax.contour(a,b,L,20) # 20 -> 등고선 개수
ax.clabel(CS, fontsize=10)
plt.xlabel('a'); plt.ylabel('b'); plt.grid()
######################################################
plt.figure(figsize=[10, 9]) # [가로, 세로]
ax = plt.axes(projection="3d")
ax.plot_surface(A,B,L)

# 이전 코드 (error)
# figure = plt.figure(figsize=[10, 9])
# ax = figure.gca(projection="3d")
# ax.plot_surface(A,B,L)

plt.figure(figsize=[10, 9])
ax = plt.axes(projection='3d')
ax.plot_wireframe(A,B,L)
########################################################3
plt.figure(figsize=[10,9]) # [가로, 세로]
ax = plt.axes(projection='3d')
ax.view_init(elev=10,azim=-45)
ax.plot_surface(A,B,L, alpha=0.7)

plt.figure(figsize=[10, 9])
ax = plt.axes(projection='3d')
ax.view_init(elev=10,azim=-45)
ax.plot_wireframe(A,B,L)
#######################################################
from matplotlib.colors import LightSource
plt.figure(figsize=[10, 9])
ax = plt.axes(projection="3d")
ls = LightSource(altdeg=10, azdeg=-45)
rgb = ls.shade(L, plt.cm.RdYlBu)
ax.plot_surface(A,B,L, facecolors=rgb)
# ax.plot_surface(A,B,L, cmap='viridis')
# 'viridis', 'plasma', 'inferno', 'magma', 'cividis'

# ax.plot_surface(A,B,L, facecolors=rgb,
#                        rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
# ax.plot_surface(A,B,L, cmap=plt.cm.viridis) # 내 필기용
######################################################3
plt.figure(figsize=[10, 9])
ax = plt.axes(projection="3d")
ls = LightSource(altdeg=0, azdeg=20)
rgb = ls.shade(L, cmap=plt.cm.gist_earth, vert_exag=0.1, blend_mode='soft')
ax.plot_surface(A,B,L, rstride=1, cstride=1, facecolors=rgb,
            linewidth=0, antialiased=False, shade=False)
###############################################################
a=np.linspace(-1,1,10)
b=np.linspace(-1,1,10)
A, B = np.meshgrid(a,b)
L = A**2 + B**2

plt.figure(figsize=[10,9])
ax = plt.axes(projection="3d")
ax.plot(A.reshape(-1,1).squeeze(),B.reshape(-1,1).squeeze(),L.reshape(-1,1).squeeze(),'ro')


plt.figure(figsize=[10,9])
ax = plt.axes(projection="3d")
# ax.scatter(A,B,L)
# ax.scatter(A,B,L,s=100, c="g", marker="*", edgecolors="r")
ax.scatter(A,B,L,s=100, c="g", marker="*", alpha=0.3)
######################################################
plt.figure(figsize=[10, 9])
ax = plt.axes(projection='3d')
ax.plot_surface(A,B,L, alpha=0.3, cmap="viridis")
ax.scatter(A,B,L,s=100, c="r", marker="*")
ax.set_zlim([0, 3])
###################################################3
import plotly.graph_objects as go

a=np.linspace(-2,2,100)
b=np.linspace(-2,2,100)
A, B = np.meshgrid(a,b)
L = np.cos(A**2.4)+np.sin(B**2.4)

fig = go.Figure(data=[go.Surface(x=a, y=b, z=L, colorscale="viridis", opacity=0.5)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
fig.update_layout(title='cos(A^2.4)+sin(B^2.4)', width=700, height=600)
#############################################################################
fig = go.Figure(data=[go.Surface(x=a, y=b, z=L, opacity=0.5)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
fig.update_layout(title='cos(A^2.4)+sin(B^2.4)', width=700, height=600,
                  scene = dict( zaxis=dict(nticks=40, range=[-3,3]) ))
