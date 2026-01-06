#!/bin/bash
# Merge all individual PDF files into a single PDF

PDF_DIR="output/pdfs"
OUTPUT_FILE="GuanYu_Fortune_Sticks_Complete.pdf"

echo "Merging all PDF files..."
echo "Input directory: $PDF_DIR"
echo "Output file: $OUTPUT_FILE"
echo ""

# Check if PDFs exist
pdf_count=$(ls ${PDF_DIR}/stick_*.pdf 2>/dev/null | wc -l | tr -d ' ')
if [ "$pdf_count" -eq 0 ]; then
    echo "ERROR: No PDF files found in $PDF_DIR"
    exit 1
fi

echo "Found $pdf_count PDF files to merge"
echo ""

# Create sorted list of PDF files
pdf_files=$(ls ${PDF_DIR}/stick_*.pdf | sort -V)

# Merge using Ghostscript
echo "Merging PDFs with Ghostscript..."
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite \
   -sOutputFile="$OUTPUT_FILE" \
   $pdf_files

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Merge successful!"
    echo ""
    echo "Output file: $OUTPUT_FILE"

    # Show file size
    file_size=$(ls -lh "$OUTPUT_FILE" | awk '{print $5}')
    echo "File size: $file_size"

    # Show size in bytes for exact check
    bytes=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE")
    mb=$(echo "scale=2; $bytes / 1048576" | bc)
    echo "Exact size: ${mb}MB"

    # Check if under 20MB
    if [ "$bytes" -lt 20971520 ]; then
        echo "✅ Size is under 20MB target"
    else
        echo "⚠️  Warning: File is larger than 20MB target"
    fi

    # Show page count
    page_count=$(gs -q -dNODISPLAY -c "($OUTPUT_FILE) (r) file runpdfbegin pdfpagecount = quit" 2>/dev/null)
    if [ -n "$page_count" ]; then
        echo "Total pages: $page_count"
    fi
else
    echo "❌ ERROR: Merge failed"
    exit 1
fi
