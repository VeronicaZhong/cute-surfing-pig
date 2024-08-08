import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure and a single subplot for a cuter pig
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the ocean (background)
ax.add_patch(patches.Rectangle((0, 0), 10, 5, color='lightblue'))

# Draw waves
wave_count = 5
for i in range(wave_count):
    wave = patches.Arc((2*i, 2.5), 4, 2, angle=0, theta1=0, theta2=180, color='blue', lw=2)
    ax.add_patch(wave)

# Draw a surfboard
surfboard = patches.Ellipse((5, 3), 3, 0.5, color='yellow')
ax.add_patch(surfboard)

# Draw a cuter pig surfing
# Pig's body
body = patches.Circle((5, 3.7), 0.6, color='pink')
ax.add_patch(body)

# Pig's head (larger and rounder for a cuter look)
head = patches.Circle((5, 4.4), 0.5, color='pink')
ax.add_patch(head)

# Pig's ears (smaller and rounder for cuteness)
left_ear = patches.Polygon([[4.85, 4.8], [4.7, 4.5], [4.95, 4.55]], color='pink')
right_ear = patches.Polygon([[5.15, 4.8], [5.3, 4.5], [5.05, 4.55]], color='pink')
ax.add_patch(left_ear)
ax.add_patch(right_ear)

# Pig's eyes (larger for a cuter look)
ax.plot([4.8, 5.2], [4.45, 4.45], 'ko', markersize=8)

# Pig's snout (larger for cuteness)
snout = patches.Circle((5, 4.2), 0.2, color='lightpink')
ax.add_patch(snout)
ax.plot([4.92, 5.08], [4.22, 4.22], 'k.', markersize=6)

# Pig's blush (to add cuteness)
ax.add_patch(patches.Circle((4.8, 4.3), 0.1, color='lightcoral', alpha=0.6))
ax.add_patch(patches.Circle((5.2, 4.3), 0.1, color='lightcoral', alpha=0.6))

# Pig's mouth (small smile for cuteness)
ax.plot([4.9, 5.1], [4.05, 4.05], 'k', linewidth=2)
ax.plot([4.9, 4.95], [4.05, 4], 'k', linewidth=2)
ax.plot([5.1, 5.05], [4.05, 4], 'k', linewidth=2)

# Pig's arms (smaller and rounder)
left_arm = patches.Polygon([[4.7, 3.9], [4.6, 3.7], [4.8, 3.6]], color='pink')
right_arm = patches.Polygon([[5.3, 3.9], [5.4, 3.7], [5.2, 3.6]], color='pink')
ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Pig's legs (smaller and rounder)
left_leg = patches.Polygon([[4.8, 3.3], [4.7, 3.1], [4.9, 3.1]], color='pink')
right_leg = patches.Polygon([[5.2, 3.3], [5.3, 3.1], [5.1, 3.1]], color='pink')
ax.add_patch(left_leg)
ax.add_patch(right_leg)

# Add the encouraging text
plt.text(1.5, 5, "Ride the waves of success!", fontsize=15, color='darkblue', weight='bold')

# Remove axes
ax.axis('off')

# Adjust the aspect ratio
ax.set_aspect('equal')

# Save the picture
plt.savefig('cute_surfing_pig.png')

# Display the picture
plt.show()