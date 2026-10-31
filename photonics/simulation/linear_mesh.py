"""Toy coherent-interferometer mesh model for PHOTON-X Rev 0.1.

This is a numerical teaching/prototyping model, not a device-level optical
solver. It models a unitary mesh with configurable phase perturbations and
per-stage amplitude loss. It does not model a foundry PDK, wavelength-dependent
components, polarization, thermal crosstalk, or a measured detector chain.
"""
from __future__ import annotations

import argparse
import json
import numpy as np


def unitary_mesh(n: int, rng: np.random.Generator, phase_sigma_rad: float = 0.0,
                 amplitude_loss_db_per_stage: float = 0.0) -> np.ndarray:
    """Build a simple product of adjacent 2x2 complex unitary couplers."""
    if n < 2:
        raise ValueError("n must be >= 2")
    if phase_sigma_rad < 0 or amplitude_loss_db_per_stage < 0:
        raise ValueError("noise and loss parameters must be non-negative")

    result = np.eye(n, dtype=np.complex128)
    stages = []
    for offset in (0, 1):
        stage = np.eye(n, dtype=np.complex128)
        for i in range(offset, n - 1, 2):
            phi = rng.normal(0.0, phase_sigma_rad)
            theta = np.pi / 4 + phi
            c, s = np.cos(theta), np.sin(theta)
            phase = rng.uniform(-np.pi, np.pi)
            block = np.array([[c, -np.exp(1j * phase) * s],
                              [np.exp(-1j * phase) * s, c]], dtype=np.complex128)
            stage[i:i + 2, i:i + 2] = block
        stages.append(stage)

    for stage in stages:
        result = stage @ result
    amplitude = 10 ** (-amplitude_loss_db_per_stage / 20.0)
    return amplitude * result


def run_demo(n: int = 4, seed: int = 7, phase_sigma_mrad: float = 0.0,
             loss_db_per_stage: float = 0.0) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=n) + 1j * rng.normal(size=n)
    ideal = unitary_mesh(n, np.random.default_rng(seed), 0.0, 0.0)
    actual = unitary_mesh(n, np.random.default_rng(seed), phase_sigma_mrad / 1000.0,
                          loss_db_per_stage)
    y_ref = ideal @ x
    y_meas = actual @ x
    denom = np.linalg.norm(y_ref)
    rel_error = float(np.linalg.norm(y_meas - y_ref) / denom) if denom else 0.0
    return {
        "matrix_dimension": n,
        "seed": seed,
        "phase_sigma_mrad": phase_sigma_mrad,
        "amplitude_loss_db_per_stage": loss_db_per_stage,
        "relative_l2_error": rel_error,
        "reference_output": [[float(v.real), float(v.imag)] for v in y_ref],
        "simulated_output": [[float(v.real), float(v.imag)] for v in y_meas],
        "model_status": "illustrative abstraction; not a validated PIC model",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=4)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--phase-noise-mrad", type=float, default=5.0)
    parser.add_argument("--loss-db-per-stage", type=float, default=0.1)
    args = parser.parse_args()
    print(json.dumps(run_demo(args.size, args.seed, args.phase_noise_mrad,
                              args.loss_db_per_stage), indent=2))


if __name__ == "__main__":
    main()
