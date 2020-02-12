## Typhoon HIL TMX Tool ![typhoon-logo](https://www.typhoon-hil.com/trac/chrome/site/typhoon.png)

The TMX Tool is a script used for executing operations related to *.tmx* files.

These instructions are update each time there is a new version of the tool/new 
commands added to the tool.

---

#### - 12. FEB. 2020.
Tmx tool got it's own Graphical User Interface. 

The gui has a help menu in each panel that does something, 
so no help will be posted on this README. 
Opening the 'About' panel in the GUI will show the address and
 what to do if there are any errors, and how to support the project.

The gui can be ran using the "run.bat" file. If any problems occur using this file
or the file simply does not run, call your local IT or software colleagues and ask for help.

If all else fails, send a mail to milan.djurisic@typhoon-hil.com and ask for help.

---
#### - Long ago ..
All the available commands are listed below with examples:

*  **-help**
    * **parameters**: none
    * **description**: Displays all possible commands and their parameters to the user.
    * **example**: python tmxtool.py -help

* **-mktmx**
    * **parameters**:
        * _(1)_: 'path-to-source-file.srt' 'source-language' 'path-to-translation-file.srt' 'translation-language' 
        * _(2)_: 'path-to-directory' 'source-language'
    * **description**: 
        * _(1)_: Creates a .tmx file that is based on the provided .srt files and their languages. The tmx file is saved with a generated name. The location of the file is displayed when the script is finished.
        * _(2)_: Creates .tmx files using file pairs from the specified directory. In order for a .tmx to be generated, there has to be a pair of files that are named the same, except for the last three characters, which need to be in the form of '-XY', where the XY are the language abbreviations of the file (eg. EN or DE). The resulting .tmx file is named the same as the pairs prefix (before the -XY). This is done for all pairs found in the directory.
    * **example**: 
        * python tmxtool.py "C:/users/file-1.srt" en "C:/users/some-other-file-2-hello.srt" de
        * python tmxtool.py "C:/users/srt-files/" en
    

* **-mkvtt**
    * **parameters**:
        * _(1)_: 'path-to-tmx-file.tmx' 'language-to-process'
        * _(2)_: 'path-to-directory' 'language-to-process'
    * **description**: 
        * _(1)_: Creates a .vtt file based on the provided path to the tmx file, extracting all items that are marked with the provided language.
        * _(2)_: Does the same as _(1)_, but for each .tmx file found in the provided directory.
    * **example**:
        * python tmxtool.py -mkvtt "C:/users/file1.tmx" en
        * python tmxtool.py -mkvtt "C:/users/documents/translations/" de
