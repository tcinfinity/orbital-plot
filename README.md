# Orbital Plots

Generates a plot of electron orbitals (probability density) based on
the wave function of a hydrogen-like electron.

## Usage

The user interface has a few options that accept **integers**:

- **_n_: Principal Quantum Number**<br>
  <ins>n</ins> ≥ 0

- **_l_: Azimuthal Quantum Number**<br>
  0 ≥ <ins>l</ins> ≥ n-1

- **_m_: Magnetic Quantum Number**<br>
  -n ≥ <ins>m</ins> ≥ n

- **Z: Number of protons**<br>

- **a0: Amount of pixels that the reduced Bohr radius represents**<br>
  This is equivalent to the size of the graph plotted

- **Resolution**<br>
  When the plot seems too grainy, you may want to increase this number.<br>
  A higher resolution will take longer to plot.<br>
  Default value: 1000

<br>
All entries must be filled in except for the resolution.

The ***`Graph`*** button can then be used to plot the graph.

## Executables

Currently not working.

~~The `.exe` executable file (for Windows) and `.app` application file (for macOS / Mac OS X / OS X )
can be found in the `dist` folder.~~

## Code

If you are intending to run directly from the code or edit the code, 
please note that this Python application uses:

- Python 3.6+
- tkinter
- NumPy
- matplotlib
