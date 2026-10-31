# PHOTON-X 1024 — 32-inch TV Display Subsystem

## Purpose
Define the workstation's direct-view 32-inch 8K display as a subsystem independent of the photonic projector. This is a research specification, not a claim that a custom panel or 50 GHz display interface already exists.

## Baseline targets
- Active resolution: 7680 × 4320 (8K UHD)
- Diagonal: 32 inches
- Aspect ratio: 16:9
- Initial refresh target: 120 Hz
- Stretch target: 240 Hz, subject to panel and timing-controller capability
- Colour pipeline: RGB, with a documented high-bit-depth internal processing path
- Host connection: high-throughput digital video link; optical transport may be used between chassis and display controller
- Experimental high-speed target: evaluate 50 GHz-class component/link bandwidth where justified by the selected PHY, optical modulator, receiver, or clocking technology

## Architecture
See [architecture.md](architecture.md), [signal_pipeline.md](signal_pipeline.md), and [requirements.md](requirements.md).

## Engineering cautions
- 50 GHz is a frequency/bandwidth target, not 50 billion frames per second.
- The panel refresh rate is limited by the pixel array, gate/source drivers, timing controller, interface, and thermal design.
- Optical fiber transports encoded data; it does not directly drive ordinary LCD/OLED pixels.
- A fiber receiver and display timing controller are required before panel drive electronics.
- A custom 8K/240 Hz panel must not be assumed available until a supplier confirms its native timing and interface specifications.

## Status
Concept specification. No custom panel, optical receiver, timing controller, or prototype has been built or validated.
