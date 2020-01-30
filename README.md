## Typhoon HIL TMX Tool

The TMX Tool is a script used to join two .srt files and generate a tmx file.

It can be used by running the command: python (path to project directory)\tmxtool.py (path to source .srt file) (source language) (path to translation file) (translation language)

For example:
> tmxtool.py is located in C:\user\tools\
>
> Source .srt file is located in C:\user\tools\example\source-en.srt
>
> Translation .srt file is located in C:\user\tools\example\translation-de.srt
> 
> The command will then look like:
> python C:\user\tools\tmxtool.py C:\user\tools\example\source-en.srt en C:\user\tools\example\translation-de.srt de
>
The output of the script is saved in the directory called 'output' that is created in the same directory where tmxtool.py is located.
So for the example above, the output directory would be created in C:\user\tools\output\ and one of the resulting .tmx files 
would be named 123419023.201947.tmx or some-such (the name of the file is generated using the time at which the file is generated).
