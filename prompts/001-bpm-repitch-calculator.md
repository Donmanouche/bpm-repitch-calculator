<objective>
Create a Python script with Tkinter GUI that calculates the pitch adjustment (in semitones) needed to align a sample from a source BPM to a target BPM.
</objective>

<context>
This is a standalone application for musicians and producers who need to calculate pitch adjustments when time-stretching isn't available or desired. The application should work cross-platform (Linux, macOS, Windows) and provide a simple, intuitive interface.
</context>

<requirements>
1. Create a Python script using Tkinter for the GUI
2. Implement a simple interface with:
   - Input field for source BPM (text box)
   - Input field for target BPM (text box)
   - "Repitch" button to trigger calculation
   - Output display showing semitone adjustment
3. Calculate pitch adjustment using standard semitone formula based on BPM ratio
4. Handle edge cases (invalid input, zero BPM, etc.)
5. Make the script executable as standalone on Linux, macOS, and Windows
</requirements>

<implementation>
- Use Tkinter for cross-platform GUI compatibility
- Implement the semitone calculation formula: semitones = 12 * log2(target_bpm/source_bpm)
- Add input validation to ensure positive numeric values
- Display the result with appropriate precision (2 decimal places)
- Include error handling for invalid inputs
- Make the script executable with proper shebang and file permissions
</implementation>

<output>
Create the following file:
- `./bpm_repitch_calculator.py` - Main Python script with Tkinter GUI and calculation logic
</output>

<verification>
Before declaring complete, verify your work:
1. Test the script runs without errors
2. Verify calculation accuracy with known values (e.g., 120→240 BPM should be +12 semitones)
3. Confirm GUI elements are present and functional
4. Test on multiple platforms if possible
</verification>

<success_criteria>
- Script runs successfully on Linux, macOS, and Windows
- GUI contains all required elements (source BPM, target BPM, Repitch button, output)
- Calculation produces correct semitone values
- Input validation prevents crashes on invalid data
- Script is properly executable as standalone application
</success_criteria>