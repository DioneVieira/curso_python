from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import numpy as np
import pandas as pd

# cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # para letra
co5 = "#e06636"  # - profit
co6 = "#6dd695"  # + profit
fundo = "#3F729B"

# janela

janela = Tk()
janela.state('zoomed')
janela.title('VENDAS')

# dividindo a janela principal em duas partes
frame_top = Frame(janela, width=1370, height=45, pady=0, padx=0, bg=co1,  relief="flat",)
frame_top.grid(row=0, column=0)

frame_quadro = Frame(janela, width=1370, height=700, bg=co1, pady=15, padx=7, relief="flat",)
frame_quadro.grid(row=1, column=0, pady=10, sticky=NW)

# configurando frame top
app_nome = Label(frame_top, text="Dashboard de Vendas", width=20, height=2, pady=1, padx=0, relief="flat",
                 anchor=N, font='Ivy 14 bold', bg=co1, fg=co4)
app_nome.place(x=0, y=5)

# Configurando frame quadro

# Receitas Vendidas
frame_Total = Frame(frame_quadro, width=200, height=90, bg=co1, relief="flat",)
frame_Total.place(x=0, y=0)

app_traco = Label(frame_Total, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 1 bold',
                  bg=co2, fg=co4)
app_traco.place(x=0, y=0)

app_nome_rev = Label(frame_Total, text="Receitas de vendas", height=1, pady=0,padx=0, relief="flat", anchor=CENTER,
                     font='Ivy 10 bold', bg=co1, fg=co4)
app_nome_rev.place(x=20, y=5)

app_nome_va = Label(frame_Total, text="$ 8,934,987", height=1, pady=0, padx=0,relief="flat", anchor=CENTER,
                    font='Ivy 18 bold', bg=co1, fg=co3)
app_nome_va.place(x=40, y=35)

app_nome_p = Label(frame_Total, text="+ 18% vs mes Junho/20", height=1, pady=0,padx=0, relief="flat", anchor=CENTER,
                   font='Ivy 8 bold', bg=co1, fg=co6)
app_nome_p.place(x=35, y=70)

# Quantidade total vendida
frame_Total_Vendido = Frame(frame_quadro, width=200, height=90,bg=co1, relief="flat",)
frame_Total_Vendido.place(x=210, y=0)

app_pr = Label(frame_Total_Vendido, text="", width=1, height=10,pady=0, padx=0, relief="flat", anchor=NW,
               font='Ivy 1 bold', bg=co2, fg=co4)
app_pr.place(x=0, y=0)

app_nome_rev = Label(frame_Total_Vendido, text="Quantidade total vendida", height=1,pady=0, padx=0, relief="flat",
                     anchor=CENTER, font='Ivy 10 bold', bg=co1, fg=co4)
app_nome_rev.place(x=20, y=5)

app_nome_va = Label(frame_Total_Vendido, text="# 9,566", height=1, pady=0,padx=0, relief="flat", anchor=CENTER,
                    font='Ivy 18 bold', bg=co1, fg=co3)
app_nome_va.place(x=60, y=35)

app_nome_p = Label(frame_Total_Vendido)

# Faturamento Mensal

frame_mes = Frame(frame_quadro, width=500, height=200, bg=co1, relief="flat",)
frame_mes.place(x=420, y=0)

# dados para valores vendidos
vendas_mensal = [2701, 4275, 6385, 8693, 2550, 3622, 1793, 5862, 7984, 9831, 3739, 4584]

# Nomes dos meses para plotagem
meses = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(11.4, 2.5), dpi=66)
ax = figura.add_subplot(111)


ax.bar(meses, vendas_mensal,  color="#82b1ff")
# create a list to collect the plt.patches data
totals = []

c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()-.03, i.get_height()+.5, str(vendas_mensal[c])+'$', fontsize=12, fontstyle='italic',
            verticalalignment='baseline', color='dimgrey')
    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

canva = FigureCanvasTkAgg(figura, frame_mes)
canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

# Faturamento produtos

frame_produto = Frame(frame_quadro, width=410, height=330, bg=co1, relief="flat")
frame_produto.place(x=0, y=100)

app_traco = Label(frame_produto, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 1 bold',
                  bg=co2, fg=co4)
app_traco.place(x=0, y=0)

app_nome_rev = Label(frame_produto, text="Faturamento por produtos Top 10", height=1, pady=0,padx=0, relief="flat", anchor=CENTER,
                     font='Ivy 10 bold', bg=co1, fg=co4)
app_nome_rev.place(x=20, y=5)

# produtos para plotagem
prod = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5', 'Produto 6', 'Produto 7', 'Produto 8',
         'Produto 9', 'Produto 10','Produto 11','Produto 12']

# dados para valores vendidos
vendas_mensal = [2701, 4275, 6385, 8693, 2550, 3622, 1793, 5862, 7984, 9831, 3739, 4584]

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(8, 8), dpi=51.5)
ax = figura.add_subplot(111)

ax.bar(prod, vendas_mensal,  color="#82b1ff")
ax.set_alpha(0.8)
# create a list to collect the plt.patches data

c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_width()+.3, i.get_y()+.50, str(vendas_mensal[c])+'Kz', fontsize=12, fontstyle='italic',  verticalalignment='center', color='dimgrey')
    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.xaxis.grid(False)

canva_produto = FigureCanvasTkAgg(figura, frame_produto)
canva_produto.get_tk_widget().place(x=0, y=16)



# Faturamento por Categoria

frame_categoria = Frame(frame_quadro, width=200,height=200, bg=co1, relief="flat",)
frame_categoria.place(x=420, y=230)


# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(5.15, 4), dpi=80)
ax = figura.add_subplot(111)


# Vendas
categoria_total = [5701, 4275, 8385, 5934, 6934]

# Categorias
labels = ["Categoria - 1", "Categoria - 2 ", "Categoria - 3", "Categoria - 4", "Categoria - 5"]

# only "explode
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

# colors = ['#665191', '#a05195','#d45087',  "#f95d6a", "#ff7c43", "#ffa600"]
colors = ['#ff9999',  '#c5cae9', '#bbdefb', '#99ff99', '#ffcc99']


ax.pie(categoria_total, explode=explode, wedgeprops=dict(width=0.64), labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

app_cat = Label(frame_categoria, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
app_cat.place(x=0, y=0)
app_categoria = Label(frame_categoria, text="Desempenho de categorias Top - 5", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_categoria.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
canva_categoria = FigureCanvasTkAgg(figura, frame_categoria)
canva_categoria.get_tk_widget().grid(row=1, column=0, sticky=NSEW)


# ------------------------------------------------------------------------------------------------------

# Faturamento por Vendedores

frame_vendedor = Frame(frame_quadro, width=200, height=200, bg=co1, relief="flat",)
frame_vendedor.place(x=840, y=230)

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(7.3, 4.6), dpi=70)
ax = figura.add_subplot(111)

# vendas
vendas_mensal = [2701, 4275, 6385, 8693, 3622]

# vendedores
vendedor = ["Vendedor - 1", "Vendedor - 2 ", "Vendedor - 3", "Vendedor - 4", "Vendedor - 5"]

ax.bar(vendedor, vendas_mensal,  color=colors)

# create a list to collect the plt.patches data
totals = []


c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()-.03, i.get_height()+.5, str(vendas_mensal[c])+'$', fontsize=12, fontstyle='italic', color='dimgrey', weight='bold', verticalalignment='baseline',)
    c += 1

ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)


app_vend = Label(frame_vendedor, text="", width=1, height=10, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=co2, fg=co4)
app_vend.place(x=0, y=0)
app_categoria_vendedor = Label(frame_vendedor, text="Faturamento por Vendedor Top - 5", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
app_categoria_vendedor.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
canva_vendedor = FigureCanvasTkAgg(figura, frame_vendedor)
canva_vendedor.get_tk_widget().grid(row=1, column=0, sticky=NSEW)



janela.mainloop()