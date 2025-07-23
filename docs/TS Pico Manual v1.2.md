# TS-Pico User Manual
## Timex Sinclair 2068 Personal Color Computer Pico Interface

*Firmware Version 1.2 - Complete User Guide*

---

## Table of Contents

- [General Description and Operation](#general-description-and-operation)
- [Installing the TS Pico](#installing-the-ts-pico)
- [Getting Started: Your First Steps](#getting-started-your-first-steps)
- [Exploring the TS Pico Hardware](#exploring-the-ts-pico-hardware)
- [Understanding the TS Pico Commands](#understanding-the-ts-pico-commands)
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
- [The TS Pico Community](#the-ts-pico-community)
- [Quick Reference Card](#quick-reference-card)
- [Appendix A: External Commands for Developers](#appendix-a-external-commands-for-developers)
- [Appendix B: Machine Language Flash Programming](#appendix-b-machine-language-flash-programming)
- [Appendix C: Technical Specifications](#appendix-c-technical-specifications)

---

## General Description and Operation

### Welcome to the Future of Your TS 2068!

Thank you for selecting the Timex Pico Interface, or the TS Pico, as we like to call it. You're about to transform your vintage TS 2068 into a modern, capable machine while keeping all the charm and character that made you fall in love with it in the first place.

### What Exactly Is the TS Pico?

Think of the TS Pico as a bridge between your classic computer and today's technology. It's like having a modern hard drive, but one that speaks the language your TS 2068 understands perfectly. This new interface was developed specifically for the Timex Sinclair 2068 computer, and it brings together the best of both worlds: the nostalgia and simplicity of your vintage machine with the convenience and reliability of modern storage.

### The Technology Behind the Magic

At its heart, the TS Pico is powered by a Raspberry Pi Pico - a tiny but powerful computer that acts as your TS 2068's new best friend. Programmed in MicroPython (a streamlined version of the popular Python programming language), the TS Pico allows you to save and load programs from TAP files stored on a standard SD card - the same kind you might use in a digital camera.

But that's not all. Your TS Pico comes equipped with an impressive 512KB of Flash memory. To put that in perspective, that's enough space to store dozens of your favorite programs instantly accessible without even touching the SD card. Some of this Flash memory holds the TS Pico's advanced operating system - think of it as the brain that makes everything work smoothly. The rest is available for your use, acting like super-fast storage for your most frequently used programs.

On top of that, you get another 512KB of static RAM (SRAM) - all of which is available to you. This is like having extra workspace for your computer to stretch out and handle bigger, more complex programs than ever before.

### A Word About Safety

Now, we need to have a brief but important conversation about taking care of your TS Pico. While we've designed it to be robust and reliable, it's still a sophisticated piece of electronics. The TS Pico is difficult to break, but not impossible. 

**Here's the important part:** If you don't have experience with electronics or programming at the hardware level, please stick to using the TS Pico as described in this manual. Don't attempt to modify the hardware or reprogram the firmware unless you really know what you're doing. While we encourage experimentation and learning, it is possible to cause irreparable damage to the interface or even to your precious TS 2068 if things go wrong.

Think of it like this: you wouldn't try to repair your car's engine without proper knowledge and tools, right? The same principle applies here. But don't worry - everything you need to use and enjoy your TS Pico is covered in this manual, and it's all designed to be safe and straightforward.

---

## Installing the TS Pico

### Before You Begin

Installation is straightforward, but let's take it step by step. The most important thing is to be gentle and patient. Your TS 2068 and TS Pico are both vintage and modern electronics respectively, and they deserve to be treated with care.

### Safety First: Powering Down

**Always, always, always turn off your TS 2068 before connecting or disconnecting anything.** This isn't just a suggestion - it's essential for protecting both your computer and your new TS Pico. Connecting or disconnecting electronics while they're powered on can cause damage that's expensive (or impossible) to repair.

Once your TS 2068 is turned off, take a moment to remove any cartridges that might be plugged into the computer. This gives you clear access to the expansion connector and eliminates any possibility of conflicts.

### Understanding Your TS Pico Style

The TS Pico comes in two different styles, and the installation process depends on which one you have:

#### Direct Connect Style
This version looks like a large cartridge and plugs directly into your TS 2068's expansion port. When connected, it will extend horizontally from the right side of your computer. This style is perfect if you want a clean, simple setup without additional cables or adapters.

To install a direct connect TS Pico:
1. **Locate the expansion connector** on the right side of your TS 2068. It's the long, rectangular slot with small metal contacts inside.
2. **Find the corresponding connector** on your TS Pico. You'll notice it has a small notch or "key" - this isn't decorative, it's a safety feature to ensure you can't insert the card backwards.
3. **Line up the key** on the TS Pico with the corresponding slot in your TS 2068's connector. This should feel natural and easy - if you're forcing anything, stop and check your alignment.
4. **Gently but firmly press the TS Pico** into the connector until it's fully seated. You should feel it slide in smoothly and then stop when it's properly connected.

#### Expansion Bus Style
This version works with an expansion bus adapter that plugs into your TS 2068 first, then provides multiple slots for various devices including your TS Pico. This style is ideal if you plan to use multiple peripherals or if you want the flexibility to easily swap devices.

To install an expansion bus TS Pico:
1. **Install the expansion bus** into your TS 2068's expansion port using the same careful alignment process described above.
2. **Choose an appropriate slot** on the expansion bus for your TS Pico. Any slot will work, but many users prefer the leftmost slot for easy access.
3. **Install the TS Pico** into the chosen slot on the expansion bus, again using the key alignment to ensure proper orientation.

### After Installation

Once your TS Pico is physically connected, take a moment to check that everything looks right:
- The TS Pico should be firmly seated with no wobbling
- All connectors should be fully engaged
- Nothing should look forced or crooked

If everything looks good, you're ready to power up and start exploring!

---

## Getting Started: Your First Steps

### The Moment of Truth: First Power-On

Now comes the exciting part - seeing your TS Pico in action for the first time. But before we jump in, let's set proper expectations so you know what to look for.

**Turn on your TS 2068** as you normally would. You should see the familiar startup sequence: the copyright messages will appear just as they always have. This is important - it means your TS 2068 is starting up normally and the TS Pico isn't interfering with basic operations.

### Your First TS Pico Command

Once you see the familiar cursor (that little "K" in the corner), you're ready to say hello to your TS Pico. Let's start with something simple that will prove everything is working:

Type exactly this:
```
LOAD "tpi:dir"
```

Then press **ENTER**.

**What just happened?** You've just asked your TS Pico to show you what files are available on the SD card. The "tpi:" part tells your TS 2068 that this command is intended for the TS Pico, not for a regular tape operation.

### Understanding What You See

Depending on what's on your SD card, you might see:
- A list of TAP files with numbers next to them
- Some folder names (these will be enclosed in angle brackets like `<foldername>`)
- File sizes shown in bytes or kilobytes
- A message about available space on your SD card

**Don't panic if you see an error message!** This is actually normal if:
- Your SD card is empty (it will say something like "no files found")
- Your SD card isn't inserted properly
- Your SD card needs to be formatted

We'll cover how to handle these situations in the troubleshooting section.

### If Everything Worked

Congratulations! You've just successfully communicated with your TS Pico. That simple command proved that:
- Your TS Pico is properly connected
- The firmware is running correctly
- Your TS 2068 can communicate with the TS Pico
- Your SD card is accessible

### If You Got an Error

Don't worry - this is a learning process, and errors are part of learning. The most common issues at this stage are:
- **No SD card inserted:** Make sure your SD card is fully inserted into the TS Pico
- **SD card not formatted:** Some SD cards need to be formatted before use
- **Connection issue:** Double-check that your TS Pico is fully seated in its connector

We'll cover all of these scenarios in detail in the troubleshooting section.

---

## Exploring the TS Pico Hardware

### Getting to Know Your New Hardware

Before we dive deep into using your TS Pico, let's take a tour of the hardware. Understanding what each part does will help you use the system more effectively and troubleshoot any issues that might arise.

### The Raspberry Pi Pico: The Brain of the Operation

The most prominent feature on your TS Pico board is the Raspberry Pi Pico itself. This small green circuit board is actually a complete computer - far more powerful than your TS 2068, but designed to work as its helpful assistant.

#### The Status LED: Your Window into the TS Pico's Mind

The Raspberry Pi Pico has a small LED that acts like a status indicator. Learning to read this LED will help you understand what your TS Pico is doing at any given moment:

**Normal Operations:**
- **Slow, steady blinking (about once per second):** This is the "all is well" signal. Your TS Pico is idle and ready to accept commands. Think of it as the TS Pico saying "I'm here and ready to help!"
  
- **Solid ON (continuously lit):** The TS Pico is busy processing a command or waiting for input from you. This is normal during file operations, directory scans, or when you're in the middle of a command sequence.

**Special Situations:**
- **Fast blinking (several times per second):** This usually indicates an error condition. The TS Pico has encountered something it can't handle and is asking for attention.

- **Pattern blinking:** During special operations like firmware upgrades or file copying, you might see specific blinking patterns. These are covered in detail in the respective sections of this manual.

- **LED goes dark:** If the LED suddenly stops blinking entirely, it usually means the watchdog timer has activated. This is a safety feature that resets the TS Pico if it gets confused or stuck.

#### Understanding the Watchdog Timer

The watchdog timer deserves special mention because it's one of the TS Pico's most important safety features. Think of it as a helpful assistant who taps you on the shoulder if you've been staring at a problem too long.

If a command doesn't complete as expected, or if the TS Pico gets confused by an unexpected situation, the watchdog timer will activate after several seconds. When this happens, you'll see the LED go dark, and then the TS Pico will automatically reset its internal state and return to normal operation.

This is actually a good thing! It means that even if something goes wrong, your TS Pico won't get permanently stuck. After a watchdog reset, you can simply try your command again or check if there was a problem with your input.

### The Control Buttons: Physical Control When You Need It

Your TS Pico includes several pushbuttons that provide direct hardware control:

#### TS Reset Button
This button is your "emergency restart" for the TS 2068. When pressed, it pulls the RESET line on your computer's Z80 processor, causing a complete restart. You'll see the familiar three copyright messages appear, just as if you had turned the computer off and on again.

**When to use the TS Reset button:**
- When your TS 2068 seems frozen or unresponsive
- After installing new software that requires a restart
- When troubleshooting suggests a clean restart

**Important:** This button restarts your TS 2068, not just the TS Pico. Any programs in memory will be lost unless you've saved them first.

#### Pico Reset and NMI Buttons
At the time this manual was written, these buttons are reserved for future functionality. The TS Pico firmware doesn't currently use them, but future versions might add features that take advantage of these additional controls.

### The SD Card Slot: Your Gateway to Unlimited Storage

The SD card slot is where the magic happens. This tiny slot accepts standard SD cards (the same type used in digital cameras) and gives your TS 2068 access to virtually unlimited storage.

**SD Card Best Practices:**
- **Use quality SD cards:** Cheap, no-name cards can be unreliable. Stick with reputable brands.
- **Format correctly:** Your SD card should be formatted as FAT32 for best compatibility.
- **Safe removal:** Always use the `SAVE "tpi:close"` command before removing your SD card.
- **Handle with care:** SD cards are small and can be easily damaged. Store them safely when not in use.

### Power and Connectivity

Your TS Pico draws its power directly from your TS 2068 through the expansion connector. There are no external power supplies or batteries to worry about. When your TS 2068 is on, your TS Pico is on. When your TS 2068 is off, your TS Pico is off. Simple!

The TS Pico also includes a micro-USB connector, but this is only used for firmware upgrades. During normal operation, you won't need to connect anything to this port.

---

## Understanding the TS Pico Commands

### The Philosophy Behind TS Pico Commands

Before we dive into specific commands, it's important to understand the philosophy behind how the TS Pico works. The designers wanted to make the TS Pico feel natural to anyone familiar with the TS 2068, while adding powerful new capabilities.

### The Magic of "tpi:" - Your Gateway to Modern Features

Every TS Pico command starts with "tpi:" - this is your signal to the system that you want to talk to the TS Pico rather than perform a traditional tape operation. Think of "tpi:" as a polite way of saying "Excuse me, TS Pico, I have a request for you."

**Why "tpi:"?** It stands for "Timex Pico Interface" and it serves an important technical purpose: it tells your TS 2068 to pass the command to the TS Pico instead of trying to access a tape drive. This allows the TS Pico to add new functionality without interfering with your computer's existing capabilities.

### LOAD vs. SAVE: Two Different Types of Conversations

The TS Pico uses your TS 2068's existing LOAD and SAVE commands, but extends them in clever ways:

#### LOAD Commands: "Show Me" or "Get Me"
LOAD commands are typically used for retrieving information or bringing files into your computer's memory. When you use a LOAD command with "tpi:", you're usually asking the TS Pico to either show you something or to load a file for use.

**Examples of LOAD commands:**
- `LOAD "tpi:dir"` - "Show me what files are available"
- `LOAD "tpi:path"` - "Show me which directory I'm currently in"
- `LOAD "program.tap"` - "Load this specific program into memory"

#### SAVE Commands: "Do This" or "Change That"
SAVE commands are used for actions that change something or perform an operation. When you use a SAVE command with "tpi:", you're usually asking the TS Pico to change a setting, perform an action, or modify something.

**Examples of SAVE commands:**
- `SAVE "tpi:cd Games"` - "Change to the Games directory"
- `SAVE "tpi:close"` - "Close the currently open file"
- `SAVE "tpi:getinfo"` - "Show me detailed system information"

### The Comfort of Familiarity

Here's one of the most beautiful things about the TS Pico: once you mount a TAP file (more on this shortly), your regular LOAD and SAVE commands work exactly as they always have. You don't need to learn a completely new way of working. Your TS 2068 will load and save programs just like it always did, but faster and more reliably than ever before.

### Building Your Command Vocabulary

Think of learning TS Pico commands like learning a new language - start with the basics and gradually expand your vocabulary. You don't need to memorize every command right away. In fact, there's a built-in help system (we'll cover this soon) that can remind you of any command you forget.

**Start with these essential commands:**
1. `LOAD "tpi:dir"` - See what files are available
2. `SAVE "tpi:gethelp"` - Get help with commands
3. `SAVE "tpi:getinfo"` - Check system status
4. `SAVE "tpi:close"` - Close files when done

Master these four commands, and you'll be well on your way to TS Pico proficiency.

---

## Basic File Operations - Your Daily Toolkit

### Understanding TAP Files: Your Digital Tape Collection

Before we dive into specific operations, let's talk about TAP files. If you're familiar with cassette tapes for your TS 2068, TAP files are the digital equivalent. Each TAP file can contain multiple programs, just like a physical tape might have several programs recorded on it.

The beauty of TAP files is that they load much faster than physical tapes, they never wear out, and you can easily organize them into folders on your SD card. Think of your SD card as a vast library, with each TAP file being like a book that contains multiple chapters (programs).

### DIR: Your Window into Available Files

The directory command is probably the one you'll use most often. It's your way of asking, "What do I have to work with?"

```
LOAD "tpi:dir"
```

**What happens when you run this command:**
1. The TS Pico scans your current directory on the SD card
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

This command tells the TS Pico, "Load whatever file is number 001 in the current directory." It's much faster than typing `LOAD "some-long-filename.tap"`, especially for files with complicated names.

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

Just as you might organize your physical cassette tapes into categories (games, utilities, programming tools), organizing your TAP files into directories makes everything easier to find and manage. The TS Pico supports unlimited subdirectories, so you can create an organization system that makes sense for your collection.

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

TAP files are the core of the TS Pico experience. Think of each TAP file as a digital cassette tape that can contain multiple programs. Unlike physical tapes, TAP files load instantly, never wear out, and can be easily copied and organized.

### The TAP File Lifecycle

Every TAP file goes through a simple lifecycle in the TS Pico:
1. **Selection:** You choose which TAP file to work with
2. **Mounting:** The TS Pico makes the file active and ready to use
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
This command temporarily switches your LOAD/SAVE commands back to the physical cassette interface. Useful if you need to load something from an actual cassette tape or save to physical media for backup.

To switch back to the TS Pico, just mount a new TAP file.

---

## Advanced System Commands

### Getting Help When You Need It

The TS Pico includes a comprehensive built-in help system. Instead of reaching for this manual every time you forget a command, you can get instant help right on your screen.

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

This command is like asking your TS Pico, "How are you doing, and what's your current status?" The response includes:

- **Firmware version:** What version of TS Pico software you're running
- **ROM version:** The version of your TS 2068's operating system
- **Board revision:** Hardware version information
- **Memory usage:** How much Flash and SRAM is being used
- **SD card status:** Information about your SD card
- **Current file:** What TAP file is currently mounted, if any
- **Configuration settings:** Various system settings and their current values

**When to use getinfo:**
- When troubleshooting problems
- Before performing major operations like upgrades
- When checking if upgrades were successful
- When documenting your system configuration

#### Activity Logging
```
SAVE "tpi:getlog"
```

The TS Pico keeps a detailed log of everything it does. This log includes timestamps and can be invaluable for troubleshooting problems or understanding what happened during a session.

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

This toggle switch enables or disables detailed status messages for commands. When verbose mode is on, the TS Pico provides much more detailed feedback about what it's doing.

**When to enable verbose mode:**
- When learning the system
- When troubleshooting problems
- When you want to understand exactly what's happening behind the scenes
- When documenting procedures for others

**When to disable verbose mode:**
- When you're comfortable with the system and don't need extra feedback
- When you want cleaner, less cluttered output
- When running automated scripts or procedures

---

## Memory and Flash Management

### Understanding TS Pico Memory Architecture

Your TS Pico has several different types of memory, each with its own purpose. Understanding these can help you make better use of your system and troubleshoot issues more effectively.

#### Flash Memory (512KB)
This is permanent storage that retains its contents even when power is off. Think of it like a hard drive - it's where the TS Pico stores:
- The firmware (operating system)
- Cached TAP files for faster access
- System configuration data
- User data that needs to persist between sessions

#### SRAM (512KB)
This is high-speed temporary storage that's available to you. Unlike Flash memory, SRAM loses its contents when power is turned off, but it's much faster to access. The TS Pico uses SRAM for:
- Temporary file operations
- Fast caching of frequently accessed data
- Buffer space for large operations

#### SD Card Storage
This is your unlimited external storage. While not as fast as the internal memory, SD cards can hold thousands of TAP files and provide easy file transfer between your TS Pico and modern computers.

### Advanced Memory Commands

**⚠️ Warning:** The commands in this section are for advanced users who understand memory management. Incorrect use can cause system instability or data loss. If you're new to the TS Pico, stick to the basic commands until you're more comfortable with the system.

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

## ZX Spectrum Compatibility Mode

### A Bridge to Another World

One of the most exciting features of the TS Pico is its ability to run ZX Spectrum software. The ZX Spectrum was the TS 2068's cousin in the Sinclair family, and while they're similar, they have some important differences. The TS Pico includes special compatibility mode that lets your TS 2068 run ZX Spectrum programs.

### Entering ZX Spectrum Mode

```
SAVE "tpi:zx48"
```

When you enter this command, several things happen behind the scenes:
- The TS Pico adjusts memory mapping to match ZX Spectrum expectations
- Screen handling is modified for Spectrum compatibility
- Keyboard mapping is adjusted for Spectrum programs
- Various system parameters are modified to create a Spectrum-like environment

### What to Expect in Spectrum Mode

**Visual changes:** You might notice slight differences in how the screen looks or how text is displayed. This is normal and expected.

**Keyboard differences:** Some keys might behave slightly differently. Most Spectrum software was designed with the Spectrum keyboard layout in mind.

**Program behavior:** Spectrum programs should run normally, though some might behave slightly differently than they would on an actual Spectrum.

### Loading Spectrum Software

While in Spectrum mode, you can load TAP files containing ZX Spectrum programs just like you would load TS 2068 programs:

```
LOAD "spectrum_game.tap"
LOAD ""
```

### Returning to TS Mode

When you're ready to return to normal TS 2068 operation:

```
SAVE "OUT 10, 100"
```

This command returns all settings to normal TS 2068 operation. You can then use your TS Pico normally with TS 2068 software.

### Tips for Spectrum Compatibility

**Not all programs will work:** Some Spectrum programs use hardware features or memory configurations that can't be perfectly emulated. Don't be discouraged if a particular program doesn't work - this is normal.

**Save your work first:** Always save any important work before switching to Spectrum mode, as the mode change affects memory configuration.

**Experiment and explore:** Spectrum mode opens up a vast library of software. Many classic Spectrum games and utilities work well on the TS 2068 through the TS Pico.

**Keep notes:** If you find Spectrum programs that work particularly well, keep track of them for future reference.

---

## Traditional LOAD and SAVE Operations

### The Beauty of Backward Compatibility

One of the most elegant aspects of the TS Pico is how it preserves the familiar LOAD and SAVE commands you already know. Once you have a TAP file mounted, your TS 2068 behaves exactly as it always has - but faster and more reliably.

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

### Saving Programs

Saving works just as you remember, but with modern conveniences:

#### Basic Program Saving
```
SAVE "my_program"
```
This saves the current program in memory to the mounted TAP file (if append mode is enabled) or creates a new TAP file.

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

### The Loading Process: What's Really Happening

When you type `LOAD ""` with a mounted TAP file, here's what happens behind the scenes:

1. **The TS Pico receives the command** through the interface
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

### Mixing Modern and Traditional Commands

You can freely mix TS Pico commands with traditional LOAD/SAVE operations:

```
LOAD "tpi:dir"              # See what's available
LOAD "games.tap"            # Mount a TAP file
LOAD "tpi:tapdir"           # See what's in the TAP file
SAVE "tpi:ffw" CODE 4,0     # Skip to program 4
LOAD ""                     # Load program 4 traditionally
SAVE "my_highscore"         # Save your progress traditionally
SAVE "tpi:close"            # Close the TAP file (TS Pico command)
```

This flexibility means you can use as much or as little of the TS Pico's advanced features as you're comfortable with.

---

## File and Directory Management Best Practices

### Organizing for Success

Good file organization isn't just about keeping things neat - it's about making your TS Pico experience more enjoyable and efficient. A well-organized SD card means you can find what you want quickly and spend more time using your computer and less time searching for files.

### Filename Best Practices

#### Stick to TS 2068 Conventions
Your TS 2068 was designed in an era of 8-character filenames, and while the TS Pico can handle longer names, it's best to keep TAP filenames to 10 characters or less (not including the .TAP extension). This ensures compatibility and makes directory listings more readable on your TS 2068's limited screen space.

**Good filename examples:**
- `zork.tap`
- `adventure.tap`
- `utils.tap`
- `games01.tap`

**Avoid these filename patterns:**
- `my-really-long-adventure-game-collection.tap` (too long)
- `Game$.tap` (special characters can cause problems)
- `GAME.TAP` vs `game.tap` (inconsistent capitalization)

#### Use Consistent Naming Conventions

Develop a consistent naming system and stick to it:

**By category:**
- `games-action.tap`
- `games-puzzle.tap`
- `utils-file.tap`
- `utils-math.tap`

**By source:**
- `magazine01.tap`
- `magazine02.tap`
- `personal01.tap`

**By frequency of use:**
- `daily.tap`
- `weekly.tap`
- `archive01.tap`

### Directory Structure Strategies

#### The Beginner's Approach
Start simple with just a few main directories:
```
/
├── Games/
├── Utilities/
├── Personal/
└── Archive/
```

#### The Enthusiast's Approach
As your collection grows, add more specific categories:
```
/
├── Games/
│   ├── Action/
│   ├── Adventure/
│   ├── Puzzle/
│   └── Educational/
├── Utilities/
│   ├── Programming/
│   ├── FileManager/
│   └── System/
├── Personal/
│   ├── MyPrograms/
│   ├── WorkInProgress/
│   └── Experiments/
└── Archive/
    ├── Magazine/
    └── Old/
```

#### The Collector's Approach
For extensive collections, consider organization by source or era:
```
/
├── Commercial/
│   ├── Timex/
│   ├── ThirdParty/
│   └── Modern/
├── Magazines/
│   ├── SinclairUser/
│   ├── ComputeGazette/
│   └── Others/
├── Homebrew/
│   ├── Contests/
│   ├── Community/
│   └── Modern/
└── Personal/
    └── MyStuff/
```

### SD Card Management

#### Use Quality Hardware
Invest in a good SD card from a reputable manufacturer. Your TS Pico deserves reliable storage, and a quality SD card will serve you well for years.

**Recommended specifications:**
- **Capacity:** 8GB to 32GB (more than enough for thousands of TAP files)
- **Speed Class:** Class 10 or better for best performance
- **Brand:** Stick with well-known manufacturers like SanDisk, Kingston, or Samsung

#### Regular Maintenance

**Weekly maintenance:**
- Check available space with `LOAD "tpi:dir"` from the root directory
- Review and clean up any temporary files
- Ensure important TAP files are properly named and organized

**Monthly maintenance:**
- Backup your SD card to your computer
- Check for and remove any corrupted files
- Reorganize directories if your collection has grown

**Before major changes:**
- Always backup before reorganizing large numbers of files
- Test new organizational schemes with a small subset first
- Keep notes about your organization system

#### Safe SD Card Practices

**Always close files before removing the SD card:**
```
SAVE "tpi:close"
```

**Power down properly:** Turn off your TS 2068 before removing the SD card.

**Handle with care:** SD cards are small and can be easily damaged. Store them in protective cases when not in use.

**Keep backups:** SD cards can fail. Regular backups to your computer ensure you never lose your collection.

### Managing Large Collections

#### Use Multiple SD Cards
If your collection becomes very large, consider using multiple SD cards organized by theme:
- One card for games
- One card for utilities and programming tools
- One card for personal projects
- One card for archives and rarely-used items

#### Create Index Files
For very large collections, consider creating simple text files that list contents:
- Create a TAP file containing a BASIC program that lists all your games
- Keep notes in a computer file about what's on each SD card
- Create "catalog" TAP files that serve as menus for your collection

#### Regular Cleanup
Periodically review your collection:
- Remove duplicate files
- Delete corrupted or non-working TAP files
- Move rarely-used items to archive directories
- Consolidate related small TAP files into larger collections

---

## System Information and Diagnostics

### Keeping Your TS Pico Healthy

Just like any sophisticated piece of equipment, your TS Pico benefits from regular monitoring and maintenance. The system includes comprehensive diagnostic tools that help you understand how your system is performing and identify potential issues before they become problems.

### Comprehensive System Monitoring

#### The System Status Command
```
SAVE "tpi:getinfo"
```

This command is like asking your TS Pico for a complete health report. The information it provides includes:

**Firmware Information:**
- Current firmware version
- Build date and version details
- Compatibility information

**Hardware Status:**
- Board revision and hardware version
- Memory configuration and usage
- SD card information and status

**Current Operations:**
- What file is currently mounted
- Current directory location
- System configuration settings

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
SD Card: 8GB, 2.3GB free
Current File: adventure.tap
Path: /Games/Adventure/
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

### Activity Logging and Monitoring

#### Understanding the Activity Log
```
SAVE "tpi:getlog"
```

The TS Pico maintains a detailed log of everything it does. This log is invaluable for:
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

Verbose mode provides detailed feedback about what the TS Pico is doing behind the scenes. When enabled, you'll see:
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

**SD card optimization:**
- Keep at least 10% of SD card space free for optimal performance
- Organize files into directories to improve access times
- Remove duplicate or corrupted files

**System optimization:**
- Use `SAVE "tpi:close"` to properly close files and free resources
- Restart the system periodically to clear temporary data
- Keep your firmware updated to the latest version

### When to Seek Help

#### Warning Signs

Contact the TS Pico community or support if you notice:
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

Every TS Pico user encounters issues from time to time. This is normal and expected - you're working with sophisticated hardware and software, and occasionally things don't go as planned. The good news is that most problems have simple solutions, and the TS Pico includes many built-in safety features to protect your data and system.

### Basic Troubleshooting Philosophy

**Start simple:** Most problems have simple causes. Check the obvious things first before assuming complex hardware or software issues.

**One step at a time:** Make one change at a time and test the results. This helps you identify exactly what fixed the problem.

**Document what works:** Keep notes about solutions that work for you. You might encounter the same issue again later.

**Don't be afraid to ask for help:** The TS Pico community is friendly and helpful. If you're stuck, reach out for assistance.

### First-Level Troubleshooting

#### When Commands Don't Respond

**Problem:** You type a TS Pico command and nothing happens, or you get an error message.

**First steps:**
1. **Check the LED:** Is the LED on the Raspberry Pi Pico blinking normally?
2. **Test basic connectivity:** Try `LOAD "tpi:dir"` to see if the TS Pico responds at all
3. **Check your typing:** TS Pico commands are case-sensitive and must be typed exactly

**If the LED isn't blinking:**
- Check that your TS Pico is properly seated in its connector
- Ensure your TS 2068 is properly powered on
- Try the TS Reset button to restart the system

**If you get error messages:**
- Read the error message carefully - it often tells you exactly what's wrong
- Check the command syntax against the examples in this manual
- Try the same command again - sometimes temporary issues resolve themselves

#### SD Card Issues

**Problem:** The TS Pico can't see your SD card or reports SD card errors.

**Troubleshooting steps:**
1. **Check physical connection:** Ensure the SD card is fully inserted
2. **Try removing and reinserting:** Sometimes cards need to be reseated
3. **Check the card in a computer:** Verify the SD card works in a regular computer
4. **Check formatting:** Ensure the SD card is formatted as FAT32

**If the SD card works in a computer but not in the TS Pico:**
- Try a different SD card to rule out compatibility issues
- Check that the SD card isn't write-protected
- Ensure the SD card isn't corrupted

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
1. **Check program compatibility:** Some programs may not work perfectly with the TS Pico
2. **Try loading from a different position:** Use FFW/REW to try loading from different blocks
3. **Check TAPDIR:** Verify the program structure looks correct
4. **Test with known-good programs:** See if the problem affects all programs

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

**Problem:** The TS Pico seems to work intermittently or loses connection.

**Connection troubleshooting:**
1. **Check physical connections:** Ensure the TS Pico is firmly seated
2. **Clean the connectors:** Use a dry cloth to clean the edge connector contacts
3. **Check for interference:** Remove other peripherals temporarily
4. **Test different positions:** If using an expansion bus, try different slots

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
3. Test basic TS Pico functionality with `LOAD "tpi:dir"`

**Level 3 - Power Cycle:**
1. Turn off the TS 2068 completely
2. Wait 10 seconds
3. Turn the TS 2068 back on
4. Test TS Pico functionality

**Level 4 - Hardware Check:**
1. Power down the TS 2068
2. Remove and reseat the TS Pico
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

**Try the basics:**
1. Power cycle the system
2. Try different TAP files
3. Test with a different SD card
4. Check physical connections

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

---

## What's Next? Upgrades and Extensions

### The Future Is Bright

Your TS Pico isn't just a storage device - it's a platform for continuous improvement and expansion. The development team has designed it with upgradability in mind, ensuring that your investment will continue to pay dividends as new features and capabilities are developed.

### Firmware Upgrades: Keeping Current

#### Why Upgrades Matter

Firmware upgrades bring:
- **New features:** Additional commands and capabilities
- **Performance improvements:** Faster operation and better reliability
- **Bug fixes:** Resolution of issues discovered after release
- **Compatibility enhancements:** Support for more software and hardware
- **Security updates:** Protection against newly discovered vulnerabilities

#### The Upgrade Process

The TS Pico includes a sophisticated upgrade system that makes updating firmware safe and straightforward. The complete upgrade process is covered in the separate "TS-Pico Firmware Upgrade Instructions" document, but here's an overview of what's involved:

**Preparation phase:**
- Download the upgrade files from the official repository
- Gather the necessary cables and tools
- Set aside time for the complete process

**Hardware phase:**
- Connect the TS Pico to your computer via USB
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

The TS Pico was designed with expansion in mind. The development team has made the hardware designs freely available, encouraging community innovation and customization.

**Available resources:**
- **Complete schematics:** Understanding how everything works
- **PCB layouts:** For creating custom versions or repairs
- **3D printable cases:** Protection and customization options
- **Extension interfaces:** Adding your own hardware

#### Community Hardware Projects

The TS Pico community is actively developing extensions and enhancements:

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

The TS Pico is built on open-source principles. This means you're not limited to what comes in the box - you can modify, enhance, and extend the system to meet your specific needs.

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

The TS Pico project embraces open-source development principles:
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

#### The Reward of Participation

Contributing to the TS Pico project isn't just about giving back - it's about:
- **Learning:** Developing new skills and understanding
- **Networking:** Connecting with like-minded enthusiasts
- **Influence:** Helping shape the future of the project
- **Satisfaction:** Seeing your contributions help others

### Future Directions

#### Planned Enhancements

The development team has outlined several exciting directions for future development:

**Short-term improvements:**
- Enhanced file management capabilities
- Better error handling and recovery
- Improved compatibility with more software
- Performance optimizations

**Medium-term projects:**
- Network connectivity options
- Integration with modern development tools
- Enhanced multimedia capabilities
- Extended memory management

**Long-term vision:**
- Complete vintage computer platform support
- Modern programming environments for vintage hardware
- Educational tools for learning computing history
- Bridge between vintage and modern computing

#### Your Role in the Future

The future of the TS Pico depends on community involvement. Whether you're a casual user who provides feedback or an active developer contributing code, your participation helps ensure that the TS Pico continues to evolve and improve.

**Stay engaged:**
- Follow development discussions
- Try new features as they become available
- Share your experiences with others
- Contribute your ideas and suggestions

The TS Pico represents more than just a storage device - it's a testament to the enduring appeal of vintage computing and the power of community-driven development. By joining this community, you're not just using a product, you're participating in a movement to preserve and enhance computing history.

---

## The TS Pico Community

### More Than Just Users - We're a Family

The TS Pico isn't just a product - it's the centerpiece of a vibrant, welcoming community of vintage computing enthusiasts, developers, educators, and hobbyists. Whether you're a newcomer to vintage computing or a long-time enthusiast, you'll find your place in this community.

### Who We Are

#### Vintage Computing Enthusiasts
People who appreciate the elegance and simplicity of classic computers. They collect, restore, and use vintage machines not just for nostalgia, but because these computers offer a different, often more intimate computing experience.

#### Modern Developers with Vintage Hearts
Programmers and engineers who bring contemporary skills to vintage platforms. They're bridging the gap between old and new, creating modern tools for classic computers.

#### Educators and Students
Teachers and learners who use vintage computers to understand computing fundamentals. The TS Pico provides an excellent platform for education because it makes vintage computing more accessible while preserving the authentic experience.

#### Hobbyists and Tinkerers
People who enjoy understanding how things work and aren't afraid to experiment. They're constantly pushing the boundaries of what's possible with vintage hardware.

### Community Values

#### Helpfulness
No question is too basic, and no problem is too simple. The community believes that everyone started somewhere, and helping newcomers is not just welcome - it's encouraged.

#### Knowledge Sharing
Members freely share their discoveries, solutions, and creations. Whether it's a new programming technique, a hardware modification, or just a great game recommendation, sharing knowledge strengthens the entire community.

#### Preservation
The community is committed to preserving computing history. This means not just keeping old machines running, but also documenting their history, preserving software, and teaching others about their significance.

#### Innovation
While respecting the past, the community embraces innovation that enhances vintage computing. The TS Pico itself is an example of this philosophy - modern technology that enhances rather than replaces vintage computing.

### Where We Gather

#### GitHub Repository
**Primary hub:** https://github.com/TS-Pico-dev/TS-Pico

This is the main development center where:
- **Source code** is maintained and developed
- **Issues** are reported and tracked
- **Discussions** about features and improvements take place
- **Documentation** is collaboratively maintained
- **Releases** are published and announced

**How to participate:**
- **Star the repository** to show support and stay informed
- **Watch for releases** to get notifications about updates
- **Report issues** if you encounter problems
- **Contribute** if you have programming skills

#### Hardware Design Resources
**Board designs:** https://github.com/jburrell7/TSPICO
**Expansion bus:** https://github.com/jburrell7/TS2068_Extender

These repositories contain everything needed to understand, modify, or recreate the TS Pico hardware:
- Complete schematics and PCB layouts
- Bills of materials for building your own
- Assembly instructions and documentation
- Custom modifications and improvements

#### Community Forums and Discussion Groups
Various platforms host ongoing discussions about the TS Pico and vintage computing in general:
- **Topic-specific forums** for detailed technical discussions
- **General chat areas** for casual conversation and quick questions
- **Project showcases** where members share their creations
- **Help sections** for troubleshooting and support

### How to Get Involved

#### For New Users

**Start by introducing yourself:** Most communities have introduction areas where you can share your background and interests. Don't be shy - the community loves meeting new members!

**Ask questions:** The community thrives on helping newcomers. Whether you're stuck on a technical issue or just want to understand how something works, ask away.

**Share your experiences:** Your fresh perspective as a new user is valuable. Share what you find confusing, what works well, and what could be improved.

**Participate in discussions:** Even if you don't have technical expertise, your opinions and experiences matter.

#### For Experienced Users

**Help newcomers:** Share your knowledge and experience with those just starting out. Remember what it was like when you were learning.

**Document your discoveries:** Write guides, create tutorials, or document solutions to problems you've encountered.

**Test new features:** Try beta releases and provide feedback to help improve the system.

**Contribute content:** Share TAP files, create collections, or develop utilities that others can use.

#### For Developers

**Contribute code:** The project welcomes code contributions, whether they're bug fixes, new features, or improvements to existing functionality.

**Review pull requests:** Help maintain code quality by reviewing contributions from others.

**Write documentation:** Technical documentation is always needed and appreciated.

**Mentor others:** Help less experienced programmers learn the codebase and contribute effectively.

### Community Projects and Initiatives

#### Collaborative Development
The TS Pico is developed collaboratively, with contributions from community members around the world. This distributed development model ensures that the project benefits from diverse perspectives and expertise.

#### Educational Outreach
Community members are working on educational materials and programs that use the TS Pico to teach:
- **Computing history:** Understanding the evolution of personal computers
- **Programming fundamentals:** Learning to code on simple, understandable systems
- **Hardware concepts:** Exploring how computers work at a basic level
- **Problem-solving:** Using limitations as creative constraints

#### Preservation Projects
The community is actively working to preserve:
- **Software libraries:** Collecting and organizing vintage software
- **Documentation:** Scanning and digitizing original manuals and materials
- **Knowledge:** Recording the experiences and expertise of veteran users
- **Hardware:** Developing tools and techniques for maintaining vintage equipment

#### Innovation Labs
Community members are exploring cutting-edge applications:
- **Modern connectivity:** Bringing vintage computers online
- **Cross-platform development:** Creating tools that work across different vintage systems
- **Hybrid systems:** Combining vintage and modern components in creative ways
- **Educational platforms:** Developing comprehensive learning systems

### Supporting the Community

#### Financial Support
While the TS Pico project is open-source and free, there are costs associated with:
- **Development infrastructure:** Hosting, tools, and services
- **Hardware development:** Prototypes, testing equipment, and components
- **Community events:** Meetups, conferences, and workshops

**Ways to provide financial support:**
- Purchase TS Pico hardware from official sources
- Contribute to development funds
- Sponsor specific features or improvements
- Support community events and initiatives

#### Non-Financial Contributions
Not everyone can contribute financially, but there are many other valuable ways to support the community:

**Time and expertise:** Volunteer your skills for development, documentation, or support.

**Testing and feedback:** Help improve the system by trying new features and reporting issues.

**Advocacy:** Spread the word about the TS Pico and vintage computing in general.

**Content creation:** Write articles, create videos, or develop educational materials.

### Community Guidelines and Etiquette

#### Be Respectful
Treat all community members with respect, regardless of their experience level or background. Everyone was a beginner once.

#### Stay On Topic
Keep discussions relevant to the TS Pico and vintage computing. Off-topic conversations can happen, but they shouldn't dominate technical forums.

#### Help Others Learn
When answering questions, explain not just what to do, but why. Help others understand the underlying concepts.

#### Give Credit
When sharing code, ideas, or solutions, acknowledge the original contributors. The community values proper attribution.

#### Be Patient
Not everyone communicates in the same way or at the same pace. Be patient with those who are learning or who may not express themselves clearly.

### The Future of the Community

#### Growing Together
As the TS Pico community grows, we're committed to maintaining the values and culture that make it special. This means:
- **Preserving helpfulness** as the community gets larger
- **Maintaining quality** as more people contribute
- **Staying true to our values** as the project evolves
- **Supporting newcomers** even as we tackle advanced topics

#### Global Reach
The TS Pico community is international, with members from many countries and cultures. This diversity is a strength that brings different perspectives and approaches to vintage computing.

#### Intergenerational Knowledge Transfer
One of the most valuable aspects of the community is the connection between people who experienced the vintage computing era firsthand and those discovering it for the first time. This knowledge transfer ensures that important skills and perspectives aren't lost.

### Making Your Mark

Every community member has the opportunity to make a meaningful contribution. Whether you:
- **Answer a newcomer's question**
- **Report a bug that helps improve the system**
- **Create a tutorial that helps others learn**
- **Develop a feature that enhances functionality**
- **Share an interesting discovery or technique**

Your contribution matters and helps make the community stronger.

The TS Pico community is more than just a support network for a vintage computing accessory - it's a gathering place for people who appreciate the art and craft of computing. By joining this community, you're not just getting help with your TS Pico; you're becoming part of a movement to preserve, understand, and extend the golden age of personal computing.

---

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

#### Advanced Features
```
SAVE "tpi:append"                # Enable append mode
SAVE "tpi:tape"                  # Switch to cassette mode
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

### Error Code Reference

| Code | Type | Meaning | Solution |
|------|------|---------|----------|
| 1 | Success | Operation completed normally | None needed |
| 2 | Error | Invalid I/O device | Check command syntax |
| J | TS 2068 | Invalid I/O device | Verify TS Pico connection |

### Memory Management Quick Reference

| Command | Purpose | Parameters |
|---------|---------|------------|
| `memboot` | Set boot ROM slot | `CODE mem,page` (mem: 1=Flash, 2=SRAM; page: 0-15) |
| `memdock` | Set cartridge slot | `CODE mem,page` (mem: 1=Flash, 2=SRAM; page: 0-15) |
| `blkrcv` | Receive data block | `CODE length,offset` (length: bytes; offset: start position) |

### Troubleshooting Quick Steps

1. **Check LED status** - Is it blinking normally?
2. **Test basic connectivity** - Try `LOAD "tpi:dir"`
3. **Check physical connections** - Ensure TS Pico is properly seated
4. **Review error messages** - Read them carefully for clues
5. **Check activity log** - Use `SAVE "tpi:getlog"`
6. **Try TS Reset** - Press reset button if needed
7. **Power cycle** - Turn TS 2068 off and on as last resort

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

### Introduction to External Commands

The TS Pico firmware includes a powerful extension system that allows developers to add custom commands without modifying the core firmware. This system uses external Python modules that integrate seamlessly with the main TS Pico software.

### Understanding the External Command Architecture

#### How External Commands Work

External commands are implemented as Python functions that are called by the main TS Pico firmware when specific command patterns are detected. This architecture provides several benefits:

- **Modularity:** New commands can be added without touching the core system
- **Safety:** External commands run in a controlled environment
- **Flexibility:** Commands can access system resources while maintaining separation
- **Community development:** Multiple developers can contribute commands independently

#### The Command Processing Flow

When you type a TS Pico command, the system follows this process:

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

The external command system makes the TS Pico incredibly extensible while maintaining system stability and safety. Whether you're adding simple utilities or complex applications, this architecture provides the foundation for unlimited creativity and functionality.

---

## Appendix B: Machine Language Flash Programming

### Introduction to Flash Memory Programming

The TS Pico includes sophisticated Flash memory management capabilities that allow advanced users to directly program the onboard Flash memory using machine language routines. This functionality is primarily intended for system developers, firmware engineers, and advanced users who need direct hardware control.

**⚠️ CRITICAL WARNING:** The routines described in this appendix directly manipulate Flash memory hardware. Incorrect use can permanently damage your TS Pico or corrupt system firmware. Only attempt these operations if you have extensive experience with machine language programming and understand the risks involved.

### Understanding the Flash Memory Architecture

#### Flash Memory Organization

The TS Pico's Flash memory is organized into two main 32KB blocks:
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
```

#### Lower Block Flash Programming

**Sector Erase Routine (Lower 32KB)**
Entry point: 0x8020

```assembly
; Flash Update - Lower Block Sector Erase
; Entry: 0x8020
; Erases lower 32KB (8 sectors of 4KB each)

8020    DI                      ; Disable interrupts
8021    PUSH    AF              ; Save registers
8022    PUSH    BC
8023    PUSH    DE
8024    PUSH    HL
8025    LD      A,15            ; Page select value (00001111b)
8027    OUT     (244),A         ; Page in Flash memory
8029    LD      B,8             ; Number of 4KB sectors to erase
802B    LD      HL,0000h        ; Start address (lower 32KB)

802E BACK1:
802E    LD      DE,1000h        ; 4KB sector size
8031    LD      A,170           ; Flash unlock command 1 (0xAA)
8033    LD      (5555h),A       ; Write to unlock address 1
8036    LD      A,85            ; Flash unlock command 2 (0x55)
8038    LD      (2AAAh),A       ; Write to unlock address 2
803B    LD      A,128           ; Sector erase setup command (0x80)
803D    LD      (5555h),A       ; Write to unlock address 1
8040    LD      A,170           ; Flash unlock command 1 (0xAA)
8042    LD      (5555h),A       ; Write to unlock address 1
8045    LD      A,85            ; Flash unlock command 2 (0x55)
8047    LD      (2AAAh),A       ; Write to unlock address 2
804A    LD      A,48            ; Sector erase command (0x30)
804C    LD      (HL),A          ; Write to sector address
804D    ADD     HL,DE           ; Move to next sector
804E    LD      DE,8000h        ; Delay loop counter

8051 WAIT:
8051    DEC     DE              ; Decrement delay counter
8052    LD      A,D             ; Check if delay complete
8053    OR      E
8054    JR      NZ,WAIT         ; Continue delay (≈25ms per sector)
8056    DJNZ    BACK1           ; Repeat for all sectors

8058    LD      B,255           ; Additional delay
805A LOOP:
805A    DJNZ    LOOP            ; Final delay loop

805C END:
805C    XOR     A               ; Clear page selection
805D    OUT     (244),A         ; Page out Flash memory
805F    POP     HL              ; Restore registers
8060    POP     DE
8061    POP     BC
8062    POP     AF
8063    EI                      ; Re-enable interrupts
8064    RET                     ; Return to caller
```

**Byte Write Routine (Lower 32KB)**
Entry point: 0x8066

```assembly
; Flash Update - Lower Block Byte Write
; Entry: 0x8066
; Writes data to lower 32KB Flash memory

8066    DI                      ; Disable interrupts
8067    PUSH    AF              ; Save registers
8068    PUSH    BC
8069    PUSH    DE
806A    PUSH    HL
806B    LD      A,15            ; Page select value (00001111b)
806D    OUT     (244),A         ; Page in Flash memory
806F    LD      DE,8000h        ; Number of bytes to write (32KB)
8072    LD      HL,0000h        ; Start address (lower 32KB)

8075 FLSHWR:
8075    LD      A,170           ; Flash unlock command 1 (0xAA)
8077    LD      (5555h),A       ; Write to unlock address 1
807A    LD      A,85            ; Flash unlock command 2 (0x55)
807C    LD      (2AAAh),A       ; Write to unlock address 2
807F    LD      A,160           ; Program command (0xA0)
8081    LD      (5555h),A       ; Write to unlock address 1

8084 SRAMWR:
8084    IN      A,(14)          ; Get data from TS-Pico
8086    LD      (HL),A          ; Write to Flash memory
8087    LD      A,E             ; Check if done
8088    OR      D
8089    JR      Z,END           ; Jump to end if complete
808B    INC     HL              ; Increment address
808C    DEC     DE              ; Decrement byte count
808D    JR      FLSHWR          ; Continue writing

; End routine same as erase routine above
```

### Using the Flash Programming Routines

#### Entry Points Summary

| Function | Entry Point | Purpose |
|----------|-------------|---------|
| Upper erase | 0x7F58 | Erase upper 32KB (8 sectors) |
| Upper write | 0x7F9E | Write to upper 32KB |
| Lower erase | 0x8020 | Erase lower 32KB (8 sectors) |
| Lower write | 0x8066 | Write to lower 32KB |

#### Calling Convention

**From BASIC:**
```basic
RANDOMIZE USR 32600    # Call upper block erase (0x7F58)
RANDOMIZE USR 32670    # Call upper block write (0x7F9E)
RANDOMIZE USR 32800    # Call lower block erase (0x8020)
RANDOMIZE USR 32870    # Call lower block write (0x8066)
```

**From machine code:**
```assembly
CALL 7F58h    ; Upper block erase
CALL 7F9Eh    ; Upper block write
CALL 8020h    ; Lower block erase
CALL 8066h    ; Lower block write
```

#### Data Source Configuration

The write routines read data from I/O port 14 (`IN A,(14)`). This can be modified to read from other sources:

**Reading from memory:**
```assembly
LD      A,(DATA_SOURCE)    ; Replace IN A,(14)
```

**Reading from a buffer:**
```assembly
LD      A,(IX+0)          ; Read from buffer pointed to by IX
INC     IX                ; Increment buffer pointer
```

### Safety Considerations and Best Practices

#### Pre-Programming Checks

**Verify power stability:** Ensure stable power supply during programming operations.

**Check memory configuration:** Verify correct page mapping before starting operations.

**Backup existing data:** Always backup Flash contents before programming new data.

**Test with small blocks:** Start with single sector operations before attempting full block programming.

#### Error Detection and Recovery

**Verify programming success:**
```assembly
; After programming, verify data
LD      A,(TARGET_ADDRESS)
CP      EXPECTED_VALUE
JR      NZ,PROGRAM_ERROR
```

**Implement timeout protection:**
```assembly
LD      BC,TIMEOUT_COUNT
VERIFY_LOOP:
    IN      A,(STATUS_PORT)
    BIT     7,A              ; Check ready bit
    JR      NZ,PROGRAM_COMPLETE
    DEC     BC
    LD      A,B
    OR      C
    JR      NZ,VERIFY_LOOP
    ; Timeout occurred - handle error
```

#### Recovery Procedures

**If programming fails:**
1. Power cycle the system
2. Attempt to read current Flash contents
3. Re-run erase operation if necessary
4. Retry programming with verified data
5. Contact support if problems persist

### Advanced Flash Programming Techniques

#### Selective Sector Programming

**Programming individual sectors:**
```assembly
; Erase single 4KB sector at address HL
ERASE_SECTOR:
    DI
    LD      A,246           ; Page in Flash
    OUT     (244),A
    
    ; Unlock sequence
    LD      A,170
    LD      (5555h),A
    LD      A,85
    LD      (2AAAh),A
    LD      A,128
    LD      (5555h),A
    LD      A,170
    LD      (5555h),A
    LD      A,85
    LD      (2AAAh),A
    LD      A,48
    LD      (HL),A          ; Erase sector at HL
    
    ; Wait for completion
    CALL    WAIT_ERASE_COMPLETE
    
    XOR     A
    OUT     (244),A         ; Page out Flash
    EI
    RET
```

#### Data Verification Routines

**Comprehensive verification:**
```assembly
VERIFY_FLASH:
    LD      HL,START_ADDRESS
    LD      DE,DATA_BUFFER
    LD      BC,DATA_LENGTH
    
VERIFY_LOOP:
    LD      A,(DE)          ; Expected data
    CP      (HL)            ; Actual Flash contents
    JR      NZ,VERIFY_ERROR
    INC     HL
    INC     DE
    DEC     BC
    LD      A,B
    OR      C
    JR      NZ,VERIFY_LOOP
    
    ; Verification successful
    RET
    
VERIFY_ERROR:
    ; Handle verification error
    ; HL points to failed address
    ; A contains Flash value
    ; (DE) contains expected value
    RET
```

### Integration with TS Pico System

#### Coordinating with Firmware

**Safe programming windows:**
- Perform Flash operations only when the TS Pico firmware is idle
- Use system commands to ensure proper coordination
- Monitor system status before beginning operations

**Resource management:**
- Ensure no conflicting memory access during programming
- Coordinate with file system operations
- Respect system memory allocation

#### Custom Applications

**Creating custom firmware:**
- Use these routines to install custom firmware modules
- Implement failsafe mechanisms for recovery
- Maintain compatibility with existing system functions

**Data storage applications:**
- Store large datasets in Flash memory
- Implement wear-leveling for frequently updated data
- Create custom file systems using Flash storage

### Troubleshooting Flash Programming Issues

#### Common Problems and Solutions

**Programming fails consistently:**
- Check power supply stability
- Verify correct memory page mapping
- Ensure Flash memory isn't write-protected
- Check for hardware conflicts

**Data corruption after programming:**
- Verify programming timing sequences
- Check for electrical interference
- Ensure complete erase before programming
- Verify data source integrity

**System instability after Flash operations:**
- Verify register preservation in routines
- Check interrupt handling during operations
- Ensure proper memory page restoration
- Verify stack integrity throughout operations

The machine language Flash programming capabilities provide powerful tools for advanced system customization and development. However, they require careful attention to detail and thorough understanding of both the hardware and software implications of direct Flash memory manipulation.

---

## Appendix C: Technical Specifications

### Hardware Specifications

#### Raspberry Pi Pico Microcontroller
- **Processor:** Dual-core ARM Cortex-M0+ @ 133MHz
- **Memory:** 264KB on-chip SRAM
- **Flash:** 2MB onboard Flash memory (firmware storage)
- **I/O:** 26 GPIO pins (subset used for TS Pico interface)
- **Communication:** USB 1.1 device interface
- **Power consumption:** Low power design, powered from TS 2068

#### TS Pico Memory Configuration
- **Flash Memory:** 512KB high-speed Flash storage
  - System firmware and cached files
  - User-programmable sections available
  - Organized in 4KB erasable sectors
- **SRAM:** 512KB static RAM
  - High-speed temporary storage
  - Fully available to user applications
  - Battery-backed operation (when available)
- **SD Card Interface:** Standard SD/SDHC card support
  - FAT32 file system
  - Up to 32GB capacity tested
  - Hot-swappable with proper procedures

#### Physical Specifications
- **Board dimensions:** Compatible with TS 2068 expansion format
- **Connectors:** 
  - TS 2068 edge connector (direct or expansion bus)
  - Micro-USB (firmware updates only)
  - SD card slot (standard size)
- **Indicators:** LED status indicator on Raspberry Pi Pico
- **Controls:** Reset buttons for TS and Pico systems

### Software Specifications

#### Firmware Architecture
- **Language:** MicroPython 3.4+ compatible
- **Real-time capabilities:** Hardware timer support
- **File systems:** FAT32 on SD card, internal Flash file system
- **Communication:** Custom protocol with TS 2068
- **Extensibility:** External command module support

#### Command Interface
- **Command syntax:** Extended LOAD/SAVE command structure
- **Response format:** Compatible with TS 2068 expectations
- **Error handling:** Comprehensive error reporting and recovery
- **Logging:** Full activity logging with timestamps

#### Performance Characteristics
- **File access time:** Sub-second TAP file mounting
- **Data transfer rate:** Optimized for TS 2068 timing requirements
- **Cache efficiency:** Intelligent Flash memory caching
- **Power efficiency:** Low-power operation with sleep modes

### Compatibility Information

#### TS 2068 Compatibility
- **Models supported:** All TS 2068 variants
- **Memory requirements:** No additional TS 2068 memory required
- **ROM compatibility:** Works with all known ROM versions
- **Peripheral compatibility:** Compatible with most TS 2068 peripherals

#### File Format Support
- **TAP files:** Full TS 2068 and ZX Spectrum TAP format support
- **DCK files:** Cartridge and dock image support
- **ROM files:** System ROM and cartridge ROM images
- **BIN files:** Raw binary data files
- **Directory structure:** Unlimited nested subdirectories

#### ZX Spectrum Compatibility
- **Spectrum 48K mode:** Full compatibility mode available
- **TAP file compatibility:** Most Spectrum TAP files supported
- **Keyboard mapping:** Automatic adjustment for Spectrum software
- **Memory mapping:** Spectrum-compatible memory configuration

### Environmental and Operating Conditions

#### Operating Environment
- **Temperature range:** 0°C to 40°C (32°F to 104°F)
- **Humidity:** 10% to 90% non-condensing
- **Power supply:** 5V DC from TS 2068 (approximately 200mA)
- **Storage temperature:** -20°C to 60°C (-4°F to 140°F)

#### Reliability and Durability
- **MTBF (Mean Time Between Failures):** >50,000 hours
- **Flash memory endurance:** >100,000 write/erase cycles per sector
- **SD card lifespan:** Dependent on card quality and usage
- **Expected service life:** >10 years with normal use

### Performance Benchmarks

#### File Operation Performance
- **Directory listing:** <100ms for typical directories
- **TAP file mounting:** <200ms for files up to 1MB
- **Program loading:** 5-10x faster than cassette tape
- **File copying:** Dependent on SD card speed class

#### Memory Usage
- **Firmware overhead:** <128KB Flash, <64KB SRAM
- **Cache efficiency:** 90%+ hit rate for frequently accessed files
- **Available user space:** >384KB Flash, >448KB SRAM
- **SD card overhead:** <1% for file system structures

#### Power Consumption
- **Idle mode:** <50mA from TS 2068 power supply
- **Active operation:** <150mA during file operations
- **Sleep mode:** <10mA when TS 2068 is inactive
- **Total system impact:** <3% increase in TS 2068 power consumption

### Upgrade and Maintenance

#### Firmware Updates
- **Update mechanism:** USB-based firmware loading
- **Backup and recovery:** Automatic firmware backup
- **Version control:** Semantic versioning (major.minor.patch)
- **Compatibility checking:** Automatic version compatibility verification

#### Maintenance Requirements
- **Periodic maintenance:** SD card organization and cleanup
- **Firmware updates:** Check quarterly for updates
- **Hardware cleaning:** Annual connector cleaning recommended
- **Backup procedures:** Regular backup of important files

#### Diagnostic Capabilities
- **Built-in diagnostics:** Comprehensive system health monitoring
- **Performance monitoring:** Real-time performance metrics
- **Error logging:** Detailed error tracking and reporting
- **Remote diagnostics:** Community support for troubleshooting

### Safety and Regulatory Information

#### Electrical Safety
- **Overcurrent protection:** Built-in current limiting
- **ESD protection:** Electrostatic discharge protection on all I/O
- **Reverse polarity protection:** Protection against incorrect connections
- **Thermal protection:** Automatic thermal management

#### Regulatory Compliance
- **CE marking:** European Conformity for electronic devices
- **FCC compliance:** Federal Communications Commission (Class B)
- **RoHS compliance:** Restriction of Hazardous Substances directive
- **Lead-free construction:** RoHS-compliant lead-free manufacturing

#### User Safety Guidelines
- **Installation safety:** Always power down before installation
- **Handling precautions:** Avoid static electricity damage
- **Operating limits:** Stay within specified environmental conditions
- **Emergency procedures:** Safe shutdown and recovery procedures

### Development and Extension Information

#### Hardware Development
- **Schematics available:** Open-source hardware design
- **PCB files:** Complete manufacturing files available
- **Component specifications:** Full bill of materials provided
- **Extension interfaces:** GPIO access for custom modifications

#### Software Development
- **Source code:** Available under open-source license
- **Development tools:** MicroPython development environment
- **API documentation:** Complete programming interface documentation
- **Community contributions:** Guidelines for contributing modifications

#### Technical Support
- **Documentation:** Comprehensive user and developer documentation
- **Community forums:** Active user and developer community
- **Issue tracking:** GitHub-based issue tracking and resolution
- **Professional support:** Commercial support options available

-----

*This manual covers TS-Pico firmware version 1.2 and is current as of April 2025. For the most up-to-date information, documentation, and firmware releases, visit the official GitHub repository at https://github.com/TS-Pico-dev/TS-Pico*

*The TS-Pico project is developed and maintained by a community of volunteers dedicated to preserving and enhancing vintage computing experiences. We encourage participation, feedback, and contributions from users of all skill levels.*