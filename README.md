# PHOTON-X 1024

Scientific workstation and quantum microscopy platform.

## Initial engineering direction

The first photonics milestone is a **simulation-first silicon-photonics optical matrix-vector engine** intended as an experimental accelerator for selected linear-algebra workloads. It is not a general-purpose optical CPU. The electronic host remains responsible for control flow, memory management, instrument safety, and microscope operation.

## First milestone

1. Define the optical compute workload and numerical precision target.
2. Model a passive interferometer mesh and its calibration requirements.
3. Simulate optical loss, phase error, detector noise, and drift.
4. Compare simulated results against a CPU/GPU reference implementation.
5. Only after the model passes acceptance tests, prepare a foundry-process-specific layout and request a fabrication quote.

## Project status

Concept and simulation planning. No photonic chip has been fabricated or validated. All performance and cost figures must be marked as estimates until supported by measured data or supplier quotations.

## Repository areas

- `photonics/` — PIC architecture, simulation, layout, and characterization
- `photonic-projector/` — separate RGB laser/SLM 8K projection subsystem, control, costs, and verification
- `quantum-microscope/` — NV-diamond microscope concept and instrument interfaces
- `hardware/` — workstation and instrument hardware
- `firmware/` — FPGA and control firmware
- `software/` — acquisition, reconstruction, and analysis
- `docs/` — requirements, safety, verification, and cost assumptions
- `tests/` — simulation and software validation
