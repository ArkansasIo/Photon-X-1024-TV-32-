# Audio Requirements

| ID | Requirement | Initial target / verification |
|---|---|---|
| AUD-001 | Baseline channels | 2.0 stereo |
| AUD-002 | Expansion | Digital multichannel pass-through where supported |
| AUD-003 | PCM input | 24-bit / 96 kHz baseline; evaluate 24-bit / 192 kHz |
| AUD-004 | DSP | EQ, volume, balance, crossover, limiter and delay |
| AUD-005 | DAC | Low-noise stereo DAC; select after measured evaluation |
| AUD-006 | Amplifier | Class-D with thermal, over-current and DC protection |
| AUD-007 | Speakers | Matched left/right drivers in tuned enclosures |
| AUD-008 | Subwoofer | Optional line-level output with configurable low-pass filter |
| AUD-009 | Headphones | Optional low-noise headphone output |
| AUD-010 | Sync | Timestamped A/V synchronization and adjustable audio delay |
| AUD-011 | Noise | No objectionable hiss, hum, buzz or switching interference |
| AUD-012 | Calibration | Frequency response, distortion, noise and SPL measurements |
| AUD-013 | Power | Separate filtered audio rails or isolated conversion as required |
| AUD-014 | Thermal | Amplifier and enclosure temperatures remain within component ratings |

## Audio quality metrics
Measure and publish:
- Frequency response and deviation across the listening window.
- THD+N at specified output power, load and frequency.
- Signal-to-noise ratio with stated weighting and bandwidth.
- Crosstalk between channels.
- Maximum unclipped output and maximum SPL at a stated distance.
- A/V synchronization error in milliseconds.
- Response to digital full-scale, silence, sample-rate changes and input dropouts.

Do not use a codec's advertised bit depth or sample rate as a substitute for measured acoustic performance. Speaker drivers, enclosure design, amplifier headroom, room placement and DSP are equally important.
