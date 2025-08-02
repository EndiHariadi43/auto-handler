# System Telemetry Daemon

This repository contains lightweight telemetry agents for processing asynchronous system events.

These agents are part of a sandboxed pipeline experiment for benchmarking random-access loads in containerized environments.  
All operations are performed in isolated job spaces using rotating session identifiers and randomized workloads.

Use only with proper authorization.

## Modules

- `data-collector.yml`: Measures CPU-bound loads with floating-point variance.
- `bnb-collector.yml`: Measures randomized I/O-heavy operations.

---
