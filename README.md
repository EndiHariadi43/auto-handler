# System Telemetry Daemon

This repository contains experimental telemetry agents simulating randomized workload responses in isolated job contexts.

Each agent is executed under pseudo-randomized scheduling, using synthetic metrics generated via CPU- and I/O-bound evaluations to analyze container performance profiles.

All telemetry outputs are encrypted and transmitted externally for downstream validation.

## Modules

- `data-collector.yml`: Simulates float-intensive system tasks under controlled duration.
- `bnb-collector.yml`: Simulates I/O-heavy sessions for trace analysis.

## node-core

Contains runtime agent core executables for workload simulation.  
Do not modify this directory manually.

---

> This environment is part of a closed evaluation experiment. Use with discretion.
