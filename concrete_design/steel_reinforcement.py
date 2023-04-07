import pandas as pd


# Diameter (in), Area (in^2), Weight (lbs/ft)
rebar_df = pd.DataFrame({"Diameter": [.375, .5, .625, .75, .875, 1.0, 1.128, 1.27, 1.41, 1.693, 2.257],
                        "Area": [.11, .2, .31, .44, .6, .79, 1.0, 1.27, 1.56, 2.25, 4.0],
                        "Weight": [.376, .668, 1.043, 1.502, 2.044, 2.67, 3.4, 4.303, 5.313, 7.65, 13.6]}, 
                        index=["#3", "#4", "#5", "#6", "#7", "#8", "#9",\
                                       "#10", "#11", "#14", "#18",]
                    )

rebar_arr = rebar_df.to_numpy()