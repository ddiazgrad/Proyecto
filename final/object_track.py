import numpy as np
import cv2
from tracker import Tracker
import time
import re

def get_track_distances(tracker, my_plane):
    distances = []
    if len(tracker.tracks) > 0:
        x0, y0 = my_plane
        for track in tracker.tracks:
            x_track = int(track.trace[-1][0, 0])
            y_track = int(track.trace[-1][0, 1])
            distance = ((x_track - x0) ** 2 + (y_track - y0) ** 2) ** 0.5
            distances.append(distance)
    return distances

def createimage(w, h):
    size = (w, h, 1)
    img = np.ones((w, h, 3), np.uint8) * 255
    return img

def main(data, tracker, my_plane,identifiers,sensor):
    track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                    (127, 127, 255), (255, 0, 255), (255, 127, 255),
                    (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]
    try:
        distances = get_track_distances(tracker, my_plane)
    except:
        distances = None

    cell_width_column1 = 4
    cell_width_column2 = 8
    cell_width_column3 = 8
    cell_width_column4 = 16
    cell_width_column5 = 16
    text_x_column1 = 20
    text_x_column2 = text_x_column1 + cell_width_column1 * 6
    text_x_column3 = text_x_column2 + cell_width_column2 * 6
    text_x_column4 = text_x_column3 + cell_width_column3 * 6
    text_x_column5 = text_x_column4 + cell_width_column4 * 6
    for i in range(data.shape[1]):
        centers = data[:, i, :]
        frame = createimage(800, 1800)
        cv2.circle(frame, (int(my_plane[0]), int(my_plane[1])), 6, (0, 0, 0), -1)
        cv2.putText(frame, "{:.2f},{:.2f}".format(my_plane[0], my_plane[1]), (int(my_plane[0]) - 10, int(my_plane[1]) - 20), 0, 0.5, (0, 0, 0), 2)
        
        if len(centers) > 0:
            tracker.update(centers)
            cv2.putText(frame, "ID  x     y     distance     sensor", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            # print (len(tracker.tracks))
            for j in range(len(tracker.tracks)):
                if len(tracker.tracks[j].trace) > 1:
                    try:
                        x = int(tracker.tracks[j].trace[-1][0, 0])
                        y = int(tracker.tracks[j].trace[-1][0, 1])
                        tl = (x - 10, y - 10)
                        br = (x + 10, y + 10)
                        cv2.rectangle(frame, tl, br, track_colors[j], 1)
                        cv2.putText(frame, str(tracker.tracks[j].trackId), (x - 10, y - 20), 0, 0.5, track_colors[j], 2)
                        for k in range(len(tracker.tracks[j].trace)):
                            x = int(tracker.tracks[j].trace[k][0, 0])
                            y = int(tracker.tracks[j].trace[k][0, 1])
                            cv2.circle(frame, (x, y), 3, track_colors[j], -1)
                        cv2.circle(frame, (x, y), 6, track_colors[j], -1)
                    except:
                        pass

                try:
                    cv2.circle(frame, (int(data[j, i, 0]), int(data[j, i, 1])), 6, (0, 0, 0), -1)
                except:
                    pass

                try:
                    x = int(tracker.tracks[j].trace[-1][0, 0])
                    y = int(tracker.tracks[j].trace[-1][0, 1])
                    distance = distances[j]                    
                    try:
                        identifier = identifiers[j]
                        sens = sensor[j]
                    except:
                        identifier = "None"
                        sens = "None"
                    text = f"{str(tracker.tracks[j].trackId):<{cell_width_column1-1}}{x:<{cell_width_column2-3}}{y:<{cell_width_column3-2}}{distance:<{cell_width_column3+3}.2f}{sens:<{cell_width_column5}} "
                    cv2.putText(frame, text, (text_x_column1, 40 + j * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, track_colors[j], 2)
                except Exception as e:
                    print (e)
                    pass

            line_height = 20
            table_width = (cell_width_column1 + cell_width_column2 + cell_width_column3+cell_width_column4+cell_width_column5) * 6
            table_height = (len(tracker.tracks) + 1) * line_height
            table_tl = (16, 5)
            table_br = (table_tl[0] + table_width, table_tl[1] + table_height)
            cv2.rectangle(frame, table_tl, table_br, (0, 0, 0), 2)
            for j in range(1, len(tracker.tracks) + 1):
                line_y = table_tl[1] + j * line_height
                cv2.line(frame, (table_tl[0], line_y), (table_br[0], line_y), (0, 0, 0), 2)
                cv2.line(frame, (text_x_column2, table_tl[1]), (text_x_column2, table_br[1]), (0, 0, 0), 2)
                cv2.line(frame, (text_x_column3, table_tl[1]), (text_x_column3, table_br[1]), (0, 0, 0), 2)
                cv2.line(frame, (text_x_column4, table_tl[1]), (text_x_column4, table_br[1]), (0, 0, 0), 2)
                cv2.line(frame, (text_x_column5, table_tl[1]), (text_x_column5, table_br[1]), (0, 0, 0), 2)

        cv2.imshow('image', frame)
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break




def create_track(data, tracker):
    array_data = []
    my_plane = []
    identifiers = []
    sensor = []
    xxx = None
    for i, track in enumerate(data):
        if i != 0:
            coords = np.array([[track["location"]["x"], track["location"]["y"]]])
            array_data.append(coords)
            identifiers.append(track["identification"])
            sensor.append (track["sensor"])
        else:
            coords = track["location"]["x"], track["location"]["y"]
            my_plane.append(coords)
            xxx = coords
    array_data = np.array(array_data)
    my_plane = np.array(my_plane)
    main(array_data, tracker, xxx,identifiers,sensor)
    # time.sleep(0.2)
