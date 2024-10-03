from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, 'Care Plan for F.K.K.', ln=True, align='C')

# Patient Information
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, 'Patient Name: F.K.K.', ln=True)
pdf.cell(200, 10, 'Age: 16 years', ln=True)
pdf.cell(200, 10, 'Gender: Female', ln=True)
pdf.cell(200, 10, 'Diagnosis: Convulsive disorder (5 years)', ln=True)
pdf.cell(200, 10, '', ln=True)  # Blank line

# Table headers
pdf.set_font("Arial", 'B', size=12)
headers = ['Nursing Assessment', 'Nursing Diagnosis', 'Goals/Expected Outcomes', 
           'Nursing Interventions/Plan of Care', 'Rationale']
widths = [40, 40, 40, 40, 40]
for header in headers:
    pdf.cell(widths[headers.index(header)], 10, header, border=1)
pdf.ln()

# Table content
pdf.set_font("Arial", size=12)
rows = [
    ["- Bedridden, unable to talk or walk", 
     "1. Impaired physical mobility related to inability to move independently as evidenced by the patient's bedridden state.",
     "The patient will maintain skin integrity and avoid contractures.", 
     "1. Perform passive range of motion (ROM) exercises daily.", 
     "1. ROM exercises prevent contractures and improve circulation."],
    
    ["- Convulsive episodes", 
     "2. Self-care deficit related to inability to perform activities of daily living (ADLs) as evidenced by the need for assistance with feeding and hygiene.",
     "The patient will participate in care with assistance as needed to meet hygiene and nutritional needs.", 
     "2. Assist with activities of daily living (ADLs), including feeding, grooming, and hygiene.", 
     "2. Assisting with ADLs ensures the patient’s basic needs are met, maintaining hygiene and nutrition."],
    
    ["- On carbamazepine, phenobarbitone, sodium valproate", 
     "3. Risk for aspiration related to immobility and difficulty managing secretions as evidenced by the patient's inability to swallow effectively.",
     "Aspiration risk will be minimized through proper care and positioning.", 
     "3. Position the patient in semi-Fowler’s position during and after feeding.", 
     "3. Semi-Fowler’s position reduces aspiration risk by allowing gravity to assist with swallowing."],
    
    ["- Risk for aspiration, pressure ulcers, poor nutrition, respiratory infections", 
     "4. Risk for pressure ulcers related to immobility and inadequate skin care as evidenced by prolonged periods of bed rest and skin assessment findings.",
     "No pressure ulcers will develop during the care period.", 
     "4. Turn the patient every 2 hours to prevent pressure ulcers.", 
     "4. Regular turning prevents pressure ulcers from immobility by alleviating pressure on bony prominences."],
    
    ["", 
     "", 
     "", 
     "5. Monitor and record nutritional intake.", 
     "5. Monitoring nutritional intake ensures the patient receives adequate nutrition to promote healing and overall health."],
    
    ["", 
     "", 
     "", 
     "6. Administer medications as prescribed (carbamazepine, phenobarbitone, sodium valproate) and monitor for side effects.", 
     "6. Carbamazepine, phenobarbitone, sodium valproate belong to the drug group anticonvulsants, which stabilize electrical activity in the brain and prevent seizure activity."],
    
    ["", 
     "", 
     "", 
     "7. Implement seizure precautions (e.g., padded side rails).", 
     "7. Seizure precautions help prevent injury during episodes by minimizing the risk of falls or other injuries."]
]

# Add rows to the PDF
for row in rows:
    for item in row:
        pdf.cell(widths[row.index(item)], 10, item, border=1)
    pdf.ln()

# Save the PDF to a file
pdf_output_path = "Care_Plan_FKK.pdf"
pdf.output(pdf_output_path)
print(f"PDF generated: {pdf_output_path}")
