# Photonic Accelerator Requirements — Rev 0.1

## Scope

Build a simulation-first silicon-photonics demonstrator for a small, explicitly defined linear-algebra workload. The target is an experimental accelerator connected to an electronic host, not a replacement for the CPU/GPU and not a universal quantum computer.

## Initial workload

- Operation: real-valued matrix-vector multiplication, `y = A x`.
- Prototype scale: begin with 2x2 and 4x4 matrices in software; increase only after error and calibration behaviour are understood.
- Reference: NumPy float64 implementation.
- Optical implementation: coherent interferometer network with tunable phase shifts; exact mesh topology is a design decision to be tested.

## Metrics to report

- Relative L2 error and maximum absolute error versus reference.
- Optical insertion loss and loss imbalance.
- Phase-setting error and thermal drift.
- Detector noise and dynamic range.
- Calibration time and recalibration frequency.
- Electrical power for laser, drivers, heaters, detectors, ADC/DAC, and control.
- End-to-end latency including electronic/optical conversion and calibration overhead.

## Provisional acceptance gates

1. Ideal numerical model reproduces the reference operation within numerical tolerance.
2. Non-ideal model reports error as a function of loss, phase error, noise, and drift.
3. Calibration algorithm converges from defined initial conditions.
4. Repeatability is quantified over repeated simulated trials.
5. A hardware prototype is not approved until measured component specifications and a process-specific PDK are available.

No speedup, energy advantage, precision, or cost target is claimed until measured against a defined electronic baseline.
