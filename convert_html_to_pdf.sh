#!/bin/bash
# Convert all HTML files to PDF using Chrome headless mode

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INPUT_DIR="output"
OUTPUT_DIR="output/pdfs"

# Create PDF output directory
mkdir -p "$OUTPUT_DIR"

# Counter for progress
total_files=$(ls ${INPUT_DIR}/stick_*.html 2>/dev/null | wc -l | tr -d ' ')
current=0

echo "Converting $total_files HTML files to PDF..."
echo "Using: Chrome headless mode"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Convert each HTML file to PDF
for html_file in ${INPUT_DIR}/stick_*.html; do
    if [ -f "$html_file" ]; then
        # Extract stick number from filename
        filename=$(basename "$html_file" .html)
        pdf_file="${OUTPUT_DIR}/${filename}.pdf"

        # Get absolute path for input file
        abs_html_path="$(cd "$(dirname "$html_file")" && pwd)/$(basename "$html_file")"

        # Convert using Chrome headless with print to PDF
        "$CHROME" \
            --headless \
            --disable-gpu \
            --print-to-pdf="$pdf_file" \
            --print-to-pdf-no-header \
            --no-margins \
            "file://${abs_html_path}" \
            2>/dev/null

        if [ $? -eq 0 ]; then
            current=$((current + 1))
            printf "\r[%3d/%3d] Converted: %s" "$current" "$total_files" "$filename"
        else
            echo ""
            echo "ERROR: Failed to convert $filename"
        fi
    fi
done

echo ""
echo ""
echo "Conversion complete!"
echo "Generated $current PDF files in: $OUTPUT_DIR"

# Show total size
total_size=$(du -sh "$OUTPUT_DIR" | cut -f1)
echo "Total size: $total_size"

# Count and list files
pdf_count=$(ls ${OUTPUT_DIR}/stick_*.pdf 2>/dev/null | wc -l | tr -d ' ')
echo "PDF files created: $pdf_count"

# Show first and last files
echo ""
echo "First 5 PDFs:"
ls ${OUTPUT_DIR}/stick_*.pdf | head -5 | xargs -I {} basename {}

echo ""
echo "Last 5 PDFs:"
ls ${OUTPUT_DIR}/stick_*.pdf | tail -5 | xargs -I {} basename {}
