# TS-Pico User Manual
## Timex Sinclair 2068 Personal Color Computer Pico Interface

*Firmware Version 1.2 - Complete User Guide*

---

## Table of Contents

- [General Description and Operation](#general-description-and-operation)
- [Installing the TS-Pico](#installing-the-ts-pico)
- [Getting Started: Your First Steps](#getting-started-your-first-steps)
- [Exploring the TS-Pico Hardware](#exploring-the-ts-pico-hardware)
- [Understanding the TS-Pico Commands](#understanding-the-ts-pico-commands)
- [Basic File Operations - Your Daily Toolkit](#basic-file-operations---your-daily-toolkit)
- [Directory Navigation - Organizing Your Files](#directory-navigation---organizing-your-files)
- [Working with TAP Files - The Heart of the System](#working-with-tap-files---the-heart-of-the-system)
- [Advanced System Commands](#advanced-system-commands)
- [Memory and Flash Management](#memory-and-flash-management)
- [ZX Spectrum Compatibility Mode](#zx-spectrum-compatibility-mode)
- [Traditional LOAD and SAVE Operations](#traditional-load-and-save-operations)
- [File and Directory Management Best Practices](#file-and-directory-management-best-practices)
- [System Information and Diagnostics](#system-information-and-diagnostics)
- [Troubleshooting Guide](#troubleshooting-guide)
- [What's Next? Upgrades and Extensions](#whats-next-upgrades-and-extensions)
- [The TS-Pico Community](#the-ts-pico-community)
- [Quick Reference Card](#quick-reference-card)
- [Appendix A: External Commands for Developers](#appendix-a-external-commands-for-developers)
- [Appendix B: Machine Language Flash Programming](#appendix-b-machine-language-flash-programming)
- [Appendix C: Technical Specifications](#appendix-c-technical-specifications)

---

## General Description and Operation

### Welcome to the Future of Your TS 2068!

Thank you for selecting the Timex Pico Interface, or the TS-Pico, as we like to call it. You're about to transform your vintage TS 2068 into a modern, capable machine while keeping all the charm and character that made you fall in love with it in the first place.

### What Exactly Is the TS-Pico?

Think of the TS-Pico as a bridge between your classic computer and today's technology. It's like having a modern hard drive, but one that speaks the language your TS 2068 understands perfectly. This new interface was developed specifically for the Timex Sinclair 2068 computer, and it brings together the best of both worlds: the nostalgia and simplicity of your vintage machine with the convenience and reliability of modern storage.

### The Technology Behind the Magic

At its heart, the TS-Pico is powered by a Raspberry Pi Pico - a tiny but powerful computer that acts as your TS 2068's new best friend. Programmed in MicroPython (a streamlined version of the popular Python programming language), the TS-Pico allows you to save and load programs from TAP files stored on a standard micro SD card - the same kind you might use in a smartphone or tablet.

But that's not all. Your TS-Pico comes equipped with an impressive 512KB of Flash memory. To put that in perspective, that's enough space to store several of your favorite cartridge programs, instantly accessible, without even touching the SD card. Some of this Flash memory holds the TS-Pico's advanced operating system - think of it as the brain that makes everything work smoothly. The rest is available for your use, which you can use as super-fast storage for your cartridges.

On top of that, you get another 512KB of static RAM (SRAM) - all of which is available to you. This is like having extra workspace for your computer to stretch out and handle bigger, more complex programs than ever before.

### A Word About Safety

Now, we need to have a brief but important conversation about taking care of your TS-Pico. While we've designed it to be robust and reliable, it's still a sophisticated piece of electronics. The TS-Pico is difficult to break, but not impossible. 

**Here's the important part:** If you don't have experience with electronics or programming at the hardware level, please stick to using the TS-Pico as described in this manual. Don't attempt to modify the hardware or reprogram the firmware unless you really know what you're doing. While we encourage experimentation and learning, it is possible to cause irreparable damage to the interface or even to your precious TS 2068 if things go wrong.

But don't worry - everything you need to use and enjoy your TS-Pico is covered in this manual, and it's all designed to be safe and straightforward.

---

## Installing the TS-Pico

### Before You Begin

Installation is straightforward, but let's take it step by step. The most important thing is to be gentle and patient. Your TS 2068 and TS-Pico are both vintage and modern electronics respectively, and they deserve to be treated with care.

### Safety First: Powering Down

**Always, always, always turn off your TS 2068 before connecting or disconnecting anything.** This isn't just a suggestion - it's essential for protecting both your computer and your new TS-Pico. Connecting or disconnecting electronics while they're powered on can cause damage to your TS 2068 that's expensive (or impossible) to repair.

Once your TS 2068 is turned off, take a moment to remove any cartridges that might be plugged into the computer. This eliminates any possibility of conflicts between the cartridge and the TS-Pico.

### Understanding Your TS-Pico Installation

The TS-Pico works with an expansion bus adapter that plugs into your TS 2068 first, then provides multiple slots for various devices including your TS-Pico. This design is ideal because it allows you to use multiple peripherals and gives you the flexibility to easily swap devices.

#### Installing Your TS-Pico with Expansion Bus
1. **Install the expansion bus** into your TS 2068's expansion port:
   - Locate the expansion connector on the right side of your TS 2068. It's the long, rectangular slot with small metal contacts inside.
   - Find the corresponding connector on your expansion bus. You'll notice it has a small notch or "key" - this isn't decorative, it's a safety feature to ensure you can't insert it backwards.
   - Line up the key on the expansion bus with the corresponding slot in your TS 2068's connector. This should feel natural and easy - if you're forcing anything, stop and check your alignment.
   - Gently but firmly press the expansion bus into the connector until it's fully seated. You should feel it slide in smoothly and then stop when it's properly connected.

2. **CRITICAL: Configure the BUSISO Bypass jumpers** on the expansion bus:
   - Locate the BUSISO Bypass jumpers on the right side of the expansion bus adapter
   - **The BUSISO Bypass jumper MUST be disconnected for the slot where you plan to install the TS-Pico**
   - **Recommended approach:** Disconnect ALL BUSISO Bypass jumpers to ensure proper operation regardless of which slot you use
   - **Failure to disconnect the BUSISO Bypass jumper for the TS-Pico slot will prevent the TS-Pico from functioning correctly**

3. **Choose an appropriate slot** on the expansion bus for your TS-Pico. Any slot will work, but many users prefer the first slot for easy access.

4. **Install the TS-Pico** into the chosen slot on the expansion bus, again using the key alignment to ensure proper orientation.

### After Installation

Once your TS-Pico is installed in the expansion bus, take a moment to check that everything looks right:
- The TS-Pico should be firmly seated with no wobbling
- All connectors should be fully engaged
- Nothing should look forced or crooked

If everything looks good, you're ready to power up and start exploring!

---

## Setting Up Your Micro SD Card

### Preparing a New Micro SD Card for Use

If you're using a brand new micro SD card with your TS-Pico, you'll need to prepare it properly before you can start using it. This is a one-time setup process that ensures your TS-Pico can find and access your TAP files correctly.

#### Why This Setup is Necessary

The TS-Pico expects to find your TAP files in a specific directory structure on your micro SD card. When you get a new micro SD card, it's usually either completely blank or formatted in a way that might not be compatible with the TS-Pico. Setting it up correctly ensures everything works smoothly from the start.

### Step 1: Format Your Micro SD Card

**Important:** Formatting will erase everything on the micro SD card. If you have important data on the card, back it up first!

#### Using Windows:
1. **Insert your micro SD card** into your computer (you may need a micro SD to SD adapter)
2. **Open File Explorer** and locate your micro SD card (it will appear as a new drive)
3. **Right-click on the micro SD card drive** and select "Format..."
4. **Choose these settings:**
   - **File system:** FAT32
   - **Allocation unit size:** Default
   - **Volume label:** You can name it "TS-PICO" or leave it blank
5. **Click "Start"** and confirm that you want to format the card
6. **Wait for formatting to complete** (this usually takes just a few seconds)

#### Using macOS:
1. **Insert your micro SD card** into your computer
2. **Open Disk Utility** (found in Applications > Utilities)
3. **Select your micro SD card** from the list on the left
4. **Click "Erase"** at the top of the window
5. **Choose these settings:**
   - **Name:** TS-PICO (or whatever you prefer)
   - **Format:** MS-DOS (FAT) - this is the same as FAT32
   - **Scheme:** Master Boot Record
6. **Click "Erase"** and confirm
7. **Wait for the process to complete**

#### Using Linux:
1. **Insert your micro SD card** and identify the device (usually /dev/sdb1 or similar)
2. **Open a terminal**
3. **Unmount the card first:** `sudo umount /dev/sdb1` (replace with your device)
4. **Format with FAT32:** `sudo mkfs.vfat -F 32 /dev/sdb1`
5. **Wait for formatting to complete**

### Step 2: Create the TAP Directory

Once your micro SD card is formatted, you need to create the directory where the TS-Pico will look for your TAP files.

#### Using Any Operating System:
1. **Open your file manager** and navigate to your micro SD card
2. **Create a new folder** called exactly `TAP` (all capital letters)
3. **Verify the folder was created** - you should see an empty TAP folder on your micro SD card

**Important naming notes:**
- The folder MUST be named "TAP" in all capital letters
- Don't use "tap", "Tap", or "TaP" - only "TAP" will work
- Make sure there are no extra spaces before or after the name

### Step 3: Test Your Setup

Now let's make sure everything is working correctly:

1. **Safely eject** your micro SD card from your computer
2. **Insert the micro SD card** into your TS-Pico
3. **Turn on your TS 2068** with the TS-Pico connected
4. **Type this command:** `LOAD "tpi:dir"`
5. **Press ENTER**

**What you should see:**
```
Path: /
File Name                    Size
```

**Success!** If you see the TAP directory listed, your micro SD card is properly set up and ready to use.

### Step 4: Organize Your TAP Directory (Optional)

You can organize your TAP files within the TAP directory using subdirectories. Here are some popular organization schemes:

#### Simple Organization:
```
TAP/
├── Games/
├── Utilities/
└── Personal/
```

#### Detailed Organization:
```
TAP/
├── Games/
│   ├── Action/
│   ├── Adventure/
│   ├── Puzzle/
│   └── Educational/
├── Utilities/
│   ├── Programming/
│   └── System/
└── Personal/
    └── MyPrograms/
```

**To create subdirectories:**
1. **Navigate into the TAP folder** on your computer
2. **Create new folders** with descriptive names
3. **Use the TS-Pico's `cd` command** to navigate between them

### Adding Your First TAP Files

Once your micro SD card is set up, you can start adding TAP files:

1. **Copy TAP files** from your computer into the TAP directory (or its subdirectories)
2. **Safely eject** the micro SD card from your computer
3. **Insert it** back into your TS-Pico
4. **Use `LOAD "tpi:dir"`** to see your files
5. **Use `LOAD "filename.tap"`** to mount a specific TAP file

### Troubleshooting Setup Issues

#### Problem: "No TAP directory found" error
**Solution:** Make sure you created a folder named exactly "TAP" (all capitals) in the root directory of your micro SD card.

#### Problem: TS-Pico doesn't recognize the micro SD card
**Solutions:**
- Verify the card is formatted as FAT32
- Try a different micro SD card to rule out hardware issues
- Check that the card is fully inserted into the TS-Pico

#### Problem: "Directory not found" when trying to access TAP files
**Solution:** Make sure your TAP files are inside the TAP directory, not in the root of the micro SD card.

### Best Practices for New Cards

- **Choose quality cards:** Invest in a reputable brand for reliability and longevity.
- **Don't overfill:** Keep at least 10% of the card's space free for optimal performance.
- **Regular backups:** Copy your TAP collection to your computer periodically as a backup.
- **Safe handling:** Micro SD cards are tiny and easy to lose - handle them carefully and store them safely.
- **Label your cards:** If you use multiple cards, label them clearly so you know what's on each one.

Once you've completed this setup process, your micro SD card is ready for years of TS-Pico enjoyment. You only need to do this setup once per card - after that, you can simply add and remove TAP files as needed using your computer.

---

## Getting Started: Your First Steps

### The Moment of Truth: First Power-On

Now comes the exciting part - seeing your TS-Pico in action for the first time. But before we jump in, let's set proper expectations so you know what to look for.

**Turn on your TS 2068** as you normally would. You should see the familiar startup sequence: the copyright messages will appear just as they always have, plus the TS-Pico copyright message. This is important - it means your TS 2068 is starting up normally and the TS-Pico has successfully initialized.

### Your First TS-Pico Command

Once you see the familiar "K" cursor, you're ready to say hello to your TS-Pico. Let's start with something simple that will prove everything is working:

Type exactly this:
```
LOAD "tpi:dir"
```

Then press **ENTER**.

**What just happened?** You've just asked your TS-Pico to show you what files are available on the SD card. The "tpi:" part tells your TS 2068 that this command is intended for the TS-Pico, not for a regular tape operation.

### Understanding What You See

Depending on what's on your SD card, you might see:
- A list of TAP files with numbers next to them
- Some folder names (these will be enclosed in angle brackets like `<foldername>`)
- File sizes shown in bytes or kilobytes
- A message about available space on your SD card

**Don't panic if you see an error message!** This is actually normal if:
- Your micro SD card is empty (it will say something like "no files found")
- Your micro SD card isn't inserted properly
- Your micro SD card needs to be formatted

We'll cover how to handle these situations in the troubleshooting section.

### If Everything Worked

Congratulations! You've just successfully communicated with your TS-Pico. That simple command proved that:
- Your TS-Pico is properly connected
- The firmware is running correctly
- Your TS 2068 can communicate with the TS-Pico
- Your SD card is accessible

### If You Got an Error

Don't worry - this is a learning process, and errors are part of learning. The most common issues at this stage are:
- **No micro SD card inserted:** Make sure your micro SD card is fully inserted into the TS-Pico
- **Micro SD card not formatted:** Some micro SD cards need to be formatted before use
- **Connection issue:** Double-check that your TS-Pico is fully seated in its connector

We'll cover all of these scenarios in detail in the troubleshooting section.

---



---

## Exploring the TS-Pico Hardware

### Getting to Know Your New Hardware

Before we dive deep into using your TS-Pico, let's take a tour of the hardware. Understanding what each part does will help you use the system more effectively and troubleshoot any issues that might arise.

### The Raspberry Pi Pico: The Brain of the Operation

The most prominent feature on your TS-Pico board is the Raspberry Pi Pico itself. This small green circuit board is actually a complete computer - far more powerful than your TS 2068, but designed to work as its helpful assistant.

#### The Status LED: Your Window into the TS-Pico's Mind

The Raspberry Pi Pico has a small LED that acts like a status indicator. Learning to read this LED will help you understand what your TS-Pico is doing at any given moment:

**Normal Operations:**
- **Slow, steady blinking (about once per second):** This is the "all is well" signal. Your TS-Pico is idle and ready to accept commands. Think of it as the TS-Pico saying "I'm here and ready to help!"
  
- **Solid ON (continuously lit):** The TS-Pico is busy processing a command or waiting for input from you. This is normal during file operations, directory scans, or when you're in the middle of a command sequence.

**Special Situations:**
- **Fast blinking (several times per second):** This usually indicates an error condition. The TS-Pico has encountered something it can't handle and is asking for attention.

- **Pattern blinking:** During special operations like firmware upgrades or file copying, you might see specific blinking patterns. These are covered in detail in the respective sections of this manual.

- **LED goes dark:** If the LED suddenly stops blinking entirely, it usually means the watchdog timer has activated. This is a safety feature that resets the TS-Pico if it gets confused or stuck.

#### Understanding the Watchdog Timer

The watchdog timer deserves special mention because it's one of the TS-Pico's most important safety features. Think of it as a helpful assistant who taps you on the shoulder if you've been staring at a problem too long.

If a command doesn't complete as expected, or if the TS-Pico gets confused by an unexpected situation, the watchdog timer will activate after several seconds. When this happens, you'll see the LED go dark, and then the TS-Pico will automatically reset its internal state and return to normal operation.

This is actually a good thing! It means that even if something goes wrong, your TS-Pico won't get permanently stuck. After a watchdog reset, you can simply try your command again or check if there was a problem with your input.

### The Control Buttons: Physical Control When You Need It

Your TS-Pico includes several pushbuttons that provide direct hardware control:

#### TS Reset Button
This button is your "emergency restart" for the TS 2068. When pressed, it pulls the RESET line on your computer's Z80 processor, causing a complete restart. You'll see the familiar three copyright messages appear, just as if you had turned the computer off and on again.

**When to use the TS Reset button:**
- When your TS 2068 seems frozen or unresponsive
- After installing new software that requires a restart
- When troubleshooting suggests a clean restart

**Important:** This button restarts your TS 2068, not just the TS-Pico. Any programs in memory will be lost unless you've saved them first.

#### Pico Reset and NMI Buttons
At the time this manual was written, these buttons are reserved for future functionality. The TS-Pico firmware doesn't currently use them, but future versions might add features that take advantage of these additional controls.

### The SD Card Slot: Your Gateway to Unlimited Storage

The micro SD card slot is where the magic happens. This tiny slot accepts standard micro SD cards and gives your TS 2068 access to virtually unlimited storage.

**Micro SD Card Best Practices:**
- **Use quality micro SD cards:** Cheap, no-name cards can be unreliable. Stick with reputable brands.
- **Format correctly:** Your micro SD card should be formatted as FAT32 for best compatibility.
- **Safe removal:** Always use the `SAVE "tpi:close"` command before removing your micro SD card.
- **Handle with care:** Micro SD cards are very small and can be easily damaged. Store them safely when not in use.

### Power and Connectivity

Your TS-Pico draws its power directly from your TS 2068 through the expansion connector. There are no external power supplies or batteries to worry about. When your TS 2068 is on, your TS-Pico is on. When your TS 2068 is off, your TS-Pico is off. Simple!

The TS-Pico also includes a micro-USB connector, but this is only used for firmware upgrades. During normal operation, you won't need to connect anything to this port.

---

## Understanding the TS-Pico Commands

### The Philosophy Behind TS-Pico Commands

Before we dive into specific commands, it's important to understand the philosophy behind how the TS-Pico works. The designers wanted to make the TS-Pico feel natural to anyone familiar with the TS 2068, while adding powerful new capabilities.

### The Magic of "tpi:" - Your Gateway to Modern Features

Every TS-Pico command starts with "tpi:" - this is your signal to the system that you want to talk to the TS-Pico rather than perform a traditional tape operation. Think of "tpi:" as a polite way of saying "Excuse me, TS-Pico, I have a request for you."

**Why "tpi:"?** It stands for "Timex Pico Interface" and it serves an important technical purpose: it tells your TS 2068 to pass the command to the TS-Pico instead of trying to access a tape drive. This allows the TS-Pico to add new functionality without interfering with your computer's existing capabilities.

### LOAD vs. SAVE: Two Different Types of Conversations

The TS-Pico uses your TS 2068's existing LOAD and SAVE commands, but extends them in clever ways:

#### LOAD Commands: "Show Me" or "Get Me"
LOAD commands are typically used for retrieving information or bringing files into your computer's memory. When you use a LOAD command with "tpi:", you're usually asking the TS-Pico to either show you something or to load a file for use.

**Examples of LOAD commands:**
- `LOAD "tpi:dir"` - "Show me what files are available"
- `LOAD "tpi:path"` - "Show me which directory I'm currently in"
- `LOAD "program.tap"` - "Load this specific program into memory"

#### SAVE Commands: "Do This" or "Change That"
SAVE commands are used for actions that change something or perform an operation. When you use a SAVE command with "tpi:", you're usually asking the TS-Pico to change a setting, perform an action, or modify something.

**Examples of SAVE commands:**
- `SAVE "tpi:cd Games"` - "Change to the Games directory"
- `SAVE "tpi:close"` - "Close the currently open file"
- `SAVE "tpi:getinfo"` - "Show me detailed system information"

### Storage Mode Commands: Switching Between Tape and SD Card

The TS-Pico operates in one of two storage modes, and you can switch between them as needed:

#### SD Card Mode (Default)
```
SAVE "tpi:sdcard"
```
This is the normal TS-Pico operating mode where:
- All TS-Pico commands and features are available
- TAP files are accessed from the micro SD card
- Fast loading and saving operations
- Directory navigation and file management work normally
- **LPRINT, LLIST, and COPY commands are NOT available**

#### Tape Mode
```
SAVE "tpi:tape"
```
This switches the system to use the traditional cassette tape interface where:
- **All TS-Pico commands are disabled** (except switching back to SD mode)
- LOAD and SAVE operations go to the physical cassette ports (EAR/MIC)
- **LPRINT, LLIST, and COPY commands become available** for use with TS 2040 printer
- You can load from physical tapes or save to physical tapes
- No access to TAP files or SD card operations

### TPMODE System Variable

The current storage mode is controlled by a system variable called TPMODE located at memory address 5DDBh (23899 decimal). You can read this variable in your programs:

```
PRINT PEEK 23899
```

**TPMODE Values:**
- **0:** Tape mode (set by `SAVE "tpi:tape"`)
- **1:** SD card mode (set by `SAVE "tpi:sdcard"`)

This allows your programs to detect which mode the system is in and behave accordingly.

### The Comfort of Familiarity

Here's one of the most beautiful things about the TS-Pico: once you mount a TAP file (more on this shortly), your regular LOAD and SAVE commands work exactly as they always have. You don't need to learn a completely new way of working. Your TS 2068 will load and save programs just like it always did, but faster and more reliably than ever before.

### Building Your Command Vocabulary

Think of learning TS-Pico commands like learning a new language - start with the basics and gradually expand your vocabulary. You don't need to memorize every command right away. In fact, there's a built-in help system (we'll cover this soon) that can remind you of any command you forget.

**Start with these essential commands:**
1. `LOAD "tpi:dir"` - See what files are available
2. `SAVE "tpi:gethelp"` - Get help with commands
3. `SAVE "tpi:getinfo"` - Check system status
4. `SAVE "tpi:close"` - Close files when done

Master these four commands, and you'll be well on your way to TS-Pico proficiency.

---

## Basic File Operations - Your Daily Toolkit

### Understanding TAP Files: Your Digital Tape Collection

Before we dive into specific operations, let's talk about TAP files. If you're familiar with cassette tapes for your TS 2068, TAP files are the digital equivalent. Each TAP file can contain multiple programs, just like a physical tape might have several programs recorded on it.

The beauty of TAP files is that they load much faster than physical tapes, they never wear out, and you can easily organize them into folders on your SD card. Think of your micro SD card as a vast library, with each TAP file being like a book that contains multiple chapters (programs).

### DIR: Your Window into Available Files

The directory command is probably the one you'll use most often. It's your way of asking, "What do I have to work with?"

```
LOAD "tpi:dir"
```

**What happens when you run this command:**
1. The TS-Pico scans your current directory on the micro SD card
2. It counts up all the files and folders
3. It presents them in an organized list with helpful information

#### Reading the Directory Display

Let's break down what you see in a typical directory listing:

```
Path: /Games/Adventure
File Name                    Size
<Action>                     0 b
<RPG>                        0 b
001 zork.tap                 48.07 Kb
002 adventure.tap            32.15 Kb
003 planetfall.tap           45.23 Kb
Press N to stop:
```

**What each part means:**
- **Path:** Shows exactly where you are in your directory structure
- **Angle brackets `< >`:** Indicate subdirectories (folders)
- **Numbers (001, 002, etc.):** Index numbers for quick file access
- **File names:** The actual names of your TAP files
- **Size:** How much space each file takes up
- **"Press N to stop":** Appears if there are more than 20 items

#### Pro Tips for Directory Navigation
- **Take your time:** Don't rush through directory listings. The information is there to help you find what you're looking for.
- **Note the index numbers:** These numbers are shortcuts for quick file access (we'll cover this soon).
- **Scroll through long listings:** If you see "Press N to stop," press any key except 'N' to see more files.

### PATH: Knowing Where You Are

Sometimes, especially when you've been navigating through multiple folders, you might forget exactly where you are. The path command is like asking for directions:

```
LOAD "tpi:path"
```

This simple command shows you your current location in the directory structure. For example, you might see:
```
Current path: /Games/Adventure/Text-Based
```

This tells you that you're in the "Text-Based" folder, which is inside the "Adventure" folder, which is inside the "Games" folder at the root of your SD card.

### Quick File Access: The Power of Index Numbers

Remember those index numbers you saw in the directory listing? Here's where they become incredibly useful. Instead of typing out a long filename, you can use these numbers as shortcuts:

```
LOAD "tpi:&001"
```

This command tells the TS-Pico, "Load whatever file is number 001 in the current directory." It's much faster than typing `LOAD "some-long-filename.tap"`, especially for files with complicated names.

**When to use index numbers:**
- Files with long or complex names
- When you want to quickly try several files in sequence
- When you're not sure of the exact spelling of a filename

### Mounting Files: Making Them Ready to Use

When you use the quick access command or load a file by name, you're "mounting" it. Think of mounting like putting a cassette tape into your tape player - you're getting it ready to use, but you haven't actually loaded any programs yet.

```
LOAD "adventure.tap"
```

**What mounting accomplishes:**
- Makes the TAP file active and ready for use
- Sets up the internal pointers so LOAD and SAVE commands work
- Prepares the file for TAPDIR examination (covered next)

**Important:** You can only have one TAP file mounted at a time. If you want to switch to a different TAP file, you'll need to close the current one first.

### TAPDIR: Exploring What's Inside a TAP File

Once you have a TAP file mounted, you can explore its contents:

```
LOAD "tpi:tapdir"
```

This is like looking at the table of contents of a book or the track listing on an album. You'll see something like:

```
File: /sd/TAP/adventure.tap
Pointer now on block: 02
Block  Offset   Len  Type    Name
-----------------------------------
00     0        19   00     adventure
>01    33       8253 FF     /
02     8309     19   00     map
03     8351     2048 FF     /
04     10421    19   00     help
05     10463    1024 FF     /
```

**Understanding the TAPDIR display:**
- **Pointer (>):** Shows which block will be loaded next
- **Block numbers:** Sequential numbering of each section
- **Type 00:** These are header blocks containing program information
- **Type FF:** These are data blocks containing the actual program code
- **Names:** The names of individual programs within the TAP file

#### Why TAPDIR Matters

Understanding TAPDIR is crucial because it helps you:
- See what programs are available in a TAP file
- Navigate to specific programs (covered in the next section)
- Understand the structure of your TAP files
- Troubleshoot loading problems

---

## Directory Navigation - Organizing Your Files

### The Importance of Good Organization

Just as you might organize your physical cassette tapes into categories (games, utilities, programming tools), organizing your TAP files into directories makes everything easier to find and manage. The TS-Pico supports unlimited subdirectories, so you can create an organization system that makes sense for your collection.

### CD: Changing Directories

The Change Directory command is your tool for navigating through your folder structure:

```
SAVE "tpi:cd foldername"
```

**Basic navigation examples:**
```
SAVE "tpi:cd Games"          # Go into the Games folder
SAVE "tpi:cd Adventure"      # Go into the Adventure subfolder
SAVE "tpi:cd .."             # Go back up one level
SAVE "tpi:cd /"              # Go to the root directory
```

#### Understanding Directory Paths

Think of directories like a filing cabinet with folders and subfolders:
- **Root directory (/):** The top level of your SD card
- **Subdirectories:** Folders within other folders
- **Parent directory (..):** The folder that contains your current folder

**Example directory structure:**
```
/ (root)
├── Games/
│   ├── Action/
│   ├── Adventure/
│   └── Puzzle/
├── Utilities/
│   ├── Programming/
│   └── System/
└── Personal/
    └── MyPrograms/
```

#### Navigation Best Practices

**Start simple:** When you're learning, stick to one or two levels of directories. You can always reorganize later as you become more comfortable.

**Use descriptive names:** Choose folder names that clearly indicate what's inside. "Games" is better than "Stuff" or "Misc."

**Be consistent:** If you use "Adventure" for one type of game, don't use "Adventures" elsewhere. Consistency makes navigation much easier.

**Plan ahead:** Think about how you'll organize your files before you start creating lots of directories. It's easier to start with good organization than to reorganize later.

### MD: Making New Directories

Creating new directories is straightforward:

```
SAVE "tpi:md NewFolderName"
```

**Planning your directory structure:**
Before creating directories, consider:
- What types of files you'll store
- How you typically think about organizing things
- Whether you'll have enough files to justify subdirectories

**Example organization strategies:**
- **By type:** Games, Utilities, Programming, Personal
- **By genre:** Action, Adventure, Puzzle, Educational
- **By source:** Magazine Programs, Downloaded, Personal Projects
- **By frequency:** Daily Use, Archive, Work in Progress

### RM: Removing Directories

You can remove empty directories with:

```
SAVE "tpi:rm foldername"
```

**Important limitations:**
- The directory must be completely empty
- You cannot remove the current directory (you must navigate out first)
- You cannot remove the root directory

**Safe directory removal process:**
1. Navigate into the directory you want to remove
2. Use `LOAD "tpi:dir"` to confirm it's empty
3. Navigate out with `SAVE "tpi:cd .."`
4. Remove the directory with `SAVE "tpi:rm foldername"`

### Directory Navigation Tips for New Users

**Don't get lost:** If you're unsure where you are, use `LOAD "tpi:path"` to check your location.

**Keep it simple at first:** Start with just a few main directories and add subdirectories as needed.

**Use the root as home base:** When in doubt, navigate back to the root directory with `SAVE "tpi:cd /"` and start over.

**Practice with test directories:** Create some test directories to practice navigation before organizing your real files.

---

## Working with TAP Files - The Heart of the System

### Understanding TAP File Operations

TAP files are the core of the TS-Pico experience. Think of each TAP file as a digital cassette tape that can contain multiple programs. Unlike physical tapes, TAP files load instantly, never wear out, and can be easily copied and organized.

### The TAP File Lifecycle

Every TAP file goes through a simple lifecycle in the TS-Pico:
1. **Selection:** You choose which TAP file to work with
2. **Mounting:** The TS-Pico makes the file active and ready to use
3. **Navigation:** You can move around within the TAP file to find specific programs
4. **Usage:** You load and save programs using standard TS 2068 commands
5. **Closing:** You properly close the file when done

### Mounting TAP Files: Three Ways to Get Started

#### Method 1: Direct Loading by Name
```
LOAD "filename.tap"
```
This is the most straightforward method. If you know the exact name of the TAP file you want, just load it directly. Remember to include the ".tap" extension.

#### Method 2: Quick Access by Index Number
```
LOAD "tpi:&005"
```
Use the index number from a directory listing. This is perfect when you can see the file in a directory but don't want to type out a long filename.

#### Method 3: Navigate and Load
```
SAVE "tpi:cd Games"
LOAD "tpi:dir"
LOAD "tpi:&001"
```
This approach lets you navigate to the right directory first, see what's available, then load the file you want.

### FFW and REW: Moving Around Inside TAP Files

Once you have a TAP file mounted, you can navigate within it using Fast Forward and Rewind commands. This is like fast-forwarding or rewinding a cassette tape to find a specific program.

#### Basic Movement
```
SAVE "tpi:ffw"    # Move forward one block
SAVE "tpi:rew"    # Move backward one block
```

#### Precise Movement
```
SAVE "tpi:ffw" CODE 5,0    # Move forward 5 blocks
SAVE "tpi:rew" CODE 3,0    # Move backward 3 blocks
```

#### Understanding Block Navigation

Remember the TAPDIR output we saw earlier? Each program in a TAP file typically consists of two blocks:
- **Header block (Type 00):** Contains program information and name
- **Data block (Type FF):** Contains the actual program code

**Important rule:** Your TS 2068 expects to start loading from a header block. If you navigate to a data block and try to load, you'll likely get an error.

#### Smart Navigation Strategy

1. **Use TAPDIR first:** Always check `LOAD "tpi:tapdir"` to see what's in your TAP file
2. **Navigate to headers:** Use FFW/REW to position on header blocks (Type 00)
3. **Load from headers:** Start your LOAD commands from header blocks for best results

**Example navigation session:**
```
LOAD "games.tap"           # Mount the TAP file
LOAD "tpi:tapdir"          # See what's inside
SAVE "tpi:ffw" CODE 4,0    # Skip ahead to block 4
LOAD ""                    # Load the program at block 4
```

### Working with Large TAP Files

Some TAP files contain dozens of programs. Here are strategies for managing them effectively:

#### Use TAPDIR as Your Map
Always start with `LOAD "tpi:tapdir"` to get oriented. Note the block numbers of programs you're interested in.

#### Navigate Efficiently
Instead of moving one block at a time, calculate how many blocks you need to skip and use the CODE parameter:
```
SAVE "tpi:ffw" CODE 12,0   # Jump ahead 12 blocks at once
```

#### Keep Notes
For TAP files you use frequently, consider keeping a simple note of which block numbers contain your favorite programs.

### CLOSE: Proper TAP File Management

When you're done with a TAP file, always close it properly:

```
SAVE "tpi:close"
```

**Why closing matters:**
- **File safety:** Ensures all data is properly saved and file handles are released
- **Memory management:** Frees up system resources for the next operation
- **SD card safety:** Prepares the system for safe SD card removal
- **Clean state:** Ensures the next TAP file starts with a clean slate

**When to close TAP files:**
- Before mounting a different TAP file
- Before removing your SD card
- When you're done working for the day
- If you encounter errors and want to start fresh

### Advanced TAP File Tips

#### Append Mode
```
SAVE "tpi:append"
```
This command enables append mode, which allows you to add new programs to the currently mounted TAP file instead of creating new files.

#### Switching to Physical Tape
```
SAVE "tpi:tape"
```
This command switches your LOAD/SAVE commands to the physical cassette interface. This also enables LPRINT, LLIST, and COPY commands for use with a TS 2040 printer. Note that all TS-Pico commands become unavailable in tape mode.

To switch back to the TS-Pico:
```
SAVE "tpi:sdcard"
```

---

## Advanced System Commands

### Getting Help When You Need It

The TS-Pico includes a comprehensive built-in help system. Instead of reaching for this manual every time you forget a command, you can get instant help right on your screen.

#### The Built-in Help System
```
SAVE "tpi:gethelp"
```

This command displays a complete list of all available LOAD and SAVE commands with their syntax. It's like having a condensed version of this manual always available. The output is organized by category and includes brief descriptions of what each command does.

**Pro tip:** Use the help command when you're learning new features or when you can't quite remember the exact syntax for a command you don't use often.

### System Information and Diagnostics

#### Comprehensive System Status
```
SAVE "tpi:getinfo"
```

This command is like asking your TS-Pico, "How are you doing, and what's your current status?" The response includes:

- **Firmware version:** What version of TS-Pico software you're running
- **ROM version:** The version of your TS 2068's operating system
- **Board revision:** Hardware version information
- **Memory usage:** How much Flash and SRAM is being used
- **SD card status:** Information about your SD card
- **Current file:** What TAP file is currently mounted, if any
- **Configuration settings:** Various system settings and their current values
- **Storage mode:** Whether you're in tape mode or SD card mode

**When to use getinfo:**
- When troubleshooting problems
- Before performing major operations like upgrades
- When checking if upgrades were successful
- When documenting your system configuration

#### Activity Logging
```
SAVE "tpi:getlog"
```

The TS-Pico keeps a detailed log of everything it does. This log includes timestamps and can be invaluable for troubleshooting problems or understanding what happened during a session.

**Viewing specific amounts of log data:**
```
SAVE "tpi:getlog" CODE 500,0    # Show last 500 bytes of log
SAVE "tpi:getlog" CODE 0,0      # Show entire log
```

**Understanding log levels:**
- **INFO (0):** Normal operational information
- **WARNING (1):** Non-critical issues that you should be aware of
- **ERROR (2):** Error conditions that prevented something from working
- **CRITICAL (3):** Serious problems that require immediate attention

#### Verbose Mode
```
SAVE "tpi:verbose"
```

This toggle switch enables or disables detailed status messages for commands. When verbose mode is on, the TS-Pico provides much more detailed feedback about what it's doing.

**When to enable verbose mode:**
- When learning the system
- When troubleshooting problems
- When you want to understand exactly what's happening behind the scenes
- When documenting procedures for others

**When to disable verbose mode:**
- When you're comfortable with the system and don't need extra feedback
- When you want cleaner, less cluttered output
- When running automated scripts or procedures

## Understanding Cartridge Compatibility

Your TS 2068 actually has two different types of connectors, and understanding how they work together with your TS-Pico is important for getting the best experience:

#### Expansion Connector (Back of Computer)

This is the long rectangular connector on the back of your TS 2068 where your TS-Pico's expansion card plugs in. This connector is designed for peripherals like the TS-Pico, disk drives, and other system expansions.

#### Cartridge Connector (Front of Computer)

This is the connector under the cartridge door on the front of your TS 2068, officially called the "DOCK" connector. This is where you would normally plug in game cartridges and certain software cartridges.

### Physical vs. Logical Compatibility

Here's something that might seem confusing at first: **physically, cartridges and the TS-Pico don't interfere with each other.** You can have a cartridge plugged into the front connector and the TS-Pico plugged into the back connector at the same time without any physical problems.

**However, having a cartridge plugged in will interfere with the TS-Pico's operation** due to how your TS 2068's ROM (the computer's built-in software) works.

### Why Cartridges Interfere with TS-Pico Operation

#### The Boot Sequence Problem

When you turn on your TS 2068, it goes through an initialization sequence that includes checking for a cartridge in the cartridge slot. If it finds an "auto boot" cartridge (like most games or certain software), the computer immediately hands over control to that cartridge and runs it. This bypasses the rest of the normal startup sequence.

#### How the TS-Pico ROM Works

The TS-Pico includes a modified version of the TS 2068's ROM that contains the same initialization sequence as the original. However, since the Raspberry Pi Pico needs a few seconds to boot up when you first turn on power, the TS-Pico holds your TS 2068 in a RESET state during this time.

#### The Timing Issue

Here's where the problem occurs: when the TS-Pico releases the RESET and your TS 2068 starts its initialization sequence, if there's a cartridge plugged in, the TS-Pico version of the TS 2068 ROM will hand control to that cartridge. This effectively bypasses the TS-Pico, and you won't be able to use any TS-Pico commands.

### The Digital Cartridge Solution

The good news is that **physical cartridges are not necessary when using the TS-Pico!** Instead, you can load cartridge ROM images digitally and run them through the TS-Pico system.

#### How Digital Cartridges Work

1. **Load the cartridge ROM image** into the TS-Pico's Flash memory or static RAM
2. **Configure the system** to use that cartridge image with the appropriate commands
3. **Restart your TS 2068** to activate the cartridge image

This approach gives you several advantages:

- **No physical cartridges to lose or damage**
- **Instant switching** between different cartridge images
- **Perfect preservation** of cartridge software
- **Full compatibility** with TS-Pico features

#### Loading Cartridge Images

**[CALLOUT NOTE TO RICARDO/DAVID: Please provide detailed instructions for the cartridge loading process, including specific commands, file preparation, and step-by-step procedures for loading cartridge ROMs into Flash/SRAM and configuring them with memboot/memdock commands.]**

### Cartridge Compatibility

#### What Works Well

The TS-Pico is compatible with **almost all cartridge images**, including:

- Commercial game cartridges
- Educational software cartridges
- Utility and programming cartridges
- Most homebrew and community-developed cartridges

#### Important Exception: Custom ROM Cartridges

There is one important category of cartridges that have limitations with the TS-Pico: **cartridges that contain their own custom version of the TS 2068 ROM**.

**Example: Zebra Systems OS-64**
The Zebra Systems OS-64 cartridge contains its own custom ROM that provides 64-column text display and other enhancements. Because it includes a complete custom ROM (just like the TS-Pico does), there are compatibility limitations:

- **OS-64 can be used** with the TS-Pico as a digital cartridge image
- **TS-Pico commands will not work** while in OS-64's 64-column mode

This limitation exists because both the TS-Pico and OS-64 need to control the computer's ROM space, and they can't both do it at the same time. Unfortunately, there's not enough free space in the OS-64 ROM to implement the TS-Pico commands.

### Best Practices for Cartridge Use

#### Recommended Approach

- **Remove physical cartridges** when using the TS-Pico to avoid any potential conflicts or confusion.
- **Use digital cartridge images** instead of physical cartridges for the best experience.
- **Keep your physical cartridges safe** for preservation purposes, but rely on digital images for day-to-day use.

#### When You Need Physical Cartridges

If you need to use a physical cartridge for some reason:

1. **Power down** your TS 2068 completely
2. **Remove the TS-Pico** from the expansion connector
3. **Install your cartridge** and use it normally
4. **When done**, power down, remove the cartridge, and reinstall the TS-Pico

#### Organizing Cartridge Images

Treat cartridge images like any other files in your TS-Pico collection:

- **Store them in organized directories** on your micro SD card
- **Use descriptive filenames** to identify what each cartridge contains
- **Document any special loading procedures** for complex cartridges

### Understanding the Technical Details

#### Memory Management

Cartridge images are loaded into either:

- **Flash memory:** For permanent storage and quick access
- **Static RAM:** For temporary use or frequently changed cartridges

The choice depends on your specific needs and usage patterns.

#### Boot Configuration Commands

The TS-Pico provides specific commands for managing cartridge images:

- **`tpi:memboot`:** Configures which memory slot contains the boot ROM
- **`tpi:memdock`:** Configures which memory slot contains the cartridge image

These commands give you precise control over how your system starts up and which cartridge image is active.

### Troubleshooting Cartridge Issues

#### Problem: TS-Pico commands don't work after startup

**Likely cause:** Physical cartridge is installed and taking control
**Solution:** Remove physical cartridge and restart

#### Problem: Digital cartridge image doesn't load

**Possible causes:**

- Cartridge image file is corrupted
- Memory slot configuration is incorrect
- Insufficient memory space for the cartridge image

#### Problem: Some cartridge features don't work

**Possible causes:**

- Cartridge requires specific hardware that's not emulated
- Cartridge has custom ROM that conflicts with TS-Pico
- File format compatibility issues

Understanding the relationship between physical cartridges and the TS-Pico helps you make the most of both your vintage cartridge collection and the modern convenience of the TS-Pico system.

## Memory and Flash Management

### Understanding TS-Pico Memory Architecture

Your TS-Pico has several different types of memory, each with its own purpose. Understanding these can help you make better use of your system and troubleshoot issues more effectively.

#### Flash Memory (512KB)
This is permanent storage that retains its contents even when power is off. Think of it like a hard drive - it's where the TS-Pico stores:
- The firmware (operating system)
- Cached TAP files for faster access
- System configuration data
- User data that needs to persist between sessions

#### SRAM (512KB)
This is high-speed temporary storage that's available to you. Unlike Flash memory, SRAM loses its contents when power is turned off, but it's much faster to access. The TS-Pico uses SRAM for:
- Temporary file operations
- Fast caching of frequently accessed data
- Buffer space for large operations

#### SD Card Storage
This is your unlimited external storage. While not as fast as the internal memory, SD cards can hold thousands of TAP files and provide easy file transfer between your TS-Pico and modern computers.

### Advanced Memory Commands

**⚠️ Warning:** The commands in this section are for advanced users who understand memory management. Incorrect use can cause system instability or data loss. If you're new to the TS-Pico, stick to the basic commands until you're more comfortable with the system.

#### Configuring Boot Memory
```
SAVE "tpi:memboot" CODE mem,page
```

This command configures which memory slot contains the boot ROM. This is primarily used for:
- Advanced system customization
- Testing alternative firmware configurations
- Development and debugging

**Parameters:**
- `mem`: Memory type (1=Flash, 2=SRAM)
- `page`: Slot number (0-15)

**Example:**
```
SAVE "tpi:memboot" CODE 1,0    # Set boot ROM to Flash memory, slot 0
```

#### Configuring Cartridge Memory
```
SAVE "tpi:memdock" CODE mem,page
```

This command configures which memory slot contains cartridge images (DCK files). Useful for:
- Running cartridge software from Flash memory
- Testing different cartridge configurations
- Advanced system setups

#### Direct Memory Operations
```
SAVE "tpi:blkrcv" CODE length,offset
```

This low-level command receives data blocks and writes them to memory. It's primarily used internally by the system but can also be used for:
- Advanced file operations
- Custom data transfer operations
- Development and testing

**Parameters:**
- `length`: Number of bytes to transfer (0 = entire file)
- `offset`: Starting position in the file

### Memory Best Practices

#### For Regular Users
- **Don't modify memory settings** unless you have a specific need and understand the consequences
- **Monitor memory usage** with `SAVE "tpi:getinfo"` to ensure you're not running low on space
- **Keep your SD card organized** to make the most efficient use of caching

#### For Advanced Users
- **Back up your configuration** before making memory changes
- **Test changes carefully** in a safe environment
- **Document your modifications** so you can reverse them if needed
- **Monitor system logs** for memory-related errors or warnings

---



---

## Traditional LOAD and SAVE Operations

### The Beauty of Backward Compatibility

One of the most elegant aspects of the TS-Pico is how it preserves the familiar LOAD and SAVE commands you already know. Once you have a TAP file mounted, your TS 2068 behaves exactly as it always has - but faster and more reliably than ever before.

### Loading Programs the Familiar Way

Once you have a TAP file mounted, loading programs works exactly as you remember:

#### Loading the Next Program
```
LOAD ""
```
This loads the next program in the TAP file, starting from wherever the pointer is currently positioned. It's exactly like pressing play on a cassette tape.

#### Loading a Specific Program
```
LOAD "program_name"
```
This searches through the TAP file for a program with the specified name and loads it. Just like searching for a specific program on a cassette tape, but much faster.

#### Loading with Memory Specifications
```
LOAD "program_name" CODE 65000,255
```
This loads a program into a specific memory location. Advanced users can use this for custom memory management or loading machine code programs.

### Advanced Loading Commands: VERIFY and MERGE

The TS-Pico fully supports the traditional TS 2068 VERIFY and MERGE commands, giving you powerful tools for program management and verification.

#### VERIFY: Ensuring Data Integrity

The VERIFY command compares a program on your TAP file with what's currently in memory, ensuring data integrity without actually loading anything.

```
VERIFY ""
VERIFY "program_name"
```

**How VERIFY works with TAP files:**
1. **Mount your TAP file** containing the program you want to verify
2. **Load the program** into memory first using standard LOAD commands
3. **Use VERIFY** to compare the TAP file version with the memory version
4. **Check the result** - you'll get "0 OK" if they match, or an error code if they don't

**When to use VERIFY:**
- **After loading important programs** to ensure they loaded correctly
- **Before saving modified programs** to confirm what's in memory
- **When diagnosing loading problems** to isolate issues
- **For data integrity checking** of critical software

**Example verification workflow:**
```
LOAD "game.tap"              # Mount the TAP file
LOAD "adventure"             # Load the adventure program
RUN                          # Play the game, make progress
VERIFY "adventure"           # Verify the original is still on tape
SAVE "adventure_save"        # Save your progress if verified OK
```

#### MERGE: Combining Programs Creatively

MERGE loads a program from a TAP file but combines it with what's already in memory, rather than replacing it completely.

```
MERGE ""
MERGE "program_name"
```

**How MERGE differs from LOAD:**
- **LOAD clears memory** before loading the new program
- **MERGE preserves existing content** and adds to it
- **Line number conflicts** are resolved by the new program taking precedence
- **Variables and data** from the existing program may be preserved

**Creative uses for MERGE:**
- **Combining utilities** with your main program
- **Adding subroutines** from a library to your current project
- **Loading additional levels** or content into games
- **Building complex programs** from multiple smaller components

**MERGE best practices:**
- **Plan your line numbers** to avoid conflicts
- **Test thoroughly** as MERGE can have unexpected results
- **Use consistent variable names** across programs you plan to merge
- **Keep backup copies** before experimenting with MERGE

**Example MERGE workflow:**
```
LOAD "utilities.tap"         # Mount utility collection
LOAD "graphics"              # Load graphics routines (lines 8000-8999)
SAVE "tpi:close"            # Close utilities TAP
LOAD "myproject.tap"         # Mount your project
MERGE "main"                 # Merge main program (lines 1000-7999)
# Now you have both graphics utilities and main program in memory
LIST                         # Check the combined program
SAVE "combined_project"      # Save the merged result
```

### Saving Programs

Saving works just as you remember, but with modern conveniences:

#### Basic Program Saving
```
SAVE "my_program"
```
This saves the current program in memory. The behavior depends on your current TS-Pico configuration:
- **If no TAP file is mounted:** Creates a new TAP file with this name
- **If a TAP file is mounted and append mode is off:** Creates a new TAP file
- **If a TAP file is mounted and append mode is on:** Adds to the current TAP file

#### Saving with Auto-start
```
SAVE "my_program" LINE 10
```
This saves the program with an automatic start line, so it will begin running immediately when loaded.

#### Saving Machine Code
```
SAVE "my_code" CODE 32768,1024
```
This saves a specific block of memory, useful for machine code programs or data.

### Creating and Managing New TAP Files

Understanding how to create and manage TAP files gives you complete control over your software collection.

#### Creating Brand New TAP Files

**Method 1: Direct Creation**
When no TAP file is currently mounted, any SAVE command creates a new TAP file:
```
SAVE "tpi:close"             # Ensure no TAP file is mounted
SAVE "my_new_collection"     # Creates "my_new_collection.tap"
```

**Method 2: Planned Creation**
Create an empty TAP file and then build it up:
```
SAVE "tpi:close"             # Start fresh
SAVE "empty_file"            # Creates the TAP file
LOAD "empty_file.tap"        # Mount it
SAVE "tpi:append"            # Enable append mode
# Now save multiple programs to build your collection
```

#### Understanding Append Mode

Append mode is a powerful feature that controls how the TS-Pico handles SAVE operations when a TAP file is mounted.

**Enable append mode:**
```
SAVE "tpi:append"
```

**How append mode works:**
- **When OFF (default):** SAVE commands create new TAP files
- **When ON:** SAVE commands add to the currently mounted TAP file
- **Persistent:** Append mode stays on until explicitly changed or system restart

**Append mode best practices:**

**Building a software collection:**
```
LOAD "utilities.tap"         # Mount your collection
SAVE "tpi:append"            # Enable append mode
# Load and save multiple programs
LOAD "calculator"            # From somewhere else
SAVE "calc_v2"              # Adds to utilities.tap
LOAD "text_editor"           # From another source  
SAVE "editor_v1"            # Also adds to utilities.tap
```

**When to use append mode:**
- **Building themed collections** (games, utilities, etc.)
- **Consolidating scattered programs** into organized TAP files
- **Adding new versions** of programs to existing collections
- **Creating backup collections** with multiple programs

**When NOT to use append mode:**
- **When creating standalone programs** that should be in separate files
- **When working with very large programs** that should have dedicated TAP files
- **When you're unsure** - it's safer to create separate files and combine later

#### Managing TAP File Size and Organization

**Optimal TAP file sizes:**
- **Small collections:** 10-50 programs per TAP file for easy browsing
- **Themed collections:** Group related programs regardless of count
- **Large programs:** Give complex programs their own TAP files
- **Micro SD card limits:** Keep individual TAP files under 1MB for best performance

### The Loading Process: What's Really Happening

When you type `LOAD ""` with a mounted TAP file, here's what happens behind the scenes:

1. **The TS-Pico receives the command** through the interface
2. **It reads the next block** from the mounted TAP file
3. **It sends the data** to your TS 2068 just as if it were coming from a cassette tape
4. **Your TS 2068 processes the data** exactly as it always has
5. **The program loads into memory** at normal speed or faster

This process is transparent to your TS 2068 - as far as it knows, it's loading from a very fast, very reliable cassette tape.

### Error Handling and Recovery

Sometimes things don't go as expected. Here's how to handle common loading issues:

#### "Program not found" errors
If you get an error saying a program wasn't found:
1. Check the spelling of the program name
2. Use `LOAD "tpi:tapdir"` to see exactly what programs are available
3. Make sure you're positioned correctly in the TAP file

#### Loading the wrong program
If you accidentally load the wrong program:
1. The previous program is gone from memory (this is normal)
2. Use FFW/REW commands to navigate to the program you actually wanted
3. Load the correct program

#### Corrupted loads
If a program loads but behaves strangely:
1. Try loading it again - sometimes temporary issues cause problems
2. Check the TAP file on a computer to verify it's not corrupted
3. Try loading from a different position in the TAP file

#### VERIFY failures
If VERIFY reports mismatches:
1. Check if the program in memory has been modified
2. Verify you're comparing the right program versions
3. Consider if the TAP file might be corrupted
4. Try loading fresh and verifying immediately

### Mixing Modern and Traditional Commands

You can freely mix TS-Pico commands with traditional LOAD/SAVE operations:

```
LOAD "tpi:dir"              # See what's available
LOAD "games.tap"            # Mount a TAP file
LOAD "tpi:tapdir"           # See what's in the TAP file
SAVE "tpi:ffw" CODE 4,0     # Skip to program 4
LOAD ""                     # Load program 4 traditionally
SAVE "my_highscore"         # Save your progress traditionally
VERIFY "my_highscore"       # Verify it saved correctly
SAVE "tpi:close"            # Close the TAP file (TS-Pico command)
```

This flexibility means you can use as much or as little of the TS-Pico's advanced features as you're comfortable with.

---

## File Naming and Organization Standards

### Avoiding Compatibility Problems

Proper file naming and organization prevents problems and ensures your TS-Pico collection works reliably across different systems and situations. Understanding these standards helps you avoid frustrating compatibility issues.

### Character Restrictions and Limitations

#### Forbidden Characters in Filenames

**Never use these characters in filenames:**
- **Forward slash (/)** - Reserved for directory separators
- **Backslash (\)** - Can cause confusion across systems
- **Colon (:)** - Reserved for TS-Pico commands (tpi:)
- **Asterisk (*)** - Wildcard character, causes parsing issues
- **Question mark (?)** - Wildcard character
- **Quote marks (" ')** - Interfere with command syntax
- **Pipe (|)** - Special character in many systems
- **Angle brackets (< >)** - Reserved for directory indicators

**Control characters to avoid:**
- **NULL (character 0)** - Terminates strings
- **TAB character** - Causes spacing issues
- **Carriage return/Line feed** - Break filename parsing
- **Characters 1-31** - Various control functions

#### Safe Characters for Filenames

**Always safe to use:**
- **Letters:** A-Z, a-z
- **Numbers:** 0-9
- **Underscore (_)** - Excellent for word separation
- **Hyphen (-)** - Good for compound names
- **Period (.)** - For file extensions only

**Use with caution:**
- **Space character** - Can work but may cause issues in some contexts
- **Parentheses ()** - Usually okay but avoid nested parentheses
- **Square brackets []** - Generally safe but not recommended

#### Best Practice Filename Examples

**Good filenames:**
```
adventure_game.tap
missile_command_v2.tap
text_editor_pro.tap
my_programs_1984.tap
space_invaders_clone.tap
```

**Problematic filenames:**
```
"my game".tap           # Quotes cause problems
space/adventure.tap     # Slash breaks directory structure
game?.tap              # Question mark is wildcard
my:program.tap         # Colon conflicts with tpi: syntax
file*.tap              # Asterisk causes parsing issues
```

### Case Sensitivity Considerations

#### Understanding Case Behavior

**TS-Pico file system (FAT32):**
- **Case preserving** - Keeps the case you type
- **Case insensitive** - Treats "Game.tap" and "game.tap" as the same file
- **Display case** - Shows filenames as you originally typed them

**TS 2068 command behavior:**
- **Generally case insensitive** for program names within TAP files
- **Case sensitive** for some TS-Pico commands and parameters
- **Consistent case** prevents confusion

#### Case Best Practices

**Recommended approach:**
- **Use lowercase** for most filenames and directories
- **Use consistent case** throughout your collection
- **Avoid mixing cases** unnecessarily (don't use "MyGame.TAP")

**Good case usage:**
```
TAP/
├── games/
│   ├── action/
│   │   ├── defender.tap
│   │   └── missile_cmd.tap
│   └── adventure/
│       ├── zork.tap
│       └── adventure.tap
└── utilities/
    ├── editor.tap
    └── calculator.tap
```

**Problematic case usage:**
```
TAP/
├── Games/           # Inconsistent with lowercase preference
├── UTILITIES/       # All caps is harder to read
├── Personal/        # Mixed case creates confusion
└── archive/         # Inconsistent with other directories
```

### Recommended Naming Conventions

#### TAP File Naming Standards

**Game files:**
- **Format:** `gamename.tap` or `game_name.tap`
- **Examples:** `pacman.tap`, `space_invaders.tap`, `adventure_quest.tap`
- **Version numbers:** `pacman_v2.tap`, `editor_v1_5.tap`

**Utility collections:**
- **Format:** `category_utils.tap` or `specific_tool.tap`
- **Examples:** `text_utils.tap`, `math_tools.tap`, `file_manager.tap`

**Personal programs:**
- **Format:** `project_name.tap` or `personal_category.tap`
- **Examples:** `my_games.tap`, `school_projects.tap`, `work_utils.tap`

**Date-based naming:**
- **Format:** `name_YYYY.tap` or `name_YYYYMM.tap`
- **Examples:** `collection_2024.tap`, `backup_202412.tap`

#### Directory Naming Standards

**Top-level directories:**
- Keep names short and descriptive
- Use lowercase for consistency
- Avoid spaces if possible

**Good directory names:**
```
games/
utilities/
personal/
development/
archive/
testing/
backup/
```

**Avoid these directory names:**
```
stuff/              # Too vague
misc/               # Becomes a dumping ground
old_junk/           # Negative and unclear
my files/           # Space causes issues
GAMES/              # Unnecessary capitalization
```

#### Special File Types

**ROM and cartridge images:**
- **Format:** `title.rom` or `title.dck`
- **Examples:** `basic_rom.rom`, `word_processor.dck`
- **Version info:** `os_v1_4.rom`, `game_cart_v2.dck`

**Binary data files:**
- **Format:** `dataname.bin`
- **Examples:** `charset.bin`, `sprites.bin`, `music_data.bin`

**Documentation files:**
- **Format:** `readme.tap`, `manual.tap`, `help.tap`
- **Examples:** `game_instructions.tap`, `program_help.tap`

### Organization Best Practices

#### Hierarchical Structure Guidelines

**Depth recommendations:**
- **Maximum depth:** 4 levels for practical navigation
- **Optimal depth:** 2-3 levels for most collections
- **Example structure:**
```
TAP/                    # Level 1 (required)
├── games/              # Level 2 (category)
│   ├── action/         # Level 3 (subcategory)
│   │   └── arcade/     # Level 4 (sub-subcategory) - maximum recommended
│   └── adventure/
└── utilities/
```

#### File Distribution Guidelines

**Files per directory:**
- **Optimal:** 10-30 files per directory
- **Maximum practical:** 50-75 files per directory
- **Technical limit:** 100+ files (but becomes unwieldy)

**When to subdivide:**
- Directory listings become longer than one screen
- Scrolling through files becomes tedious
- Logical subcategories emerge naturally
- Performance starts to degrade

#### Naming for Sorting and Display

**Alphabetical considerations:**
- Files are typically sorted alphabetically
- Use prefixes to control sort order when needed
- Consider how names will appear in directory listings

**Sorting strategies:**
```
# Priority-based prefixes
01_essential_games.tap
02_good_games.tap
03_archive_games.tap

# Category prefixes
action_defender.tap
action_invaders.tap
puzzle_tetris.tap
puzzle_blocks.tap

# Date prefixes
2024_01_new_games.tap
2024_02_updates.tap
```

### Troubleshooting Naming Issues

#### Common Problems and Solutions

**Problem: Files don't appear in listings**
- **Cause:** Illegal characters in filename
- **Solution:** Rename using only safe characters

**Problem: Cannot load specific files**
- **Cause:** Case sensitivity confusion or special characters
- **Solution:** Use consistent lowercase naming

**Problem: Directory navigation fails**
- **Cause:** Spaces or special characters in directory names
- **Solution:** Rename directories using underscores instead of spaces

**Problem: Files appear corrupted or unreadable**
- **Cause:** Filename too long or contains control characters
- **Solution:** Shorten filename and remove special characters

#### Filename Validation Checklist

Before finalizing any filename, check:
- [ ] No forbidden characters (/, \, :, *, ?, ", ', |, <, >)
- [ ] Length under 20 characters for best compatibility
- [ ] Uses only letters, numbers, underscore, hyphen, and period
- [ ] Consistent case throughout your collection
- [ ] Descriptive enough to identify contents
- [ ] Won't conflict with existing files
- [ ] Follows your established naming convention

### Migration and Cleanup Strategies

#### Cleaning Up Existing Collections

**Assessment process:**
1. List all files with problematic names
2. Identify inconsistent naming patterns
3. Plan standardized replacement names
4. Back up everything before making changes

**Batch renaming approach:**
```
# Document current state
LOAD "tpi:dir" > current_files.txt

# Plan new names
old_name.tap -> new_standardized_name.tap

# Rename systematically
# Copy files to computer, rename, copy back
```

#### Establishing Standards

**Create a naming guide for your collection:**
- Document your chosen conventions
- Include examples of good and bad names
- Share standards with anyone who contributes to your collection
- Review and update standards as your collection grows

**Template for personal naming standards:**
```
MY TS-PICO NAMING STANDARDS
===========================

Directories: lowercase, no spaces, descriptive
TAP files: lowercase, underscores for spaces, .tap extension
Versions: _v1, _v2, etc.
Dates: _YYYY or _YYYYMM format
Personal files: my_ prefix
Work files: work_ prefix
Archive files: archive_ prefix

Examples:
✓ games/action/space_invaders_v2.tap
✓ utilities/text_editor_pro.tap
✓ personal/my_programs_2024.tap
✗ Games/Action/Space Invaders (v2).TAP
✗ "My Special Programs".tap
```

Following these naming and organization standards ensures your TS-Pico collection remains reliable, portable, and easy to manage as it grows over time.

## ZX Spectrum Compatibility Mode

One of the most exciting features of the TS-Pico is its ability to run ZX Spectrum software. The ZX Spectrum was the TS 2068's cousin in the Sinclair family, and while they're similar, they have some important differences. The TS-Pico includes a TC2048 ROM in its Flash ROM that enables your TS 2068 to run ZX Spectrum programs.

### Entering ZX Spectrum Mode

To switch to Spectrum mode, follow these steps carefully:


1. **Optional - Mount a TAP file:** If you want to load a Spectrum program:

   ```
   LOAD "tpi:filename.tap"
   ```

2. **Notify the Pico to stop TPI commands:**

   ```
   SAVE "tpi:zx48"
   ```

3. **Activate the Spectrum ROM:**

   ```
   OUT 244, 3
   ```

After these steps, your TS 2068 will be running in ZX Spectrum mode with the TC2048 ROM active.

### What to Expect in Spectrum Mode

**Keyboard differences:** Some keys might behave slightly differently. Most Spectrum software was designed with the Spectrum keyboard layout in mind.

**Limited TPI support:** Once in Spectrum mode, you cannot use TPI commands. The limited ROM space means minimal customization is available.

**Basic SAVE/LOAD/VERIFY/MERGE support:** The mode provides basic support for SLVM ZX Spectrum functionality.

### Loading Spectrum Software

Before entering Spectrum mode, mount your TAP files using the TPI command. Once in Spectrum mode, you can load programs using standard LOAD commands, but with limitations on file management.

### Returning to TS 2068 Mode

To return to normal TS 2068 operation:

1. **Re-enable TPI commands:**

   ```
   OUT 10, 100
   ```

2. **Switch back to TS 2068 ROM:**

   ```
   OUT 244, 0
   ```

3. **If the system behaves unexpectedly:** Use the TS Reset function to restore normal operation.

### Important Limitations and Cautions

**Limited functionality:** Due to ROM space constraints, Spectrum mode offers basic support only. You cannot use TPI commands while in Spectrum mode.

**TAP file behavior:** Some TAP files may cause unexpected behavior. Always test new files carefully.

**File management limitations:** Loading and saving files has limitations in Spectrum mode. You may need to restart the system to load recently saved files.

**Experiment and explore:** Despite the limitations, Spectrum mode opens up a vast library of software. Many classic Spectrum games and utilities work well on the TS 2068 through the TS-Pico.

## System Information and Diagnostics

### Keeping Your TS-Pico Healthy

Just like any sophisticated piece of equipment, your TS-Pico benefits from regular monitoring and maintenance. The system includes comprehensive diagnostic tools that help you understand how your system is performing and identify potential issues before they become problems.

### Comprehensive System Monitoring

#### The System Status Command
```
SAVE "tpi:getinfo"
```

This command is like asking your TS-Pico for a complete health report. The information it provides includes:

**Firmware Information:**
- Current firmware version
- Build date and version details
- Compatibility information

**Hardware Status:**
- Board revision and hardware version
- Memory configuration and usage
- Micro SD card information and status

**Current Operations:**
- What file is currently mounted
- Current directory location
- System configuration settings
- Current storage mode (tape or SD card)

**Performance Metrics:**
- Memory usage statistics
- Cache effectiveness
- Error counts and system health indicators

#### Understanding the Status Report

When you run `getinfo`, you'll see output similar to this:
```
TS-Pico System Information
Firmware: v1.2 (Build 2024-04-22)
ROM Version: v1.2
Board: Rev 3.1
Flash: 256KB used / 512KB total
SRAM: 128KB used / 512KB total
Micro SD Card: 8GB, 2.3GB free
Current File: adventure.tap
Path: /Games/Adventure/
Storage Mode: SD Card (TPMODE=1)
Verbose: OFF
```

**What each section means:**
- **Firmware:** Confirms you're running the latest version
- **ROM Version:** Shows your TS 2068's operating system version
- **Board:** Hardware revision information
- **Flash/SRAM:** Memory usage - helps identify if you're running low on space
- **SD Card:** Storage information and remaining space
- **Current File:** What TAP file is currently active
- **Path:** Your current directory location
- **Storage Mode:** Whether you're in tape mode (0) or SD card mode (1)

### Activity Logging and Monitoring

#### Understanding the Activity Log
```
SAVE "tpi:getlog"
```

The TS-Pico maintains a detailed log of everything it does. This log is invaluable for:
- Understanding what happened when something goes wrong
- Monitoring system performance over time
- Identifying patterns in system behavior
- Documenting system activity for troubleshooting

#### Log Management

**Viewing recent activity:**
```
SAVE "tpi:getlog" CODE 200,0    # Show last 200 bytes of activity
```

**Viewing specific amounts:**
```
SAVE "tpi:getlog" CODE 1000,0   # Show last 1000 bytes
SAVE "tpi:getlog" CODE 0,0      # Show entire log (can be very long!)
```

#### Interpreting Log Entries

Log entries include timestamps and severity levels:

**INFO level entries:** Normal operations like file loading, directory changes, successful commands. These are routine and indicate normal system health.

**WARNING level entries:** Non-critical issues that you should be aware of, such as:
- Files taking longer than expected to load
- Minor compatibility issues
- Performance degradation warnings

**ERROR level entries:** Problems that prevented something from working:
- Failed file operations
- Invalid commands
- Hardware communication issues

**CRITICAL level entries:** Serious problems requiring immediate attention:
- Memory corruption detected
- Hardware failures
- System instability

### Performance Monitoring

#### Verbose Mode for Detailed Feedback
```
SAVE "tpi:verbose"
```

Verbose mode provides detailed feedback about what the TS-Pico is doing behind the scenes. When enabled, you'll see:
- Step-by-step progress during file operations
- Detailed error messages with specific causes
- Performance timing information
- Cache hit/miss statistics

**When to enable verbose mode:**
- When learning the system
- When troubleshooting problems
- When you want to understand system performance
- When documenting procedures

**When to disable verbose mode:**
- When you're comfortable with the system
- When you want cleaner, simpler output
- When running routine operations

### Preventive Maintenance

#### Regular Health Checks

**Weekly monitoring:**
1. Run `SAVE "tpi:getinfo"` to check system status
2. Review memory usage - if Flash or SRAM usage is consistently above 80%, consider cleanup
3. Check SD card space - ensure you have adequate free space

**Monthly monitoring:**
1. Review system logs for any recurring warnings or errors
2. Check for firmware updates
3. Verify that your backup procedures are working correctly

#### Performance Optimization

**Memory management:**
- If Flash memory usage is high, consider removing unused cached files
- If SRAM usage is high, restart the system periodically to clear temporary data
- Monitor for memory leaks in the activity log

**Micro SD card optimization:**
- Keep at least 10% of micro SD card space free for optimal performance
- Organize files into directories to improve access times
- Remove duplicate or corrupted files

**System optimization:**
- Use `SAVE "tpi:close"` to properly close files and free resources
- Restart the system periodically to clear temporary data
- Keep your firmware updated to the latest version

### When to Seek Help

#### Warning Signs

Contact the TS-Pico community or support if you notice:
- Frequent CRITICAL level log entries
- Memory usage consistently above 90%
- Slow file loading times
- Frequent system resets or crashes
- Corrupted files or data

#### Information to Gather

Before seeking help, gather this information:
- Output from `SAVE "tpi:getinfo"`
- Recent entries from `SAVE "tpi:getlog"`
- Description of what you were doing when the problem occurred
- Whether the problem is consistent or intermittent
- Your firmware version and hardware revision

---

## Troubleshooting Guide

### Don't Panic - Problems Are Solvable

Every TS-Pico user encounters issues from time to time. This is normal and expected - you're working with sophisticated hardware and software, and occasionally things don't go as planned. The good news is that most problems have simple solutions, and the TS-Pico includes many built-in safety features to protect your data and system.

### Basic Troubleshooting Philosophy

**Start simple:** Most problems have simple causes. Check the obvious things first before assuming complex hardware or software issues.

**One step at a time:** Make one change at a time and test the results. This helps you identify exactly what fixed the problem.

**Document what works:** Keep notes about solutions that work for you. You might encounter the same issue again later.

**Don't be afraid to ask for help:** The TS-Pico community is friendly and helpful. If you're stuck, reach out for assistance.

### First-Level Troubleshooting

#### When Commands Don't Respond

**Problem:** You type a TS-Pico command and nothing happens, or you get an error message.

**First steps:**
1. **Check the LED:** Is the LED on the Raspberry Pi Pico blinking normally?
2. **Test basic connectivity:** Try `LOAD "tpi:dir"` to see if the TS-Pico responds at all
3. **Check your typing:** TS-Pico commands are case-sensitive and must be typed exactly
4. **Check storage mode:** Use `PRINT PEEK 23899` to see if you're in the right mode

**If the LED isn't blinking:**
- Check that your TS-Pico is properly seated in its connector
- Ensure your TS 2068 is properly powered on
- Try the TS Reset button to restart the system

**If you get error messages:**
- Read the error message carefully - it often tells you exactly what's wrong
- Check the command syntax against the examples in this manual
- Try the same command again - sometimes temporary issues resolve themselves

#### Micro SD Card Issues

**Problem:** The TS-Pico can't see your micro SD card or reports micro SD card errors.

**Troubleshooting steps:**
1. **Check physical connection:** Ensure the micro SD card is fully inserted
2. **Try removing and reinserting:** Sometimes cards need to be reseated
3. **Check the card in a computer:** Verify the micro SD card works in a regular computer (with adapter if needed)
4. **Check formatting:** Ensure the micro SD card is formatted as FAT32

**If the micro SD card works in a computer but not in the TS-Pico:**
- Try a different micro SD card to rule out compatibility issues
- Check that the micro SD card isn't write-protected
- Ensure the micro SD card isn't corrupted

### File Operation Problems

#### TAP Files Won't Load

**Problem:** You can see TAP files in the directory, but they won't mount or load properly.

**Diagnostic steps:**
1. **Check file size:** Very small files might be corrupted
2. **Try a different file:** See if the problem affects all files or just one
3. **Check the filename:** Ensure it ends with .tap or .TAP
4. **Verify file integrity:** Check the file on a computer

**Common causes:**
- **Corrupted files:** The TAP file itself is damaged
- **Filename issues:** Special characters or very long names
- **SD card problems:** The SD card may have bad sectors

#### Programs Load But Don't Work

**Problem:** TAP files mount and programs load, but they crash or behave strangely.

**Investigation steps:**
1. **Check program compatibility:** Some programs may not work perfectly with the TS-Pico
2. **Try loading from a different position:** Use FFW/REW to try loading from different blocks
3. **Check TAPDIR:** Verify the program structure looks correct
4. **Test with known-good programs:** See if the problem affects all programs

#### Printer Commands Don't Work

**Problem:** LPRINT, LLIST, or COPY commands give errors or don't work.

**Solution steps:**
1. **Switch to tape mode:** Use `SAVE "tpi:tape"` first
2. **Check TPMODE:** Use `PRINT PEEK 23899` - it should show 0 for tape mode
3. **Verify TS 2040 connection:** Ensure your printer is properly connected
4. **Remember the limitation:** These commands only work in tape mode

### Memory and Performance Issues

#### System Runs Slowly

**Problem:** File operations take much longer than expected, or the system seems sluggish.

**Performance diagnosis:**
1. **Check memory usage:** Use `SAVE "tpi:getinfo"` to see memory utilization
2. **Review the activity log:** Look for warning messages about performance
3. **Check SD card space:** Ensure adequate free space on the SD card
4. **Restart the system:** Sometimes a fresh start resolves performance issues

**Common causes:**
- **High memory usage:** Too many files cached in Flash memory
- **SD card full:** Insufficient free space affects performance
- **Fragmented SD card:** The SD card may need defragmentation

#### Out of Memory Errors

**Problem:** You get errors about insufficient memory or the system refuses to load files.

**Memory management:**
1. **Check current usage:** Use `SAVE "tpi:getinfo"` to see how much memory is used
2. **Close unused files:** Use `SAVE "tpi:close"` to free resources
3. **Restart the system:** A fresh start clears temporary memory usage
4. **Remove cached files:** If Flash memory is full, some cached files may need to be cleared

### Hardware-Related Issues

#### LED Behavior Problems

**Understanding LED patterns:**
- **No LED activity:** Power or connection problem
- **Solid LED (won't turn off):** System may be hung
- **Fast blinking:** Error condition detected
- **No response to commands:** Communication problem

**Solutions by LED behavior:**
- **No LED:** Check connections and power
- **Solid LED:** Use TS Reset button or power cycle
- **Fast blinking:** Check activity log for error details
- **No response:** Try TS Reset, then power cycle if needed

#### Connection Problems

**Problem:** The TS-Pico seems to work intermittently or loses connection.

**Connection troubleshooting:**
1. **Check physical connections:** Ensure the TS-Pico is firmly seated in the expansion bus
2. **Clean the connectors:** Use a dry cloth to clean the edge connector contacts
3. **Check for interference:** Remove other peripherals temporarily
4. **Test different positions:** Try different slots on the expansion bus

### Storage Mode Issues

#### Wrong Storage Mode

**Problem:** Commands don't work or printer functions are unavailable.

**Check current mode:**
```
PRINT PEEK 23899
```
- **0:** Tape mode (LPRINT/LLIST/COPY available, TS-Pico commands disabled)
- **1:** SD card mode (TS-Pico commands available, printer commands disabled)

**Switch modes as needed:**
```
SAVE "tpi:tape"      # Switch to tape mode for printer
SAVE "tpi:sdcard"    # Switch to SD card mode for TS-Pico
```

### Advanced Troubleshooting

#### System Recovery Procedures

**When normal troubleshooting doesn't work:**

**Level 1 - Soft Reset:**
1. Use `SAVE "tpi:close"` to close all files
2. Try `LOAD "tpi:dir"` to test basic functionality
3. If responsive, continue normal operation

**Level 2 - TS Reset:**
1. Press the TS Reset button
2. Wait for the copyright messages to appear
3. Test basic TS-Pico functionality with `LOAD "tpi:dir"`

**Level 3 - Power Cycle:**
1. Turn off the TS 2068 completely
2. Wait 10 seconds
3. Turn the TS 2068 back on
4. Test TS-Pico functionality

**Level 4 - Hardware Check:**
1. Power down the TS 2068
2. Remove and reseat the TS-Pico in the expansion bus
3. Check all physical connections
4. Power up and test

#### Data Recovery

**If you suspect file corruption:**
1. **Don't panic:** Most file corruption is recoverable
2. **Copy files to a computer:** Use an SD card reader to backup files
3. **Check files on computer:** Many corrupted TAP files can be repaired
4. **Try different SD card:** Rule out SD card hardware problems

### When to Seek Community Help

#### Before Asking for Help

**Gather information:**
1. Record the exact error messages you're seeing
2. Note what you were doing when the problem occurred
3. Run `SAVE "tpi:getinfo"` and record the output
4. Check the activity log with `SAVE "tpi:getlog"`
5. Check TPMODE with `PRINT PEEK 23899`

**Try the basics:**
1. Power cycle the system
2. Try different TAP files
3. Test with a different micro SD card
4. Check physical connections
5. Try switching storage modes

#### Where to Get Help

**Community resources:**
- GitHub repository: Issues and discussions
- User forums: Shared experiences and solutions
- Documentation: Always check for updated manuals
- Community chat: Real-time help from other users

**When posting for help:**
- Describe exactly what you were trying to do
- Include exact error messages
- Mention your firmware version
- Note what troubleshooting steps you've already tried
- Include TPMODE value if relevant to your issue

---

## What's Next? Upgrades and Extensions

Your TS-Pico isn't just a storage device - it's a platform for continuous improvement and expansion. The development team has designed it with upgradability in mind, ensuring that your investment will continue to pay dividends as new features and capabilities are developed.

### Firmware Upgrades: Keeping Current

#### Why Upgrades Matter

Firmware upgrades bring:
- **New features:** Additional commands and capabilities
- **Performance improvements:** Faster operation and better reliability
- **Bug fixes:** Resolution of issues discovered after release
- **Compatibility enhancements:** Support for more software and hardware
- **Security updates:** Protection against newly discovered vulnerabilities

#### The Upgrade Process

The TS-Pico includes a sophisticated upgrade system that makes updating firmware safe and straightforward. The complete upgrade process is covered in the separate "TS-Pico Firmware Upgrade Instructions" document, but here's an overview of what's involved:

**Preparation phase:**
- Download the upgrade files from the official repository
- Gather the necessary cables and tools
- Set aside time for the complete process

**Hardware phase:**
- Connect the TS-Pico to your computer via USB
- Install the new firmware using the built-in bootloader
- Update support files on the SD card

**Software phase:**
- Run the automated upgrade process
- Apply any necessary ROM patches
- Verify the upgrade was successful

**The upgrade process is designed to be safe,** with multiple safeguards to prevent damage to your system. However, it's important to follow the instructions carefully and not interrupt the process once it's started.

#### Staying Informed About Updates

**Official sources:**
- **GitHub repository:** https://github.com/TS-Pico-dev/TS-Pico
- **Release notifications:** Watch the repository for update announcements
- **Community forums:** Other users often share upgrade experiences and tips

**Before upgrading:**
- Read the release notes to understand what's new
- Check for any special instructions or requirements
- Backup your current configuration and important files
- Ensure you have time to complete the entire process

### Hardware Extensions and Modifications

#### Designed for Expansion

The TS-Pico was designed with expansion in mind. The development team has made the hardware designs freely available, encouraging community innovation and customization.

**Available resources:**
- **Complete schematics:** Understanding how everything works
- **PCB layouts:** For creating custom versions or repairs
- **3D printable cases:** Protection and customization options
- **Extension interfaces:** Adding your own hardware

#### Community Hardware Projects

The TS-Pico community is actively developing extensions and enhancements:

**Current projects:**
- **Enhanced cases:** Better protection and easier access
- **Extended memory modules:** Even more storage capacity
- **Additional interfaces:** Connecting modern peripherals
- **Development tools:** Hardware for firmware development

**Future possibilities:**
- **Networking capabilities:** Connect your TS 2068 to the internet
- **Modern storage interfaces:** USB drives, external hard drives
- **Audio enhancements:** Improved sound capabilities
- **Video upgrades:** Enhanced graphics options

### Software Development and Customization

#### You Can Do Your Own Thing

The TS-Pico is built on open-source principles. This means you're not limited to what comes in the box - you can modify, enhance, and extend the system to meet your specific needs.

**Development resources:**
- **Complete source code:** Available on GitHub
- **Programming documentation:** Detailed technical guides
- **Development tools:** Everything needed to modify the firmware
- **Community support:** Help from experienced developers

#### Getting Started with Development

**If you're new to programming:**
1. Start with simple modifications to existing features
2. Join the community forums to learn from others
3. Follow along with documented examples
4. Ask questions - the community is very supportive of newcomers

**If you're an experienced developer:**
1. Review the existing codebase to understand the architecture
2. Check the issue tracker for requested features
3. Consider contributing to the main project
4. Share your modifications with the community

#### Examples of Custom Modifications

**User interface enhancements:**
- Custom command shortcuts
- Enhanced directory displays
- Improved error messages
- Custom help systems

**Functionality extensions:**
- Support for additional file formats
- Custom file management utilities
- Enhanced compatibility modes
- Performance monitoring tools

**Integration projects:**
- Connecting to modern development tools
- Interfacing with other vintage computers
- Creating modern programming environments
- Building automated testing systems

### Community Contributions

#### Open Source Philosophy

The TS-Pico project embraces open-source development principles:
- **Transparency:** All design decisions are made openly
- **Collaboration:** Community input shapes development priorities
- **Sharing:** Improvements benefit everyone
- **Education:** Learning and teaching are core values

#### How You Can Contribute

**Even if you're not a programmer:**
- **Testing:** Try new features and report issues
- **Documentation:** Help improve manuals and guides
- **Support:** Help other users in forums and chat
- **Feedback:** Share your experiences and suggestions

**If you have technical skills:**
- **Bug reports:** Detailed problem reports help fix issues
- **Feature requests:** Suggest improvements and new capabilities
- **Code contributions:** Submit improvements and new features
- **Hardware designs:** Share custom modifications and extensions

## Quick Reference Card

### Essential Commands for Daily Use

#### File and Directory Operations
```
LOAD "tpi:dir"                   # Show files in current directory
LOAD "tpi:path"                  # Show current directory path
LOAD "tpi:&005"                  # Mount file by index number
SAVE "tpi:cd foldername"         # Change to directory
SAVE "tpi:cd .."                 # Go up one directory level
SAVE "tpi:cd /"                  # Go to root directory
SAVE "tpi:close"                 # Close current file
```

#### Storage Mode Commands
```
SAVE "tpi:sdcard"                # Switch to SD card mode (default)
SAVE "tpi:tape"                  # Switch to tape mode (enables printer)
PRINT PEEK 23899                 # Check TPMODE (0=tape, 1=SD card)
```

#### TAP File Navigation
```
LOAD "filename.tap"              # Mount a TAP file
LOAD "tpi:tapdir"                # Show contents of mounted TAP file
SAVE "tpi:ffw"                   # Fast forward one block
SAVE "tpi:rew"                   # Rewind one block
SAVE "tpi:ffw" CODE 5,0          # Fast forward 5 blocks
SAVE "tpi:rew" CODE 3,0          # Rewind 3 blocks
```

#### System Information
```
SAVE "tpi:getinfo"               # Display system status
SAVE "tpi:gethelp"               # Show command help
SAVE "tpi:getlog"                # Display activity log
SAVE "tpi:verbose"               # Toggle detailed messages
```

#### Traditional Loading and Saving
```
LOAD ""                          # Load next program in TAP file
LOAD "program_name"              # Load specific program
SAVE "my_program"                # Save current program
SAVE "my_program" LINE 10        # Save with auto-start line
```

#### Printer Commands (Tape Mode Only)
```
SAVE "tpi:tape"                  # Switch to tape mode first
LPRINT "Hello, World!"           # Print text to TS 2040 printer
LLIST                            # Print program listing
COPY                             # Print screen contents
SAVE "tpi:sdcard"                # Return to SD card mode
```

#### Advanced Features
```
SAVE "tpi:append"                # Enable append mode
SAVE "tpi:zx48"                  # Enter ZX Spectrum mode
SAVE "OUT 10, 100"               # Return from Spectrum mode
```

### LED Status Reference

| Pattern | Meaning | Action |
|---------|---------|---------|
| Slow blink (1/sec) | Normal, idle | None needed |
| Solid ON | Processing command | Wait for completion |
| Fast blink (2/sec) | Error condition | Check logs, try reset |
| Dark (no activity) | Watchdog reset | Wait, then retry command |

### Storage Mode Reference

| Mode | TPMODE Value | TS-Pico Commands | Printer Commands |
|------|-------------|------------------|------------------|
| SD Card | 1 | Available | NOT Available |
| Tape | 0 | NOT Available | Available |

### Memory Map Reference

```
Standard TS 2068 Memory Map with TS-Pico Integration:
0000h-3FFFh: ROM (modified by TS-Pico)
4000h-57FFh: Screen memory
5800h-5AFFh: Attributes
5B00h-5BFFh: Printer buffer
5C00h-5CBFh: System variables
5CC0h-5DCCh: User accessible area
5DCDh-5DDCh: TS-Pico RESERVED (16 bytes) - DO NOT USE
5DDBh:       TPMODE variable (0=tape, 1=SD card)
5DDDh-FFFFh: User RAM (continues standard map)
```

### Error Code Reference

| Code | Type | Meaning | Solution |
|------|------|---------|----------|
| 0 | Success | Operation completed normally | None needed |
| J | TS 2068 | Invalid I/O device | (use a command to find out what happened?) |

### Memory Management Quick Reference

| Command | Purpose | Parameters |
|---------|---------|------------|
| `memboot` | Set boot ROM slot | `CODE mem,page` (mem: 1=Flash, 2=SRAM; page: 0-15) |
| `memdock` | Set cartridge slot | `CODE mem,page` (mem: 1=Flash, 2=SRAM; page: 0-15) |
| `blkrcv` | Receive data block | `CODE length,offset` (length: bytes; offset: start position) |

### Troubleshooting Quick Steps

1. **Check LED status** - Is it blinking normally?
3. **Test basic connectivity** - Try `LOAD "tpi:dir"`
4. **Check physical connections** - Ensure TS-Pico is properly seated
6. **Check activity log** - Use `SAVE "tpi:getlog"`
7. **Try TS Reset** - Press reset button if needed
8. **Power cycle** - Turn TS 2068 off and on as last resort

### File Organization Tips

- **Keep filenames short** - 10 characters or less
- **Use consistent naming** - Develop a system and stick to it
- **Organize with directories** - Group related files together
- **Regular maintenance** - Clean up unused files periodically
- **Backup important data** - Copy files to computer regularly

### Common File Extensions

| Extension | Type | Description |
|-----------|------|-------------|
| .TAP | Tape | Standard TS 2068/Spectrum tape files |
| .DCK | Cartridge | Cartridge/dock images |
| .ROM | ROM | ROM images for system modification |
| .BIN | Binary | Raw binary data files |

---

## Appendix A: External Commands for Developers

The TS-Pico firmware includes a powerful extension system that allows developers to add custom commands without modifying the core firmware. This system uses external Python modules that integrate seamlessly with the main TS-Pico software.

### Understanding the External Command Architecture

#### How External Commands Work

External commands are implemented as Python functions that are called by the main TS-Pico firmware when specific command patterns are detected. This architecture provides several benefits:

- **Modularity:** New commands can be added without touching the core system
- **Safety:** External commands run in a controlled environment
- **Flexibility:** Commands can access system resources while maintaining separation
- **Community development:** Multiple developers can contribute commands independently

#### The Command Processing Flow

When you type a TS-Pico command, the system follows this process:

1. **Command parsing:** The firmware analyzes the command syntax
2. **Type determination:** Determines if it's a core command or external command
3. **Module lookup:** For external commands, finds the appropriate function
4. **Parameter passing:** Sends necessary data to the external function
5. **Execution:** Runs the external command with system access
6. **Result handling:** Processes the command output and returns results

### Setting Up External Commands

#### Modifying the Core Firmware

To enable external commands, you need to make small modifications to the main `tspico.py` file:

**Step 1: Remove placeholder imports**
Around line 2281, you'll find placeholder imports that prevent import errors. Comment out these lines:
```python
# Comment out these placeholder lines:
# EXT_LD_FUNCT = {}
# EXT_SA_FUNCT = {}
```

**Step 2: Add proper imports**
Add these imports at the beginning of the file where other imports are located:
```python
from my_commands import EXT_LD_FUNCT, EXT_SA_FUNCT
```

**Step 3: Modify the command processor**
In the `PROCESS_CMD()` function around line 2064, find the external command handling section and modify it to pass additional parameters:

**Original code:**
```python
elif cmd_exec in EXT_LD_FUNCT:
    EXEC = EXT_LD_FUNCT[cmd_exec]
    EXEC(pre, cmd)
```

**Modified code:**
```python
elif cmd_exec in EXT_LD_FUNCT:
    EXEC = EXT_LD_FUNCT[cmd_exec]
    EXEC(MQ, pre, cmd, TSP.f_name, TSP.VERBOSE)
```

**Step 4: Handle SAVE commands (if needed)**
If you're implementing SAVE-based external commands, make similar modifications around line 2141 for the SAVE command processor.

#### Creating the External Commands Module

Create a new file called `my_commands.py` in the same directory as `tspico.py`. This file will contain your custom command implementations.

### Example External Commands

#### Basic Command Structure

Here's the basic structure for an external command module:

```python
import random
from rp2 import StateMachine
from tspico import ACTIVATE_MQ, SEND_MSG, SEND_MSG2

# Dictionary mapping command names to functions
EXT_LD_FUNCT = {
    'fact': FACTORIAL,
    'word': RANDOM_WORD,
}

EXT_SA_FUNCT = {
    # SAVE-based commands go here
}

def FACTORIAL(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """Calculate factorial of a number"""
    # Command implementation here
    pass

def RANDOM_WORD(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """Get a random word from a list"""
    # Command implementation here
    pass
```

#### Example 1: Factorial Calculator

This command calculates the factorial of a number passed as a parameter:

```python
def FACTORIAL(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """
    Calculates the factorial of a number.
    Usage: SAVE "tpi:fact" CODE n,0
    Where n is the number to calculate factorial for
    """
    wrt = MQ.put
    type_res = 128  # Response type: 128-199 "normal", 200 OK, 201+ error
    length = 0      # Length of response
    
    SEND_MSG(MQ, "Calculating Factorial...", "", 1, VERBOSE)
    
    try:
        # Extract the number from the command parameters
        # This is a simplified example - real implementation would
        # need proper parameter parsing
        number = extract_number_from_command(cmd)
        
        if number < 0:
            result = "Error: Factorial not defined for negative numbers"
            type_res = 201  # Error condition
        elif number > 20:
            result = "Error: Number too large"
            type_res = 201  # Error condition
        else:
            # Calculate factorial
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            result = f"Factorial of {number} is {factorial}"
            type_res = 200  # Success
    
    except Exception as e:
        result = f"Error: {str(e)}"
        type_res = 201  # Error condition
    
    # Send result back to TS 2068
    SEND_MSG2(MQ, result, type_res, VERBOSE)
```

#### Example 2: Random Word Generator

This command selects a random word from a predefined list:

```python
def RANDOM_WORD(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """
    Returns a random word from a word list.
    Usage: LOAD "tpi:word"
    """
    wrt = MQ.put
    type_res = 128
    
    SEND_MSG(MQ, "Selecting random word...", "", 1, VERBOSE)
    
    # Word list - in a real implementation, this might be loaded from a file
    word_list = [
        "COMPUTER", "KEYBOARD", "MONITOR", "PROGRAM", "VARIABLE",
        "FUNCTION", "ARRAY", "LOOP", "CONDITION", "ALGORITHM",
        "DATABASE", "NETWORK", "PROTOCOL", "INTERFACE", "SYSTEM"
    ]
    
    try:
        # Select random word
        selected_word = random.choice(word_list)
        result = f"Random word: {selected_word}"
        type_res = 200  # Success
        
    except Exception as e:
        result = f"Error selecting word: {str(e)}"
        type_res = 201  # Error condition
    
    # Send result back to TS 2068
    SEND_MSG2(MQ, result, type_res, VERBOSE)
```

### Advanced External Command Concepts

#### Parameter Passing and Parsing

External commands receive several parameters that provide access to system state:

- **MQ (StateMachine):** The communication channel with the TS 2068
- **pre:** The command prefix information
- **cmd:** The complete command string
- **f_name:** Current mounted filename
- **VERBOSE:** Current verbose mode setting

#### Error Handling Best Practices

**Always use try-catch blocks:**
```python
try:
    # Your command logic here
    result = perform_operation()
    type_res = 200  # Success
except ValueError as e:
    result = f"Invalid input: {str(e)}"
    type_res = 201  # Error
except Exception as e:
    result = f"Unexpected error: {str(e)}"
    type_res = 202  # Critical error
```

**Use appropriate response types:**
- **128-199:** Normal informational responses
- **200:** Success/OK
- **201:** Recoverable error
- **202:** Critical error requiring attention

#### File System Integration

External commands can interact with the file system:

```python
def LIST_FILES(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """List files in current directory with details"""
    try:
        import os
        files = os.listdir('/sd')
        result = "Files: " + ", ".join(files)
        type_res = 200
    except Exception as e:
        result = f"Error listing files: {str(e)}"
        type_res = 201
    
    SEND_MSG2(MQ, result, type_res, VERBOSE)
```

#### Memory and Performance Considerations

**Efficient memory usage:**
- Avoid creating large data structures unnecessarily
- Clean up resources when done
- Use generators for large datasets when possible

**Performance optimization:**
- Cache frequently accessed data
- Minimize file I/O operations
- Use efficient algorithms for computations

### Testing and Debugging External Commands

#### Development Workflow

1. **Create your command function** in `my_commands.py`
2. **Add it to the appropriate dictionary** (EXT_LD_FUNCT or EXT_SA_FUNCT)
3. **Test with simple inputs** to verify basic functionality
4. **Test error conditions** to ensure robust error handling
5. **Test with edge cases** to verify reliability
6. **Document the command** for other users

#### Debugging Techniques

**Use verbose mode for debugging:**
```python
if VERBOSE:
    SEND_MSG(MQ, f"Debug: Processing parameter {param}", "", 1, True)
```

**Log important information:**
```python
import time
timestamp = time.time()
SEND_MSG(MQ, f"Command started at {timestamp}", "", 1, VERBOSE)
```

**Test incrementally:**
Start with simple functionality and gradually add complexity.

### Best Practices for External Command Development

#### Command Design Principles

**Keep commands focused:** Each command should do one thing well.

**Use clear naming:** Command names should clearly indicate their purpose.

**Provide helpful feedback:** Always give users clear information about what's happening.

**Handle errors gracefully:** Never let external commands crash the main system.

#### Documentation Standards

**Document command purpose:**
```python
def MY_COMMAND(MQ: StateMachine, pre, cmd, f_name, VERBOSE):
    """
    Brief description of what the command does.
    
    Usage: LOAD "tpi:mycommand" [parameters]
    
    Parameters:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of what the command returns
    
    Examples:
        LOAD "tpi:mycommand"  # Basic usage
        SAVE "tpi:mycommand" CODE 5,0  # With parameters
    """
```

**Maintain a command registry:**
Keep a separate documentation file listing all available external commands and their usage.

### Contributing External Commands to the Community

#### Sharing Your Commands

**Code quality:** Ensure your code is clean, well-commented, and follows Python best practices.

**Testing:** Thoroughly test your commands before sharing.

**Documentation:** Provide clear documentation and examples.

**Compatibility:** Verify your commands work with current firmware versions.

#### Contribution Process

1. **Fork the repository** on GitHub
2. **Create a feature branch** for your commands
3. **Add your commands** with full documentation
4. **Test thoroughly** on real hardware
5. **Submit a pull request** with detailed description
6. **Respond to feedback** from code reviewers

The external command system makes the TS-Pico incredibly extensible while maintaining system stability and safety. Whether you're adding simple utilities or complex applications, this architecture provides the foundation for unlimited creativity and functionality.

---

## Appendix B: Machine Language Flash Programming

The TS-Pico includes sophisticated Flash memory management capabilities that allow advanced users to directly program the onboard Flash memory using machine language routines. This functionality is primarily intended for system developers, firmware engineers, and advanced users who need direct hardware control.

**CRITICAL WARNING:** The routines described in this appendix directly manipulate Flash memory hardware. Incorrect use can permanently damage your TS-Pico or corrupt system firmware. Only attempt these operations if you have extensive experience with machine language programming and understand the risks involved.

### Understanding the Flash Memory Architecture

#### Flash Memory Organization

The TS-Pico's Flash memory is organized into two main 32KB blocks:
- **Lower Block (0x0000-0x7FFF):** Lower 32KB of Flash memory
- **Upper Block (0x8000-0xFFFF):** Upper 32KB of Flash memory

Each block is further divided into 4KB sectors that can be erased and programmed independently.

#### Memory Mapping and Access

Flash memory access requires specific hardware configuration:
- **Page selection:** Memory blocks must be paged into the TS 2068's address space
- **Write protection:** Flash memory has hardware write protection that must be disabled
- **Timing requirements:** Flash operations require precise timing sequences
- **Verification:** All write operations should be verified for correctness

### Flash Programming Command Sequences

#### Standard Flash Command Protocol

Flash memory chips use standardized command sequences for erase and program operations:

**Unlock Sequence:**
```
Write 0xAA to address 0x5555
Write 0x55 to address 0x2AAA
```

**Program Command:**
```
Write 0xA0 to address 0x5555 (after unlock sequence)
Write data byte to target address
```

**Sector Erase Command:**
```
Write 0x80 to address 0x5555 (after unlock sequence)
Write 0xAA to address 0x5555
Write 0x55 to address 0x2AAA
Write 0x30 to sector address
```

### Machine Language Routines

#### Upper Block Flash Programming

**Sector Erase Routine (Upper 32KB)**
Entry point: 0x7F58

```assembly
; Flash Update - Upper Block Sector Erase
; Entry: 0x7F58
; Erases upper 32KB (8 sectors of 4KB each)

7F58    DI                      ; Disable interrupts
7F59    PUSH    AF              ; Save registers
7F5A    PUSH    BC
7F5B    PUSH    DE
7F5C    PUSH    HL
7F5D    LD      A,246           ; Page select value (11110110b)
7F5F    OUT     (244),A         ; Page in Flash memory
7F61    LD      B,8             ; Number of 4KB sectors to erase
7F63    LD      HL,8000h        ; Start address (upper 32KB)

7F66 BACK1:
7F66    LD      DE,1000h        ; 4KB sector size
7F69    LD      A,170           ; Flash unlock command 1 (0xAA)
7F6B    LD      (5555h),A       ; Write to unlock address 1
7F6E    LD      A,85            ; Flash unlock command 2 (0x55)
7F70    LD      (2AAAh),A       ; Write to unlock address 2
7F73    LD      A,128           ; Sector erase setup command (0x80)
7F75    LD      (5555h),A       ; Write to unlock address 1
7F78    LD      A,170           ; Flash unlock command 1 (0xAA)
7F7A    LD      (5555h),A       ; Write to unlock address 1
7F7D    LD      A,85            ; Flash unlock command 2 (0x55)
7F7F    LD      (2AAAh),A       ; Write to unlock address 2
7F82    LD      A,48            ; Sector erase command (0x30)
7F84    LD      (HL),A          ; Write to sector address
7F85    ADD     HL,DE           ; Move to next sector
7F86    LD      DE,8000h        ; Delay loop counter

7F89 WAIT:
7F89    DEC     DE              ; Decrement delay counter
7F8A    LD      A,D             ; Check if delay complete
7F8B    OR      E
7F8C    JR      NZ,WAIT         ; Continue delay (≈25ms per sector)
7F8E    DJNZ    BACK1           ; Repeat for all sectors

7F90    LD      B,255           ; Additional delay
7F92 LOOP:
7F92    DJNZ    LOOP            ; Final delay loop

7F94 END:
7F94    XOR     A               ; Clear page selection
7F95    OUT     (244),A         ; Page out Flash memory
7F97    POP     HL              ; Restore registers
7F98    POP     DE
7F99    POP     BC
7F9A    POP     AF
7F9B    EI                      ; Re-enable interrupts
7F9C    RET                     ; Return to caller
```

**Byte Write Routine (Upper 32KB)**
Entry point: 0x7F9E

```assembly
; Flash Update - Upper Block Byte Write
; Entry: 0x7F9E
; Writes data to upper 32KB Flash memory

7F9E    DI                      ; Disable interrupts
7F9F    PUSH    AF              ; Save registers
7FA0    PUSH    BC
7FA1    PUSH    DE
7FA2    PUSH    HL
7FA3    LD      A,246           ; Page select value (11110110b)
7FA5    OUT     (244),A         ; Page in Flash memory
7FA7    LD      DE,8000h        ; Number of bytes to write (32KB)
7FAA    LD      HL,8000h        ; Start address (upper 32KB)

7FAD FLSHWR:
7FAD    LD      A,170           ; Flash unlock command 1 (0xAA)
7FAF    LD      (5555h),A       ; Write to unlock address 1
7FB2    LD      A,85            ; Flash unlock command 2 (0x55)
7FB4    LD      (2AAAh),A       ; Write to unlock address 2
7FB7    LD      A,160           ; Program command (0xA0)
7FB9    LD      (5555h),A       ; Write to unlock address 1

7FBC SRAMWR:
7FBC    IN      A,(14)          ; Get data from TS-Pico
7FBE    LD      (HL),A          ; Write to Flash memory
7FBF    LD      A,E             ; Check if done
7FC0    OR      D
7FC1    JR      Z,END           ; Jump to end if complete
7FC3    INC     HL              ; Increment address
7FC4    DEC     DE              ; Decrement byte count
7FC5    JR      FLSHWR          ; Continue writing

; End routine same as erase routine above