import numpy as np
import matplotlib.pyplot as plt

x = [150, 160, 170, 175, 185] #height
y= [55, 70, 64, 80, 75] #weight
plt.plot(x,y,'o')
############################################3
a = 0.45
b = -35
x_plot = np.linspace(145,180,100)
y_plot = a*x_plot + b

plt.plot(height,y,'o')
plt.plot(x_plot, y_plot, 'r')
####################################################
a = 0.5 +np.linspace(-0.2, 0.2 ,100)
b = -30 + np.linspace(-20,20,100)
A, B=np.meshgrid(a,b)

L=np.zeros_like(A)

L= np.zeros_like(A)
#zip(x,y)
#xi,yi
for xi,yi in zip(x,y):
  L += (yi-(A*xi+B))**2
plt.figure()
plt.contour(a,b,L,30); plt.xlabel("a"); plt.ylabel("b"); plt.grid()

plt.figure(figsize=[10,9])
ax= plt.axes(projection="3d")
ax.plot_surface(A,B,L); plt.xlabel("a"); plt.ylabel("b")
ax.set_zlim([0,5000])

a_opt=A[L==np.min(L)]
b_opt=B[L==np.min(L)]

print(f"optimal a= {a_opt}")
print(f"optimal b= {b_opt}")
plt.figure()
y_plot = a_opt*x_plot + b_opt
plt.plot(x,y,'o')
plt.plot(x_plot,y_plot,'r')
####################################################################
import plotly.graph_objects as go
fig = go.Figure(data=[go.Surface(x=a, y=b, z=L,colorscale="viridis",opacity=0.5)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen",project_z=True))
fig.update_layout(title='Loss',width=700, height=600,
                  scene= dict(zaxis=dict(nticks=20, range=[0,5000])))
######################################################################
import torch
a=torch.tensor(0.45, requires_grad=True)
b=torch.tensor(-35.0, requires_grad=True)

L=0
for xi,yi in zip(x,y):
  L += (yi-(a*xi+b))**2

L.backward() #미분값 구함
print(a.grad)
print(b.grad)

LR=1e-6
a=a.detach() - LR*a.grad
b=b.detach() - LR*b.grad
print(a,b)

plt.figure()
y_plot = a*x_plot + b
plt.plot(x,y,'o')
plt.plot(x_plot,y_plot,'r') #실행 할수록 조금씩 업데이트됨 (Loss 감소)
