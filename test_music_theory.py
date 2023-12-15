#!/usr/bin/env pytest-3.11
# -*- coding: utf-8 -*-

from music_theory import Music_Theory
import pytest


def test_get_scale():
    # Test all the supported scales.
    #
    # Supported scale types: "major", "minor" (alias for "natural minor"),
    # "natural minor", "harmonic minor" and "melodic minor".
    #
    # There are a lot of special cases, so attempt to test all the scales,
    # to cover all the exceptions and catch any regression.
    #
    # The test covers the following cases:
    #  - Scales with sharps
    #  - Scales with flats
    #  - Scales with double-sharps
    #  - Scales with double-flats
    #  - Scales with both sharps and flats (some minor scales)

    assert Music_Theory.get_scale("C") == ["C", "D", "E", "F", "G", "A", "B", "C"]
    assert Music_Theory.get_scale("C", "major") == ["C", "D", "E", "F", "G", "A", "B", "C"]
    assert Music_Theory.get_scale("G", "major") == ["G", "A", "B", "C", "D", "E", "F#", "G"]
    assert Music_Theory.get_scale("D", "major") == ["D", "E", "F#", "G", "A", "B", "C#", "D"]
    assert Music_Theory.get_scale("A", "major") == ["A", "B", "C#", "D", "E", "F#", "G#", "A"]
    assert Music_Theory.get_scale("E", "major") == ["E", "F#", "G#", "A", "B", "C#", "D#", "E"]
    assert Music_Theory.get_scale("B", "major") == ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"]
    assert Music_Theory.get_scale("F#", "major") == ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"]
    assert Music_Theory.get_scale("C#", "major") == ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"]
    assert Music_Theory.get_scale("F", "major") == ["F", "G", "A", "Bb", "C", "D", "E", "F"]
    assert Music_Theory.get_scale("Bb", "major") == ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"]
    assert Music_Theory.get_scale("Eb", "major") == ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"]
    assert Music_Theory.get_scale("Ab", "major") == ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"]
    assert Music_Theory.get_scale("Db", "major") == ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C", "Db"]
    assert Music_Theory.get_scale("Gb", "major") == ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"]
    assert Music_Theory.get_scale("Cb", "major") == ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb", "Cb"]

    assert Music_Theory.get_scale("A", "natural minor") == ["A", "B", "C", "D", "E", "F", "G", "A"]
    assert Music_Theory.get_scale("A", "minor") == ["A", "B", "C", "D", "E", "F", "G", "A"]
    assert Music_Theory.get_scale("E", "minor") == ["E", "F#", "G", "A", "B", "C", "D", "E"]
    assert Music_Theory.get_scale("B", "minor") == ["B", "C#", "D", "E", "F#", "G", "A", "B"]
    assert Music_Theory.get_scale("F#", "minor") == ["F#", "G#", "A", "B", "C#", "D", "E", "F#"]
    assert Music_Theory.get_scale("C#", "minor") == ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"]
    assert Music_Theory.get_scale("G#", "minor") == ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"]
    assert Music_Theory.get_scale("D#", "minor") == ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"]
    assert Music_Theory.get_scale("A#", "minor") == ["A#", "B#", "C#", "D#", "E#", "F#", "G#", "A#"]
    assert Music_Theory.get_scale("D", "minor") == ["D", "E", "F", "G", "A", "Bb", "C", "D"]
    assert Music_Theory.get_scale("G", "minor") == ["G", "A", "Bb", "C", "D", "Eb", "F", "G"]
    assert Music_Theory.get_scale("C", "minor") == ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"]
    assert Music_Theory.get_scale("F", "minor") == ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"]
    assert Music_Theory.get_scale("Bb", "minor") == ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]
    assert Music_Theory.get_scale("Eb", "minor") == ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db", "Eb"]
    assert Music_Theory.get_scale("Ab", "minor") == ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "Ab"]

    assert Music_Theory.get_scale("A", "harmonic minor") == ["A", "B", "C", "D", "E", "F", "G#", "A"]
    assert Music_Theory.get_scale("E", "harmonic minor") == ["E", "F#", "G", "A", "B", "C", "D#", "E"]
    assert Music_Theory.get_scale("B", "harmonic minor") == ["B", "C#", "D", "E", "F#", "G", "A#", "B"]
    assert Music_Theory.get_scale("F#", "harmonic minor") == ["F#", "G#", "A", "B", "C#", "D", "E#", "F#"]
    assert Music_Theory.get_scale("C#", "harmonic minor") == ["C#", "D#", "E", "F#", "G#", "A", "B#", "C#"]
    assert Music_Theory.get_scale("Ab", "harmonic minor") == ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "G", "Ab"]
    assert Music_Theory.get_scale("Eb", "harmonic minor") == ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "D", "Eb"]
    assert Music_Theory.get_scale("Bb", "harmonic minor") == ["Bb", "C", "Db", "Eb", "F", "Gb", "A", "Bb"]
    assert Music_Theory.get_scale("F", "harmonic minor") == ["F", "G", "Ab", "Bb", "C", "Db", "E", "F"]
    assert Music_Theory.get_scale("C", "harmonic minor") == ["C", "D", "Eb", "F", "G", "Ab", "B", "C"]
    assert Music_Theory.get_scale("G#", "harmonic minor") == ["G#", "A#", "B", "C#", "D#", "E", "F##", "G#"]
    assert Music_Theory.get_scale("D#", "harmonic minor") == ["D#", "E#", "F#", "G#", "A#", "B", "C##", "D#"]
    assert Music_Theory.get_scale("A#", "harmonic minor") == ["A#", "B#", "C#", "D#", "E#", "F#", "G##", "A#"]
    assert Music_Theory.get_scale("G", "harmonic minor") == ["G", "A", "Bb", "C", "D", "Eb", "F#", "G"]
    assert Music_Theory.get_scale("D", "harmonic minor") == ["D", "E", "F", "G", "A", "Bb", "C#", "D"]

    assert Music_Theory.get_scale("A", "melodic minor") == ["A", "B", "C", "D", "E", "F#", "G#", "A"]
    assert Music_Theory.get_scale("E", "melodic minor") == ["E", "F#", "G", "A", "B", "C#", "D#", "E"]
    assert Music_Theory.get_scale("B", "melodic minor") == ["B", "C#", "D", "E", "F#", "G#", "A#", "B"]
    assert Music_Theory.get_scale("F#", "melodic minor") == ["F#", "G#", "A", "B", "C#", "D#", "E#", "F#"]
    assert Music_Theory.get_scale("C#", "melodic minor") == ["C#", "D#", "E", "F#", "G#", "A#", "B#", "C#"]
    assert Music_Theory.get_scale("Ab", "melodic minor") == ["Ab", "Bb", "Cb", "Db", "Eb", "F", "G", "Ab"]
    assert Music_Theory.get_scale("Eb", "melodic minor") == ["Eb", "F", "Gb", "Ab", "Bb", "C", "D", "Eb"]
    assert Music_Theory.get_scale("Bb", "melodic minor") == ["Bb", "C", "Db", "Eb", "F", "G", "A", "Bb"]
    assert Music_Theory.get_scale("F", "melodic minor") == ["F", "G", "Ab", "Bb", "C", "D", "E", "F"]
    assert Music_Theory.get_scale("C", "melodic minor") == ["C", "D", "Eb", "F", "G", "A", "B", "C"]
    assert Music_Theory.get_scale("G#", "melodic minor") == ["G#", "A#", "B", "C#", "D#", "E#", "F##", "G#"]
    assert Music_Theory.get_scale("D#", "melodic minor") == ["D#", "E#", "F#", "G#", "A#", "B#", "C##", "D#"]
    assert Music_Theory.get_scale("A#", "melodic minor") == ["A#", "B#", "C#", "D#", "E#", "F##", "G##", "A#"]
    assert Music_Theory.get_scale("G", "melodic minor") == ["G", "A", "Bb", "C", "D", "E", "F#", "G"]
    assert Music_Theory.get_scale("D", "melodic minor") == ["D", "E", "F", "G", "A", "B", "C#", "D"]


def test_get_diatonic_chords():
    # Test finding the diatonic chords for all keys in major, natural minor, harmonic minor and melodic minor.
    # This should cover all the special cases, that need either double-sharps, double-flats, diminished or
    # augmented chords, or a combination thereof.

    assert Music_Theory.get_diatonic_chords("C") == ["C", "Dm", "Em", "F", "G", "Am", "Bo"]
    assert Music_Theory.get_diatonic_chords("C", "major") == ["C", "Dm", "Em", "F", "G", "Am", "Bo"]
    assert Music_Theory.get_diatonic_chords("C", "minor") == ["Cm", "Do", "Eb", "Fm", "Gm", "Ab", "Bb"]
    assert Music_Theory.get_diatonic_chords("C", "natural minor") == ["Cm", "Do", "Eb", "Fm", "Gm", "Ab", "Bb"]
    assert Music_Theory.get_diatonic_chords("C", "harmonic minor") == ["Cm", "Do", "Eb+", "Fm", "G", "Ab", "Bo"]
    assert Music_Theory.get_diatonic_chords("C", "melodic minor") == ["Cm", "Dm", "Eb+", "F", "G", "Ao", "Bo"]

    assert Music_Theory.get_diatonic_chords("C#", "major") == ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#o"]
    assert Music_Theory.get_diatonic_chords("C#", "natural minor") == ["C#m", "D#o", "E", "F#m", "G#m", "A", "B"]
    assert Music_Theory.get_diatonic_chords("C#", "harmonic minor") == ["C#m", "D#o", "E+", "F#m", "G#", "A", "B#o"]
    assert Music_Theory.get_diatonic_chords("C#", "melodic minor") == ["C#m", "D#m", "E+", "F#", "G#", "A#o", "B#o"]

    assert Music_Theory.get_diatonic_chords("Db", "major") == ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Co"]
    assert Music_Theory.get_diatonic_chords("Db", "natural minor") == ["Dbm", "Ebo", "Fb", "Gbm", "Abm", "Bbb", "Cb"]
    assert Music_Theory.get_diatonic_chords("Db", "harmonic minor") == ["Dbm", "Ebo", "Fb+", "Gbm", "Ab", "Bbb", "Co"]
    assert Music_Theory.get_diatonic_chords("Db", "melodic minor") == ["Dbm", "Ebm", "Fb+", "Gb", "Ab", "Bbo", "Co"]

    assert Music_Theory.get_diatonic_chords("D", "major") == ["D", "Em", "F#m", "G", "A", "Bm", "C#o"]
    assert Music_Theory.get_diatonic_chords("D", "natural minor") == ["Dm", "Eo", "F", "Gm", "Am", "Bb", "C"]
    assert Music_Theory.get_diatonic_chords("D", "harmonic minor") == ["Dm", "Eo", "F+", "Gm", "A", "Bb", "C#o"]
    assert Music_Theory.get_diatonic_chords("D", "melodic minor") == ["Dm", "Em", "F+", "G", "A", "Bo", "C#o"]

    assert Music_Theory.get_diatonic_chords("D#", "major") == ["D#", "E#m", "F##m", "G#", "A#", "B#m", "C##o"]
    assert Music_Theory.get_diatonic_chords("D#", "natural minor") == ["D#m", "E#o", "F#", "G#m", "A#m", "B", "C#"]
    assert Music_Theory.get_diatonic_chords("D#", "harmonic minor") == ["D#m", "E#o", "F#+", "G#m", "A#", "B", "C##o"]
    assert Music_Theory.get_diatonic_chords("D#", "melodic minor") == ["D#m", "E#m", "F#+", "G#", "A#", "B#o", "C##o"]

    assert Music_Theory.get_diatonic_chords("Eb", "major") == ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Do"]
    assert Music_Theory.get_diatonic_chords("Eb", "natural minor") == ["Ebm", "Fo", "Gb", "Abm", "Bbm", "Cb", "Db"]
    assert Music_Theory.get_diatonic_chords("Eb", "harmonic minor") == ["Ebm", "Fo", "Gb+", "Abm", "Bb", "Cb", "Do"]
    assert Music_Theory.get_diatonic_chords("Eb", "melodic minor") == ["Ebm", "Fm", "Gb+", "Ab", "Bb", "Co", "Do"]

    assert Music_Theory.get_diatonic_chords("E", "major") == ["E", "F#m", "G#m", "A", "B", "C#m", "D#o"]
    assert Music_Theory.get_diatonic_chords("E", "natural minor") == ["Em", "F#o", "G", "Am", "Bm", "C", "D"]
    assert Music_Theory.get_diatonic_chords("E", "harmonic minor") == ["Em", "F#o", "G+", "Am", "B", "C", "D#o"]
    assert Music_Theory.get_diatonic_chords("E", "melodic minor") == ["Em", "F#m", "G+", "A", "B", "C#o", "D#o"]

    assert Music_Theory.get_diatonic_chords("F", "major") == ["F", "Gm", "Am", "Bb", "C", "Dm", "Eo"]
    assert Music_Theory.get_diatonic_chords("F", "natural minor") == ["Fm", "Go", "Ab", "Bbm", "Cm", "Db", "Eb"]
    assert Music_Theory.get_diatonic_chords("F", "harmonic minor") == ["Fm", "Go", "Ab+", "Bbm", "C", "Db", "Eo"]
    assert Music_Theory.get_diatonic_chords("F", "melodic minor") == ["Fm", "Gm", "Ab+", "Bb", "C", "Do", "Eo"]

    assert Music_Theory.get_diatonic_chords("F#", "major") == ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#o"]
    assert Music_Theory.get_diatonic_chords("F#", "natural minor") == ["F#m", "G#o", "A", "Bm", "C#m", "D", "E"]
    assert Music_Theory.get_diatonic_chords("F#", "harmonic minor") == ["F#m", "G#o", "A+", "Bm", "C#", "D", "E#o"]
    assert Music_Theory.get_diatonic_chords("F#", "melodic minor") == ["F#m", "G#m", "A+", "B", "C#", "D#o", "E#o"]

    assert Music_Theory.get_diatonic_chords("Gb", "major") == ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fo"]
    assert Music_Theory.get_diatonic_chords("Gb", "natural minor") == ["Gbm", "Abo", "Bbb", "Cbm", "Dbm", "Ebb", "Fb"]
    assert Music_Theory.get_diatonic_chords("Gb", "harmonic minor") == ["Gbm", "Abo", "Bbb+", "Cbm", "Db", "Ebb", "Fo"]
    assert Music_Theory.get_diatonic_chords("Gb", "melodic minor") == ["Gbm", "Abm", "Bbb+", "Cb", "Db", "Ebo", "Fo"]

    assert Music_Theory.get_diatonic_chords("G", "major") == ["G", "Am", "Bm", "C", "D", "Em", "F#o"]
    assert Music_Theory.get_diatonic_chords("G", "natural minor") == ["Gm", "Ao", "Bb", "Cm", "Dm", "Eb", "F"]
    assert Music_Theory.get_diatonic_chords("G", "harmonic minor") == ["Gm", "Ao", "Bb+", "Cm", "D", "Eb", "F#o"]
    assert Music_Theory.get_diatonic_chords("G", "melodic minor") == ["Gm", "Am", "Bb+", "C", "D", "Eo", "F#o"]

    assert Music_Theory.get_diatonic_chords("G#", "major") == ["G#", "A#m", "B#m", "C#", "D#", "E#m", "F##o"]
    assert Music_Theory.get_diatonic_chords("G#", "natural minor") == ["G#m", "A#o", "B", "C#m", "D#m", "E", "F#"]
    assert Music_Theory.get_diatonic_chords("G#", "harmonic minor") == ["G#m", "A#o", "B+", "C#m", "D#", "E", "F##o"]
    assert Music_Theory.get_diatonic_chords("G#", "melodic minor") == ["G#m", "A#m", "B+", "C#", "D#", "E#o", "F##o"]

    assert Music_Theory.get_diatonic_chords("Ab", "major") == ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Go"]
    assert Music_Theory.get_diatonic_chords("Ab", "natural minor") == ["Abm", "Bbo", "Cb", "Dbm", "Ebm", "Fb", "Gb"]
    assert Music_Theory.get_diatonic_chords("Ab", "harmonic minor") == ["Abm", "Bbo", "Cb+", "Dbm", "Eb", "Fb", "Go"]
    assert Music_Theory.get_diatonic_chords("Ab", "melodic minor") == ["Abm", "Bbm", "Cb+", "Db", "Eb", "Fo", "Go"]

    assert Music_Theory.get_diatonic_chords("A", "major") == ["A", "Bm", "C#m", "D", "E", "F#m", "G#o"]
    assert Music_Theory.get_diatonic_chords("A", "natural minor") == ["Am", "Bo", "C", "Dm", "Em", "F", "G"]
    assert Music_Theory.get_diatonic_chords("A", "harmonic minor") == ["Am", "Bo", "C+", "Dm", "E", "F", "G#o"]
    assert Music_Theory.get_diatonic_chords("A", "melodic minor") == ["Am", "Bm", "C+", "D", "E", "F#o", "G#o"]

    assert Music_Theory.get_diatonic_chords("A#", "major") == ["A#", "B#m", "C##m", "D#", "E#", "F##m", "G##o"]
    assert Music_Theory.get_diatonic_chords("A#", "natural minor") == ["A#m", "B#o", "C#", "D#m", "E#m", "F#", "G#"]
    assert Music_Theory.get_diatonic_chords("A#", "harmonic minor") == ["A#m", "B#o", "C#+", "D#m", "E#", "F#", "G##o"]
    assert Music_Theory.get_diatonic_chords("A#", "melodic minor") == ["A#m", "B#m", "C#+", "D#", "E#", "F##o", "G##o"]

    assert Music_Theory.get_diatonic_chords("Bb", "major") == ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Ao"]
    assert Music_Theory.get_diatonic_chords("Bb", "natural minor") == ["Bbm", "Co", "Db", "Ebm", "Fm", "Gb", "Ab"]
    assert Music_Theory.get_diatonic_chords("Bb", "harmonic minor") == ["Bbm", "Co", "Db+", "Ebm", "F", "Gb", "Ao"]
    assert Music_Theory.get_diatonic_chords("Bb", "melodic minor") == ["Bbm", "Cm", "Db+", "Eb", "F", "Go", "Ao"]

    assert Music_Theory.get_diatonic_chords("B", "major") == ["B", "C#m", "D#m", "E", "F#", "G#m", "A#o"]
    assert Music_Theory.get_diatonic_chords("B", "natural minor") == ["Bm", "C#o", "D", "Em", "F#m", "G", "A"]
    assert Music_Theory.get_diatonic_chords("B", "harmonic minor") == ["Bm", "C#o", "D+", "Em", "F#", "G", "A#o"]
    assert Music_Theory.get_diatonic_chords("B", "melodic minor") == ["Bm", "C#m", "D+", "E", "F#", "G#o", "A#o"]

    assert Music_Theory.get_diatonic_chords("Cb", "major") == ["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbo"]
    assert Music_Theory.get_diatonic_chords("Cb", "natural minor") == ["Cbm", "Dbo", "Ebb", "Fbm", "Gbm", "Abb", "Bbb"]
    assert Music_Theory.get_diatonic_chords("Cb", "harmonic minor") == ["Cbm", "Dbo", "Ebb+", "Fbm", "Gb", "Abb", "Bbo"]
    assert Music_Theory.get_diatonic_chords("Cb", "melodic minor") == ["Cbm", "Dbm", "Ebb+", "Fb", "Gb", "Abo", "Bbo"]


def test_get_chord_notes():
    # Test all the chords returned by the get_diatonic_chords function (for all the scales above)

    assert Music_Theory.get_chord_notes("C") == ["C", "E", "G"]
    assert Music_Theory.get_chord_notes("Cm") == ["C", "Eb", "G"]
    assert Music_Theory.get_chord_notes("Co") == ["C", "Eb", "Gb"]
    assert Music_Theory.get_chord_notes("C-") == ["C", "Eb", "Gb"]
    assert Music_Theory.get_chord_notes("C+") == ["C", "E", "G#"]
    assert Music_Theory.get_chord_notes("B#m") == ["B#", "D#", "F##"]
    assert Music_Theory.get_chord_notes("B#o") == ["B#", "D#", "F#"]

    assert Music_Theory.get_chord_notes("C#") == ["C#", "E#", "G#"]
    assert Music_Theory.get_chord_notes("C#m") == ["C#", "E", "G#"]
    assert Music_Theory.get_chord_notes("C#o") == ["C#", "E", "G"]
    assert Music_Theory.get_chord_notes("C#-") == ["C#", "E", "G"]
    assert Music_Theory.get_chord_notes("C#+") == ["C#", "E#", "G##"]
    assert Music_Theory.get_chord_notes("Db") == ["Db", "F", "Ab"]
    assert Music_Theory.get_chord_notes("Dbm") == ["Db", "Fb", "Ab"]
    assert Music_Theory.get_chord_notes("Dbo") == ["Db", "Fb", "Abb"]
    assert Music_Theory.get_chord_notes("Db+") == ["Db", "F", "A"]

    assert Music_Theory.get_chord_notes("D") == ["D", "F#", "A"]
    assert Music_Theory.get_chord_notes("Dm") == ["D", "F", "A"]
    assert Music_Theory.get_chord_notes("Do") == ["D", "F", "Ab"]
    assert Music_Theory.get_chord_notes("D-") == ["D", "F", "Ab"]
    assert Music_Theory.get_chord_notes("D+") == ["D", "F#", "A#"]
    assert Music_Theory.get_chord_notes("Ebb") == ["Ebb", "Gb", "Bbb"]
    assert Music_Theory.get_chord_notes("C##m") == ["C##", "E#", "G##"]
    assert Music_Theory.get_chord_notes("C##o") == ["C##", "E#", "G#"]

    assert Music_Theory.get_chord_notes("D#") == ["D#", "F##", "A#"]
    assert Music_Theory.get_chord_notes("D#m") == ["D#", "F#", "A#"]
    assert Music_Theory.get_chord_notes("D#o") == ["D#", "F#", "A"]
    assert Music_Theory.get_chord_notes("D#-") == ["D#", "F#", "A"]
    assert Music_Theory.get_chord_notes("D#+") == ["D#", "F##", "A##"]
    assert Music_Theory.get_chord_notes("Eb") == ["Eb", "G", "Bb"]
    assert Music_Theory.get_chord_notes("Ebm") == ["Eb", "Gb", "Bb"]
    assert Music_Theory.get_chord_notes("Ebo") == ["Eb", "Gb", "Bbb"]
    assert Music_Theory.get_chord_notes("Eb+") == ["Eb", "G", "B"]

    assert Music_Theory.get_chord_notes("E") == ["E", "G#", "B"]
    assert Music_Theory.get_chord_notes("Em") == ["E", "G", "B"]
    assert Music_Theory.get_chord_notes("Eo") == ["E", "G", "Bb"]
    assert Music_Theory.get_chord_notes("E-") == ["E", "G", "Bb"]
    assert Music_Theory.get_chord_notes("E+") == ["E", "G#", "B#"]
    assert Music_Theory.get_chord_notes("Fb") == ["Fb", "Ab", "Cb"]
    assert Music_Theory.get_chord_notes("Fb+") == ["Fb", "Ab", "C"]

    assert Music_Theory.get_chord_notes("E#") == ["E#", "G##", "B#"]
    assert Music_Theory.get_chord_notes("E#m") == ["E#", "G#", "B#"]
    assert Music_Theory.get_chord_notes("E#o") == ["E#", "G#", "B"]
    assert Music_Theory.get_chord_notes("E#-") == ["E#", "G#", "B"]
    assert Music_Theory.get_chord_notes("F") == ["F", "A", "C"]
    assert Music_Theory.get_chord_notes("Fm") == ["F", "Ab", "C"]
    assert Music_Theory.get_chord_notes("Fo") == ["F", "Ab", "Cb"]
    assert Music_Theory.get_chord_notes("F+") == ["F", "A", "C#"]

    assert Music_Theory.get_chord_notes("F#") == ["F#", "A#", "C#"]
    assert Music_Theory.get_chord_notes("F#m") == ["F#", "A", "C#"]
    assert Music_Theory.get_chord_notes("F#o") == ["F#", "A", "C"]
    assert Music_Theory.get_chord_notes("F#-") == ["F#", "A", "C"]
    assert Music_Theory.get_chord_notes("F#+") == ["F#", "A#", "C##"]
    assert Music_Theory.get_chord_notes("Gb") == ["Gb", "Bb", "Db"]
    assert Music_Theory.get_chord_notes("Gbm") == ["Gb", "Bbb", "Db"]
    assert Music_Theory.get_chord_notes("Gbo") == ["Gb", "Bbb", "Dbb"]
    assert Music_Theory.get_chord_notes("Gb+") == ["Gb", "Bb", "D"]

    assert Music_Theory.get_chord_notes("G") == ["G", "B", "D"]
    assert Music_Theory.get_chord_notes("Gm") == ["G", "Bb", "D"]
    assert Music_Theory.get_chord_notes("Go") == ["G", "Bb", "Db"]
    assert Music_Theory.get_chord_notes("G-") == ["G", "Bb", "Db"]
    assert Music_Theory.get_chord_notes("G+") == ["G", "B", "D#"]
    assert Music_Theory.get_chord_notes("F##m") == ["F##", "A#", "C##"]
    assert Music_Theory.get_chord_notes("F##o") == ["F##", "A#", "C#"]

    assert Music_Theory.get_chord_notes("G#") == ["G#", "B#", "D#"]
    assert Music_Theory.get_chord_notes("G#m") == ["G#", "B", "D#"]
    assert Music_Theory.get_chord_notes("G#o") == ["G#", "B", "D"]
    assert Music_Theory.get_chord_notes("G#-") == ["G#", "B", "D"]
    assert Music_Theory.get_chord_notes("G#+") == ["G#", "B#", "D##"]
    assert Music_Theory.get_chord_notes("Ab") == ["Ab", "C", "Eb"]
    assert Music_Theory.get_chord_notes("Abm") == ["Ab", "Cb", "Eb"]
    assert Music_Theory.get_chord_notes("Abo") == ["Ab", "Cb", "Ebb"]
    assert Music_Theory.get_chord_notes("Ab+") == ["Ab", "C", "E"]

    assert Music_Theory.get_chord_notes("A") == ["A", "C#", "E"]
    assert Music_Theory.get_chord_notes("Am") == ["A", "C", "E"]
    assert Music_Theory.get_chord_notes("Ao") == ["A", "C", "Eb"]
    assert Music_Theory.get_chord_notes("A-") == ["A", "C", "Eb"]
    assert Music_Theory.get_chord_notes("A+") == ["A", "C#", "E#"]
    assert Music_Theory.get_chord_notes("G##o") == ["G##", "B#", "D#"]
    assert Music_Theory.get_chord_notes("Bbb") == ["Bbb", "Db", "Fb"]
    assert Music_Theory.get_chord_notes("Bbb+") == ["Bbb", "Db", "F"]

    assert Music_Theory.get_chord_notes("A#") == ["A#", "C##", "E#"]
    assert Music_Theory.get_chord_notes("A#m") == ["A#", "C#", "E#"]
    assert Music_Theory.get_chord_notes("A#o") == ["A#", "C#", "E"]
    assert Music_Theory.get_chord_notes("A#-") == ["A#", "C#", "E"]
    assert Music_Theory.get_chord_notes("A#+") == ["A#", "C##", "E##"]
    assert Music_Theory.get_chord_notes("Bb") == ["Bb", "D", "F"]
    assert Music_Theory.get_chord_notes("Bbm") == ["Bb", "Db", "F"]
    assert Music_Theory.get_chord_notes("Bbo") == ["Bb", "Db", "Fb"]
    assert Music_Theory.get_chord_notes("Bb+") == ["Bb", "D", "F#"]

    assert Music_Theory.get_chord_notes("B") == ["B", "D#", "F#"]
    assert Music_Theory.get_chord_notes("Bm") == ["B", "D", "F#"]
    assert Music_Theory.get_chord_notes("Bo") == ["B", "D", "F"]
    assert Music_Theory.get_chord_notes("B-") == ["B", "D", "F"]
    assert Music_Theory.get_chord_notes("B+") == ["B", "D#", "F##"]
    assert Music_Theory.get_chord_notes("Cb") == ["Cb", "Eb", "Gb"]
    assert Music_Theory.get_chord_notes("Cbm") == ["Cb", "Ebb", "Gb"]
    assert Music_Theory.get_chord_notes("Cb+") == ["Cb", "Eb", "G"]


def test_pretty_display():
    # Test a few regular cases and a few special cases, with and without verbose

    assert Music_Theory.pretty_display("C") == "C"
    assert Music_Theory.pretty_display("Am") == "Am"
    assert Music_Theory.pretty_display("Abo") == "Ab°"
    assert Music_Theory.pretty_display("Ab-") == "Ab°"
    assert Music_Theory.pretty_display("Gbm+") == "Gbm⁺"
    assert Music_Theory.pretty_display("C", verbose=True) == "C"
    assert Music_Theory.pretty_display("Am", verbose=True) == "Am (min)"
    assert Music_Theory.pretty_display("Abo", verbose=True) == "Ab° (dim)"
    assert Music_Theory.pretty_display("Ab-", verbose=True) == "Ab° (dim)"
    assert Music_Theory.pretty_display("Gbm+", verbose=True) == "Gbm⁺ (aug)"


def test_get_enharmonic_note():
    # This method is used to find an enharmonic equivalent. If the second argument is provided,
    # the method will return the specific equivalent for that note.
    assert Music_Theory._get_enharmonic_note("E#", None) == "F"
    assert Music_Theory._get_enharmonic_note("E#", "F") == "F"
    assert Music_Theory._get_enharmonic_note("F", "E") == "E#"
    assert Music_Theory._get_enharmonic_note("G", "A") == "Abb"
    assert Music_Theory._get_enharmonic_note("A", "G") == "G##"


def test_get_next_expected_note():
    # This method is used to find the name of the next note, without accidentals
    assert Music_Theory._get_next_expected_note("C") == "D"
    assert Music_Theory._get_next_expected_note("C#") == "D"
    assert Music_Theory._get_next_expected_note("Cb") == "D"
    assert Music_Theory._get_next_expected_note("G") == "A"
    assert Music_Theory._get_next_expected_note("Gb") == "A"
    assert Music_Theory._get_next_expected_note("G#") == "A"
    with pytest.raises(ValueError):
        Music_Theory._get_next_expected_note("H")


def test_get_intervals():
    assert Music_Theory._get_intervals("major") == [2, 2, 1, 2, 2, 2, 1]
    assert Music_Theory._get_intervals("minor") == [2, 1, 2, 2, 1, 2, 2]
    assert Music_Theory._get_intervals("natural minor") == [2, 1, 2, 2, 1, 2, 2]
    assert Music_Theory._get_intervals("harmonic minor") == [2, 1, 2, 2, 1, 3, 1]
    assert Music_Theory._get_intervals("melodic minor") == [2, 1, 2, 2, 2, 2, 1]
    with pytest.raises(ValueError):
        Music_Theory._get_intervals("invalid")


def test_get_note_position():
    assert Music_Theory._get_note_position("C", ["C", "D", "E", "F", "G", "A", "B", "C"]) == 0
    assert Music_Theory._get_note_position("G", ["C", "D", "E", "F", "G", "A", "B", "C"]) == 4
    assert Music_Theory._get_note_position("G#", ["C", "D", "E", "F", "G", "A", "B", "C"]) == -1


def test_sharpen():
    assert Music_Theory._sharpen("C") == "C#"
    assert Music_Theory._sharpen("C#") == "C##"
    assert Music_Theory._sharpen("Cb") == "C"
    assert Music_Theory._sharpen("Gbb") == "Gb"
    assert Music_Theory._sharpen(Music_Theory._sharpen("Gbb")) == "G"
    assert Music_Theory._sharpen(Music_Theory._sharpen(Music_Theory._sharpen("Gbb"))) == "G#"


def test_flatten():
    assert Music_Theory._flatten("C") == "Cb"
    assert Music_Theory._flatten("Cb") == "Cbb"
    assert Music_Theory._flatten("C#") == "C"
    assert Music_Theory._flatten("C##") == "C#"
    assert Music_Theory._flatten(Music_Theory._flatten("C##")) == "C"
    assert Music_Theory._flatten(Music_Theory._flatten(Music_Theory._flatten("C##"))) == "Cb"
