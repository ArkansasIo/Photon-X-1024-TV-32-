# PHOTON-X Audio Architecture

```text
PHOTON-X HOST / VIDEO SOURCE
          |
          +---- DIGITAL AUDIO STREAM + TIMESTAMPS
                         |
                         v
                AUDIO INPUT RECEIVER
                         |
                         v
                 CLOCK / BUFFER STAGE
                         |
                         v
                  AUDIO DSP ENGINE
           EQ / CROSSOVER / VOLUME / DELAY
                         |
                         v
                    DAC (L/R)
                         |
                         v
                CLASS-D AMPLIFIER
                    |       |
                    v       v
                  LEFT    RIGHT
                 SPEAKER SPEAKER

Optional digital pass-through:
DSP / audio receiver -> eARC or digital output -> external AV receiver
Optional subwoofer:
DSP low-pass output -> line-level subwoofer output
```

## Functional blocks
1. **Input receiver:** Accept digital audio from the host over the selected video/audio interface or dedicated audio link.
2. **Clock and buffering:** Recover or derive a stable audio clock, buffer packets and detect dropouts.
3. **DSP:** Apply channel mapping, parametric EQ, crossover, volume, limiter and lip-sync delay.
4. **DAC:** Convert processed PCM to analog with a low-noise reference and carefully managed grounding.
5. **Amplifier:** Drive the speakers with adequate headroom and protection.
6. **Acoustic system:** Enclosure, drivers, damping and port/passive-radiator design are tuned as one system.
7. **External output:** Provide a digital pass-through path for users who prefer an external receiver or higher-power speaker system.

## Synchronization
Use timestamps or a shared media clock to align audio with displayed video. Measure end-to-end A/V offset at each supported refresh mode. Provide adjustable audio delay to correct display processing latency. Avoid assuming that the fiber video link automatically transports synchronized audio; define the audio transport and clocking explicitly.

## Design choice
Start with a high-quality stereo system integrated into the display chassis, plus digital audio output for multichannel expansion. This avoids forcing a complex surround-speaker array into a 32-inch enclosure.
