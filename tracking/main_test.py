import numpy as np
import tkinter as tk
from tkinter import ttk
from tracker import Tracker
from tkinter import Label
import re

def create_image(w, h):
    img = np.ones((w, h, 3), np.uint8) * 255
    return img

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def update_tracks(centers):
    if len(centers) > 0:
        tracker.update(centers)
    return tracker

def draw_tracks(tracker):
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

def get_track_distances(tracker):
    distances = []
    if len(tracker.tracks) > 0:
        x0, y0 = tracker.tracks[0].trace[-1][0, 0], tracker.tracks[0].trace[-1][0, 1]
        for track in tracker.tracks[1:]:
            x_track = int(track.trace[-1][0, 0])
            y_track = int(track.trace[-1][0, 1])
            distance = ((x_track - x0)**2 + (y_track - y0)**2)**0.5
            distances.append(distance)
    return distances

def update_table(tracker, distances):
    table.delete(*table.get_children())  
    for i, track in enumerate(tracker.tracks):
        if i != 0:
            x = int(track.trace[-1][0, 0])
            y = int(track.trace[-1][0, 1])
            table.insert("", tk.END, values=(i, f"{x}, {y}", distances[i-1]))

def update_frame():
    global frame_idx, table
    if frame_idx >= data.shape[1]:
        return
    centers = data[:, frame_idx, :]
    # print ("Detections",centers)
    cv.delete("all")  
    cv.create_rectangle(10, 10, 1790, 790)
    tracker = update_tracks(centers)
    draw_tracks(tracker)
    distances = get_track_distances(tracker)
    update_table(tracker, distances)

    frame_idx += 1
    if frame_idx < data.shape[1]:
        root.after(100, update_frame)

def setup_gui():
    global root, cv, frame_idx, data, tracker, track_colors, table, aircraft_info_label

    data = np.array(np.load('centers.npy'))[0:10, 0:150, 0:150]
    # print (data.shape[1])
    # print (data)

    # data = []

    # with open('centers.txt', 'r') as file:
    #     lines = file.readlines()

    #     for line in lines:
    #         print ("###############################################################################################################")
    #         line = line.strip()  # Eliminar espacios en blanco y saltos de línea            
    #         coords = re.findall(r"\((.*?), (.*?)\)", line)
    #         coords = [(float(x), float(y)) for x, y in coords]
    #         data.append(coords)
    #         print (coords)

    # data = np.array(data)
    tracker = Tracker(150, 30, 5)
    track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                    (127, 127, 255),(255, 0, 255), (255, 127, 255),
                    (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]

    frame_idx = 0

    root = tk.Tk()
    root.configure(bg='white')
    root.title("Tracker Output")

    aircraft_info_label = Label(root, text="", font=("Helvetica", 14,"bold"), fg="blue")
    aircraft_info_label.pack(side=tk.BOTTOM, padx=20, pady=20)

    cv = tk.Canvas(root, width=1800, height=800,bg='white')
    cv.pack()

    style = ttk.Style()
    style.theme_use("clam")

    table_frame = ttk.Frame(root)
    table_frame.pack(pady=20)

    headers = ["Identificación", "Ubicación","Distancia"]

    table = ttk.Treeview(table_frame, columns=headers, show="headings", style="Custom.Treeview")
    table.pack()

    style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
    style.configure("Custom.Treeview", font=("Arial", 10))

    for header in headers:
        table.heading(header, text=header)

def main():
    setup_gui()
    update_frame()
    root.mainloop()


if __name__ == '__main__':
    main()

