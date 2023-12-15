# Music Scales and Diatonic Chords Generator (web version)
#### Video Demo:  https://youtu.be/RHHrZnS_mzU
#### Description: Web interface to compute, show and play music scales and diatonic chords, or chords/triads.

# INTRODUCTION

This is my final project for the CS50x course. It is a followup to my [final project for the CS50P course](https://github.com/antoine-reid/cs50p).

This is a web application that is used to learn about music theory, specifically the key signatures and corresponding scales (major, natural minor, harmonic minor and melodic minor), along with the diatonic chords for each key. 

There is also a specific page to explore the chords (triads) such as major chords, minor chords, diminished chords and augmented chords.

The main page (scales) shows a Circle of Fifths, which is a very common way of displaying the key signatures and corresponding chords, in a visual manner.

This web application provides an HTML/CSS/JavaScript frontend and uses a backend written in Python and Flask. A fair portion of the backend code is implemented in the Music_Theory class, which I originally developped for [my CS50P final project](https://github.com/antoine-reid/cs50p).

This project *is* the implementation of the complete web frontend.

This application uses JavaScript to dynamically update the pages when the user makes a selection (key signature or chord). The images are SVG files and some objects are dynamically updated by the JavaScript code. Some of the changes are implemented using my own JS code, other changes are done using JavaScript libraries.

Another feature implemented using a JavaScript library allows the audio playback of the notes and chords.

The application can be seen in action [here](https://scales-and-chords.onrender.com/). Please be patient, it can take some time for the application to auto-deploy if it hasn't been used in a while.

***

# PROJECT FILES AND SOURCE CODE ORGANIZATION

## File: ```README.md```

This document.


## File: ```requirements.txt```

This file contains a list of Python packages (installable via ```pip```), which must be present for the code to run.

Here are the required packages:
- ```Flask```
- ```pytest```

The ```gunicorn``` package is also listed, as a requirement for the ```render.com``` hosting.

## Python source code

### File: ```app.py```

This is the main entry point for the application backend. It uses Flask and returns either HTML documents for the pages, or JSON responses for the AJAX calls. Most of the heavy lifting is done by the Music_Theory class, as described below.

#### Top-level functions

The top-level functions in the app.py file are:
- ```returns_json()```: this creates a new decorator, used to indicate which functions return a JSON response. The decorator adjusts the response's content-type.
- ```after_request()```: this function adds HTTP headers to every response, to ensure that the browser does not cache any of the responses
- ```index()```: this function is called for the ```/``` route and presents the main page, using the ```scales.html``` template
- ```chords_page()```: this function is called for the ```/chords``` route and presents the chords page, using the ```chords.html``` template
- ```about_page()```: this function is called for the ```/about``` route and presents the About page, using the ```about.html``` template
- ```scale()```: this function is called via AJAX for the ```/scale/<s>/<t>``` route and returns a JSON array, containing the notes for the ```<s>``` scale, type ```<t>``` (eg: ```G``` ```harmonic minor```)
- ```diatonic_chords()```: this function is called via AJAX for the ```/diatonic_chords/<s>/<t>``` route and returns a JSON array, containing the diatonic chord names for the ```<s>``` scale, type ```<t>```  (eg: ```C``` ```harmonic minor```)
- ```chord()```: this function is called via AJAX for the ```/chord/<chord>``` route and returns a JSON array, containing the notes that compose the ```<chord>``` triad (eg: ```Gm+```)

### File: ```music_theory.py```

This file implements the Music_Theory class, where all the computation is being done for the scales and chords. This is pure Python code, which uses only the ```re``` package for some text manipulation, using regular expressions (regexes). The code also uses the ```typing``` package, in order to define type hints, which can be checked with ```mypy```.

#### Class: ```Music_Theory```

This class implements all the methods used by this application, to compute the supported scales and chords.

Since there is no state maintained between any of the calls, there is no need to instantiate an object from this class. All the functions are implemented as class methods, using the ```@classmethod``` decorator. Some of the methods are not meant to be called directly by outside code, but only from other class methods within the Music_Theory class. Those private methods have names that begin with ```_```.

The class also contains some class variables (lists and dictionaries), with data that is used by all the methods in the class.

Here is a list of the class variables:
- ```ENHARMONIC_NOTES```: this dict contains enharmonic equivalents, for example ```C♯``` is equivalent to ```D♭```.
- ```CHROMATIC_SCALE```: this dict contains two chromatic scales, both starting with ```C```; one scale uses sharp notes, the other uses flat notes.
- ```MAJOR_SCALES```: this dict contains two lists of scales (key signatures in major); one list contains all the scales that use sharps, the other list contains the scales that use flats.
- ```MINOR_SCALES```: this dict contains two lists of scales (key signatures in minor); one list contains all the scales that use sharps, the other list contains the scales that use flats.
- ```SCALE_CHORD_QUALITIES```: this dict contains lists of lists with chord qualities for each degree in the supported scales. For example, in a major key signature, degrees ```I```, ```IV``` and ```V``` use major chords, degrees ```ii```, ```iii``` and ```vi``` use minor chords and degree ```vii``` uses a diminished chord.
- ```SUPPORTED_SCALES```: this list contains the types of scales currently supported: ```major```, ```minor```/```natural minor```, ```harmonic minor``` and ```melodic minor```.
- ```INTERVALS```: this dict contains lists with the numeric intervals (half steps) between each note, for all our supported scales. For example, in ```major```, the intervals are ```2, 2, 1, 2, 2, 2, 1```, which in music is often written ```W - W - H - W - W - W - H``` (W for whole step, H for half step).

Here is a list of the class methods:
- ```_get_enharmonic_note()```: this method is used to find an enharmonic equivalent for one note, for an expected note name. This also covers some special edge cases like double-sharps and double-flats. For example, ```E``` could be called ```F♭``` or ```D♯♯``` depending on the expected note.
- ```_get_next_expected_note()```: this method returns the next expected note name. This makes sure that every note *name* will be unique and consecutive in our scales and also loops back to ```A``` after ```G```.
- ```_get_intervals()```: this method is used to obtain the list of intervals for the requested scale type; it also substitutes ```natural minor``` for ```minor``` (alias).
- ```_get_note_position()```: this method finds the numeric position (index) in the specified scale, for a specified note.
- ```get_scale()```: this is one of the main methods. It returns a list containing the exact notes (including accidentals) for any of the supported scales, for the requested scale and type (key signature). Internally, it uses many of the other class methods.
- ```get_diatonic_chords()```: this is another important method. It returns a list containing the chord names (including qualities) for each degree of the specified scale.
- ```get_chord_notes()```: this method returns a list of notes that compose a specified chord.
- ```_sharpen()```: this method is used to raise a note by a half step (adding ```♯``` or removing ```♭``` as appropriate).
- ```_flatten()```: this method is used to reduce a note by a half step (adding ```♭``` or removing ```♯``` as appropriate).
- ```pretty_display()```: this method is used to produce a nicer output for chord names, with proper symbols for diminished and augmented chords. It can also optionally add some text suffixes for minor, diminished and augmented chords, when called in ```verbose``` mode. This method is implemented in the class and correctly tested, but unused in this current project. This project uses correct symbols in SVG files, or features of VexFlow to draw accidentals and chord names.


### File: ```test_music_theory.py```

This file implements all the test functions and uses ```pytest``` to execute the tests.

Here is a list of test functions implemented in this file:
- ```test_get_scale()```: this function tests the ```Music_Theory.get_scale()``` method, with over 60 different calls, and validates the output of each call. This includes key signatures that return notes with double-sharps or double-flats.
- ```test_get_diatonic_chords()```: this function tests the ```Music_Theory.get_diatonic_chords()``` method, with over 70 different calls, and validates the output of each call. This includes validating the signatures that contain chords named with double-sharps or double-flats and also validates the chord qualities (major, minor, diminished, augmented).
- ```test_get_chord_notes()```: this function tests the ```Music_Theory.get_chord_notes()``` method, with almost 100 different calls, and validates the output of each call. This includes chords with double-sharps and double-flats, and chords of various qualities.
- ```test_pretty_display()```: this function tests the ```Music_Theory.pretty_display()``` for different chords, testing each chord quality. Tests are done with and without verbose mode.
- ```test_get_enharmonic_note()```: this function tests the ```Music_Theory._get_enharmonic_note()``` method.
- ```test_get_next_expected_note()```: this function tests the ```Music_Theory._get_next_expected_note()``` method, including expected exceptions.
- ```test_get_intervals()```: this function tests the ```Music_Theory._get_intervals()``` method, including expected exceptions.
- ```test_get_note_position()```: this function tests the ```Music_Theory._get_note_position()``` method, including cases where the note is either found or not found.
- ```test_sharpen()```: this function tests the ```Music_Theory._sharpen()``` method, including calling it multiple times in cascade and validating the expected result.
- ```test_flatten()```: this function tests the ```Music_Theory._flatten()``` method, including calling it multiple times in cascade and validating the expected result.


## HTML templates and CSS

### File: ```templates/layout.html```

This is the main template file, which all the other templates extend. This is where the external JavaScript libraries are loaded, so they become available on all pages. 

The main CSS file, ```static/css/styles.css``` is also linked here and is used globally throughout the pages. 

There is also a global JavaScript script (```static/js/project.js```) which is loaded here. The script contains variables and functions that are used throughout the application.

This template also includes a responsive ```Bootstrap``` ```Navbar```, which appears and is identical on all pages.

This template also defines blocks called ```title``` and ```main```, to let other templates that extend it provided a page title, in addition to the main contents of the page.

### File: ```templates/scales.html```

This template extends the ```templates/layout.html``` template and is used for the ```/``` page.

It displays a Circle of Fifths diagram, a reset link, a form to let the user select a key signature, and two staves with notes and chords, respectively.

This is a responsive page. On a wide browser window, the diagram is on the left side, and the form and staves appear on the right side. On a smaller screen resolution, the form and staves appear underneath the diagram.

Besides each staff, a play button is present to let the user trigger the audio playback of the notes or chords.

This page is dynamic. Some of the objects automatically update or refresh when the user makes a different selection in the form. In particular, the background colors of the cells in the diagram automatically update to indicate the diatonic chords and qualities, and the two staves also automatically update with the correct notes and chords.

The play buttons play the notes and chords for the selected key signature, the notes update automatically when the selection is changed.

The page automatically initializes with the ```C Major``` scale selected.

### File: ```templates/chords.html```

This template extends the ```templates/layout.html``` template and is used for the ```/chords``` page.

It displays a reset link, a form to select a chord (root note and quality), a staff with the arpeggiated notes and the complete chord, and a play button to listen to the results. The form also includes a checkbox to allow adding an extra root note, one octave higher.

This page is dynamic. The staff automatically refreshes when the user makes a different selection in the form.

The page automatically initializes with the ```C Major``` chord selected, without an additional root note (one octave higher) option selected.

### File: ```templates/about.html```

This template extends the ```templates/layout.html``` template and is used for the ```/about``` page.

It displays a brief description of the application and a list of tools, components and libraries used to build the application.

A link is provided for each of the tool, component and library listed.


## JavaScript source code

### File: ```static/js/project.js```

This is the main JavaScript file, loaded by the ```layout.html``` template. Therefore, all the variables and functions defined in this file are available in all pages.

The JavaScript code initializes a few variables, used for calls to the ```VexFlow``` and ```WebAudioFont``` libraries.

Here are the functions defined in this JavaScript file:
- ```piano()```: function used to prepare a specific piano note (sample, pitch, gain and duration) for playback via ```WebAudioFont```.
- ```playPiece()```: function used to execute the playback of a previously-prepared list of notes or chords.
- ```start_stop_playback()```: function used to toggle the sound playback between the play and stop states. 
- ```start_playback()```: function used to start the audio playback, dynamically change the play button image to a stop button image, and set a timer to call ```stop_playback()``` once the playback has completed.
- ```stop_playback()```: function used to stop the audio playback if it is still in progress, and dynamically change the stop button back to a play button image.
- ```get_chords()```: async function used to issue an AJAX request to the backend, to fetch the list of diatonic chords for a specified scale.
- ```get_scale()```: async function used to issue an AJAX request to the backend, to fetch the list of notes for a specified scale.
- ```get_chord()```: async function used to issue an AJAX request to the backend, to fetch the list of notes that compose a specified chord.
- ```convert_individual_notes_to_vexnotes()```: function used to convert an array of individual notes (eg: scale) to vexnotes objects, used for adding notes to a ```VexFlow``` staff. It returns an array with two elements. The first element contains an array of ```StaveNotes``` objects and the second element contains the octave number of the last note (useful when chaining calls).
- ```convert_chords_to_vexnotes()```: function used to convert an array of chords to vexnotes objects, used for adding chords to a ```VexFlow``` staff. It returns an array with two elements. The first element contains an array of arrays of ```StaveNotes``` objects and the second element contains the octave number of the root note of the last chord (useful when chaining calls).
- ```convert_single_chord_to_vexnotes()```: function used to convert a single chord to an array of vexnotes objects. It can also add an extra root note (one octave higher) via one of the arguments. It returns an array with two elements. The first element contains an array of ```StaveNotes``` objects and the second element contains the octave number. This function is called whenever a chord needs to be converted to a "stack" of vexnotes, to avoid duplicating code.
- ```arpeggiate_single_chord_to_vexnotes()```: function used to arpeggiate a chord. It prepares individual vexnotes using the notes from the chord, then adds the chord itself. It can also optionally add an extra root note (one octave higher), via one of the arguments. If the extra note is not requested, the function instead adds a quarter rest at the beginning of the sequence, to always generate exactly 8 beats.
- ```prepare_individual_notes()```: function used to convert an array of individual notes (eg: scale) to piano notes, used for audio playback via ```WebAudioFont```.
- ```prepare_chords_notes()```: async function used to convert an array of chords to piano notes, used for audio playback via ```WebAudioFont```. 
- ```prepare_single_chord_notes()```: async function used to convert a single chord to piano notes, used for audio playback via ```WebAudioFont```. The chord will contain a stack of three notes. Optionally, an extra root note (one octave higher) can be added, via one of the arguments. This function is called whenever a chord needs to be converted to a "stack" of piano notes, to avoid duplicating code.
- ```arpeggiate_single_chord_to_notes()```: async function used to arpeggiate a chord. It prepares individual piano notes using the notes from the chord, then the chord itself. It can also optionally add an extra root note (one octave higher), via one of the arguments.
- ```note_value()```: function used to calculate the pitch for a given note (including accidentals) and the requested octave.

### File: ```static/js/scales.js```

This JavaScript file is loaded only by the ```scales.html``` template. 

The code initializes a few variables that are specific to this page, specifically for the colors and borders adjustments applied to the circle of fifths diagram.

Here are the functions defined in this JavaScript file:
- ```all_highlights_off()```: function used to clear all the cell highlights in the circle of fifths diagram. The background colors are cleared and the borders' line thickness is reset to the default value.
- ```highlight_cells()```: function used to highlight specific cells in the diagram, with specific colors used to identify major, minor, diminished and augmented chords.
- ```execute_form()```: function called to highlight the correct cells in the diagram and to update the notes and cell staves, based on the form selection. The variables containing the individual notes and chords (pitches) are also updated, to be ready for audio playback by ```WebAudioFont```.
- ```draw_scale_staff()```: function called to dynamically update the scale staff (with individual notes), using ```VexFlow```.
- ```draw_chords_staff()```: function called to dynamically update the chords staff, using ```VexFlow```.

These JavaScript functions call the functions defined in the ```project.js``` file, to obtain the list of notes and chords. There is also a conversion performed on the chords names in order to locate the appropriate cells in the diagram. Since the SVG for the diagram is included (inline) in the HTML, the JavaScript code can access the objects in the DOM via their ```id``` fields, to adjust the ```style``` element. This is used to change the ```fill``` color and the ```stroke-width```.

The ```execute_form()``` function is also called once, when the page has finished loading.

The code also adds Event Listeners on the form elements, calling ```execute_form()``` again, every time an element is changed.

### File: ```static/js/chords.js```

This JavaScript file is loaded only by the ```chords.html``` template. 

Here are the functions defined in this JavaScript file:
- ```execute_form()```: function used to update the notes and chord in the staff, based on the form selection. The variable containing the notes (pitches) is also updated, to be ready for audio playback by ```WebAudioFont```.
- ```draw_arpeggiated_chord_staff()```: function called to dynamically update the chord staff (with both individual notes and the chord), using ```VexFlow```.

These JavaScript functions call the functions defined in the ```project.js``` file, to obtain the list of notes for the selected chord.

The ```execute_form()``` function is also called once, when the page has finished loading.

The code also adds Event Listeners on the form elements, calling ```execute_form()``` again, every time an element is changed.


## Image files

### File: ```static/images/inkscape/Circle_of_Fifths_Inkscape.svg```

This is the most complex image of the whole application. It is used to represent the Circle of Fifths, as seen on the main page.

The outer ring represents major chords and derivatives (eg: augmented). The inner ring represents minor chords and derivatives (eg: diminished).

Each "cell" is designed as a closed loop in the SVG (using lines and arcs) and has a unique "id" tag. Each cell also contains the name of the key (chord), sometimes with two different names that indicate the same pitch (eg: F♯ and B♭).

This file is included (inline) in the HTML code, using a Jinja ```{% include '...' %}``` directive. Using the ```id``` tags of the various shapes, the JavaScript code can find the cells in the DOM and modify properties such as the background color and line thickness.

This allows updating the visual representation of the Circle of Fifths without having to reload the page or the SVG.

This is the original Inkscape document, with all the attributes intact.

### File: ```templates/Circle_of_Fifths.svg```

This is the modified version of the "Circle_of_Fifts_Inkscape.svg" file as described above. This is a slightly modified version of the original SVG file, with a ```class="img-fluid"``` attribute added and a lot of unnecessary tags and attributes removed. Those were tags and attributes that were useful for the Inkscape application, but which are unnecessary in an HTML context.

The resulting file is approximately 13% smaller, which should improve loading time. The main reason to remove those tags and attributes was to take care of warnings found when the page was analyzed using the ```W3C Markup Validation Service```.

Since this file gets included (inline) in the HTML page via a Jinga include directive, it has to be located in the ```templates/``` sub-directory.

### File: ```static/images/main-logo.svg```

This is an SVG file created with Inkscape, used as the "brand" in the ```Bootstrap``` ```Navbar```. It uses a simplified circle of fifths (without text) and an example staff with chords.

### File: ```static/images/play.svg```

This is a small and simple SVG image, drawn using Inkscape. It is designed to look like a "Play" button and is used everywhere a sound playback feature has been implemented. Clicking on a play button calls a JavaScript function and starts audio playback using ```WebAudioFont```.

### File: ```static/images/stop.svg```

This is another small and simple SVG image, also drawn using Inkscape. It is designed to look like a "Stop" button and has the same size as the play button. When audio playback is started, the ```play.svg``` button is dynamically replaced by ```stop.svg``` using JavaScript. 

If the user clicks on the stop button before the playback is over, playback stops. Whenever the playback is done (either by playing all the notes, or by the user clicking on the stop button), the ```stop.svg``` image is dynamically replaced by ```play.svg``` using JavaScript. This indicates to the user that playback has completed and can be started again.

***

# EXTERNAL LIBRARIES

## Bootstrap

> Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains HTML, CSS and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
>> (Wikipedia)

This project uses ```Bootstrap``` version 5.2.3. This is useful to generate the Navbar and the general layout of the pages. 

In particular, it made it relatively easy to develop a responsive application, which works in various resolutions and screen sizes, using the ```d-flex``` and ```flex-wrap``` classes for example.

[Link for Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

## Flask

> Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
>> (Wikipedia)

The backend is developed in ```Python``` and uses the ```Flask``` package. This allows the use of the ```Jinja``` templating system to dynamically build the ```HTML``` pages, ensuring the navbar will be identical in all pages, for example. 

Using ```Flask```, routes have been defined for all the pages that can be requested by the user.

Additional routes have also been defined for the URLs used by the JavaScript code (using ```AJAX```) to ask the backend to compute and return raw data in ```JSON``` format. This is used to generate the notes and diatonic chords for a specified key signature, and the composition of chords (triads).

[Link for Flask](https://flask.palletsprojects.com/en/3.0.x/)

## WebAudioFont

> WebAudioFont is a set of resources and associated technology that uses sample-based synthesis to play musical instruments in the browser.
>> (WebAudioFont on github)

This is an open-source ```JavaScript``` library, which is used to playback notes and music directly in the web browser. It uses wavetable synthesis and has an extensive sound library. It can be used to play drums and percussions, string instruments, choirs and so on. For this application, a piano sound has been selected.

This library also provides support for ```Chrome```, ```Firefox``` and ```Safari```, using ```window.AudioContext``` or ```window.webkitAudioContext```, as appropriate.

This library allows for queueing multiple notes and duration, including chords. This is a ***very nice*** library and allowed this application to easily produce sounds.

[Link for WebAudioFont](https://github.com/surikov/webaudiofont)

## VexFlow

> VexFlow is an open-source online music notation rendering API. It is written completely in JavaScript, and runs right in the browser.
>> (vexflow.com)

This is another open-source ```JavaScript``` library, which is used to prepare graphical representations of staves and notes, including clefs, time signatures, accidentals, etc. It is a ***great*** library and it covers all kinds of special cases, while adhering to the usual conventions for sheet music.

Using this library, I was able to easily add staves to display scale notes or chords. The API is very extensive and it was really easy to add clefs, accidentals to the notes and change the duration of the notes.

[Link for VexFlow](https://github.com/0xfe/vexflow)


# OTHER TOOLS

## Inkscape

> Inkscape is professional quality vector graphics software which runs on Linux, Mac OS X and Windows desktop computers.
>> (inkscape.org, meta description tag)

Using Inkscape, I was able to create all my logos and images from scratch. I used it to create the Circle of Fifths diagram for the scales page. Using straight lines and arcs and editing the resulting nodes, I was able to create closed shapes (cells) that can have a background color applied. 

Inkscape saves its files in the SVG format, which can be directly inserted in the HTML page, without conversion.

Using the built-in properties editor in Inkscape, I was able to assign ```id``` tags to each element, so that they could be manipulated in JavaScript via the DOM.

[Link for Inkscape](https://inkscape.org/)

## Visual Studio Code

> Visual Studio Code, also commonly referred to as VS Code, is a source-code editor developed by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.
>> (Wikipedia)

I used a local installation of Visual Studio Code on my workstation to perform all the local development and testing. This was easier than using the CS50 Codespace, since I could modify any SVG image or logo using Inkscape, and instantly reload the page to test the results. There was no file upload operation necessary at each iteration, since the whole development environment was running locally on my workstation.

Being able to run the ```Flask``` application locally was also useful, since I could also test with various web browsers locally and access the app through ```127.0.0.1```.

[Link for Visual Studio Code](https://code.visualstudio.com/)

## W3C Markup Validation Service

> This validator checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, etc.
>> (validator.w3.org)

After creating the various pages and testing them in multiple browsers, I ran the resulting pages through this validator, to make sure I did not have mismatched HTML tags or similar errors. This tool indicated that the SVG files produced by Inkscape contain some unsupported tags.

I was then able to simplify the ```Circles_of_Fifths.svg``` file and remove the unsupported tags. This cleared the warnings in the validator. It also resulted in a smaller file, which should improve the loading time. I kept the original SVG file with the Inkscape tags untouched, in the ```/static/images/inkscape``` directory.

[Link for the W3C Markup Validation Service](https://validator.w3.org/)
