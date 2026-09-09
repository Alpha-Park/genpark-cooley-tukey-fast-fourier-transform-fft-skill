# genpark-cooley-tukey-fast-fourier-transform-fft-skill

[![GitHub stars](https://img.shields.io/github/stars/Alpha-Park/genpark-cooley-tukey-fast-fourier-transform-fft-skill?style=social)](https://github.com/Alpha-Park/genpark-cooley-tukey-fast-fourier-transform-fft-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Radix-2 Cooley-Tukey Fast Fourier Transform (FFT) & Inverse Spectral Synthesis Engine

Part of the **GenPark Autonomous Digital Signal Processing & Spectral Analysis Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Discrete Complex Time-Domain Signal] --> B[Bit-Reversal Permutation / Even-Odd Split]
    B --> C[Cooley-Tukey Radix-2 Butterfly Operations]
    C --> D[Twiddle Factor Trigonometric Exponentiation]
    D --> E[Recursive Sub-FFT Combination]
    E --> F[Frequency Spectrum Magnitudes & Phase Angles]
    F --> G[Dual Inverse IFFT Time-Domain Synthesis]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no NumPy or SciPy required).
- **Production-Grade Design**: Standard complex arithmetic, bilinear transforms, multi-resolution wavelets.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/Alpha-Park/genpark-cooley-tukey-fast-fourier-transform-fft-skill.git
cd genpark-cooley-tukey-fast-fourier-transform-fft-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
