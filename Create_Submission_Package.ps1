# Universal Horror Unleashed Application Package Creator
# Run this script to create submission package

Write-Host "🎃 Creating Universal Horror Unleashed Application Package..." -ForegroundColor Green

# Create submission directory
$SubmissionDir = "UHU_Application_Package"
if (Test-Path $SubmissionDir) {
    Remove-Item $SubmissionDir -Recurse -Force
}
New-Item -ItemType Directory -Path $SubmissionDir

Write-Host "📁 Packaging website files..." -ForegroundColor Yellow

# Copy website folder
Copy-Item "website" -Destination "$SubmissionDir\Interactive_Website" -Recurse

# Create simple instructions file
$Instructions = @"
UNIVERSAL HORROR UNLEASHED - INTERACTIVE PORTFOLIO
==================================================

TO VIEW HANNIBAL HERRERA'S INTERACTIVE PORTFOLIO:

1. Open the "index.html" file in any web browser
2. Explore the interactive automation demonstration
3. Try the different control buttons:
   - Emergency Stop (Red) - Safety protocols
   - Scene Transition (Yellow) - Precision timing
   - Horror Unleashed (Green) - Full automation
   - Auto Sequence - Professional operations cycle
   - Horror Mode - Personal Halloween connection!

This demonstrates the technical precision and automation 
control skills perfect for UHU's special effects systems.

Contact: herrera.hannibal84@gmail.com | 702-626-7678
Location: Las Vegas, NV (5.5 miles from Area 15)
Availability: Immediate

Ready to bring military precision and authentic horror 
passion to Universal Horror Unleashed!
"@

$Instructions | Out-File "$SubmissionDir\Interactive_Website\README.txt" -Encoding UTF8

Write-Host "📄 Package created in: $SubmissionDir" -ForegroundColor Green
Write-Host "🎯 Next steps:" -ForegroundColor Cyan
Write-Host "   1. Generate PDFs using markdown-to-pdf-converter.html" -ForegroundColor White
Write-Host "   2. Add PDF files to $SubmissionDir folder" -ForegroundColor White
Write-Host "   3. ZIP the entire $SubmissionDir folder" -ForegroundColor White
Write-Host "   4. Email to Universal Horror Unleashed!" -ForegroundColor White
Write-Host ""
Write-Host "🚀 Ready to unleash horror at Universal! 🎃" -ForegroundColor Green
