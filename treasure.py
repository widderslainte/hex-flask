# -*- coding: utf-8 -*-
import random
from dice import *

# Gem Type d100
# Dice Score Base Value Description (or Size)
# 01-25 10 g.p. each Ornamental Stones very small
# 26-50 50 g.p. each Semi-precious Stones small
# 51-70 100 g.p. each Fancy Stones average
# 71-90 500 g.p. each Fancy Stones (Precious) large
# 91-99 1,000 g.p. each Gem Stones very large
# 00 5,000 g.p. each Gem Stones (Jewels) huge

# ORNAMENTAL STONES, Base Value 10 g.p.: d12
def check_ornamental():
    array_ornamental = ["0", "1. Azurite: mottled deep blue, 10 gp", "2. Banded Agate: striped brown and blue and white and reddish, 10gp", "3. Blue Quartz: pale blue, 10 gp", "4. Eye Agate: circles of gray, white, brown, blue and/or green, 10gp", "5. Hematite: gray-black, 10gp", "6. Lapis Lazuli: light and dark blue with yellow flecks, 10gp", "7. Malachite: striated light and dark green, 10gp", "8. Moss Agate: pink or yellow-white with grayish or greenish 'moss markings', 10gp", "9. Obsidian: black, 10gp",  "10. Rhodochrosite: light pink, 10gp", "11. Tiger Eye: rich brown with golden center under-hue, 10gp", "12. Turquoise: light blue-green, 10gp"]
    return 'Ornamental Stone: ' + array_ornamental[roll1d12()]

# SEMI-PRECIOUS STONES, Base Value 50 g.p.: d12
def check_semiprecious():
    array_semiprecious = ["0", "1. Bloodstone: dark gray with red flecks, 50gp", "2. Carnelian: orange to reddish brown, 50gp", "3. Zircon: clear pale blue-green, 50gp", "4. Chrysoprase: apple green to emerald green, 50gp", "5. Citrine: pale yellow brown, 50gp", "6. Jasper: blue, black to brown, 50gp", "7. Moonstone: white with pale blue glow, 50gp", "8. Onyx: bands of black and white or pure black or white, 50gp", "9. Rock Crystal: clear, 50gp", "10. Sardonyx: bands of sard (red) and onyx (white), 50gp", "11. Smoky Quartz: gray, yellow, or blue (Cairngorm), all light, 50gp", "12. Star Rose Quartz: translucent rosy stone with white “star” center, 50gp"]
    return 'Semi-Precious Stone: ' + array_semiprecious[roll1d12()]

#    FANCY STONES, Base Value 100 to 500 g.p.: 
def check_fancy():
    array_fancy = ["0", "1. Amber: watery gold to rich gold, 100gp", "2. Alexandrite: dark green, 100gp", "3. Amethyst: deep purple, 100gp", "4. Aquamarine: pale blue green, 500gp", "5. Chrysoberyl: yellow green to green, 100gp", "7. Garnet: red, brown-green, or violet, 100-500gp", "8. Jade: light green, deep green, green and white, white, 100gp", "10. Pearl*: lustrous white, yellowish, pinkish, etc. to pure black, 100-500gp", "11. Peridot: rich olive green, 500gp", "12. Spinel: red, red-brown, deep green, or very deep blue, 100-500gp", "13. Topaz: golden yellow, 500gp", "14. Tourmaline: green pale, blue pale, brown pale, or reddish pale, 100gp"] 
    return 'Fancy Stone: ' + array_fancy[roll1d12()]

# GEM STONES, 1,000 or more g.p. Base Value:
# 1. Black Opal: dark green with black mottling and golden flecks
# 2. Black Sapphire: lustrous black with glowing highlights (5,000)
# 3. Diamond: clear blue-white with lesser stones clear white or pale tints (5,000)
# 4. Emerald: deep bright green
# 5. Fire Opal: fiery red
# 6. Jacinth: fiery orange (Corundum) (5,000)
# 7. Opal: pale blue with green and golden mottling
# 8. Oriental Amethyst: rich purple (Corundum)
# 9. Oriental Emerald: clear bright green (Corundum) (5,000)
# 10. Oriental Topaz: fiery yellow (Corundum)
# 11. Ruby: clear red to deep crimson (Corundum) (5,000)
# 12. Sapphire: clear to medium blue (Corundum)
# 13. Star Ruby: translucent ruby with white “star” center
# 14. Star Sapphire: translucent sapphire with white “star” center