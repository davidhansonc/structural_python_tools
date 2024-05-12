"""
stone_veneer = 165 #pcf
rigid_insulation_XV = 3.0 #pcf
semi_rigid_insulation = 4.3 #pcf
studs_2x6 = 2.7 #psf 
studs_2x8 = 1.77 #psf (bare studs)
WSP_sheathing = 2.1 #psf
wood_wall_panel = 50 #pcf

rigid_insulation_XV = 0.50 #psf per layer (3.0 pcf per each 2" layer)
batt_insulation = 2.0 #pcf
wood_joists = 4.5 / 1.333 #psf (linear weight / spacing)
floor_sheathing = 2.3 #psf (3/4" T&G)
stone_flooring = 10 #psf (1" stone + mortar bed)
soil_weight = 85 #pcf
granite_ballast = 11 #psf per inch layer
"""

insulation = {
	"semi-rigid mineral wool": 0.7, #(R-5)
	"batt insulation": 0.17,
	"rigid insulation (XPS)": 0.167,
	"closed-cell insulation": 0.167,
} #psf/in

sheathing = {
	"plywood": 3,
	"OSB": 3,
	"WSP": 3,
} #psf/in

gypsum = {
	"GWB": 3.2,
	"type X fire-resistant": 4.8,
} #psf/in

# D.F. studs. γtd/s -> 31.2 * (1.5/12) * (d/12) / (16/12)
wood_studs = {
	"2x at 12 O.C.": 0.325,
	"2x at 16 O.C.": 0.2438,
	"2x at 24 O.C.": 0.1625,
	"(2) 2x at 16 O.C.": 0.4876,
} #psf/in

veneer = {
	"limestone veneer": 15,
	"clay brick veneer": 12.5,
} #psf/in

tile = {
	"ceramic tile": 4,
	"porcelain tile": 6,
	"granite tile": 13,
	"marble tile": 14,
	"slate tile": 15,
} #psf/in

masonry = {
	"clay brick": 120,
	"adobe brick": 100,
} #pcf

green_roof = {
}