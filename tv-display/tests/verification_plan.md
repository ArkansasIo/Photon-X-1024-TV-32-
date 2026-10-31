# TV Display Verification Plan

## Test stages
### TV-VT-01 — Panel capability
- Obtain panel datasheet and supplier confirmation.
- Verify native 7680 × 4320 resolution.
- Verify native refresh rate at the intended bit depth and chroma mode.
- Record brightness, contrast, uniformity, viewing angle, power and thermal limits.

### TV-VT-02 — Transport bandwidth
- Calculate payload from resolution, refresh, bit depth and chroma format.
- Add measured protocol overhead, FEC and engineering margin.
- Verify sustained throughput without dropped or reordered packets.
- Measure BER and link margin at the intended fiber length.

### TV-VT-03 — 50 GHz component characterization
- Identify the exact component and whether 50 GHz refers to clock, symbol rate, carrier, or analog bandwidth.
- Use suitable calibrated test equipment and fixtures.
- Measure frequency response, jitter, eye opening, insertion loss and temperature dependence.
- Do not infer end-to-end throughput from a component bandwidth label.

### TV-VT-04 — Timing and latency
- Measure host-to-panel latency with timestamped test frames.
- Measure frame period, scan timing and input-to-photon latency.
- Verify clock recovery, genlock and clock-domain crossings.
- Test line/tile streaming and buffer underflow/overflow handling.

### TV-VT-05 — Image quality
- Verify pixel mapping, geometry, colour accuracy, grayscale, gamma/EOTF, uniformity and dead/stuck pixels.
- Verify no tearing, line corruption, flicker or frame judder at supported modes.

### TV-VT-06 — Thermal and reliability
- Run sustained maximum-rate patterns at worst-case ambient conditions.
- Monitor panel, TCON, PHY, memory and power supply temperatures.
- Test power sequencing, link loss, watchdog and safe blanking behavior.

## Exit criteria
A mode is declared supported only after all panel, transport, timing, image-quality and thermal tests pass together. Label simulation-only results separately from measured hardware results.
