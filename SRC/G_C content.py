import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProfessionalBioVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bioinformatics Visualizer Pro")
        self.root.geometry("1000x700")

        self.sequence = ""
        self.sequence_name = ""

        # --- UI Layout ---
        self.toolbar = tk.Frame(self.root, pady=5)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.btn_load = tk.Button(self.toolbar, text="Load FASTA", command=self.load_fasta)
        self.btn_load.pack(side=tk.LEFT, padx=5)

        # Area for DNA Sequence (Top)
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.dna_canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.dna_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Area for GC Plot (Bottom)
        self.plot_frame = tk.Frame(self.root, height=250, bg="lightgray")
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # This is where the plot will live
        self.plot_canvas = None 

    def load_fasta(self):
        file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta"), ("Text files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                self.sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
                self.sequence_name = lines[0].strip()
            
            if not self.sequence:
                raise ValueError("No sequence found in file.")

            self.render_all()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def calculate_gc_content(self, sequence, window_size=50):
        """Calculates GC percentage using a sliding window."""
        gc_values = []
        for i in range(len(sequence) - window_size + 1):
            window = sequence[i : i + window_size].upper()
            gc_count = window.count('G') + window.count('C')
            gc_percentage = (gc_count / window_size) * 100
            gc_values.append(gc_percentage)
        return gc_values

    def render_all(self):
        # 1. Clear previous drawings
        self.dna_canvas.delete("all")
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # 2. Draw DNA (Simplified version for testing)
        self.render_dna_sequence()

        # 3. Calculate and Plot GC Content
        if self.sequence:
            gc_data = self.calculate_gc_content(self.sequence)
            self.render_gc_plot(gc_data)

    def render_dna_sequence(self):
        # Very basic visualizer for testing
        x, y = 10, 10
        for char in self.sequence[:500]: # Limiting to 500 for performance in this example
            color = "grey"
            if char == 'A': color = "red"
            elif char == 'T': color = "blue"
            elif char == 'C': color = "green"
            elif char == 'G': color = "yellow"
            
            self.dna_canvas.create_rectangle(x, y, x+15, y+15, fill=color, outline="black")
            x += 17
            if x > 800: # New line
                x = 10
                y += 20

    def render_gc_plot(self, data):
        """The crucial part: Integrating Matplotlib into Tkinter"""
        fig, ax = plt.subplots(figsize=(8, 2), dpi=100)
        ax.plot(data, color='green')
        ax.set_title("GC Content Sliding Window (%)")
        ax.set_ylabel("% GC")
        ax.grid(True, linestyle='--', alpha=0.6)

        # IMPORTANT: Convert Matplotlib figure to Tkinter Canvas
        self.plot_canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalBioVisualizer(root)
    root.mainloop()
