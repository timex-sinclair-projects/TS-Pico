# TS-Pico Upgrade Video Production Guide
## Complete Production Manual for Firmware Upgrade Tutorial

---

## Video Overview

**Target Length:** 8-12 minutes  
**Style:** Instructional/Tutorial  
**Tone:** Friendly, reassuring, professional  
**Audience:** TS-Pico owners with basic technical skills  

---

## Pre-Production Setup

### Equipment Needed
- **Camera:** Fixed overhead shot capability + handheld for close-ups
- **Lighting:** Bright, even lighting to show small components clearly
- **Audio:** Clear narration (lapel mic or good room audio)
- **Props:** 
  - TS-Pico board
  - TS 2068 computer
  - Micro-USB cable
  - SD card and reader
  - Computer (laptop/desktop)
  - LED magnifying glass (optional, for close-ups)

### Materials to Have Ready
- upgrade.uf2 file
- UPGRADE.zip file
- SD card with existing TAP folder structure
- Printed copy of upgrade instructions (as backup reference)

---

## Shot List and Scripting

### INTRO SEQUENCE (0:00 - 0:30)
**Shot:** Wide shot of complete TS 2068 setup with TS-Pico installed

**Script:**
> "Welcome to the TS-Pico firmware upgrade tutorial. Today we're going to upgrade your TS-Pico from version 1.0 to version 1.2, which adds new commands and improves performance. Don't worry - this process is straightforward and will only take about 10 minutes. Let's get started!"

**Notes:** 
- Show confidence and enthusiasm
- Keep the TS-Pico visible in frame

---

### SAFETY OVERVIEW (0:30 - 1:00)
**Shot:** Close-up of hands with materials laid out

**Script:**
> "Before we begin, let's talk about what you'll need and some important safety notes. You'll need a micro-USB cable, the upgrade files I've provided, and about 10 minutes of uninterrupted time. The most important thing is to read through all the instructions before starting and never interrupt the upgrade process once it begins."

**Visual Elements:**
- Point to each item as mentioned
- Show upgrade files on computer screen

---

### STEP 1: PREPARATION (1:00 - 1:30)
**Shot:** Hands turning off TS 2068, removing TS-Pico

**Script:**
> "First, we need to turn off the TS 2068 completely. For extra safety, I'm going to remove the TS-Pico card entirely. If you have the expansion bus version, remove it from there. If you have the direct-connect version, carefully remove it from the edge connector."

**Technical Notes:**
- Show both removal methods if possible
- Emphasize gentle handling
- Close-up shot of connector alignment

---

### STEP 2: IDENTIFYING THE PICO (1:30 - 2:00)
**Shot:** Extreme close-up of Raspberry Pi Pico on TS-Pico board

**Script:**
> "Now we need to locate the Raspberry Pi Pico. It's this green board here with the white button. This button is our gateway to upgrade mode. You can see it's clearly labeled and easy to access."

**Visual Elements:**
- Use pointer or finger to indicate the Pico
- Zoom in on the white button
- Show it from multiple angles if needed

---

### STEP 3: ENTERING UPGRADE MODE (2:00 - 3:15)
**Shot:** Split between overhead and side angle showing button press and USB connection

**Script:**
> "Here's the most critical step. I'm going to press and hold this white button - see my finger here - and while holding it down, I'll connect the USB cable. First to the Pico, then to my computer. I need to keep holding the button until... there! You can see my computer has recognized a new device."

**Technical Direction:**
- **Shot 1:** Overhead view showing finger position on button
- **Shot 2:** Side angle showing USB cable connection
- **Shot 3:** Computer screen showing device recognition notification
- **Timing:** Hold shots long enough for viewers to see each step clearly

**Script Continuation:**
> "The Pico now appears as a drive called 'RPI-RP2' or similar. If you don't see this, disconnect and try again, making sure to hold the button firmly while connecting."

---

### STEP 4: FIRMWARE INSTALLATION (3:15 - 4:00)
**Shot:** Computer screen capture showing file drag-and-drop

**Script:**
> "Now for the easy part. I'm simply going to drag the upgrade.uf2 file from my downloads folder to the new RPI drive. Watch what happens - as soon as the file transfer completes, the drive disappears automatically. That means the firmware has been successfully installed."

**Visual Elements:**
- Screen recording of actual drag-and-drop
- Show file transfer progress
- Highlight when drive disappears
- Show brief celebration gesture

---

### STEP 5: SD CARD PREPARATION (4:00 - 5:00)
**Shot:** Hands removing SD card, inserting into computer

**Script:**
> "Next, I'll disconnect the USB cable and remove the SD card from the TS-Pico. Now I'm inserting it into my computer's card reader. We need to add the upgrade support files to complete the process."

**Technical Notes:**
- Show SD card removal clearly
- Demonstrate proper handling of small SD card
- Show computer recognizing SD card

---

### STEP 6: FILE INSTALLATION (5:00 - 5:45)
**Shot:** Computer screen showing file extraction and copying

**Script:**
> "I'm extracting the UPGRADE zip file and copying the contents to the SD card. It's important that we create an UPGRADE folder at the root level, right alongside the existing TAP folder. Your SD card should now have just two main folders: TAP and UPGRADE."

**Visual Elements:**
- Screen capture of zip extraction
- Show folder structure clearly
- Highlight the two-folder organization

---

### STEP 7: INITIAL TESTING (5:45 - 6:30)
**Shot:** TS 2068 screen showing directory command

**Script:**
> "Let's put everything back together and test. SD card goes back in the TS-Pico, TS-Pico goes back in the computer, and now I'll turn on the TS 2068. First test: LOAD "tpi:dir" - perfect! We can see our files, which means the basic installation is working."

**Technical Notes:**
- Show reassembly process
- Clear shot of TS 2068 screen with command output
- Express confidence in the successful test

---

### STEP 8: FIRMWARE UPGRADE (6:30 - 7:15)
**Shot:** Close-up of TS 2068 screen, then Raspberry Pi Pico LED

**Script:**
> "Now for the main event. I'll type SAVE "tpi:upgrade" and press enter. This starts the automated upgrade process. It's crucial not to interrupt this! After about 15 seconds, I'm watching the LED on the Raspberry Pi Pico. See that? It's blinking slowly - about once per second. That's exactly what we want to see. Success!"

**Critical Visual Elements:**
- Clear shot of command being typed
- Timer overlay showing elapsed time
- Close-up of LED blinking pattern
- Excited but controlled reaction to success

---

### STEP 9: VERIFICATION AND ROM PATCH (7:15 - 8:30)
**Shot:** TS 2068 screen showing new commands

**Script:**
> "After power cycling the computer, let's test the new firmware. SAVE "tpi:getinfo" - look at that! We can see we're now running version 1.2. Let's try SAVE "tpi:gethelp" - amazing! All these new commands are available. But we're not quite done yet. We need to apply the ROM patch."

**Visual Elements:**
- Show clear command output
- Highlight version number
- Express excitement about new features

**Script Continuation:**
> "I'll type SAVE "tpi:rompatch" followed by LOAD "". The rompatch program starts automatically. I'll follow the on-screen instructions... and we're done!"

---

### FINAL TESTING AND WRAP-UP (8:30 - 10:00)
**Shot:** Wide shot returning to complete setup

**Script:**
> "After one final power cycle, our upgrade is complete! Let me demonstrate some of the new features. The getinfo command shows detailed system status, gethelp provides comprehensive command reference, and we even have ZX Spectrum compatibility mode. Your TS-Pico is now running the latest firmware with all these improvements and more."

**Closing Script:**
> "That's it! You've successfully upgraded your TS-Pico to version 1.2. Remember, if you run into any issues, check the troubleshooting section in the manual or visit our GitHub community. Thanks for watching, and enjoy your upgraded TS-Pico!"

---

## Technical Production Notes

### Camera Work
- **Primary Camera:** Fixed overhead position for hands-on work
- **Secondary Camera:** Handheld for screen captures and detail shots
- **Macro Lens:** Essential for Raspberry Pi Pico close-ups
- **Steady Shots:** Use tripods for all static shots

### Audio Considerations
- **Record in quiet environment** - no background noise
- **Consistent audio levels** throughout
- **Clear pronunciation** of technical terms
- **Pace:** Speak slowly enough for viewers to follow along

### Screen Recording
- **High resolution** for computer screen captures
- **Zoom in** on relevant areas during file operations
- **Highlight cursor** movement for clarity
- **Stable recording** - avoid camera shake on screen shots

### Lighting Setup
- **Even, bright lighting** for small component visibility
- **Avoid shadows** when hands are working
- **Color accurate** lighting to show LED status correctly
- **Consistent lighting** throughout video

### Editing Guidelines
- **Cut out dead time** but maintain instructional pacing
- **Add text overlays** for key steps and warnings
- **Use zoom/crop** to highlight important details
- **Include timer overlays** during waiting periods
- **Add captions** for accessibility

---

## Post-Production Checklist

### Video Elements
- [ ] Clear audio throughout
- [ ] All steps visible and well-lit
- [ ] LED blinking patterns clearly shown
- [ ] Screen text readable at all sizes
- [ ] Smooth transitions between steps

### Content Verification
- [ ] All steps match written instructions
- [ ] No contradictory information
- [ ] Technical accuracy verified
- [ ] Safety warnings emphasized
- [ ] Troubleshooting tips included

### Final Quality Check
- [ ] Export in high resolution (1080p minimum)
- [ ] Test playback on different devices
- [ ] Verify captions/subtitles accuracy
- [ ] Check for any missing or unclear steps
- [ ] Confirm video length is appropriate

---

## Supplementary Materials for Video

### On-Screen Text Overlays
- "CRITICAL: Do not interrupt the upgrade process"
- "Hold button while connecting USB cable"
- "Success: LED blinks slowly (1x per second)"
- "Error: LED blinks fast (2x per second)"

### Chapter Markers (for longer platforms)
1. Introduction and Materials (0:00)
2. Preparation and Safety (0:30)
3. Entering Upgrade Mode (2:00)
4. Installing Firmware (3:15)
5. SD Card Setup (4:00)
6. Running the Upgrade (6:30)
7. Final Testing (8:30)

### Video Description Template
```
Learn how to upgrade your TS-Pico firmware from version 1.0 to 1.2 in this step-by-step tutorial. This upgrade adds new commands, improves performance, and enhances compatibility.

⏰ Time required: ~10 minutes
🔧 Difficulty: Easy to Moderate
📋 Materials needed: micro-USB cable, upgrade files

Timestamps:
0:00 - Introduction
0:30 - Materials and Safety
2:00 - Upgrade Mode
3:15 - Firmware Installation
[continue with all timestamps]

🔗 Download upgrade files: [link]
📖 Written instructions: [link]
💬 Community support: [GitHub link]

#TSPico #RetroComputing #Firmware #Tutorial
```

---

*This production guide ensures a professional, clear, and helpful video tutorial that matches the quality and tone of the TS-Pico documentation.*