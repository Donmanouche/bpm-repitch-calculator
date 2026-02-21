#!/usr/bin/env python3
"""
BPM Repitch Calculator
A simple Tkinter application to calculate the pitch adjustment needed
to align a sample from a source BPM to a target BPM.
"""

import tkinter as tk
from tkinter import messagebox
import math
import sys

class BPMRepitchCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BPM Repitch Calculator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Create and place widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Source BPM
        tk.Label(self.root, text="Source BPM:").pack(pady=(20, 5))
        self.source_bpm_entry = tk.Entry(self.root, width=20)
        self.source_bpm_entry.pack(pady=5)
        
        # Target BPM
        tk.Label(self.root, text="Target BPM:").pack(pady=(10, 5))
        self.target_bpm_entry = tk.Entry(self.root, width=20)
        self.target_bpm_entry.pack(pady=5)
        
        # Repitch button
        self.repitch_button = tk.Button(
            self.root, 
            text="Repitch", 
            command=self.calculate_repitch,
            width=15, 
            height=2
        )
        self.repitch_button.pack(pady=20)
        
        # Result display
        tk.Label(self.root, text="Semitone Adjustment:").pack(pady=(10, 5))
        self.result_label = tk.Label(self.root, text="", font=('Arial', 14, 'bold'))
        self.result_label.pack(pady=5)
        
        # Info label
        self.info_label = tk.Label(
            self.root, 
            text="Enter source and target BPM values",
            fg="gray"
        )
        self.info_label.pack(pady=10)
    
    def calculate_repitch(self):
        """Calculate the semitone adjustment needed for BPM change"""
        try:
            # Get input values
            source_bpm = float(self.source_bpm_entry.get())
            target_bpm = float(self.target_bpm_entry.get())
            
            # Validate inputs
            if source_bpm <= 0 or target_bpm <= 0:
                messagebox.showerror("Error", "BPM values must be positive numbers")
                return
            
            # Calculate semitone adjustment
            # Formula: semitones = 12 * log2(target_bpm/source_bpm)
            ratio = target_bpm / source_bpm
            semitones = 12 * math.log2(ratio)
            
            # Display result with 2 decimal places
            self.result_label.config(text=f"{semitones:.2f} semitones")
            self.info_label.config(text=f"Adjust pitch by {semitones:.2f} semitones")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric BPM values")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = BPMRepitchCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    # Make sure we're running with proper Python version
    if sys.version_info < (3, 6):
        print("Error: This script requires Python 3.6 or higher")
        sys.exit(1)
    
    main()