import PyPDF2
import os

def merge_pdfs(pdf_list, output_filename):
    """Merge multiple PDFs into one"""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as {output_filename}")

def split_pdf(input_pdf, output_folder):
    """Split a single PDF into individual pages"""
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        for i in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            
            output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")
            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"Saved: {output_filename}")

# Example usage
if __name__ == "__main__":
    # Merging PDFs
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Replace with actual file paths
    merge_pdfs(pdf_files, "merged_output.pdf")
    
    # Splitting a PDF
    split_pdf("merged_output.pdf", "output_pages")  # Ensure 'output_pages' directory exists
