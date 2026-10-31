# PHOTON-X Photonic Projector — Rev 0.1

A second, separate optical-output subsystem in the PHOTON-X 1024 repository. It shares the workstation's system-level targets while using a projector-specific optical engine.

## Project targets

- Native output target: 7680 × 4320 (8K UHD).
- Refresh target: 120 Hz; 240 Hz is a stretch goal requiring a suitable 8K spatial-light modulator, driver electronics, and validated optical/thermal performance.
- Reference image size: 32-inch diagonal for initial optical qualification; projection optics should support a wider throw/size range after optical design.
- Light engine: RGB laser-illuminated reflective LCoS or another qualified 8K spatial-light-modulator architecture selected after component research.
- Compute platform: shared PHOTON-X host; retain the proposed 1024-bit vector datapath as an experimental compute architecture, not a claim of an available commercial 1024-bit projector chip.
- Photonic compute: optional accelerator module; projection light engine and photonic matrix processor are distinct subsystems.
- Primary application: scientific visualization for quantum microscopy, including high-resolution maps, spectra, reconstructed volumes, and instrument dashboards.

## Important distinction

This is a **photonic/laser projection system**, not a projector that computes by sending pixels through a photonic CPU. The projector's light engine forms the image; the workstation and optional photonic accelerator perform the calculations.

## Engineering status

Concept-level specification only. No optical engine, projector lens, 8K SLM, laser module, or thermal design has yet been selected or validated. Cost fields remain quote-required until vendors and parts are selected.

## Work packages

- `requirements.md` — performance and acceptance requirements
- `architecture.md` — optical/electronic block architecture
- `optics/optical_engine.md` — RGB illumination, SLM, projection lens, and calibration
- `firmware/control_interface.md` — timing, sync, and safety interface
- `costs/preliminary_bom.csv` — cost categories and quote status
- `costs/README.md` — estimating rules and exclusions
- `tests/verification_plan.md` — bench validation plan

## Safety

Laser classification, accessible emission limits, interlocks, beam containment, thermal management, and service procedures must be evaluated against the selected laser modules and applicable standards before any powered prototype is operated.
