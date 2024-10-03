from manim import *
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 
import os

# Lee el archivo de texto y crea un DataFrame
nombres_columnas = ['Estrella', 'TYC', '2MASS']
data = pd.read_csv('Nombres_de_Estrellas.txt', delimiter=' ', names=nombres_columnas, header=None)  # Si el archivo está tabulado, usa '\t' como separador
columns = ["Star","Date","RV","err_RV","S/N"]
Estrella = {}
mean = []
range = []
std = []
sn_all = []
for i in data["Estrella"]:
    Estrella[i] = pd.read_csv(i+'.dat', delimiter='\t', names=columns, header=None)
    #print(Estrella[i])
    mean.append(np.mean(Estrella[i]["RV"]))
    range.append(np.max(Estrella[i]["RV"])-np.min(Estrella[i]["RV"]))
    std.append(np.std(Estrella[i]["RV"]))
    sn_all.append(list(Estrella[i]["S/N"]))

standard_1 = pd.DataFrame()
standard_1["Star"] = ["HD10700","HD10700","HD10700","HD10700","HD10700","HD10700"]
standard_1["Date"] = [2459909.65073789, 2459909.65501101,2459909.65659494,2460140.86979848,2460140.87719779,2460140.88436262]
standard_1["RV"] = [-16.6332,-16.6272,-16.6358,-16.6113,-16.5844,-16.5975]
standard_1["err_RV"] = [0.0055,0.0054,0.0055,0.0051,0.0052,0.0052]

standard_2 = pd.DataFrame()
standard_2["Star"] = ["HD48381","HD48381"]
standard_2["Date"] = [ 2459911.82061493,2459932.73709687]
standard_2["RV"] = [40.5002, 40.5425]
standard_2["err_RV"] = [0.0058,0.0058]

standard_3 = pd.DataFrame()
standard_3["Star"] = ["HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673",
                      "HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673","HD72673",
                      "HD72673","HD72673","HD72673","HD72673","HD72673"]

standard_3["Date"] = [2459689.56129858,2459689.57085397,2459691.54070173,2459692.51501392,2459693.56949426,
                      2459700.54481159,2459703.53651666,2459703.54594784,2459705.57899704,2459705.58848409,
                      2459710.54248262,2459710.55199144,2459712.55740839,2459713.53461976,2460020.61160702,
                      2460020.61525735,2460020.61891691,2460020.62260781,2460020.62630010,2460027.56858592,
                      2460027.57286141,2460027.57651549,2460035.51305523,2460035.51741199,2460035.52194853]

standard_3["RV"] = [14.8275,14.8201,14.8206,14.8347,14.8304,14.8235,14.8149,14.8084,14.7835,14.7304,
                    14.7931,14.8058,14.8059,14.8040,14.8114,14.8075,14.8089,14.8147,14.7963,14.7705,
                    14.7488,14.7497,14.8127,14.8051,14.8082]

standard_3["err_RV"] = [0.0069,0.0074,0.0061,0.0060,0.0060,0.0064,0.0063,0.0063,0.0074,0.0090,
                        0.0063,0.0067,0.0067,0.0072,0.0080,0.0079,0.0080,0.0082,0.0080,0.0090,
                        0.0066,0.0064,0.0072,0.0073,0.0069]

standard_3["SNR"] = [163,138,237,252,247,204,211,213,133,92,
                     211,179,175,145,106,107,106,99,104,60,
                     106,114,135,131,148]


standard_4 = pd.DataFrame()
standard_4["Star"] = ["HD157347","HD157347","HD157347","HD157347","HD157347","HD157347","HD157347","HD157347","HD157347","HD157347",
                     "HD157347","HD157347","HD157347","HD157347"]

standard_4["Date"] = [2459682.80175885,2459682.81123673,2460056.77139151,2460056.77576483,2460056.78013197,
                      2460057.73995220,2460057.75056925,2460062.84027507,2460062.84394942,2460062.84762835,
                      2460063.83831262,2460063.84268851,2460098.68104677,2460098.72986503]

standard_4["RV"] = [-35.8622,-35.8708,-35.8824,-35.8826,-35.8796,-35.8712,-35.8755,-35.8939,-35.8903,-35.8891,
                    -35.8909,-35.8935,-35.9016,-35.9101]

standard_4["err_RV"] = [0.0053,0.0053,0.0060,0.0059,0.0058,0.0053,0.0056,0.0063,0.0063,0.0064,
                        0.0061,0.0061,0.0058,0.0063]

standard_4["SNR"] = [196,201,124,133,138,194,162,112,112,109,
                     119,121,135,107]

from manim import *
import numpy as np

# Datos de ejemplo

## ANIMACIÓN
class RVGraphScene(Scene):
    def construct(self):
        # Título del gráfico
        tilte = Tex(f"Datos de la Estándar {standard_3['Star'][0]} ", font_size=36)
        tilte.to_edge(UP)
        self.play(Write(tilte))
        self.wait(1)
        # Crear los ejes
        axes = Axes(
            x_range=[2459680, 2460036, 20],
            y_range=[14.72,14.88, 0.05],
             axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [-300+2.46e6, -200+2.46e6, -100+2.46e6,0+2.46e6],
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": [14.725, 14.750, 14.775, 14.800, 14.825, 14.850, 14.875],
                "label_direction": LEFT,
            },
            tips=False,
        ).scale(0.7)

        # Etiquetas de los ejes
        # Crear las líneas de los ejes
        x_axis_line = axes.get_x_axis()
        y_axis_line = axes.get_y_axis()
        
       # Crear etiquetas usando Tex
        x_label = Tex(r"JD", font_size=24)
        y_label = Tex(r"VR [km/s]", font_size=24)

        # Asumiendo que ya tienes tu sistema de coordenadas 'axes' definido
        x_min, x_max = axes.x_range[:2]
        y_min, y_max = axes.y_range[:2]
        
        # Posicionar la etiqueta del eje Y (velocidad radial)
        y_label.move_to(axes.coords_to_point(x_min - 50 , (y_min + y_max) / 2))
        
        # Posicionar la etiqueta del eje X (Julian Day)
        x_label.move_to(axes.coords_to_point((x_min + x_max) / 2, y_min-0.02))
        
        # Añadir las etiquetas al gráfico
        # Girar la etiqueta del eje Y
        y_label.rotate(PI / 2)
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label))
        
        # Crear puntos con errores
        points = VGroup()
        for i, (jd, v, err) in enumerate(zip(standard_3["Date"], standard_3["RV"], standard_3["err_RV"])):
            error_line = Line(
                axes.coords_to_point(jd, v - err), axes.coords_to_point(jd, v + err),
                color="#4A235A", stroke_width=2)
            point = Dot(axes.coords_to_point(jd, v), color="#7D3C98")
            
            points.add(point, error_line)

        # Calcular y dibujar la línea de la media
        mean_velocity = np.mean(standard_3["RV"])
        mean_line = axes.get_horizontal_line(axes.c2p(2460036, mean_velocity), color=RED)

        # Animar la creación de los ejes, puntos y la línea de la media
        self.play(Create(points))
        self.play(Create(mean_line))


        # Añadir un texto para la línea de la media
        # Colores para cada molécula
        colors = ["#7D3C98",RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]

        #----------------
        ## ANIMACIÓN DE PRESENTAR LAS MOLÉCULAS
        # Añadir los nombres de las moléculas
        molecule_labels = [f"{standard_3['Star'][0]}",f"Mean Velocity = {mean_velocity}"]
        for i, mol in enumerate(molecule_labels):
            # Crear la etiqueta grande en el centro
            large_label = Tex(mol, font_size=30, color=colors[i])
            large_label.move_to(ORIGIN)
            
            # Crear la etiqueta pequeña en la esquina superior derecha
            small_label = Tex(mol, font_size=24, color=colors[i])
            small_label.to_edge(UP+RIGHT)
            small_label.shift(DOWN * i * 0.5)
            
            # Animar la transición de grande en el centro a pequeña en la esquina
            self.play(Write(large_label))
            self.wait(0.1) # Esperar un segundo
            self.play(Transform(large_label, small_label))
            self.remove(large_label)
            self.add(small_label)
    

        # Mantener la escena unos segundos
        self.wait(2)

        

if __name__ == "__main__":
    from manim import config, tempconfig
    with tempconfig({"quality": "low_quality", "preview": True}):
        scene = RVGraphScene()
        scene.render()