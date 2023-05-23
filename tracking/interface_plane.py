# import numpy as np
# import tkinter as tk
# from tkinter import ttk
# from tracker import Tracker
# from tkinter import Label


# def create_image(w, h):
#     img = np.ones((w, h, 3), np.uint8) * 255
#     return img

# def rgb_to_hex(rgb):
#     return '#%02x%02x%02x' % rgb

# # def draw_aircraft_info(x, y):
# #     # cv.create_text(10, 10, text=f"Posición: x = {x} y =  {y}", fill="green", font=("Arial", 12), anchor=tk.NW)
# #     # cv.create_text(10, 10, text=f"Avión 0 - ({x}, {y})", fill="#000080", font=("Helvetica", 14, "bold"), anchor=tk.NW)
# #     cv.create_text(120, 500, text=f"Avión 0 - ({x}, {y})", fill="#000080", font=("Helvetica", 14,"bold"), anchor=tk.NW)




# def update_frame():
#     global frame_idx, table

#     if frame_idx >= data.shape[1]:
#         return

#     centers = data[:, frame_idx, :]
#     frame = create_image(800, 1800)

#     cv.delete("all")  # Limpiar el lienzo
#     cv.create_rectangle(10, 10, 1790, 790)

#     if len(centers) > 0:
#         tracker.update(centers)
#         for j, track in enumerate(tracker.tracks):

#             if len(track.trace) > 1:
#                 for k in range(len(track.trace)-1):
#                     x1 = int(track.trace[k][0, 0])
#                     y1 = int(track.trace[k][0, 1])
#                     x2 = int(track.trace[k+1][0, 0])
#                     y2 = int(track.trace[k+1][0, 1])
#                     cv.create_line(x1, y1, x2, y2, fill=rgb_to_hex(track_colors[j]), width=2)

#                 last_trace = track.trace[-1]
#                 x = int(last_trace[0, 0])
#                 y = int(last_trace[0, 1])
#                 tl = (x - 10, y - 10)
#                 br = (x + 10, y + 10)
#                 cv.create_rectangle(tl[0], tl[1], br[0], br[1], outline=rgb_to_hex(track_colors[j]), width=1)
#                 cv.create_text(x - 10, y - 20, text=str(track.trackId), fill=rgb_to_hex(track_colors[j]), font=("Arial", 12), anchor=tk.NW)

#                 if j == 0:
#                     # draw_aircraft_info(x, y)
#                     aircraft_info_label.config(text=f"Posición: x = {x} y =  {y}")

#         # for j in range(len(tracker.tracks)):
#         #     x = int(tracker.tracks[j].trace[-1][0, 0])
#         #     y = int(tracker.tracks[j].trace[-1][0, 1])
#         #     text = f"({x}, {y})"
#         #     cv.create_text(10, 30 + j * 20, text=text, fill=rgb_to_hex(track_colors[j]), font=("Arial", 8), anchor=tk.NW)

#     # Actualizar la tabla
#     table.delete(*table.get_children())  # Borra todos los elementos existentes en la tabla
#     for i, track in enumerate(tracker.tracks):
#         if i!=0:
#             x = int(track.trace[-1][0, 0])
#             y = int(track.trace[-1][0, 1])
#             table.insert("", tk.END, values=(i, f"{x}, {y}"))  # Inserta la nueva información

#     frame_idx += 1
#     if frame_idx < data.shape[1]:
#         root.after(100, update_frame)

# def main():
#     global root, cv, frame_idx, data, tracker, track_colors, table,aircraft_info_label

#     data = np.array(np.load('centers.npy'))[0:10, 0:150, 0:150]

#     tracker = Tracker(150, 30, 5)
#     track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
#                     (127, 127, 255),(255, 0, 255), (255, 127, 255),
#                     (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]

#     frame_idx = 0

#     root = tk.Tk()
#     root.configure(bg='white')
#     root.title("Tracker Output")

#     aircraft_info_label = Label(root, text="", font=("Helvetica", 14,"bold"), fg="blue")
#     # aircraft_info_label.pack(side=tk.BOTTOM, anchor = tk.SW, padx=20, pady=20)
#     aircraft_info_label.pack(side=tk.BOTTOM, padx=20, pady=20)


#     cv = tk.Canvas(root, width=1800, height=800,bg='white')
#     cv.pack()

#     # Crear la tabla con estilo mejorado
#     style = ttk.Style()
#     style.theme_use("clam")  # Cambiar el tema de la tabla

#     table_frame = ttk.Frame(root)
#     table_frame.pack(pady=20)

#     headers = ["Identificación", "Ubicación"]

#     table = ttk.Treeview(table_frame, columns=headers, show="headings", style="Custom.Treeview")
#     table.pack()

#     style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))  # Estilo de encabezados
#     style.configure("Custom.Treeview", font=("Arial", 10))  # Estilo de contenido

#     for header in headers:
#         table.heading(header, text=header)

#     update_frame()

#     root.mainloop()

# if __name__ == '__main__':
#     main()

import numpy as np
import tkinter as tk
from tkinter import ttk
from tracker import Tracker
from tkinter import Label


def create_image(w, h):
    img = np.ones((w, h, 3), np.uint8) * 255
    return img

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# def draw_aircraft_info(x, y):
#     # cv.create_text(10, 10, text=f"Posición: x = {x} y =  {y}", fill="green", font=("Arial", 12), anchor=tk.NW)
#     # cv.create_text(10, 10, text=f"Avión 0 - ({x}, {y})", fill="#000080", font=("Helvetica", 14, "bold"), anchor=tk.NW)
#     cv.create_text(120, 500, text=f"Avión 0 - ({x}, {y})", fill="#000080", font=("Helvetica", 14,"bold"), anchor=tk.NW)




def update_frame():
    global frame_idx, table
    

    if frame_idx >= data.shape[1]:
        return

    centers = data[:, frame_idx, :]
    frame = create_image(800, 1800)

    cv.delete("all")  # Limpiar el lienzo
    cv.create_rectangle(10, 10, 1790, 790)

    if len(centers) > 0:
        tracker.update(centers)
        for j, track in enumerate(tracker.tracks):

            if len(track.trace) > 1:
                for k in range(len(track.trace)-1):
                    x1 = int(track.trace[k][0, 0])
                    y1 = int(track.trace[k][0, 1])
                    x2 = int(track.trace[k+1][0, 0])
                    y2 = int(track.trace[k+1][0, 1])
                    cv.create_line(x1, y1, x2, y2, fill=rgb_to_hex(track_colors[j]), width=2)

                last_trace = track.trace[-1]
                x = int(last_trace[0, 0])
                y = int(last_trace[0, 1])
                tl = (x - 10, y - 10)
                br = (x + 10, y + 10)
                cv.create_rectangle(tl[0], tl[1], br[0], br[1], outline=rgb_to_hex(track_colors[j]), width=1)
                cv.create_text(x - 10, y - 20, text=str(track.trackId), fill=rgb_to_hex(track_colors[j]), font=("Arial", 12), anchor=tk.NW)

                if j == 0:
                    aircraft_info_label.config(text=f"Posición: x = {x} y =  {y}")
                    
        # Crear una lista de distancias para cada track respecto al track 0
        distances = []
        if len(tracker.tracks) > 0:
            x0, y0 = tracker.tracks[0].trace[-1][0, 0], tracker.tracks[0].trace[-1][0, 1]
            for track in tracker.tracks[1:]:
                x_track = int(track.trace[-1][0, 0])
                y_track = int(track.trace[-1][0, 1])
                distance = ((x_track - x0)**2 + (y_track - y0)**2)**0.5
                distances.append(distance)


    # Actualizar la tabla
    table.delete(*table.get_children())  # Borra todos los elementos existentes en la tabla
    for i, track in enumerate(tracker.tracks):
        if i != 0:
            x = int(track.trace[-1][0, 0])
            y = int(track.trace[-1][0, 1])
            table.insert("", tk.END, values=(i, f"{x}, {y}", distances[i-1]))  # Inserta la nueva información




    frame_idx += 1
    if frame_idx < data.shape[1]:
        root.after(100, update_frame)

def main():
    global root, cv, frame_idx, data, tracker, track_colors, table,aircraft_info_label

    data = np.array(np.load('centers.npy'))[0:10, 0:150, 0:150]

    tracker = Tracker(150, 30, 5)
    track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                    (127, 127, 255),(255, 0, 255), (255, 127, 255),
                    (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]

    frame_idx = 0

    root = tk.Tk()
    root.configure(bg='white')
    root.title("Tracker Output")

    aircraft_info_label = Label(root, text="", font=("Helvetica", 14,"bold"), fg="blue")
    # aircraft_info_label.pack(side=tk.BOTTOM, anchor = tk.SW, padx=20, pady=20)
    aircraft_info_label.pack(side=tk.BOTTOM, padx=20, pady=20)


    cv = tk.Canvas(root, width=1800, height=800,bg='white')
    cv.pack()

    # Crear la tabla con estilo mejorado
    style = ttk.Style()
    style.theme_use("clam")  # Cambiar el tema de la tabla

    table_frame = ttk.Frame(root)
    table_frame.pack(pady=20)

    headers = ["Identificación", "Ubicación","Distancia", "Tipo Aeronave"]

    table = ttk.Treeview(table_frame, columns=headers, show="headings", style="Custom.Treeview")
    table.pack()

    style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))  # Estilo de encabezados
    style.configure("Custom.Treeview", font=("Arial", 10))  # Estilo de contenido

    for header in headers:
        table.heading(header, text=header)

    update_frame()

    root.mainloop()

if __name__ == '__main__':
    main()


