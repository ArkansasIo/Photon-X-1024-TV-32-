# PHOTON-X Photonic Projector Requirements — Rev 0.1

## 1. System purpose

Provide a high-resolution optical display output for scientific visualization from the PHOTON-X quantum microscopy workstation. The projector is a companion output device; it does not replace the microscope sensor or create additional experimental resolution.

## 2. Target specifications

| Requirement | Rev 0.1 target | Status |
|---|---:|---|
| Native image raster | 7680 × 4320 pixels | Target; SLM availability must be verified |
| Refresh rate | 120 Hz | Target; requires matching SLM, driver and optical engine |
| Stretch refresh | 240 Hz | Research item, not committed |
| Reference projected image | 32-inch diagonal | Initial optical qualification target |
| Projection size | Adjustable | To be set by throw ratio and lens design |
| Colour | RGB | Laser wavelengths and gamut to be selected |
| Light engine | RGB laser + reflective LCoS candidate | Architecture candidate |
| Focus | Motorized or calibrated manual | Design decision |
| Geometry correction | Keystone/warp correction | Required |
| Synchronization | External trigger/genlock option | Required for microscope acquisition playback |
| Input | DisplayPort/HDMI-class high-bandwidth interface | Standard/version TBD after bandwidth budget |
| Control | Ethernet + USB/service interface | Target |
| Host compute | PHOTON-X CPU/GPU and experimental vector datapath | Shared platform |
| Photonic compute | Optional PIC accelerator | Separate from projector light engine |

## 3. Image data budget

For uncompressed 24-bit RGB active pixels only:

- Pixels per frame: 7,680 × 4,320 = 33,177,600.
- Bits per frame: 33,177,600 × 24 = 796,262,400 bits.
- At 60 Hz: 47.78 Gbit/s active-pixel payload.
- At 120 Hz: 95.55 Gbit/s active-pixel payload.
- At 240 Hz: 191.10 Gbit/s active-pixel payload.

These are payload-only calculations. Actual link capacity must account for blanking, encoding, colour depth, chroma format, transport overhead, and compression. The interface must be selected from the complete timing and bandwidth budget.

## 4. Image-quality requirements

Measure and report:
- Native pixel mapping and focus uniformity across the field.
- Modulation transfer function (MTF) and contrast.
- Brightness and uniformity at the reference image size.
- Colour gamut, white point, and channel balance.
- Speckle and temporal stability for coherent laser illumination.
- Geometric distortion and correction residual.
- Thermal drift and focus shift.
- Input-to-photon latency and frame synchronization.

No numerical brightness, contrast, gamut, MTF, or speckle target is claimed until the screen size, ambient illumination, throw distance, optical engine, and SLM are selected.

## 5. Acceptance gates

1. Verify the chosen 8K SLM supports the intended raster and refresh timing.
2. Demonstrate stable RGB illumination and safe beam containment.
3. Measure focus, MTF, contrast, colour, brightness uniformity, and speckle.
4. Validate full input bandwidth and synchronization.
5. Pass thermal soak and fault/interlock tests.
6. Confirm measured performance against the approved requirements before claiming a specification.
