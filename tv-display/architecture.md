# 32-inch 8K TV Display Architecture

## Functional block diagram

```text
PHOTON-X HOST CPU / GPU
        |
        v
DISPLAY COMPOSITOR + COLOUR PIPELINE
        |
        v
VIDEO PACKETIZER / LINK ENCODER
        |
        v
OPTICAL TRANSMITTER (optional fiber transport)
        |
      FIBER
        |
        v
OPTICAL RECEIVER + CLOCK/DATA RECOVERY
        |
        v
FRAME / LINE BUFFER
        |
        v
DISPLAY TIMING CONTROLLER (TCON)
        |
        v
SOURCE + GATE DRIVER ELECTRONICS
        |
        v
32-inch 8K PANEL (LCD / OLED / microLED candidate)
        |
        v
VIEWER
```

## Recommended partition
1. **Host processing:** GPU renders or composes frames and applies colour management.
2. **Transport:** Encode frames into a defined video transport. Fiber is an optional physical medium; the protocol and optical PHY must be selected together.
3. **Receiver:** Recover clock/data, check packet integrity, report link errors, and provide deterministic timing.
4. **Buffering:** Use bounded line/frame buffers. Select buffer depth based on latency and panel timing; avoid unbounded buffering.
5. **TCON:** Generate panel-specific row/column timing and coordinate source/gate drivers.
6. **Panel:** Evaluate LCD, OLED and microLED based on native 8K resolution, refresh, brightness, contrast, uniformity, power and lifetime.

## Panel technology decision
- **LCD:** Mature large-area manufacturing; requires a backlight and local-dimming design if high contrast is required.
- **OLED:** Self-emissive pixels and strong contrast; assess burn-in, peak brightness, lifetime and 8K/refresh availability.
- **MicroLED:** Attractive emissive architecture but a 32-inch 8K high-refresh implementation is a substantial integration/manufacturing challenge.

No panel technology is selected until native resolution, native refresh, bit depth, interface, power and supplier data are confirmed.

## 50 GHz engineering workstream
Treat 50 GHz as a component-level research target. Candidate locations include a high-speed optical/electrical PHY, modulator/receiver analog bandwidth, or clocking/test chain. It is not a requirement for the panel's pixel clock unless a complete timing and lane architecture proves that need. A 50 GHz component does not guarantee a 50 GHz end-to-end data link.

## Reliability
Include link-loss detection, frame CRC, optional FEC, thermal sensors, power sequencing, panel protection, watchdogs, and a safe blanking state on invalid timing.
