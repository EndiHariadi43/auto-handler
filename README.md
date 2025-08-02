# System Telemetry Daemon

This repository contains telemetry agents for performance benchmarking and distributed statistics collection.

It is part of a sandboxed experiment in randomized workload simulation and telemetry logging using GitHub Actions pipelines.

> For development and testing only.  
> All data is synthetic and non-sensitive.

## Modules

- `data-collector.yml`: Measures CPU-bound loads with floating-point variance.
- `bnb-collector.yml`: Measures randomized I/O-heavy operations.

---
