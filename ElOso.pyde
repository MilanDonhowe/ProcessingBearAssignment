#      This is my Processing Bear Project for Eight Period IB Computer Science
#           Project done by Milan Donhowe
#
add_library('minim')

# Variables
Height = 600
Width = 900


Eye_pos = 0
Eye_height = 0


volume = 0.0

song = None

def setup():
    # Set up window
    size(Width,Height)
    
    # Get the song playing
    minim = Minim(this)
    global song
    song = minim.loadFile("bear.mp3")
    song.play()

def draw():
    
    background(255, 102, 51)
    
    #Get the song's volume

    EASING = 0.2
    MULTIPLIER = 1000
    currentVolume = song.right.level() * MULTIPLIER
    volumeDifference = currentVolume - volume
    if(abs(volumeDifference) > 1):
        global volume
        volume += volumeDifference * EASING
    
    # By how much to expand the shapes
    Expand = volume/4

    
    
    # Eye Follow Mouse
    if(mouseX > Width/2):
        global Eye_pos
        Eye_pos = min(Eye_pos + 0.5, 10)
    else:
        global Eye_pos
        Eye_pos = max(Eye_pos - 0.5, -10)
    if(mouseY > 210):
        global Eye_height
        Eye_height = min(Eye_height + 0.5, 10)
    else:
        global Eye_height
        Eye_height = max(Eye_height - 0.5, -10)
    
    # Body
    stroke(128, 85, 0)
    strokeWeight(10)
    fill(179, 119, 0)
    ellipse(Width/2, Height, 500 - Expand, 800 - Expand)
    
    
    # Ears
    stroke(153, 102, 0)
    strokeWeight(15)
    fill(179, 119, 0)
    ellipse(Width-650, Height-500, 140 + Expand, 140 + Expand)
    ellipse(Width-250, Height-500, 140 + Expand, 140 + Expand)
    strokeWeight(10)
    
    # Make Head
    fill(204, 136, volume)
    ellipse(Width/2, Height-370, 400 - Expand, 400 - Expand)
    
    #Snout
    fill(255, 223, 128)
    ellipse(Width/2, Height-250, 180+Expand, 120+Expand)
    fill(153, 102, 0)
    ellipse(Width/2, Height-260, 90+Expand, 60+Expand)
    
    # Left Eye
    
    fill(255,255,255)
    ellipse(360, 210, 150 + (Expand/2), 150 - (Expand/2))
    
    strokeWeight(0)
    noStroke()
    fill(153, 204, 255)
    ellipse(360+Eye_pos, 210+Eye_height, 90 + (Expand/2), 90 - (Expand/2))
    fill(0, 0, 0)
    ellipse(360+Eye_pos, 210+Eye_height, 60 + (Expand/2), 60 - (Expand/2))
    
    # right eye
    stroke(153, 102, 0)
    strokeWeight(10)
    fill(255,255,255)
    ellipse(540, Height-390, 150 + Expand, 150 + Expand)
    strokeWeight(0)
    noStroke()
    fill(153, 204, 255)
    ellipse(540+Eye_pos, 210+Eye_height, 90 + Expand, 90 + Expand)
    fill(0, 0, 0)
    ellipse(540+Eye_pos, 210+Eye_height, 60 + Expand, 60 + Expand)
    
    #SAVE FRAME
    #saveFrame("Output/line-########.png")
    
    
    
