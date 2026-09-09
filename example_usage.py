"""Example usage for Fast Fourier Transform Skill."""
from client import FastFourierTransform

def main():
    print("Executing Fast Fourier Transform (FFT)...")
    sig = [1.0, 2.0, 3.0, 4.0]
    spec = FastFourierTransform.analyze_spectrum(sig)
    print("Spectrum Analysis:", spec)
    assert len(spec["magnitudes"]) == 3
    print("Fast Fourier Transform verified successfully!")

if __name__ == "__main__":
    main()
