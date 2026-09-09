"""
Autonomous Agent Radix-2 Cooley-Tukey Fast Fourier Transform Skill
Pure Python Standard Library implementation.
"""
import cmath
from typing import List, Dict, Any, Tuple

class FastFourierTransform:
    """
    Cooley-Tukey Radix-2 Decimation-in-Time FFT & IFFT.
    """
    @staticmethod
    def fft(x: List[complex]) -> List[complex]:
        n = len(x)
        if n <= 1:
            return list(x)
        even = FastFourierTransform.fft(x[0::2])
        odd = FastFourierTransform.fft(x[1::2])
        t = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
        return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]

    @staticmethod
    def ifft(x: List[complex]) -> List[complex]:
        n = len(x)
        conj = [val.conjugate() for val in x]
        transformed = FastFourierTransform.fft(conj)
        return [val.conjugate() / n for val in transformed]

    @staticmethod
    def analyze_spectrum(real_signal: List[float]) -> Dict[str, Any]:
        # Pad to power of 2
        n = len(real_signal)
        power_of_two = 1
        while power_of_two < n:
            power_of_two <<= 1
        padded = [complex(v, 0.0) for v in real_signal] + [0j] * (power_of_two - n)

        freq_bins = FastFourierTransform.fft(padded)
        magnitudes = [round(abs(f), 4) for f in freq_bins[:power_of_two // 2 + 1]]
        phases = [round(cmath.phase(f), 4) for f in freq_bins[:power_of_two // 2 + 1]]

        return {
            "magnitudes": magnitudes,
            "phases": phases,
            "fft_size": power_of_two
        }
