# PDF Batcher
PDF Batcher is a small script that uses `PIL` to create a single PDF file from images within a folder and giving the final result PDF the name of the image's parent folder. This script was made with the intention to bulk create PDF files from scanned lineart manga images without having to do this manually in a third-party program. The script will convert `.png` and `.webp` files to `.jpg` before creating the PDF.

## Setup
In order for **PDF Batcher** to work, you need to install [Python](https://www.python.org/). After installing Python, users must also install `PIL` using the following command:
```
$ pip install Pillow
```

## Where to put the files?
- The script must be in the root repository folder.
- The images that are to be converted must be in a sub-directory in `/Images`. (i. e. `/Images/My Book of Fairy Tales/` (the name of the folder will be the name of the PDF)
- The finished PDF files will be in the `/PDF` directory.

## Visualisation
![PDF Batcher visualised](https://i.imgur.com/nhjMymG.png)
