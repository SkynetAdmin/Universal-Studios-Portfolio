# HANNIBAL HERRERA
## Technology Operations Manager - Universal Horror Unleashed

**📧 herrera.hannibal84@gmail.com | 📱 702-626-7678 | 📍 Las Vegas, NV**

---

## 🎯 EXECUTIVE SUMMARY

14-year military veteran with extensive crisis management experience, Docker expertise, and automation programming skills. Ready to bring operational excellence and authentic horror passion to Universal Horror Unleashed's 24/7/365 technology operations at Area 15.

**Key Differentiators:**
- ✅ Military-grade crisis management (Iraq deployment experience)
- ✅ Docker containerization and automation expert
- ✅ Las Vegas resident (5.5 miles from Area 15)
- ✅ Authentic horror enthusiast (married on Halloween, traveled to Derry, Ireland)
- ✅ Multilingual: English, Spanish, ASL Level 2

---

## 🎖️ MILITARY EXPERIENCE

### **Downed Aircraft Recovery Team Leader | U.S. Military**
**Iraq Deployment | 14 Years Total Service**

**Mission-Critical Responsibilities:**
- Led emergency response teams in combat zones with 100% mission success rate
- Managed complex technical equipment under extreme pressure
- Coordinated multi-team operations across different time zones
- Trained hundreds of personnel in crisis management protocols
- Maintained 24/7/365 operational readiness with zero tolerance for failure

**Universal Applications:**
- Emergency response protocols for attraction malfunctions
- Team leadership during high-stress operational incidents
- Training staff on safety and emergency procedures
- Managing complex technology systems under pressure

---

## 🤖 TECHNICAL AUTOMATION DEMOS

### **G-Code Programming for Special Effects**

**Animatronic Controller Example:**
```gcode
; Universal Horror Witch Animatronic Controller
; Hardware: Arduino Mega 2560 + RAMPS 1.4

M117 "Initializing Horror Sequence..."
G28 ; Home all positions (head, arms, jaw)

; Witch Activation Sequence
G1 X50 F1500 ; Turn head left (creepy slow movement)
M106 S255 ; Activate LED eyes (full brightness)
G4 P2000 ; Wait 2 seconds for dramatic effect

; Scream Sequence
G1 Y20 F3000 ; Open jaw quickly
M300 S440 P1000 ; Play scream sound (A4 note)
G1 Y0 F500 ; Close jaw slowly

; Horror Dance Movement
G1 X0 Y0 Z10 F2000 ; Multi-axis coordinated movement
G1 X-30 Y5 Z0 F1000 ; Arm swing with head tilt
G1 X30 Y-5 Z5 F1000 ; Opposite movement

; Emergency Stop Protocol
M112 ; Immediate stop all movement
M107 ; Turn off all effects
M117 "EMERGENCY STOP ACTIVATED"
```

**Hardware Stack:**
- Arduino Mega 2560 + RAMPS 1.4 Shield
- NEMA 17 Stepper Motors (head/arm movement)
- Servo Motors SG90 (jaw/eye control)
- DFPlayer Mini (audio effects)
- WS2812B LED strips (atmospheric lighting)
- PIR Motion Sensors (guest detection)

### **Python Automation Scripts**

**Fog Machine Choreography Controller:**
```python
import time
import serial
import threading
from datetime import datetime

class UniversalFogController:
    def __init__(self, port='COM3', baud=9600):
        self.arduino = serial.Serial(port, baud)
        self.emergency_stop = False
        self.sequence_active = False
        
    def log_event(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] UHU FOG CONTROL: {message}")
        
    def emergency_stop_all(self):
        """Critical safety function for Universal operations"""
        self.emergency_stop = True
        self.arduino.write(b'STOP_ALL\n')
        self.log_event("EMERGENCY STOP ACTIVATED")
        
    def fog_burst_sequence(self, intensity=75, duration=3):
        """Synchronized fog burst for scare moments"""
        if self.emergency_stop:
            return False
            
        command = f"FOG_BURST:{intensity}:{duration}\n"
        self.arduino.write(command.encode())
        self.log_event(f"Fog burst: {intensity}% for {duration}s")
        
    def cascading_fog_effect(self):
        """Multi-zone fog cascade for dramatic reveals"""
        zones = [1, 2, 3, 4]  # Different fog machine zones
        
        for zone in zones:
            if self.emergency_stop:
                break
            self.arduino.write(f"FOG_ZONE_{zone}:ON\n".encode())
            time.sleep(0.5)  # Staggered activation
            
        # Synchronized shutdown
        time.sleep(5)
        for zone in zones:
            self.arduino.write(f"FOG_ZONE_{zone}:OFF\n".encode())
            
    def health_monitor(self):
        """24/7 system monitoring for Universal operations"""
        while not self.emergency_stop:
            # Check fog machine fluid levels
            # Monitor temperature sensors
            # Verify communication with all devices
            # Log operational status
            time.sleep(30)  # Check every 30 seconds
```

### **Docker Containerization for Universal's Systems**

**Multi-Service Deployment:**
```yaml
# docker-compose.yml for Universal Horror Unleashed
version: '3.8'

services:
  attraction-controller:
    image: universal/horror-controller:latest
    ports:
      - "8080:8080"
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=info
    volumes:
      - ./logs:/app/logs
      - ./config:/app/config
    restart: always
    
  monitoring-dashboard:
    image: universal/monitoring:latest
    ports:
      - "3000:3000"
    depends_on:
      - attraction-controller
    restart: always
    
  emergency-systems:
    image: universal/emergency:latest
    privileged: true
    network_mode: host
    restart: always
    volumes:
      - /dev:/dev
```

---

## 💼 CURRENT TECHNICAL EXPERTISE

### **Infrastructure & Operations**
- 24/7/365 Operations Management
- Docker Containers & Orchestration
- Network Infrastructure & Troubleshooting
- System Monitoring & Alerting
- Emergency Response Protocols

### **Automation & Programming**
- G-Code/M-Code Programming
- Python Automation Scripts
- Arduino & Raspberry Pi Development
- Real-time Control Systems
- POS System Integration

### **Leadership & Crisis Management**
- Military Leadership (14 Years)
- Emergency Response Training
- Multi-team Coordination
- Crisis Decision Making
- Personnel Training & Development

### **Security & Compliance**
- Cybersecurity (Bug Bounty Experience)
- Google IT Certifications
- Risk Assessment & Mitigation
- Incident Response Procedures
- Safety Protocol Development

---

## 🎃 UNIVERSAL HORROR UNLEASHED APPLICATIONS

### **Direct Skill Applications:**

**🎭 Animatronics Management:**
- G-Code programming for creature movements
- Emergency stop protocols for guest safety
- Preventive maintenance scheduling
- Real-time troubleshooting capabilities

**💡 Lighting & Effects:**
- Automated lighting sequences
- Strobe and mood effect programming
- Synchronized multi-zone control
- Emergency lighting protocols

**🌫️ Atmospheric Effects:**
- Fog machine choreography
- Timed special effects coordination
- Environmental condition monitoring
- Safety system integration

**🚨 Safety & Emergency Response:**
- Crisis management protocols
- Emergency evacuation procedures
- System failure response plans
- Team coordination during incidents

---

## 🏆 EDUCATION & CERTIFICATIONS

**Cornell University - Business Management (2023)**
- Operations Management & Strategy
- Team Leadership & Development
- Crisis Management & Response
- Technology Integration

**Google IT Certifications**
- IT Support Professional
- Network Security
- System Administration

**Military Training**
- Advanced Leadership Course
- Emergency Response Certification
- Technical Equipment Operation
- Multi-cultural Communication

---

## 🎯 WHY UNIVERSAL HORROR UNLEASHED?

**Authentic Horror Passion:**
- Married on Halloween (genuine horror culture appreciation)
- Traveled to Derry, Ireland (Stephen King's IT filming location)
- Deep understanding of what creates memorable horror experiences

**Operational Excellence:**
- Military-trained crisis management
- Zero-failure mission mentality
- 24/7/365 operational experience
- Guest safety as top priority

**Local Advantage:**
- Las Vegas resident (immediate availability)
- 5.5 miles from Area 15 (reliable attendance)
- Understanding of Las Vegas tourism industry
- Multilingual capabilities for diverse guest base

**Technical Innovation:**
- Cutting-edge automation skills
- Docker containerization expertise
- Real-time system monitoring capabilities
- Proactive maintenance approaches

---

## 📞 IMMEDIATE AVAILABILITY

**Contact Information:**
- 📧 **Email:** herrera.hannibal84@gmail.com
- 📱 **Phone:** 702-626-7678
- 📍 **Location:** Las Vegas, NV (5.5 miles from Area 15)
- ⏰ **Availability:** Immediate start available

**Ready to bring military-grade operational excellence, cutting-edge technical skills, and authentic horror passion to Universal Horror Unleashed's technology operations team!**

---

*"In the military, we had a saying: 'Failure is not an option.' At Universal Horror Unleashed, that same mentality will ensure every guest has an unforgettable, safe, and terrifying experience."*

**- Hannibal Herrera, Technology Operations Manager Candidate**
