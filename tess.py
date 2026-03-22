import lightkurve as lk
import matplotlib.pyplot as plt

results = lk.search_lightcurve("Pi Mensae", mission="TESS", author="SPOC")
lc_collection = results[0:4].download_all()
lc_stitched = lc_collection.stitch()
lc_clean = lc_stitched.remove_outliers().normalize()
lc_folded = lc_clean.fold(period=6.27, normalize_phase=True)

# Bin the folded curve — averages nearby points to reduce noise
lc_binned = lc_folded.bin(bins=200)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

lc_clean.plot(ax=axes[0], color='steelblue')
axes[0].set_title("Pi Mensae: TESS Stitched Light Curve (4 Sectors)")
axes[0].set_xlabel("Time (days)")
axes[0].set_ylabel("Normalized Flux")

lc_binned.plot(ax=axes[1], color='darkorange')
axes[1].set_title("Pi Mensae c: Binned Folded Transit (Period = 6.27 days)")
axes[1].set_xlabel("Phase")
axes[1].set_ylabel("Normalized Flux")

plt.tight_layout()
plt.savefig("pimensae_transit_v3.png", dpi=150)
plt.show()
print("Done!")