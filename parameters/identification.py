class TrackId:
    def __init__(self):
        self.track_dict = {}

    def add_track(self,new_id, track_id):
        self.track_dict[new_id] = track_id

    def get_tracks(self):
        return self.track_dict
    
    def get_track(self,track_id):
        return self.track_dict[track_id]

    def id (self,data):
        vehicle_type = None
        id_type = None
        trackId = None
        print ("Gestionando identificador")
            
        if (data["freq"] == 2.4e9 or data ["freq"] == 5.8e9):
            print ("ICAO message")
            vehicle_type = "x"  #Se puede obtener a partir de ICAO, ya que lleva el modelo en el numero
            id_type = "icao"
            

        elif (data["freq"] == 1091e6):
            print ("RemoteId message")
            vehicle_type = "drone"
            id_type = "remoteid"
            
            
        if (data ["identification"] != None):
            if (not self.get_tracks()):
                self.add_track(data ["identification"],1) 
            else:
                
                if (data ["identification"] in self.get_tracks()):
                    trackId = self.get_track (data ["identification"])
                else:
                    trackId = max(self.get_tracks().values())+1
                    self.add_track(data ["identification"],trackId)
        else:
            print ("No hay identificador")

                
        print(self.get_tracks()) 
        return trackId,vehicle_type
        