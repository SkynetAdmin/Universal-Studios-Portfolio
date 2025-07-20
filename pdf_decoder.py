#!/usr/bin/env python3
"""
PDF Certificate Decoder
Extracts text content from PDF certificates to identify correct titles
For workspace use only - not for deployment
"""

import os
import re
import sys
from pathlib import Path

def extract_pdf_text_simple(pdf_path):
    """Simple PDF text extraction using basic parsing"""
    try:
        with open(pdf_path, 'rb') as file:
            content = file.read()
            
        # Convert to string, ignoring errors
        text_content = content.decode('latin-1', errors='ignore')
        
        # Extract text between parentheses (common PDF text encoding)
        text_matches = re.findall(r'\(([^)]*)\)', text_content)
        
        # Extract text between brackets
        bracket_matches = re.findall(r'\[([^\]]*)\]', text_content)
        
        # Extract potential text strings
        string_matches = re.findall(r'[A-Za-z][A-Za-z\s]{5,50}', text_content)
        
        all_text = text_matches + bracket_matches + string_matches
        
        # Filter and clean text
        meaningful_text = []
        for text in all_text:
            cleaned = text.strip()
            if len(cleaned) > 3 and not cleaned.startswith('%') and 'obj' not in cleaned.lower():
                meaningful_text.append(cleaned)
        
        return meaningful_text
        
    except Exception as e:
        return [f"Error reading {pdf_path}: {str(e)}"]

def analyze_certificates():
    """Analyze all certificate PDFs in the certificates folder"""
    cert_folder = Path("certificates")
    
    if not cert_folder.exists():
        print("Certificates folder not found!")
        return
    
    pdf_files = list(cert_folder.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in certificates folder!")
        return
    
    print("=== CERTIFICATE ANALYSIS ===\n")
    
    for pdf_file in pdf_files:
        print(f"📄 FILE: {pdf_file.name}")
        print("-" * 50)
        
        text_content = extract_pdf_text_simple(pdf_file)
        
        # Look for certificate-related keywords
        certificate_info = []
        for text in text_content:
            if any(keyword in text.lower() for keyword in 
                   ['certificate', 'completion', 'google', 'coursera', 'cornell', 
                    'business', 'management', 'support', 'automation', 'python',
                    'technical', 'fundamentals', 'operating', 'systems']):
                certificate_info.append(text)
        
        if certificate_info:
            print("POTENTIAL CERTIFICATE TITLES:")
            for i, info in enumerate(certificate_info[:10], 1):  # Limit to first 10 matches
                print(f"  {i}. {info}")
        else:
            print("NO CLEAR CERTIFICATE TITLES FOUND")
            print("RAW TEXT SAMPLE:")
            for i, text in enumerate(text_content[:20], 1):  # Show first 20 text strings
                print(f"  {i}. {text}")
        
        print("\n" + "="*60 + "\n")

def main():
    """Main function"""
    print("PDF Certificate Decoder - Workspace Tool")
    print("Analyzing certificate files...\n")
    
    analyze_certificates()
    
    print("\nDECODER COMPLETE")
    print("Use this information to update certificate titles in your portfolio documents")

if __name__ == "__main__":
    main()
