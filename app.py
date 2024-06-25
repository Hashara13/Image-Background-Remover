from rembg import remove
import easygui
from PIL import Image

inputFile = easygui.fileopenbox(title="Import File")
exportFile = easygui.filesavebox(title="Export File")

if inputFile and exportFile:

    input_img = Image.open(inputFile)
    output_img = remove(input_img)
 
    output_img.save(exportFile)
    print("Background removed and image saved successfully.")
else:
    print("File selection was canceled.")
