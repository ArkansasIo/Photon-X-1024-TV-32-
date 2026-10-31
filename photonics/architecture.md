# Photonic Accelerator Architecture — Rev 0.1

## System partition

`Host CPU/GPU -> FPGA/control -> DAC + modulator drivers -> PIC -> photodetectors + TIAs -> ADC -> host reconstruction`

### Optical path

1. A qualified laser source supplies a stable optical carrier.
2. Input modulators encode vector elements as optical amplitudes/phases.
3. A tunable interferometer mesh applies the programmed linear transform.
4. Output couplers route optical signals to photodetectors.
5. Detector electronics convert optical power to electrical signals.

### Electronic path

- CPU: experiment orchestration, data integrity, configuration, safety state machine.
- GPU: reference computation, image reconstruction, and post-processing.
- FPGA: deterministic timing, synchronized DAC/ADC, modulator and detector control.
- Analog front end: drivers, bias circuits, photodiode TIAs, filtering, and conversion.

## Initial design decisions

- Start with a software model, not a custom chip.
- Keep the optical compute core small and observable.
- Include monitor taps and calibration structures in any future PIC.
- Separate the microscope's NV-sensor laser/microwave controls from the photonic compute laser path. They are different subsystems with different safety and stability requirements.
- Do not mount vibration-sensitive optical components to the display enclosure. Use a rigid optical base and connect the workstation electronically.

## PDK and fabrication

A fabrication layout must target one named process and its released PDK. PDK rules, device models, wavelength range, layer stack, heater limits, coupler design, and DRC/LVS flow govern the final design. Generic GDS is not tapeout-ready.

## Block diagram

```text
Scientific data / microscope reconstruction
                 |
             Host CPU/GPU
                 |
       FPGA timing + calibration
          /              \
     DAC/drivers       ADC/TIAs
          |                ^
       Modulators       Detectors
          |                ^
          +--> PIC mesh ---+
                 |
          optical transform
```

## Not in Rev 0.1

- Quantum-state generation or universal quantum computing.
- General-purpose photonic instruction set.
- 1024-bit address space or proven 1024-bit CPU/GPU.
- Fabrication-ready GDS or validated performance claims.
