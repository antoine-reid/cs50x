var cell_highlighted = false;
var highlight_off = 'display:inline;fill:none;stroke:#000000;stroke-linecap:butt;stroke-linejoin:miter;stroke-width:0.5;stroke-dasharray:none;';

var borders_tonic = 'display:inline;stroke:#000000;stroke-linecap:square;stroke-linejoin:round;stroke-width:2.5;stroke-dasharray:none;';
var borders_others = 'display:inline;stroke:#000000;stroke-linecap:square;stroke-linejoin:round;stroke-width:1.5;stroke-dasharray:none;';
var color_maj = 'fill:#78a0eb;';
var color_min = 'fill:#e3bf2d;';
var color_dim = 'fill:#e06d1f;';
var color_aug = 'fill:#3dba5f;';

// Hash signs are not allowed in IDs, so we use an underscore instead
var all_cells = ['CM', 'GM', 'DM', 'AM', 'EM', 'BM', 'F_M', 'C_M', 'AbM', 'EbM', 'BbM', 'FM', 
                 'Am', 'Em', 'Bm', 'F_m', 'C_m', 'G_m', 'D_m', 'A_m', 'Fm', 'Cm', 'Gm', 'Dm'];

var cell_enharmonic_equivalents = { 'E_M': 'FM', 'Abm': 'G_m', 'E_m': 'Fm', 'Bbm': 'A_m', 'DbM': 'C_M', 'G_M': 'AbM',
                                    'B_m': 'Cm', 'Ebm': 'D_m', 'GbM': 'F_M', 'CbM': 'BM', 'Dbm': 'C_m', 'FbM': 'EM',
                                    'D_M': 'EbM', 'F__m': 'Gm', 'C__m': 'Dm', 'G__m': 'Am', 'A_M': 'BbM', 'Cbm': 'Bm',
                                    'EbbM': 'DM', 'AbbM': 'GM', 'BbbM': 'AM', 'Gbm': 'F_m', 'Fbm': 'Em' };

function all_highlights_off() {
    for (cell of all_cells) {
        document.getElementById('Cell_' + cell).style = highlight_off;
    }
    cell_highlighted = false;
}

function highlight_cells(cells) {
    all_highlights_off();

    for (key in cells) {
        let chord = cells[key];
        let borders = '';
        let color = '';
        let cell_prefix = 'Cell_';

        // Replace sharp (#) symbols by underscores, to match our cell names
        chord = chord.replaceAll('#', '_');

        // Mark the Major chords with uppercase M
        if (!chord.endsWith('m') && !chord.endsWith('o') && !chord.endsWith('+')) {
            chord = chord + 'M';
        }

        if (chord.endsWith('m')) {
            quality = 'min';
            cell_name = cell_prefix + chord;
            color = color_min;
        } else if (chord.endsWith('o')) {
            quality = 'dim';
            cell_name = cell_prefix + chord.slice(0, -1) + 'm';
            color = color_dim;
        } else if (chord.endsWith('+')) {
            quality = 'aug';
            cell_name = cell_prefix + chord.slice(0, -1) + 'M';
            color = color_aug;
        } else {
            quality = 'maj';
            cell_name = cell_prefix + chord;
            color = color_maj;
        }

        // Enharmonic equivalents are needed to find the correct cell
        for (equiv in cell_enharmonic_equivalents) {
            cell_name = cell_name.replace(equiv, cell_enharmonic_equivalents[equiv]);
        }

        // For the tonic, we use thicker borders
        if (key == 0) {
            borders = borders_tonic;
        } else {
            borders = borders_others;
        }

        element = document.getElementById(cell_name);
        if (element) {
            element.style = borders + color;
        } else {
            console.log('Element for cell ' + cell_name + ' not found');
        }
    }
    cell_highlighted = true;
}

async function execute_form() {
    let scale_select = document.getElementById('scale_select');
    let type_select = document.getElementById('type_select');

    if (scale_select == '' || type_select == '') {
        return;
    }

    if (scale_select.value == '' || type_select.value == '') {
        return;
    }

    // Highlight the cells in the Circle of Fifths (do not process the tonic twice)
    let chords = await get_chords(scale_select.value, type_select.value);
    highlight_cells(chords.slice(0, -1));

    // Draw the scale staff
    let scale = await get_scale(scale_select.value, type_select.value);
    let vexnotes_array = convert_individual_notes_to_vexnotes(scale, 4, 'q');
    draw_scale_staff(vexnotes_array[0]);

    // Draw the chords staff (reuse the chords we got for the circle above)
    let vexchords_array = await convert_chords_to_vexnotes(chords, 4, 'q', false);
    draw_chords_staff(vexchords_array[0]);

    // Prepare the notes for the scale and chords, ready for playback
    playback_notes = prepare_individual_notes(scale);
    playback_chords = await prepare_chords_notes(chords, false);

    // Display the scale and chords play buttons
    document.getElementById('results').removeAttribute('hidden');
}

function draw_scale_staff(vexnotes) {
    // Create an SVG renderer and attach it to the DIV element named 'scale_staff'.
    const scale_staff = document.getElementById('scale_staff');
    scale_staff.innerHTML = '';
    const scale_renderer = new Renderer(scale_staff, Renderer.Backends.SVG);

    // Configure the rendering context for scale_staff
    scale_renderer.resize(555, 150);
    const scale_context = scale_renderer.getContext().scale(0.95, 0.95);

    // Create a staff of width 555 at position 0, 30 on the canvas.
    const stave = new Stave(0, 30, 555);

    // Add a clef but no time signature
    stave.addClef('treble');

    // Connect it to the rendering context and draw
    stave.setContext(scale_context).draw();

    // Create a voice and add the above notes
    const voice = new Voice({ num_beats: vexnotes.length, beat_value: 4 });
    voice.addTickables(vexnotes);

    // Format and justify the notes
    new Formatter().joinVoices([voice]).format([voice], 465);

    // Render voice
    voice.draw(scale_context, stave);
}

function draw_chords_staff(vexchords) {
    // Create an SVG renderer and attach it to the DIV element named 'chords_staff'.
    const chords_staff = document.getElementById('chords_staff');
    chords_staff.innerHTML = '';
    const chords_renderer = new Renderer(chords_staff, Renderer.Backends.SVG);

    // Configure the rendering context for chords_staff
    chords_renderer.resize(555, 150);
    const chords_context = chords_renderer.getContext().scale(0.95, 0.95);

    // Create a staff of width 555 at position 0, 30 on the canvas.
    const stave = new Stave(0, 30, 555);

    // Add a clef but no time signature
    stave.addClef('treble');

    // Connect it to the rendering context and draw
    stave.setContext(chords_context).draw();

    // Create a voice and add the above notes
    const voice = new Voice({ num_beats: vexchords.length, beat_value: 4 });
    voice.addTickables(vexchords);

    // Format and justify the notes
    new Formatter().joinVoices([voice]).format([voice], 465);
    
    // Render voice
    voice.draw(chords_context, stave);
}

document.addEventListener('DOMContentLoaded', function() {  
    // Execute the form at least once
    execute_form();
    
    // Add events to call execute_form() every time one of the selects is changed
    document.getElementById('scale_select').addEventListener('change', async function(event) {
        execute_form();
    });
    document.getElementById('type_select').addEventListener('change', async function(event) {
        execute_form();
    });
 });
