# import numpy as np 
# import cv2
# from tracker import Tracker
# import time
# import imageio
# images = []

# def createimage(w,h):
# 	size = (w, h, 1)
# 	img = np.ones((w,h,3),np.uint8)*255
# 	return img

# # def createimage(w, h):
# #     img = cv2.imread('avion.png')  # Ruta de la imagen del avión
# #     img = cv2.resize(img, (w, h))  # Ajustar tamaño del avión a la imagen
# #     return img


# def main():
# 	data = np.array(np.load('centers.npy'))[0:10,0:150,0:150]
# 	# data = np.load('centers.npy')

# 	tracker = Tracker(150, 30, 5)
# 	skip_frame_count = 0
# 	track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
# 					(127, 127, 255), (255, 0, 255), (255, 127, 255),
# 					(127, 0, 255), (127, 0, 127),(127, 10, 255), (0,255, 127)]

# 	for i in range(data.shape[1]):
# 		print (i)
# 		centers = data[:,i,:]
# 		frame = createimage(800,1800)
# 		if (len(centers) > 0):
# 			tracker.update(centers)
# 			for j in range(len(tracker.tracks)):
# 				if (len(tracker.tracks[j].trace) > 1):
# 					x = int(tracker.tracks[j].trace[-1][0,0])
# 					y = int(tracker.tracks[j].trace[-1][0,1])
# 					tl = (x-10,y-10)
# 					br = (x+10,y+10)
# 					cv2.rectangle(frame,tl,br,track_colors[j],1)
# 					cv2.putText(frame,str(tracker.tracks[j].trackId), (x-10,y-20),0, 0.5, track_colors[j],2)
# 					for k in range(len(tracker.tracks[j].trace)):
# 						x = int(tracker.tracks[j].trace[k][0,0])
# 						y = int(tracker.tracks[j].trace[k][0,1])
# 						cv2.circle(frame,(x,y), 3, track_colors[j],-1)
# 					cv2.circle(frame,(x,y), 6, track_colors[j],-1)
# 				cv2.circle(frame,(int(data[j,i,0]),int(data[j,i,1])), 6, (0,0,0),-1)
# 			cv2.imshow('image',frame)
# 			# cv2.imwrite("image"+str(i)+".jpg", frame)
# 			# images.append(imageio.imread("image"+str(i)+".jpg"))
# 			time.sleep(0.1)
# 			if cv2.waitKey(1) & 0xFF == ord('q'):
# 				cv2.destroyAllWindows()
# 				break

# # 	# imageio.mimsave('Multi-Object-Tracking.gif', images, duration=0.08)
			


# if __name__ == '__main__':
# 	main()



# import numpy as np
# import cv2
# from tracker import Tracker
# import time
# import re

# def createimage(w, h):
#     size = (w, h, 1)
#     img = np.ones((w, h, 3), np.uint8) * 255
#     return img

# def main(data,tracker):    
#     track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
#                     (127, 127, 255), (255, 0, 255), (255, 127, 255),
#                     (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]

#     for i in range(data.shape[1]):
#         centers = data[:, i, :]
#         frame = createimage(800, 1800)

#         if len(centers) > 0:
#             tracker.update(centers)
#             for j in range(len(tracker.tracks)):
#                 if len(tracker.tracks[j].trace) > 1:
#                     try:
#                         x = int(tracker.tracks[j].trace[-1][0, 0])
#                         y = int(tracker.tracks[j].trace[-1][0, 1])
#                         tl = (x - 10, y - 10)
#                         br = (x + 10, y + 10)
#                         cv2.rectangle(frame, tl, br, track_colors[j], 1)
#                         cv2.putText(frame, str(tracker.tracks[j].trackId), (x - 10, y - 20), 0, 0.5, track_colors[j], 2)
#                         for k in range(len(tracker.tracks[j].trace)):
#                             x = int(tracker.tracks[j].trace[k][0, 0])
#                             y = int(tracker.tracks[j].trace[k][0, 1])
#                             cv2.circle(frame, (x, y), 3, track_colors[j], -1)
#                         cv2.circle(frame, (x, y), 6, track_colors[j], -1)
#                     except:
#                         pass
#             try:
#                 cv2.circle(frame, (int(data[j, i, 0]), int(data[j, i, 1])), 6, (0, 0, 0), -1)
#             except:
#                 pass
#             # Mostrar las coordenadas al lado del cuadro
#             for j in range(len(tracker.tracks)):
#                 try:
#                     x = int(tracker.tracks[j].trace[-1][0, 0])
#                     y = int(tracker.tracks[j].trace[-1][0, 1])
#                     text = f"({x}, {y})"
#                     cv2.putText(frame, text, (10, 30 + j * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, track_colors[j], 2)
#                 except: 
#                     pass
#             cv2.imshow('image', frame)
#             time.sleep(0.1)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 break

# if __name__ == '__main__':
#     tracker = Tracker(150, 30, 5)
#     data = []
#     with open('centerss.txt', 'r') as file:
#         lines = file.readlines()        
#         for line in lines:            
#             line = line.strip()  # Eliminar espacios en blanco y saltos de línea            
#             coords = re.findall(r"\((.*?), (.*?)\)", line)
#             coords = [(float(x), float(y)) for x, y in coords]
#             data.append(coords)
#     data = np.array(data)

#     for i in range(150):
#         data0 = data[0][i]
#         data1 = data[1][i]
#         data2 = data[2][i]
#         data3 = data[3][i]

#         data0 = np.array([data0])
#         data1 = np.array([data1])
#         data2 = np.array([data2])
#         data3 = np.array([data3])

#         sample = np.array ([data0,data1,data2,data3])
#         # if i<80:
#         #     sample = np.array ([data0,data1])
#         # else:
#         #     sample = np.array ([data0,data1,data2])

#         main(sample,tracker)
#         time.sleep(2)


import numpy as np
import cv2
from tracker import Tracker
import time
import re

def createimage(w, h):
    size = (w, h, 1)
    img = np.ones((w, h, 3), np.uint8) * 255
    return img

def main(data, tracker):
    track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                    (127, 127, 255), (255, 0, 255), (255, 127, 255),
                    (127, 0, 255), (127, 0, 127), (127, 10, 255), (0, 255, 127)]

    for i in range(data.shape[1]):
        centers = data[:, i, :]
        frame = createimage(800, 1800)

        if len(centers) > 0:
            tracker.update(centers)
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

                # Mostrar las coordenadas al lado del cuadro
                try:
                    x = int(tracker.tracks[j].trace[-1][0, 0])
                    y = int(tracker.tracks[j].trace[-1][0, 1])
                    text = f"({x}, {y})"
                    cv2.putText(frame, text, (10, 30 + j * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, track_colors[j], 2)
                except:
                    pass

        cv2.imshow('image', frame)
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    tracker = Tracker(150, 30, 5)
    data = []
    with open('centerss.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # Eliminar espacios en blanco y saltos de línea
            coords = re.findall(r"\((.*?), (.*?)\)", line)
            coords = [(float(x), float(y)) for x, y in coords]
            data.append(coords)
    data = np.array(data)

    for i in range(150):
        data0 = data[0][i]
        data1 = data[1][i]
        data2 = data[2][i]
        data3 = data[3][i]

        data0 = np.array([data0])
        data1 = np.array([data1])
        data2 = np.array([data2])
        data3 = np.array([data3])
        if i<80:

            sample = np.array([data0, data1, data2, data3])
        else:
            sample = np.array([data0, data1, data2])
        main(sample, tracker)
        # time.sleep(2)
