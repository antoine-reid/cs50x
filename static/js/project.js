const { Accidental, Annotation, ChordSymbol, Formatter, Renderer, Stave, StaveNote, SymbolModifiers, Voice } = Vex.Flow;

var note_position = { 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7};
var base_note_values = { 'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11};

var AudioContextFunc = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContextFunc();
var player = new WebAudioFontPlayer();
player.loader.decodeAfterLoading(audioContext, '_tone_0010_Aspirin_sf2_file');

var gainPiano = audioContext.createGain();
gainPiano.connect(audioContext.destination);
gainPiano.gain.value=0.6;

var bpm = 80;
var N = 4 * 60 / bpm;
var pieceDuration = N + 0.25;
var beatLen = 1 / 8 * N;

var started = false;
var startTime = 0;
var intervalId;
var playback_notes = [];
var playback_chords = [];

function piano(pitch, duration) {
    return {
        gain:gainPiano,
        preset:_tone_0010_Aspirin_sf2_file,
        pitch:pitch,
        duration:duration*N };
}

function playPiece(play_notes) {
    for (var n = 0; n < play_notes.length; n++) {
        var beat = play_notes[n];
        for (var i = 0; i < beat.length; i++) {
            if (beat[i]) {
                player.queueWaveTable(audioContext, beat[i].gain, beat[i].preset, startTime + n * beatLen , beat[i].pitch, beat[i].duration);
            }
        }
    }
}

function start_stop_playback(play_notes, button_id) {
    if (play_notes.length == 0) {
        console.log('not playing, play_notes list is empty');
        return;
    }
    if (started == false) {
        start_playback(play_notes, button_id);
    } else {
        stop_playback();
    }
}

function start_playback(play_notes, button_id) {
    if (started) {
        console.log('started already');
    } else {
        started = true;
        document.getElementById(button_id).src = '/static/images/stop.svg';
        startTime = audioContext.currentTime + 0.1;
        playPiece(play_notes);
        endTime = startTime + pieceDuration;
        intervalId = setInterval(function () {
            if (audioContext.currentTime > endTime) {
                stop_playback();
            }
        }, 20);
    }
}

function stop_playback() {
    if (started) {
        if (intervalId) {
            clearInterval(intervalId);                  
        }

        started = false;
        player.cancelQueue(audioContext)

        // Replace the src on all buttons, to cover special cases like clicking play on the scale and stop on the chords
        for (button_id of ['scale_play_button', 'chords_play_button', 'chord_play_button']) {
            button = document.getElementById(button_id);
            if (button) {
                button.src = '/static/images/play.svg';
            }
        }
    }
}

async function get_chords(scale, type) {
   let response = await fetch('/diatonic_chords/' + encodeURIComponent(scale) + '/' + encodeURIComponent(type));
   let chords_json = await response.text();
   let chords = JSON.parse(chords_json);

   // Repeat 1st degree at the end, so we get 8 chords instead of 7
   chords.push(chords[0]);
   return chords;
}

async function get_scale(scale, type) {
   let response = await fetch('/scale/' + encodeURIComponent(scale) + '/' + encodeURIComponent(type));
   let notes_json = await response.text();
   return JSON.parse(notes_json);
}

async function get_chord(chord, add_extra_root_note) {
    let response = await fetch('/chord/' + encodeURIComponent(chord));
    let notes_json = await response.text();
    let notes = JSON.parse(notes_json);

    if (add_extra_root_note) {
        notes.push(notes[0]);
    }
    return notes;
}

function convert_individual_notes_to_vexnotes(notes, octave, duration) {
    let vexnotes = [];
    let previous_note_position = 0;

    for (let note of notes) {
        let note_first_char = note.charAt(0);
        let current_note_position = note_position[note_first_char];

        if (current_note_position < previous_note_position) {
            octave++;
        }

        let vexnote = new StaveNote({ keys: [note + '/' + octave.toString()], duration: duration});
        let modifier = new ChordSymbol().setFontSize(14).setVertical('bottom').addText(note_first_char);

        if (note.endsWith('##')) {
            vexnote.addModifier(new Accidental('##'));
            modifier.addGlyph('#').addGlyph('#');
        } else if (note.endsWith('#')) {
            vexnote.addModifier(new Accidental('#'));
            modifier.addGlyph('#');
        } else if (note.endsWith('bb')) {
            vexnote.addModifier(new Accidental('bb'));
            modifier.addGlyph('b').addGlyph('b');
        } else if (note.endsWith('b')) {
            vexnote.addModifier(new Accidental('b'));
            modifier.addGlyph('b');
        }

        // Center the modifier on the note
        modifier.setHorizontal('center');

        vexnote.addModifier(modifier);
        vexnotes.push(vexnote);
        previous_note_position = current_note_position;
    }

    // Return our notes and the final octave we reached
    return [vexnotes, octave];
}

async function convert_chords_to_vexnotes(chords, octave, duration, add_extra_root_note) {
    let vexchords = [];
    let previous_root_note_position = 0;

    for (single_chord of chords) {
        let current_root_note_position = note_position[single_chord.charAt(0)];
        if (current_root_note_position < previous_root_note_position) {
            octave++;
        }
    
        let results_array = await convert_single_chord_to_vexnotes(single_chord, octave, duration, add_extra_root_note);
        octave = results_array[1];
        
        // Add the completed chord to our vexchords array
        vexchords.push(results_array[0]);   
        previous_root_note_position = current_root_note_position;
    }

    // Return our chords and the final (root note) octave we reached
    return [vexchords, octave];
}

async function convert_single_chord_to_vexnotes(chord, octave, duration, add_extra_root_note) {
    let notes = await get_chord(chord, add_extra_root_note);
    let previous_note_position = 0;
    let this_chord_notes = [];
    let note_octave = octave;

    for (note of notes) {
        let note_first_char = note.charAt(0);
        let current_note_position = note_position[note_first_char];

        if (current_note_position < previous_note_position) {
            note_octave++;
        }

        let this_note_name = note + '/' + note_octave.toString();
        this_chord_notes.push(this_note_name);
        previous_note_position = current_note_position;
    }
    this_chord = new StaveNote({ keys: this_chord_notes, duration: duration});
    let modifier = new ChordSymbol().setFontSize(14).setVertical('bottom').addText(chord.charAt(0));

    // Add accidentals using the note index
    for (idx in notes) {
        i = parseInt(idx);
        if (notes[idx].endsWith('##')) {
            this_chord.addModifier(new Accidental('##'), i);
        } else if (notes[idx].endsWith('#')) {
            this_chord.addModifier(new Accidental('#'), i);
        } else if (notes[idx].endsWith('bb')) {
            this_chord.addModifier(new Accidental('bb'), i);
        } else if (notes[idx].endsWith('b')) {
            this_chord.addModifier(new Accidental('b'), i);
        }
    }

    if (chord.includes('##')) {
        modifier.addGlyph('#').addGlyph('#');
    } else if (chord.includes('#')) {
        modifier.addGlyph('#');
    } else if (chord.includes('bb')) {
        modifier.addGlyph('b').addGlyph('b');
    } else if (chord.includes('b')) {
        modifier.addGlyph('b');
    }

    // Adjust the modifier based on quality
    if (chord.endsWith('m')) {
        modifier.addText('m');
    } else if (chord.endsWith('o')) {
        modifier.addGlyph('diminished', { symbolModifier: SymbolModifiers.SUPERSCRIPT });
    } else if (chord.endsWith('+')) {
        modifier.addGlyph('augmented', { symbolModifier: SymbolModifiers.SUPERSCRIPT });
    }

    // Center the modifier on the chord
    modifier.setHorizontal('center');

    // Apply an annotation to this chord
    this_chord.addModifier(modifier);

    return [this_chord, octave];
}

async function arpeggiate_single_chord_to_vexnotes(chord, octave, duration, add_extra_root_note) {
    let vexnotes = [];

    // Fetch the chord notes
    let chord_notes = await get_chord(chord, add_extra_root_note);

    if (!add_extra_root_note) {
        // HACK: Start with a quarter rest, otherwise out results would only provide 7 beats instead of 8
        let qrest = new StaveNote({ keys: ['B/4'], duration: 'qr'});
        vexnotes.push(qrest);
    }

    // Prepare three individual notes and add them to our array
    let individual_vexnotes_array = convert_individual_notes_to_vexnotes(chord_notes, octave, duration);
    for (vexnote of individual_vexnotes_array[0]) {
        vexnotes.push(vexnote);
    }

    // Now prepare the complete chord and add it to our array
    // HACK: Hardcode a whole note duration for the chord (4 beats)
    let chord_vexnotes_array = await convert_single_chord_to_vexnotes(chord, octave, 'w', add_extra_root_note);
    vexnotes.push(chord_vexnotes_array[0]);

    return [vexnotes, octave];
}

function prepare_individual_notes(scale) {
    let octave = 4;
    let new_notes = [];
    let duration = 1/8;
    let previous_note_position = 0;

    for (idx in scale) {
        note_first_char = scale[idx].charAt(0);
        current_note_position = note_position[note_first_char];

        if (current_note_position < previous_note_position) {
            octave++;
        }

        let new_note_list = [piano(note_value(scale[idx], octave), duration)];
        new_notes.push(new_note_list);
        previous_note_position = current_note_position;
    }
    return new_notes;
}

async function prepare_chords_notes(chords, add_extra_root_note) {
    let octave = 4;
    let new_notes = [];
    let duration = 1/8;
    let previous_root_note_position = 0;

    for (chord of chords) {
        let current_root_note_position = note_position[chord.charAt(0)];
        if (current_root_note_position < previous_root_note_position) {
            octave++;
        }
        let chord_notes_array = await prepare_single_chord_notes(chord, octave, duration, add_extra_root_note);
        previous_root_note_position = current_root_note_position;
        new_notes.push(chord_notes_array[0]);
    }

    return new_notes;
}

async function prepare_single_chord_notes(chord, octave, duration, add_extra_root_note) {
    let notes = await get_chord(chord, add_extra_root_note);
    let previous_note_position = 0;
    let this_chord_notes = [];

    for (note of notes) {
        let note_first_char = note.charAt(0);
        let current_note_position = note_position[note_first_char];

        if (current_note_position < previous_note_position) {
            octave++;
        }

        let this_note = piano(note_value(note, octave), duration);
        this_chord_notes.push(this_note);
        previous_note_position = current_note_position;
    }

    return [this_chord_notes, octave];
}

async function arpeggiate_single_chord_to_notes(chord, octave, duration, add_extra_root_note) {
    let new_notes = [];

    // Fetch the chord notes
    let chord_notes = await get_chord(chord, add_extra_root_note);

    // First prepare three individual notes and add them to our array
    let individual_notes = prepare_individual_notes(chord_notes, octave, duration);
    for (note of individual_notes) {
        new_notes.push(note);
    }

    // Now prepare the complete chord and add it to our array
    // HACK: Make the chord 4 beats, to match what we will be displaying
    let chord_notes_array = await prepare_single_chord_notes(chord, octave, duration * 4, add_extra_root_note);
    new_notes.push(chord_notes_array[0]);

    return [new_notes, octave];    
}

function note_value(note, octave) {
    note_name = note.charAt(0);
    note_offset = 0;

    if (note.endsWith('##')) {
        note_offset = 2;
    } else if (note.endsWith('#')) {
        note_offset = 1;
    } else if (note.endsWith('bb')) {
        note_offset = -2;
    } else if (note.endsWith('b')) {
        note_offset = -1;
    }

    numeric_value = (octave * 12) + base_note_values[note_name] + note_offset;
    return numeric_value;
}
