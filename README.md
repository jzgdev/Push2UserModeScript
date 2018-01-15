# Ableton Push 2 - User Mode Custom Script

## Quick Start & Install
1. Download latest [release](https://github.com/jzgdev/Push2UserModeScript/releases/download/v1.0/Push2UserModeScript-v1.0.zip)
2. UnZip the archive
3. Place the contained folder, `Push2UserModeScript` in MIDI Remote Scripts folder:
	- **Mac**:
		1. Navigate to Ableton Live App in `Applications`
		2. Right-click and press `Show Package Contents`
		3. Navigate to `Contents/App-Resources/MIDI Remote Scripts`
	- **Windows**
		- `\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`
4. Start Ableton Live, or restart if already running
5. Open Ableton preferences and navigate to MIDI
6. Change settings to the following:

| Control Surface | Input | Output |
| ------------- | ------------- | ------------- |
| Push2UserMode | Ableton Push 2 (User Port) | Ableton Push 2 (User Port) |


### Overview

When using Ableton Push 2 for performance, I got a bit frustrated with some of the default behaviors of the built in Push 2 script so I put together this easily customizable script that allowed Push 2 to be controlled the way I wanted it to.

#### More Details on My Setup

- Top row of 8 buttons (above display)
	- Arms corresponding track for recording
- Bottom row of buttons (below display)
	- Selects corresponding track
- Top row encoders (knobs)
	- Controls macro paramaters of selected track/last selected device on track

- Top 4 x 8 grid
	- Triggers clips in corresponding slot
- Repeat division buttons (right side)
	- Trigger corresponding scenes

- Bottom grid
	- Drum pads/standard notes (C1 - G3)

- Arrows
	- Controls location of session contol ring (rectangle visible in Session View)		

- Stop Clip
	- Stops all playing clips

- Master
	- Select master channel

Since this script doesn't have modes, I initially set it up to have the bottom four rows of pads act as drum pads, while the top four rows controlled clips, however, if you only want clip control you change this in `MIDI_Map.py` by setting `DRUM_PADS_ENABLED=0`. I didn't include an option if you wanted ONLY drum pads, easiest way to achieve that is just disabling the script. 				

#### Customizing
If you want to customize this to better suit your needs, you can edit the file `MIDI_Map.py` to suit your tastes, most of the mappings available in that file are fairly self-explanatory.

Just enter in the number corresponding to the control desired, you can find the number with the help of free programs like [MIDI Monitor](https://www.snoize.com/MIDIMonitor/)


### Limitations

#### Special Functions
Functions like "Duplicate", "Quantize", "New", etc. won't work, but the buttons can be mapped to something else if you'd like.

#### Lights
Lights for things like armed/selected track and currently playing clips works fine.
Light that unfortunately don't work as of now: 
	
	- Drum pads lit up when occupied by a sample (as in default mode)
	- Light feedback when pressing a drum/note pad
	- Available (non-playing) clips

#### Encoders
Past versions of this had worked fine, but somewhere along the way, the encoder's mapping mode stopped functioning properly and typically only makes big jumps from 1-127 as opposed to a smooth transition through the range.	

#### Play/Stop
Since by default, the play button controls both play and stop (and does so with coded in logic I haven't implemented), I had to remap the `Stop` button to the `Mute` button.

### To-Do
	- Fix encoder mapping mode problem
	- Fix above mentioned issues with non-working lights
	- Perhaps using `Layout`, `Note`, and/or `Session` buttons to access different modes
	- Add logic to allow Play/Stop to function as they do in the default script

### Contributing

The To-Do list is more of a "wish list" that I may or may not get to, I'm not in a rush and have quite a few other commitments that take priority, but if anyone would like to take a stab at it, or any other things you think would benefit the script, feel free.

If you would like to contribute, fork the repo and make a pull request.

#### Issues
If you're having, or notice, any issues file just file the issue here on GitHub.

#### Questions/Help
I can't promise it will be quickly answered, but, if you want ask a question, just ask it in the the "Issues" section of this repo and I'll mark it as a question and do my best to answer/help when I'm able.


### Acknowledgements

Based on [st4rchild](https://github.com/st4rchild/Ableton-Live-MIDI-Remote-Scripts)'s work as well [FCB1020 scripts](http://remotescripts.blogspot.com)

----------
DISCLAIMER
----------

THESE FILES ARE PROVIDED AS-IS, WITHOUT ANY WARRANTY, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO FITNESS FOR ANY PARTICULAR PURPOSE.
