# TV Display Requirements

## 1. Display envelope
| ID | Requirement | Target / status |
|---|---|---|
| TV-MECH-001 | Diagonal | 32 in nominal |
| TV-MECH-002 | Aspect ratio | 16:9 |
| TV-MECH-003 | Active resolution | 7680 × 4320 |
| TV-PNL-001 | Native refresh | 120 Hz initial target; supplier verification required |
| TV-PNL-002 | High refresh | 240 Hz stretch target; custom panel/driver feasibility study |
| TV-COL-001 | Colour format | RGB pipeline; chroma subsampling permitted only as an explicit transport mode |
| TV-COL-002 | Processing precision | 10-bit/channel target; 12-bit internal processing where practical |
| TV-LNK-001 | Host link | Capacity sized from measured payload plus protocol overhead |
| TV-LNK-002 | Optical link | Fiber transport option with optical receiver at display controller |
| TV-LNK-003 | High-speed research | Assess 50 GHz-class bandwidth components; characterize BER, jitter, thermal drift and eye margin |
| TV-TIM-001 | Synchronization | Frame/line timing, clock recovery, deterministic link alignment |
| TV-IMG-001 | Processing | Scaling, colour management, transfer function, uniformity and calibration |
| TV-THM-001 | Thermal | Panel, timing controller, PHY and power supply temperature monitoring |
| TV-SAF-001 | Safety | Electrical, thermal, optical and enclosure safety review |

## 2. Raw active-pixel bandwidth
For 7680 × 4320 pixels, RGB 8-bit/channel (24 bits/pixel), active image payload is:
- 60 Hz: 47.78 Gbit/s
- 120 Hz: 95.55 Gbit/s
- 240 Hz: 191.10 Gbit/s
- 480 Hz: 382.21 Gbit/s
- 1000 Hz: 796.26 Gbit/s

For RGB 10-bit/channel (30 bits/pixel), multiply these values by 1.25. For RGB 12-bit/channel (36 bits/pixel), multiply by 1.5. These are active-pixel payloads only; blanking, packet framing, FEC, line coding and link margin increase required transport capacity.

## 3. Meaning of 50 GHz
50 GHz denotes 50 billion cycles per second. It may describe an analog bandwidth, clock frequency, or symbol rate only when the component specification says so. It does not by itself specify bits per second or frames per second. The system-level link budget must state modulation, symbols per second, bits per symbol, coding overhead, lane count, and measured error performance.

## 4. Acceptance principles
- Use native panel timing, not interpolated marketing refresh, for refresh-rate claims.
- Verify sustained operation at target resolution, refresh, bit depth and chroma format simultaneously.
- Measure end-to-end latency and frame drops.
- Do not claim 50 GHz operation without a named component, interface specification, and bench measurement.
