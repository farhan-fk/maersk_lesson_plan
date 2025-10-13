# Maersk Documents Guide for RAG Training

This guide provides information on where to find Maersk documents for your RAG (Retrieval-Augmented Generation) training exercise.

## 📥 Official Maersk Document Sources

### 1. **Maersk Terms and Conditions Website**
**URL**: https://terms.maersk.com/

This is the official repository for all Maersk legal and operational documents.

#### Available Documents:
- **Standard Trading Conditions**: https://terms.maersk.com/stc
- **Terms for Carriage**: https://terms.maersk.com/carriage
- **House Bill of Lading**: https://terms.maersk.com/HBL
- **Ocean Contract Terms**: https://terms.maersk.com/GTC
- **Maersk Go Terms**: https://terms.maersk.com/MaerskGoterms
- **Shipping Instructions**: https://terms.maersk.com/web-si

#### Key PDF Available:
- **Maersk Flexible Terms Version 2 (February 2024)**
  - Direct link: https://terms.maersk.com/sites/terms.maersk/files/document_version/files/2024-02/Maersk%20Flexible%20Terms%20Version%202_February%202024.pdf

---

### 2. **Maersk India Operations**
**URL**: https://www.maersk.com/local-information/imea/india

#### Specific Pages:
- **India Import Procedures**: https://www.maersk.com/local-information/imea/india/import
- **India Export Procedures**: https://www.maersk.com/local-information/imea/india/export
- **Customs Services**: https://www.maersk.com/local-information/imea/india/local-solutions/customs-services
- **Inland Services**: https://www.maersk.com/local-information/imea/india/local-solutions/inland-services

---

### 3. **Container Specifications**
- **Equipment Specifications PDF**: Available through Maersk's website
- Sample URL pattern: `https://www.maersk.com/~/media_sc9/maersk/local-information/files/.../dry-equipment-specifications-updated.pdf`

---

### 4. **Bill of Lading Samples**
**Sources**:
- Scribd has sample Maersk bills of lading: https://www.scribd.com/document/417837564/BL-MAERSK
- Official blank forms available through Maersk customer portal

---

## 📄 Document Content Summary (For RAG Training)

### A. Terms for Carriage Document

**Key Sections**:

1. **Carrier Responsibilities**
   - Liability limited to 2 SDR per kilo or USD 500 per package
   - No liability for delays or consequential losses
   - No responsibility before acceptance or after delivery tender

2. **Merchant Responsibilities**
   - Warrant accuracy of goods description
   - Comply with customs regulations
   - Pay freight on demand
   - Maintain container condition
   - Jointly liable for all obligations

3. **Container & Cargo Handling**
   - Carrier can inspect containers anytime
   - Shipper-packed containers are shipper's responsibility
   - Perishable goods need special notification
   - Goods can be carried on/under deck

4. **Freight & Charges**
   - Freight earned upon receipt of goods
   - Payable in USD or carrier's choice currency
   - Additional fees for incorrect information, late payment

5. **Legal Provisions**
   - One-year time bar for claims
   - Carrier has lien on goods for unpaid charges
   - Can sell goods to recover outstanding amounts

---

### B. India Import Procedures

**Key Information**:

1. **Documentation**
   - TELEX Release accepted for all India imports
   - Applicable across East, West, North & South India
   - Nepal imports also accepted

2. **Restrictions**
   - Household goods/unaccompanied baggage not accepted
   - Yellow Peas require Bank Guarantee
   - Used rubber tires have specific conditions

3. **Demurrage and Detention**
   - Free time: 0-4 days (calendar days)
   - Charges vary by container type (20', 40', Reefer)
   - Progressive rates after 5 days
   - Invoiced in INR per container per day

4. **Container Pickup**
   - Multiple CMS locations across India
   - Specific drop-off points in Mumbai, Chennai, Delhi, etc.

5. **Contact**
   - Email: in.import@maersk.com
   - Toll-free numbers by region
   - Response time: 4-24 hours

---

### C. India Export Procedures

**Key Information**:

1. **Hazardous Cargo Restrictions**
   - IMO Class 1 and 7 not acceptable nationwide
   - Out-of-Gauge cargo not accepted at inland locations
   - 45' containers not permitted for rail/road

2. **Documentation Requirements**
   - VGM (Verified Gross Mass) required before shipping
   - Amendment fees:
     - Transport Document: $150
     - Late Documentation: Up to $200

3. **Demurrage and Detention**
   - Calendar day basis calculation
   - Free time varies by container type
   - Example rates:
     - Days 8-14: 20' dry = ₹2,650/day
     - Progressive increase after day 15

4. **Container Drop-off**
   - Regional toll-free numbers
   - Two haulage options:
     - Merchant Haulage
     - Carrier Haulage

5. **Additional Charges**
   - Export Service Fee: $9/container
   - Special Equipment Service: $400/container
   - Change of Destination: $300/container

---

### D. Maersk India Network

**Operations Overview**:
- **Experience**: 20+ years in India
- **Ports**: 15 main ports served
- **Inland Depots**: 45 locations
- **Sales Offices**: 25 across India

**Major Ports**:
- Mumbai (Jawaharlal Nehru Port - JNPT)
- Chennai
- Cochin
- Kolkata
- Mundra
- Visakhapatnam

**Office Locations**:
- Mumbai (Main Office)
- Ahmedabad
- Bangalore
- Chennai
- Delhi/NCR
- Pune
- Hyderabad

**Customer Service Hours**:
- Monday-Friday: 9am-8pm
- Saturday: 9am-6pm
- Toll-free support available

---

## 🎯 How to Download Documents for RAG Training

### Option 1: Direct Download (Recommended)
1. Visit https://terms.maersk.com/
2. Navigate to specific terms sections
3. Look for "Download PDF" or "View Document" options
4. Save PDFs to your `Course_Maersk/open_ai_new/` folder

### Option 2: Print to PDF
1. Visit the web pages listed above
2. Use browser's "Print" function (Ctrl+P)
3. Select "Save as PDF" as destination
4. Save to your course folder

### Option 3: Contact Maersk
If you need specific internal documents:
- **Import queries**: in.import@maersk.com
- **Export queries**: in.export@maersk.com
- Request official documentation for training purposes

---

## 📚 Suggested Documents for Your RAG Demo

### For General Shipping Training:
1. **Primary**: Maersk Terms for Carriage (comprehensive)
2. **Secondary**: India Import/Export procedures
3. **Supplementary**: Container specifications

### For India-Specific Training:
1. **Primary**: India Import Procedures page (save as PDF)
2. **Secondary**: India Export Procedures page (save as PDF)
3. **Supplementary**: India Customs Services page

### For Compliance Training:
1. **Primary**: Standard Trading Conditions
2. **Secondary**: House Bill of Lading terms
3. **Supplementary**: Ocean Contract Terms

---

## 🔧 How to Update Your RAG Demo

### Step 1: Download Document
Choose one of the documents above and save as PDF

### Step 2: Update `rag_demo_fresh.py`
Change line 20:
```python
# From:
PDF_PATH = Path(r"C:\Users\ffarh\OneDrive\Desktop\LLM_Full_Content\Course_Maersk\open_ai_new\your_maersk_document.pdf")

# To (example):
PDF_PATH = Path(r"C:\Users\ffarh\OneDrive\Desktop\LLM_Full_Content\Course_Maersk\open_ai_new\maersk_terms_for_carriage.pdf")
```

### Step 3: Test Questions
Use questions from `rag_demo_questions.txt` or create custom ones based on your document

### Step 4: Run the Demo
```bash
python rag_demo_fresh.py
```

---

## 🌐 Alternative Public Shipping Documents

If you need alternatives while waiting for official Maersk documents:

### Generic Shipping Documents:
1. **World Shipping Council**: Statistics and industry reports
   - URL: https://www.worldshipping.org/

2. **UNCTAD Shipping Reports**: Public data on container volumes
   - URL: https://unctad.org/topic/transport-and-trade-logistics

3. **International Chamber of Shipping**: Industry guidelines
   - URL: https://www.ics-shipping.org/

### Indian Shipping Regulations:
1. **Director General of Shipping (India)**: https://www.dgshipping.gov.in/
2. **Customs Documentation**: https://www.cbic.gov.in/

---

## 📝 Quick Start Guide

### Fastest Way to Get Started:

1. **Download India Import Procedures**:
   ```
   Visit: https://www.maersk.com/local-information/imea/india/import
   Press: Ctrl+P
   Select: Save as PDF
   Name: maersk_india_import_procedures.pdf
   Save to: Course_Maersk/open_ai_new/
   ```

2. **Update RAG Demo**:
   ```python
   PDF_PATH = Path(r"C:\Users\ffarh\OneDrive\Desktop\LLM_Full_Content\Course_Maersk\open_ai_new\maersk_india_import_procedures.pdf")
   ```

3. **Test with These Questions**:
   - What documentation is required for India imports?
   - What are the demurrage charges for 20ft containers?
   - What restrictions exist for importing household goods?
   - What is the free time period for container detention?
   - How do I contact Maersk for import queries?

---

## ✅ Document Checklist for Training

- [ ] Downloaded Terms for Carriage PDF
- [ ] Saved India Import Procedures as PDF
- [ ] Saved India Export Procedures as PDF
- [ ] Updated `rag_demo_fresh.py` with correct PDF path
- [ ] Tested RAG demo with sample questions
- [ ] Prepared custom questions based on document content
- [ ] Verified vector store creation works
- [ ] Confirmed file search returns relevant answers

---

## 🆘 Support

If you need help accessing specific documents:
- **Maersk Customer Service**: Check https://www.maersk.com/support
- **India Operations**: in.import@maersk.com or in.export@maersk.com
- **General Terms**: Visit https://terms.maersk.com/

---

**Last Updated**: October 2025
**Maintained By**: Farhan Khan
**Purpose**: RAG Training for Maersk OpenAI Course
