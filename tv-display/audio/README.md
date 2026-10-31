# PHOTON-X TV Audio Subsystem

## Purpose
Specify the audio system for the 32-inch PHOTON-X display. Audio is treated as a separate signal chain from the 8K video path, with synchronized playback, low noise, clear dialogue, accurate stereo imaging, and expansion for multichannel audio.

## Design goals
- High-fidelity stereo playback as the baseline.
- Optional multichannel output through external amplification or powered speakers.
- Digital audio transport from the workstation, synchronized to video timestamps.
- Low-noise DAC and amplifier stages with appropriate grounding and power filtering.
- User-selectable EQ, loudness, balance, channel mapping and audio delay.
- Headphone output and digital audio output as optional interfaces.

## Proposed configuration
- Digital input: HDMI/DisplayPort audio or a dedicated USB/I2S audio interface, depending on host and controller selection.
- Internal processing: DSP for crossover, EQ, volume, delay and protection.
- Conversion: high-performance stereo DAC for analog outputs.
- Amplification: Class-D power amplifier module with thermal and over-current protection.
- Speakers: matched left/right drivers in acoustically isolated enclosures; optional subwoofer output.
- Expansion: eARC/optical digital output or multichannel digital output, subject to interface licensing and implementation.

## Quality targets
These are engineering targets, not measured product specifications:
- Support lossless PCM input at common studio rates, including 24-bit/96 kHz; evaluate 24-bit/192 kHz end-to-end.
- Frequency response target: 60 Hz–20 kHz within a defined tolerance after enclosure tuning.
- Low audible hiss, hum, clipping and distortion at normal listening levels.
- Controlled latency and adjustable A/V synchronization.
- Acoustic measurements required before any THD+N, SNR, frequency-response or maximum-SPL claim is published.

## Safety and implementation
Speaker amplifier power must be selected from driver impedance, sensitivity, enclosure volume and thermal limits. Include DC protection, over-current/over-temperature protection, startup mute, pop suppression and safe shutdown. Do not connect speaker outputs directly to line-level inputs.
