import lightkurve as lk
import matplotlib.pyplot as plt

# kepler-17 a real star
results = lk.search_lightcurve("Kepler-17", mission="Kepler",) 
print(results)

# Download the first observation
lc = results[0].download()

# Plot the light curve
lc.plot()
plt.show()

# Clean the data and fold it on the planet's orbital period
lc_clean = lc.remove_outliers()
lc_folded = lc_clean.fold(period=1.4857)

# Plot the folded light curve
lc_folded.plot()
plt.show()

import lightkurve as lk
import matplotlib.pyplot as plt

# Download and clean
results = lk.search_lightcurve("Kepler-17", mission="Kepler")
lc = results[0].download()
lc_clean = lc.remove_outliers()
lc_folded = lc_clean.fold(period=1.4857)

# Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# First plot — raw data
lc_clean.plot(ax=axes[0], color='steelblue')
axes[0].set_title("Kepler-17: Raw Light Curve")
axes[0].set_xlabel("Time (days)")
axes[0].set_ylabel("Flux (e/s)")

# Second plot — folded transit
lc_folded.plot(ax=axes[1], color='darkorange')
axes[1].set_title("Kepler-17b: Folded Transit Signal (Period = 1.4857 days)")
axes[1].set_xlabel("Phase")
axes[1].set_ylabel("Flux (e/s)")

plt.tight_layout()
plt.savefig("kepler17_transit.png", dpi=150)
plt.show()

print("Plot saved as kepler17_transit.png")