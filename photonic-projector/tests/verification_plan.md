# Projector Verification Plan — Rev 0.1

## Bench tests

| ID | Test | Measurement | Pass condition |
|---|---|---|---|
| PRJ-T01 | Raster | Capture and inspect native pixel map | 7680 × 4320 native mapping verified |
| PRJ-T02 | Refresh | High-speed photodiode/camera timing | Stable 120 Hz if claimed |
| PRJ-T03 | Focus | Resolution target across image field | Meets approved MTF/focus limits |
| PRJ-T04 | Uniformity | Calibrated imaging photometer | Meets approved brightness and colour uniformity limits |
| PRJ-T05 | Colour | Spectroradiometer | Meets approved white point and gamut limits |
| PRJ-T06 | Speckle | Defined imaging geometry and estimator | Meets approved speckle criterion |
| PRJ-T07 | Latency | Input timestamp to optical output | Measured and reported |
| PRJ-T08 | Thermal | Thermal soak under maximum rated mode | No component exceeds rated limit |
| PRJ-T09 | Synchronization | External trigger and frame capture | No dropped or mis-timed frames in test interval |
| PRJ-T10 | Safety | Interlock and fault injection | Emission disables safely on every defined fault |

## Test reporting

Every report must record:
- Hardware revision and serial numbers.
- Firmware/software version.
- Ambient conditions and screen geometry.
- Instrument calibration status.
- Raw data and analysis scripts.
- Pass/fail result and deviations.

No pass claim is valid until measurements are captured from a physical prototype.
