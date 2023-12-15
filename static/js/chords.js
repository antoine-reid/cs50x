async function execute_form() {
    let chord_select = document.getElementById('chord_select');
    let type_select = document.getElementById('type_select');
    let include_octave = document.getElementById('include_octave');
    let add_extra_root_note = false;

    if (chord_select == '' || type_select == '') {
        return;
    }

    if (chord_select.value == '' || type_select.value == '') {
        return;
    }

    if (include_octave.checked) {
        add_extra_root_note = true;
    }

    let chord_name = chord_select.value;
    if (type_select.value == 'minor') {
        chord_name = chord_name + 'm';
    } else if (type_select.value == 'diminished') {
        chord_name = chord_name + 'o';
    } else if (type_select.value == 'augmented') {
        chord_name = chord_name + '+';
    }

    // Draw the chord staff
    let vexnotes_array = await arpeggiate_single_chord_to_vexnotes(chord_name, 4, 'q', add_extra_root_note);
    draw_arpeggiated_chord_staff(vexnotes_array[0]);

    // Prepare the notes for the scale and chords, ready for playback
    let results_array = await arpeggiate_single_chord_to_notes(chord_name, 4, 1/8, add_extra_root_note);
    playback_notes = results_array[0];

    // Display the staff and play button
    document.getElementById('results').removeAttribute('hidden');
}

function draw_arpeggiated_chord_staff(vexnotes) {
    // Create an SVG renderer and attach it to the DIV element named 'chord_staff'.
    const chord_staff = document.getElementById('chord_staff');
    chord_staff.innerHTML = '';
    const chord_renderer = new Renderer(chord_staff, Renderer.Backends.SVG);

    // Configure the rendering context for chord_staff
    chord_renderer.resize(450, 150);
    const chord_context = chord_renderer.getContext().scale(0.95, 0.95);

    // Create a staff of width 440 at position 0, 30 on the canvas.
    const stave = new Stave(0, 30, 440);

    // Add a clef but no time signature
    stave.addClef('treble');

    // Connect it to the rendering context and draw
    stave.setContext(chord_context).draw();

    // Create a voice and add the above notes
    // HACK: Hardcode the number of 8 beats, to match the vexnotes we have prepared
    const voice = new Voice({ num_beats: 8, beat_value: 4 });
    voice.addTickables(vexnotes);

    // Format and justify the notes
    new Formatter().joinVoices([voice]).format([voice], 395);

    // Render voice
    voice.draw(chord_context, stave);
}

document.addEventListener('DOMContentLoaded', function() {  
    // Execute the form at least once
    execute_form();
    
    // Add events to call execute_form() every time one of the selects is changed
    document.getElementById('chord_select').addEventListener('change', async function(event) {
        execute_form();
    });
    document.getElementById('type_select').addEventListener('change', async function(event) {
        execute_form();
    });
    document.getElementById('include_octave').addEventListener('change', async function(event) {
        execute_form();
    });
 });
