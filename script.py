import os
import math
 
 
def write(folder, name, range):
    contents = f"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>class</key>
        <string>BSScaleModule2</string>
        <key>cprurl</key>
        <string>/Scale/{folder}/{name}.drmodule</string>
        <key>hcv</key>
        <false/>
        <key>inputs</key>
        <array>
            <dict>
                <key>ac</key>
                <true/>
                <key>ace</key>
                <false/>
                <key>opid</key>
                <integer>5</integer>
            </dict>
        </array>
        <key>modelId</key>
        <integer>0</integer>
        <key>modelName</key>
        <string>Scale</string>
        <key>name</key>
        <string>{name}</string>
        <key>outputs</key>
        <array>
            <dict>
                <key>pid</key>
                <integer>4</integer>
            </dict>
        </array>
        <key>params</key>
        <array>
            <dict>
                <key>pid</key>
                <integer>1</integer>
                <key>v</key>
                <real>1</real>
            </dict>
            <dict>
                <key>pid</key>
                <integer>2</integer>
                <key>v</key>
                <real>1</real>
            </dict>
            <dict>
                <key>pid</key>
                <integer>3</integer>
                <key>v</key>
                <real>{range}</real>
            </dict>
        </array>
        <key>pid</key>
        <integer>0</integer>
    </dict>
</plist>
"""
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{name}.drmodule", 'w') as file:
        file.write(contents)
 
 
def edf():
    bb = (12 * math.log(3) / math.log(2)) - 12
    for i in range(3, 32):
        write("ED2_3 (fifth)", f"{i:02} EDF", bb/i)
 
 
def edo():
    for i in range(5, 54):
        write("ED2 (octave)", f"{i:02} EDO", 12/i)
 
 
def edn():
    bb = 12 * math.log(math.e) / math.log(2)
    for i in range(8, 33):
        write("ED2.718", f"{i:02} EDN", bb/i)
 
 
def edt():
    bb = 12 * math.log(3) / math.log(2)
    for i in range(8, 40):
        write("ED3", f"{i:02} EDT", bb/i)
 
 
def harmonics():
    # add more here :)
    for harm in [5, 7]:
        bb = 12 * math.log(harm) / math.log(2)
        for i in range(10, 56):
            write(f"ED{harm}", f"{i:02} ED{harm}", bb/i)
 
 
def wendy():
    write("Wendy Carlos", f"Wendy Carlos Alpha", 0.77965)
    write("Wendy Carlos", f"Wendy Carlos Beta", 0.63833)
    write("Wendy Carlos", f"Wendy Carlos Gamma", 0.350985422804)
 
 
def cET():
    for cents in [88, 65, 125, 97.5]:
        write("cET", f"{cents}cET", cents/100)
 
 
if __name__ == '__main__':
    edf()
    edo()
    edn()
    edt()
    harmonics()
    wendy()
    cET()
 
