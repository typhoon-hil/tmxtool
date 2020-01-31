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

As of 1/31/2020, the tmxtool can be used to process an entire directory filled with pairs of files. The pairs must be named the same except for the language. The language of the files must be at very end of the filename (but before the file extension), and in the form of '-xy', so for example, one directories content would look like:
> c:/user/files/
> translate-this-en.srt, translate-this-de.srt, hello-en.srt, hello-de.srt
Processing this directory can be done using the command pattern:
> python /path-to-tmx-tool/tmxtool.py directory-path source-language
So one example would look like:
> python /path-to-tmx-tool/tmxtool.py "c:/user/files/" "en"

This is a fast fix, and there could be LOADS of errors, so be advised to follow all guidelines from above ...
