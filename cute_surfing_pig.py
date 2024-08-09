import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Set canvas size according to the golden ratio
fig, ax = plt.subplots(figsize=(6, 9.7))

# Draw the ocean (background) with adjusted proportions
ax.add_patch(patches.Rectangle((0, 0), 10, 6.18, color="lightblue"))

# Recalculate wave positions for symmetry
wave_count = 5
wave_spacing = 10 / wave_count
for i in range(wave_count):
    wave_center_x = wave_spacing * i + wave_spacing / 2
    wave = patches.Arc(
        (wave_center_x, 3.09), 4, 2, angle=0, theta1=0, theta2=180, color="blue", lw=2
    )
    ax.add_patch(wave)

# Adjust the surfboard position and size for better centering
surfboard = patches.Ellipse((5, 4.2), 3, 0.5, color="yellow")
ax.add_patch(surfboard)

# Adjust the cuter pig's position and size for symmetry
# Pig's body
body = patches.Circle((5, 5.0), 0.6, color="pink")
ax.add_patch(body)

# Pig's head (keeping larger and rounder for a cuter look)
head = patches.Circle((5, 5.7), 0.5, color="pink")
ax.add_patch(head)

# Pig's ears (aligned symmetrically)
left_ear = patches.Polygon([[4.85, 6.1], [4.7, 5.8], [4.95, 5.85]], color="pink")
right_ear = patches.Polygon([[5.15, 6.1], [5.3, 5.8], [5.05, 5.85]], color="pink")
ax.add_patch(left_ear)
ax.add_patch(right_ear)

# Pig's eyes (keeping them large and symmetric for cuteness)
ax.plot([4.8, 5.2], [5.75, 5.75], "ko", markersize=8)

# Pig's snout (centered for symmetry)
snout = patches.Circle((5, 5.5), 0.2, color="lightpink")
ax.add_patch(snout)
ax.plot([4.92, 5.08], [5.52, 5.52], "k.", markersize=6)

# Pig's blush (symmetric position)
ax.add_patch(patches.Circle((4.8, 5.6), 0.1, color="lightcoral", alpha=0.6))
ax.add_patch(patches.Circle((5.2, 5.6), 0.1, color="lightcoral", alpha=0.6))

# Pig's mouth (small and symmetric)
ax.plot([4.9, 5.1], [5.35, 5.35], "k", linewidth=2)
ax.plot([4.9, 4.95], [5.35, 5.3], "k", linewidth=2)
ax.plot([5.1, 5.05], [5.35, 5.3], "k", linewidth=2)

# Pig's arms (adjusted symmetrically)
left_arm = patches.Polygon([[4.7, 5.2], [4.6, 5.0], [4.8, 4.9]], color="pink")
right_arm = patches.Polygon([[5.3, 5.2], [5.4, 5.0], [5.2, 4.9]], color="pink")
ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Pig's legs (symmetrically adjusted)
left_leg = patches.Polygon([[4.8, 4.6], [4.7, 4.4], [4.9, 4.4]], color="pink")
right_leg = patches.Polygon([[5.2, 4.6], [5.3, 4.4], [5.1, 4.4]], color="pink")
ax.add_patch(left_leg)
ax.add_patch(right_leg)

# Adjust the text position for better symmetry
plt.text(
    5,
    9.4,
    "Ride the waves of success!",
    fontsize=15,
    color="darkblue",
    weight="bold",
    ha="center",
)

# Remove axes
ax.axis("off")

# Adjust the aspect ratio
ax.set_aspect("equal")

# Save the picture
plt.savefig("cute_surfing_pig.png")

# Display the picture
plt.show()

