# I gave up on writing it in Rust. Too difficult
import numpy as np
import plasmapy
import astropy
import astropy.units as u

def main():
    n0 = 1e20 * u.cm**-3
    wpe = plasmapy.formulary.frequencies.plasma_frequency(n0,particle = 'e-') / astropy.units.rad
    print(f"wpe = {wpe}")
    B_norm = (astropy.constants.m_e * wpe / astropy.constants.e.si).to(astropy.units.Gauss)
    B_real = 100_000_0 * u.Gauss
    print(f"A field strength of {B_real.to('kG')} corresponds to {(B_real / B_norm).to(astropy.units.dimensionless_unscaled)} in osiris units")

    electron_temps_eV = np.array([10, 100, 1000]) * u.eV
    electron_thermal_velocities = np.sqrt(electron_temps_eV / astropy.constants.m_e).to(astropy.units.cm / u.s)
    print(f"Electron thermal velocities in osiris units {electron_temps_eV}: {(electron_thermal_velocities / astropy.constants.c.si).to(astropy.units.dimensionless_unscaled)}")
    electron_larmor = (astropy.constants.m_e * electron_thermal_velocities / (astropy.constants.e.si * B_real)).to(astropy.units.cm)
    print(f"Electron Larmor radii for {electron_temps_eV}: {electron_larmor}")
    print(f"In osiris units this corresponds to: {(electron_larmor / (astropy.constants.c.si / wpe)).to(astropy.units.dimensionless_unscaled)}")

    # The expected heat suppression requires accessing a high beta regime
    beta = (n0 * electron_temps_eV / (B_real**2 / (2 * astropy.constants.mu0))).to(astropy.units.dimensionless_unscaled)
    print(f"Plasma beta for {electron_temps_eV}: {beta}")
    

if __name__ == "__main__":
    main()