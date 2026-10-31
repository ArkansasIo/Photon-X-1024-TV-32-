# Projector Control Interface — Rev 0.1

## Controller responsibilities

- Receive and validate projector configuration.
- Coordinate frame timing and optional external synchronization.
- Monitor SLM, laser drivers, optical power monitors, fans/pumps, and temperature sensors.
- Enforce hardware interlock state and laser-enable sequencing.
- Record faults and telemetry for the host.
- Enter a safe state on watchdog timeout, overtemperature, enclosure-open, or interlock fault.

## Suggested logical signals

| Signal | Direction | Description |
|---|---|---|
| FRAME_SYNC_IN | Input | External frame/genlock reference |
| FRAME_VALID | Input | Valid incoming frame indication |
| SLM_RESET_N | Output | SLM controller reset |
| SLM_ENABLE | Output | SLM operation enable |
| LASER_ENABLE_R/G/B | Output | Per-channel laser enable, gated by safety chain |
| LASER_FAULT_R/G/B | Input | Driver fault status |
| OPTICAL_POWER_MON | Input | Monitor photodiode telemetry |
| INTERLOCK_OK | Input | Independent safety-chain state |
| TEMP_WARN/FAULT | Input | Thermal thresholds |
| FAN_OK | Input | Cooling system health |
| WATCHDOG | Internal | Controller health supervision |

## Safety rule

The FPGA or host software must not be the sole laser safety mechanism. Use an independent hardware interlock and fail-safe emission-disable path designed and reviewed for the selected laser modules.
