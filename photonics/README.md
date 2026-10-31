# PHOTON-X Photonics — First Milestone

## Goal

Develop a simulation-validated photonic integrated circuit (PIC) that accelerates a narrowly defined matrix-vector operation used in image reconstruction or scientific signal processing. The first design is an **experimental optical linear-algebra accelerator**, not a 1024-bit general-purpose CPU and not a complete photonic computer.

## Recommended starting platform

- **Process:** silicon photonics, selected only after comparing available foundry PDKs.
- **Core concept:** coherent optical interferometer mesh with tunable phase shifters and calibrated input/output coupling.
- **Electronic support:** laser source, modulators, drivers, monitor photodiodes, transimpedance amplifiers, ADC/DAC, thermal control, and FPGA controller.
- **Initial workload:** small real-valued matrix-vector multiplication, then complex-valued operations if the chosen architecture supports them.
- **Numerical validation:** compare output against NumPy double-precision reference; quantify absolute/relative error, insertion loss, energy per operation, drift, and repeatability.

## Work packages

1. `requirements.md` — workload, precision, bandwidth, and acceptance criteria.
2. `architecture.md` — optical/electronic partition and signal path.
3. `simulation/` — ideal and non-ideal numerical model.
4. `layout/` — PDK-specific GDS only after a process is selected.
5. `characterization/` — test structures, calibration, and measurement plan.
6. `costs/` — explicit assumptions, ranges, and supplier quote tracking.

## Important constraints

- Photonic propagation is not display refresh rate and does not imply light-speed FPS.
- Optical matrix computation is affected by loss, phase errors, detector noise, wavelength drift, thermal crosstalk, and calibration overhead.
- A foundry PDK and its design rules are mandatory before a fabrication-ready layout can be claimed.
- Do not send generic GDS to a foundry without process-specific DRC/LVS and tapeout checks.

## First acceptance gate

A software simulation must reproduce a set of known matrix-vector results within a declared error tolerance under both ideal and non-ideal conditions. The tolerance will be selected after the target microscope workload and sensor data range are specified.
