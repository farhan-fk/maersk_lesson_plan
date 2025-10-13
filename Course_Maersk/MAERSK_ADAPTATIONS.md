# Maersk Course Adaptations Summary

This document outlines all the changes made to adapt the John Deere OpenAI course for Maersk India training.

## Overview
All code remains **unchanged** - only prompts, use cases, and examples have been modified to reflect Maersk's shipping, logistics, and supply chain operations in India.

## File-by-File Changes

### 📁 Function_Calling_OpenAi/

#### lesson_function_calling.py
- **Original**: Horoscope generation system
- **Adapted**: Shipment tracking status system
- **Changes**:
  - Function name: `get_horoscope()` → `get_shipment_status()`
  - Parameter: `sign` → `container_number`
  - Example: "MAEU1234567" container at Mumbai Port

#### lesson_structured_output.py
- **Original**: Calendar event extraction
- **Adapted**: Container booking extraction
- **Changes**:
  - Pydantic model: `CalendarEvent` → `ContainerBooking`
  - Fields: title/date/time/participants → origin_port/destination_port/departure_date/container_size
  - Example: 40ft container from Mumbai to Rotterdam

---

### 📁 open_ai_courses/

#### lesson0.py
- **No changes** - Baby name suggestion app remains universal

#### lesson1.py
**Tactic 2 - Structured Output (Commented)**:
- **Original**: Tractor models (John Deere)
- **Adapted**: Ship spare parts
- Fields: tractor_id/model/manufacturer → part_id/name/manufacturer

**Tactic 3 - Condition Checking (Commented)**:
- **Original**: Tractor parts inventory (Dealer_Ahmedabad, WH_Pune)
- **Adapted**: Ship spare parts inventory (Mumbai_Warehouse, Chennai_Depot)
- Parts examples:
  - Fuel Filter → Marine Diesel Filter (SP-ENG-001)
  - Hydraulic Hose → Hydraulic Pump (SP-DEC-002)
  - Air Filter → Radar Antenna (SP-NAV-003)
- Context: Ship engineer at Mumbai Port

**Tactic 4 - Few-shot Prompting**:
- **Original**: Tractor oil leaking, tire replacement
- **Adapted**: Container stuck at customs, shipment delayed
- Context: Mumbai customs, Chennai port operations
- Email style: Logistics operations communication

#### Lesson3.py
**Chain-of-Thought Call Analysis**:
- **Original**: John Deere tractor support call (5075E model, fuel pump)
- **Adapted**: Maersk logistics support call
- Issue: Container MAEU7894561 delayed at Nhava Sheva port
- Problem: Customs clearance documentation issue
- Impact: Production line stopped, financial losses
- Agent: Priya (Maersk Logistics)
- Context: 3-day delay, escalation to port operations manager

**Mathematical Problem (Commented)**:
- **Original**: Solar power installation costs
- **Adapted**: Container yard setup costs
- Currency: USD → INR (Indian Rupees)
- Elements:
  - Land cost: ₹5,000/sq meter
  - Infrastructure: ₹2,000/sq meter
  - Maintenance: ₹500,000/year + ₹100/sq meter

#### lesson4.py
- **No changes** - Generic iterative prompting concepts

#### chat_demo.py & chat_with_memory.py
- **No changes** - Generic chat functionality

---

### 📁 open_ai_new/

#### lesson_gpt5.py
- **Original**: "Tell me John Deere Inception story"
- **Adapted**: "Tell me Maersk company inception story"

#### lesson_audio.py
- **Original**: Generic text-to-speech
- **Adapted**: Shipment notification audio
- Content: "Your container MAEU1234567 has arrived at Mumbai Port and is ready for pickup"
- Output file: `shipment_notification.mp3`

#### lesson_image.py
- **Original**: "Green John Deere Tractor Farming on Jupiter"
- **Adapted**: "Large blue Maersk container ship docked at Mumbai Port during sunset"
- Output file: `tractor.png` → `maersk_ship.png`

#### lesson_reasoning.py
**Complete scenario transformation**:

| Aspect | John Deere Original | Maersk Adapted |
|--------|-------------------|----------------|
| **Location** | Punjab farm | JNPT Mumbai Port |
| **Task** | Harvest 40 hectares paddy | Load 250 containers |
| **Equipment** | Combine harvester (5 ha/day) | Loading crane (30 containers/hour) |
| **Challenge** | Heavy rains in 6 days | Cyclone warning in 7 hours |
| **Weather Impact** | 3 days rain duration | 12 hours storm duration |
| **Quality Loss** | 12% price reduction | Port operations suspended |
| **Base Revenue** | ₹70,000/hectare | ₹8,000 delay fee/container |
| **Total Loss** | ₹2,80,000 quality loss | ₹20,00,000 delay cost |
| **Additional Equipment** | Rented combine (₹18,000/day, 4 ha/day) | Mobile harbor crane (₹1,50,000/hour, 25 containers/hour) |
| **Currency** | Indian Rupees (₹) | Indian Rupees (₹) |
| **Decision** | Rent combine or not? | Deploy additional crane or not? |

#### lesson_tool_use.py
- **Original**: "Fetch India's population growth data"
- **Adapted**: "Fetch global container shipping volume data"
- Data sources: World Bank/UN → World Shipping Council/UNCTAD
- Chart focus: Population by year → Shipping volumes by year

#### rag_demo_fresh.py
- **Original**: Vector store name "my_policies_store", PDF "precision-ag-technology-johndeere.pdf"
- **Adapted**: Vector store name "maersk_docs_store", PDF placeholder "your_maersk_document.pdf"
- System prompt: "insurance policy assistant" → "Maersk logistics assistant"
- Instructions: Updated to use Maersk shipping documents

#### rag_demo_questions.txt
- **Completely rewritten** with 15 Maersk-specific questions covering:
  - Shipping & Logistics (transit times, documentation, container sizes)
  - Policy & Terms (liability, payment terms, detention charges)
  - Operations (tracking, bookings, port cut-offs, refrigerated transport)

#### simple_tool_demo.py
- **No changes** - Generic tool demonstration

---

## Key Maersk Context Elements Used

### Indian Operations
- **Ports**: Mumbai Port, JNPT (Jawaharlal Nehru Port), Chennai, Nhava Sheva
- **Locations**: Mumbai, Chennai, Ahmedabad
- **Logistics**: Container tracking, customs clearance, port operations

### Maersk-Specific Terms
- **Container Numbers**: MAEU prefix (e.g., MAEU1234567, MAEU7894561)
- **Equipment**: Container ships, harbor cranes, mobile cranes
- **Services**: Shipping, logistics support, customs clearance
- **Facilities**: Warehouses, depots, port terminals

### Industry Challenges Addressed
- Container delays and tracking
- Customs documentation issues
- Port operations optimization
- Weather-related scheduling (cyclones)
- Financial impact of delays (demurrage, detention)
- Supply chain disruptions
- Spare parts inventory management

### Financial Context
- All monetary values in Indian Rupees (₹)
- Realistic Indian port operation costs
- Container-based pricing models
- Delay fees and operational costs

---

## Training Recommendations

### Module 1 (open_ai_courses/)
Focus on logistics communication scenarios:
- Email writing for shipping updates
- Inventory management for spare parts
- Customer service for delayed shipments

### Module 2 (Function_Calling_OpenAi/)
Emphasize operational tools:
- Real-time shipment tracking APIs
- Booking system integration
- Structured data extraction from shipping documents

### Module 3 (open_ai_new/)
Highlight decision support:
- Port operations cost-benefit analysis
- Visual documentation (ship images, port layouts)
- RAG for shipping policy documents

---

## Setup Instructions for Trainers

1. **Environment Setup**: Same as original (Python, OpenAI API key)
2. **Customize Documents**: Replace `your_maersk_document.pdf` with actual:
   - Shipping terms and conditions
   - Bill of lading templates
   - Container specifications
   - Port operation guidelines
3. **Local Context**: Update location references for specific Maersk India offices
4. **Examples**: Add more India-specific scenarios as needed

---

## Course Completion for Maersk Participants

After completing this course, Maersk team members will be able to:
- Build AI assistants for shipment tracking and customer support
- Create structured data extraction from shipping documents
- Implement decision support systems for port operations
- Develop RAG applications using Maersk policy documents
- Generate logistics reports and visualizations
- Automate routine shipping communication

---

**Adapted By**: Farhan Khan
**Date**: October 2025
**Original Course**: John Deere OpenAI Course
**Target Audience**: Maersk India Training Participants
