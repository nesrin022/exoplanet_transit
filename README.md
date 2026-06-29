# exoplanet_transit
# Exoplanet Transit Analysis

Detecting exoplanet transits using NASA Kepler and TESS open data.

## Projects

### Kepler-17b (Kepler Telescope)
Analyzed Kepler light curve data to detect the transit signal of Kepler-17b.
Applied phase-folding with a 1.4857-day orbital period to isolate the transit.

  Tools: Python, lightkurve, matplotlib

### Pi Mensae c (TESS Telescope)
Stitched 4 TESS sectors, applied normalization and binning to detect
the transit of Pi Mensae c (59.6 light-years from Earth).

  Orbital period: 6.27 days
  Tools: Python, lightkurve, matplotlib

## Transit Method?
A planet passing in front of its star blocks a small fraction of its light.
By folding repeated observations on the orbital period, the transit signal
emerges from the noise.
