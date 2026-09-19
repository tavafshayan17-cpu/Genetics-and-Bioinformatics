# Genetics-and-Bioinformatics
Python projects related to Genetics and Bioinformatics; Fields of reaserch area by Mehdi Tavaf
Bioinformatics Toolkit
A comprehensive collection of Python scripts developed for genomic data analysis, visualization, and biological modeling. This repository serves as a utility toolkit for research-level genetics tasks.

🧬 Included Tools
1. DNA Sequence Visualizer
Purpose: Provides a clear graphical interface for analyzing DNA sequences.
Key Features:
Optimized for segments up to 400 nt.
Multi-row alignment visualization for easier pattern spotting.
Highlights conserved sequences/motifs.
2. GC-Content Calculator
Purpose: Rapidly calculates the GC-percentage of a given DNA sequence.
Application: Essential for determining DNA stability and designing primers for PCR experiments.
3. Genomic Decay (Half-Life) Calculator
Purpose: Models the degradation of genomic material over time based on specific half-life parameters.
Functionality: Calculates the remaining quantity of a substance based on the elapsed time between production and the present date.
🛠 Tech Stack
Language: Python 3.x
Dependencies: Biopython, Matplotlib, NumPy.
🚀 How to Run
You can run individual modules directly from the command line:

bash
# Clone the repository
git clone https://github.com/tavafshayan17-cpu

# Run the DNA Visualizer
python visualizer.py

# Run the GC-Content Calculator
python gc_calculator.py

# Run the Half-Life Calculator
python half_life.py
📈 Project Roadmap
[ ] Implement a unified Command Line Interface (CLI) using argparse.
[ ] Add unit testing for the Half-Life calculation logic.
[ ] Export results directly to CSV/Excel for lab reports.
📬 Contact
Email: [tavafshayan17@gmail.com]
Developed with a focus on reproducibility and clean code for genetic research.

