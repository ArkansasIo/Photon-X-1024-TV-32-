# PHOTON-X Photonic Projector Architecture — Rev 0.1

## 1. Functional partition

The projector is an optical output subsystem. The workstation computes and prepares frames; the projector converts those frames into a controlled optical image.

```text
Microscope acquisition / reconstructed data
                 |
          PHOTON-X host CPU/GPU
                 |
       Optional photonic compute PIC
                 |
       Image compositor / calibration
                 |
     High-bandwidth video interface
                 |
      Projector timing + frame buffer
                 |
       SLM driver and synchronization
                 |
 RGB laser sources -> illumination optics
                 |              |
                 +----> reflective SLM
                              |
                     projection lens
                              |
                     calibrated screen
```

## 2. Candidate optical engine

Candidate Rev 0.1: three-channel RGB laser illumination with a reflective LCoS spatial-light modulator (SLM).

Potential benefits:
- Separate red, green, and blue illumination channels.
- High-resolution spatial modulation if a suitable native 8K SLM is available.
- Optical efficiency and colour gamut can be evaluated independently.

Key engineering risks:
- Native 8K SLM resolution and refresh-rate availability.
- Pixel fill factor, diffraction, contrast, polarization management, and thermal load.
- Laser speckle and coherence artifacts.
- Uniform illumination and colour registration.
- Optical alignment and long-term stability.

Alternative architectures (DLP, transmissive LCD, scanned-laser, tiled SLM) must be compared before selecting a final engine. Do not assume that a single-chip 8K/120 Hz component exists in the required form factor.

## 3. Electronic control

- Video receiver and frame buffer.
- SLM timing controller and high-speed drivers.
- RGB laser current drivers and monitor photodiodes.
- Optical power monitoring and thermal sensors.
- FPGA or deterministic controller for synchronization and safety state.
- Host control over Ethernet/USB.
- Independent hardware interlock that disables laser emission on fault.

## 4. Mechanical and thermal

- Separate rigid optical chassis; do not attach precision optics to the display panel.
- Adjustable lens mount and alignment references.
- Heat sink and forced-air or liquid cooling selected from measured thermal load.
- Service access for filters, optics, laser modules, and SLM.
- Enclosure designed to contain stray beams and prevent user access to hazardous emission.

## 5. Interface with quantum microscope

The microscope sends measured data and reconstructed images to the workstation. The projector displays those results. It is not part of the microscope's measurement chain and must not introduce light into the sample path unless a separately designed illumination/measurement mode explicitly requires it.

## 6. Separation from photonic computing

The silicon-photonics matrix processor in `/photonics` performs selected computational operations. The projector's laser/SLM engine forms visible images. They may share host software, timing, and power infrastructure, but they are not the same optical subsystem.
