import pandas as pd

dls = {
    "Roof DL" : 15.0, #psf
    "Roof LL" : 20.0, #psf
    "Floor DL" : 25.0, #psf
    "Floor LL" : 40.0, #psf
    "Balcony DL" : 50.0, #psf
    "Balcony LL" : 60.0 #psf
}

DLS = pd.DataFrame(data=dls, index=["Load (psf)"])