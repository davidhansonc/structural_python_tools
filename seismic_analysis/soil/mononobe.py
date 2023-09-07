from numpy import sqrt, cos, rad2deg


def dyn_Kae(φ, ψ, δ, β, θ):
    K_ae = cos(φ - ψ - θ)**2 / (cos(ψ)*cos(θ)**2*cos(δ+θ+ψ)*(1 + sqrt((sin(φ+δ)*sin(φ-ψ-β))/(cos(δ+θ+ψ)*cos(β-θ))))**2)
    return K_ae


def dyn_Pae(K_ae, γ, k_v, H):
    P_ae = 1/2*γ*H**2*(1-k_v)*K_ae #plf
    return P_ae



def dyn_qae(P_ae, H):
    h_load = 0.6*H #P_ae application point height from base
    area_load_start_height = H - (H - h_load) * 2  #location equivalent area load starts from base
    q_ae = P_ae / (H - area_load_start_height) #psf (equivalent area load)
    return q_ae, area_load_start_height


# Steepness check.
def MO_validity(φ, β, ψ, k_h, k_v):
    if φ - β >=  ψ and k_h <= (1-k_v)*rad2deg(tan(φ-β)): #Mononobe-Okabe method is valid if both are true.
        return "valid"
    else:
        return "not valid"