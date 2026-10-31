# TV Signal Pipeline and Timing

## Data path
1. GPU produces a frame with a timestamp and frame sequence number.
2. Colour pipeline converts to the panel's supported colour space, transfer function and bit depth.
3. Packetizer divides the frame into line or tile packets with frame-start, line/tile coordinates, sequence numbers and integrity checks.
4. Optional optical transmitter converts encoded electrical data into a modulated optical carrier.
5. Fiber carries the encoded stream to the TV receiver.
6. Receiver performs clock/data recovery, decoding, integrity checks and error reporting.
7. Line/frame buffer aligns incoming data to panel scan timing.
8. TCON drives the panel-specific source and gate timing.

## Timing model
At refresh rate F, one frame period is T = 1/F:
- 120 Hz -> 8.333 ms
- 240 Hz -> 4.167 ms
- 480 Hz -> 2.083 ms
- 1000 Hz -> 1.000 ms

These are frame periods, not fiber propagation times. Fiber propagation in typical silica is approximately 5 microseconds per kilometre one-way; transceiver, coding, buffering and panel scan add further latency.

## Streaming policy
- Prefer line/tile streaming when the selected panel controller supports it.
- Preserve frame and line boundaries.
- Use a small deterministic buffer to absorb packet jitter.
- Do not update panel regions asynchronously unless the panel supports the required partial-update mode.
- Use genlock or a defined clock-domain crossing strategy between host, link and panel.
- On CRC/FEC failure or loss of synchronization, discard the damaged region/frame and enter the defined recovery path.

## 50 GHz vs throughput
A 50 GHz carrier or analog bandwidth is not the same as 50 Gbit/s. A 50 GBd symbol stream has 50 billion symbols per second; raw bit rate depends on bits per symbol and coding. The exact link rate must be derived from the chosen modulation, number of wavelengths/lanes, coding and receiver capability.
