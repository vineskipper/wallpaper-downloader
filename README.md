# Wallpaper Downloader (WIP)
## Description
A simple program that downloads, and stores files from links in a text file.

## Usage
(WIP)

**Optional arguments:**
* (WIP)

## Format Guide
- All entries should be written on seperate lines
- Directory names should be preceeded by an at sign ("@") with no spaces between the at sign and the first character of the directory name (unless the space is an intended part of the directory name)
- Links should include their web protocol (e.g: "https://") and be seperated from their intended file name by a space and a comma (" , "). **Be sure that the link is a file link**.
- Comments must begin with ":-" and must be placed either at the end of a line, or on a seperate line.
- While all entries must be on a seperate line, a blank line between each entry is not required.

**Example file:**
```text
@Directory name one
https://images.pexels.com/photos/31203664/pexels-photo-31203664.jpeg , Галина Ласаева :- valid comment position
https://images.pexels.com/photos/34423216/pexels-photo-34423216.jpeg , WRITE ONDANDELIONS

:- valid comment position

@Directory name two
https://images.pexels.com/photos/34375868/pexels-photo-34375868.jpeg , Memet Öz
https://images.pexels.com/photos/34533069/pexels-photo-34533069.jpeg , Daniel J. Schwarz
```

## Upcoming Features (WIP)
### Automatic formating for directory and file names
This will include file extension addition to file names. These features will not be enabled by default.

### Interactive mode
This will run the program with a TUI that includes image displays, file and directory name changing, and a chance to manually select which files to download.

### Silent mode
This will run the program without displaying any errors that were encountered during runtime. It will instead store any error found in a log file for later use.

### Configuration Files
Self-explanatory.

## Origin
I had the idea when I was getting new wallpapers, because:

>1. After a while it became annoying to download, rename, and then choose the directory to store the files in; and
>2. I couldn't download all the files at the time I was viewing them, and I wanted a way to remember the files so I could download them at the later time.

I ended up just storing the image links in a text file, and, because I didn't want to have to look at each image again to come up with descriptive names for them, wrote down their names in the text file.

Later when I wanted to download the files, I realized could've just solved all the problems listed above by creating this program.