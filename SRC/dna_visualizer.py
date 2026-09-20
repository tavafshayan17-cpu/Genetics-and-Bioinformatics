import tkinter as tk
from tkinter import ttk

class DNAVisualizerApp:
    def __init__(self, root, sequences):
        self.root = root
        self.root.title("Professional DNA Alignment Viewer (High Capacity)")
        self.sequences = sequences
        self.seq_length = len(sequences[0])
        
        #outlook settings
        self.cell_size = 15  # size of each nucleotide
        self.row_height = 30
        self.margin_left = 80
        
        # creating main container and scrollbar
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", 
                                 width=self.seq_length * self.cell_size + 100,
                                 height=len(sequences) * self.row_height + 100)
        
        # creating horizental and vertical scrollbar
        self.hbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.vbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # scrollbars arrangement
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.color_map = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'yellow'}
        
        self.render()

    def render(self):
        # drawing sequences
        for row_idx, seq in enumerate(self.sequences):
            current_y = 50 + (row_idx * self.row_height)
            
            # draing row name
            self.canvas.create_text(10, current_y, text=f"S{row_idx+1}", 
                                   anchor="e", font=("Arial", 10, "bold"))

            for col_idx, base in enumerate(seq):
                x_pos = self.margin_left + (col_idx * self.cell_size)
                
                # (Comparison)
                is_conserved = False
                if row_idx == 0:
                    is_conserved = True
                else:
                    if seq[col_idx] == self.sequences[row_idx-1][col_idx]:
                        is_conserved = True
                
                if is_conserved:
                    # drawing colored rectangle instead of pencile (much more faster and precicer)
                    color = self.color_map.get(base.upper(), "grey")
                    self.canvas.create_rectangle(
                        x_pos, current_y - 10, 
                        x_pos + self.cell_size - 1, current_y + 10, 
                        fill=color, outline=""
                    )
                
                # adding nucleotide numbers in the first row
                if row_idx == 0 and col_idx % 10 == 0:
                    self.canvas.create_text(x_pos, 20, text=str(col_idx+1), font=("Arial", 8))

        # activating scroll ability
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    # 1- creating huge data (5000 nucleotide)
    import random
    print("Generating 5000 nucleotides... please wait.")
    length = 5000
    bases = ['A', 'T', 'G', 'C']
    
    seq1 = "".join(random.choices(bases, k=length))
    seq2 = "".join(random.choices(bases, k=length))
    seq3 = "".join(random.choices(bases, k=length))
    
    test_sequences = [seq1, seq2, seq3]

    # 2- running application
    root = tk.Tk()
    app = DNAVisualizerApp(root, test_sequences)
    root.mainloop()
