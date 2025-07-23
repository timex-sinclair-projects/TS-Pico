# TS-Pico Firmware Upgrade Instructions
## From Version 1.0 to Version 1.2

---

### Before You Begin

Upgrading your TS-Pico firmware is straightforward, but like any technical procedure, it requires your attention and a little patience. This upgrade will take your TS-Pico from version 1.0 to version 1.2, adding new commands and improving overall performance.

**Time Required:** About 10 minutes  
**Difficulty Level:** Easy to Moderate  
**Risk Level:** Low (but follow the instructions carefully!)

---

### What You'll Need

Before starting, gather these materials:

- **A micro-USB cable** to connect the Raspberry Pi Pico in your TS-Pico to your computer
- **The UPGRADE zip file** (provided separately)
- **The upgrade.uf2 file** (provided separately)
- **Your computer** (PC, Mac, or Linux - any will work)
- **About 10 minutes of uninterrupted time**

---

### Important Safety Notes

**READ THIS SECTION COMPLETELY** before proceeding:

1. **Read all instructions** to the end before starting. Make sure you understand each step.
2. **Ask questions** if something isn't clear - it's better to be safe than sorry.
3. **Set aside time** to complete the entire process without interruption.
4. **Have everything ready** before you begin.
5. **Don't rush** - take your time with each step.

---

## Upgrade Procedure

### Step 1: Prepare Your TS-Pico

**Turn off your TS 2068** completely. For extra safety, remove the TS-Pico card from either:
- The multi-slot adapter, or  
- The TS 2068 edge connector (depending on your setup)

This ensures no electrical activity during the upgrade process.

### Step 2: Locate the Raspberry Pi Pico

Find the Raspberry Pi Pico board inside your TS-Pico. It's the **green board with a white button** on it. This little button is your gateway to upgrade mode.

### Step 3: Enter Upgrade Mode

Here's the trickiest part, but it's not too bad:

1. **Get your USB cable ready**
2. **Press and HOLD the white button** on the Raspberry Pi Pico
3. **While holding the button**, connect the USB cable to both the Pico and your computer
4. **Keep holding** until your computer recognizes a new device

Your computer should show a notification that a new mass-storage device has been connected. The Raspberry Pi Pico will appear as a new drive in your file system - just like plugging in a USB flash drive.

**Congratulations!** The Pico is now in "update mode."

### Step 4: Install the Firmware

This step is surprisingly simple:

1. **Drag and drop** the `upgrade.uf2` file to the new drive that appeared
2. **Wait** for the file transfer to complete
3. **Watch for the notification** that the drive has been disconnected

The drive will automatically disappear from your computer when the firmware installation is complete. The Raspberry Pi Pico is now running in "operating mode" with the new firmware.

### Step 5: Prepare the SD Card

1. **Unplug the USB cable** from both the Pico and your computer
2. **Remove the SD card** from your TS-Pico
3. **Insert the SD card** into your computer's card reader

### Step 6: Install the Support Files

The firmware needs some additional files to complete the upgrade:

1. **Extract the UPGRADE zip file** contents
2. **Copy the extracted files** to your SD card in a folder named `UPGRADE`
3. **Make sure the folder structure** looks like this:

```
SD Card Root
├── TAP/
│   ├── A-C/
│   ├── D-E/
│   └── (other folders...)
└── UPGRADE/
    └── (extracted files here)
```

There should be only **two top-level directories**: `TAP` and `UPGRADE`.

### Step 7: Test the Basic Installation

1. **Insert the SD card** back into your TS-Pico
2. **Connect the TS-Pico** to your TS 2068 (multi-slot adapter or edge connector)
3. **Turn on your TS 2068**

Let's make sure everything is working:

```
LOAD "tpi:dir"
```

If you see your directory listing, everything looks good so far.

### Step 8: Complete the Firmware Upgrade

Now for the magic moment:

```
SAVE "tpi:upgrade"
```

This starts the automated upgrade process. **DO NOT INTERRUPT** this process once it starts.

After 10-20 seconds, watch the LED on the Raspberry Pi Pico:

- **Slow blinking** (once per second): Success! 🎉
- **Fast blinking** (twice per second): Something went wrong - contact support

### Step 9: Power Cycle and Test

Regardless of the blinking pattern:

1. **Turn off your TS 2068** completely
2. **Turn it back on**

You should now be running firmware version 1.2! Test it with these new commands:

```
SAVE "tpi:gethelp"
SAVE "tpi:getinfo"
```

**Important:** Don't use `LOAD "tpi:dir"` just yet - we have one more step.

### Step 10: Apply the ROM Patch

There's one final step to complete the upgrade:

1. **Type this command:**
   ```
   SAVE "tpi:rompatch"
   ```

2. **Then type:**
   ```
   LOAD ""
   ```

A BASIC program called "rompatch" should start automatically. **Follow the simple on-screen instructions** - they'll guide you through applying the final ROM patch.

### Step 11: Final Power Cycle

After the ROM patch completes:

1. **Turn off your TS 2068** one final time
2. **Turn it back on**

**Congratulations!** Your TS-Pico is now fully upgraded to version 1.2 with all the latest features and improvements.

---

## What's New in Version 1.2?

Your upgraded TS-Pico now includes:

- **Enhanced system information** with `SAVE "tpi:getinfo"`
- **Built-in help system** with `SAVE "tpi:gethelp"`
- **Activity logging** with `SAVE "tpi:getlog"`
- **ZX Spectrum compatibility** with `SAVE "tpi:zx48"`
- **Advanced memory management** commands
- **Improved file handling** and error reporting
- **Many other under-the-hood improvements**

---

## If Something Goes Wrong

Don't panic! Here's what to do:

### If the LED blinks fast after upgrade:
- Contact the TS-Pico support team
- Have your upgrade files ready
- Note any error messages you saw

### If the computer doesn't recognize the Pico:
- Try a different USB cable
- Make sure you're holding the white button while connecting
- Try a different USB port on your computer

### If the TS-Pico doesn't respond after upgrade:
- Try the troubleshooting steps in the main manual
- Power cycle your TS 2068 completely
- Contact support if problems persist

---

## Support and Community

Having trouble? The TS-Pico community is here to help:

- **GitHub Repository:** https://github.com/TS-Pico-dev/TS-Pico
- **Community Forums:** (check the GitHub for current links)
- **Documentation:** Always check for the latest documentation updates

Remember, this is a community project, and we're all learning together. Your feedback helps make the TS-Pico better for everyone!

---

*This upgrade guide is for TS-Pico firmware version 1.2. Always check for the latest version and instructions before upgrading.*