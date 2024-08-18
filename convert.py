import subprocess
import os

def convert_tex_to_pdf(tex_file, output_pdf_file=None):
    # Ensure the .tex file exists
    if not os.path.isfile(tex_file):
        raise FileNotFoundError(f"{tex_file} does not exist")

    # Default output PDF filename
    if output_pdf_file is None:
        output_pdf_file = os.path.splitext(os.path.basename(tex_file))[0] + '.pdf'
    
    # Set output directory
    output_dir = os.path.dirname(tex_file)
    
    # Command to run xelatex
    command = ['xelatex', f'-output-directory={output_dir}', tex_file]
    print(f"Running command: {' '.join(command)}")
    
    # Run xelatex to convert .tex to .pdf
    try:
        result = subprocess.run(command, check=True, text=True)

        print("xelatex output:")
        print(result.stdout)  # Print the output of xelatex
        print("xelatex errors (if any):")
        print(result.stderr)  # Print the error output of xelatex
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(e.stdout)  # Print standard output
        print(e.stderr)  # Print standard error
    else:
        # Verify the output PDF file
        pdf_file_path = os.path.join(output_dir, output_pdf_file)
        if os.path.isfile(pdf_file_path):
            print(f"Successfully converted {tex_file} to PDF as {pdf_file_path}")
        else:
            print(f"PDF conversion failed or output PDF not found. Expected at: {pdf_file_path}")

if __name__ == "__main__":
    # Hardcoded directory and .tex file path
    tex_file = "/home/keaton/Desktop/TexResume/examples/resume.tex"


    convert_tex_to_pdf(tex_file)
